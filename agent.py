#!/usr/bin/env python3
"""SlothDigest — overnight group-chat digest, fully local.

Reads an exported group chat (JSON list of {"sender", "time", "text"}),
produces a two-line morning digest plus key points.

- If a local Ollama-compatible endpoint is reachable on localhost:11434,
  it asks the local model to summarize (no cloud, no API key).
- Otherwise it falls back to a lightweight on-device extractive pass
  (keyword heuristics for plans, deadlines, and asks).

Nothing ever leaves the device. Usage:
    python agent.py chat_export.json
    python agent.py chat_export.json --model llama3.2   # via local Ollama

Sample chat_export.json:
    [{"sender": "Mia", "time": "23:14", "text": "hotpot saturday 7pm!"}]
"""

import json
import re
import sys
import urllib.request

PLAN_WORDS = ["hotpot", "dinner", "lunch", "meet", "party", "movie", "trip",
              "saturday", "sunday", "monday", "tuesday", "pm", "am"]
DEADLINE_WORDS = ["deadline", "due", "assignment", "homework", "submit", "exam"]
ASK_WORDS = ["bring", "please", "pls", "need", "charger", "help", "remember"]


def extractive_digest(messages):
    """Pick the most informative lines by simple keyword scoring."""
    scored = []
    for m in messages:
        text = m["text"].lower()
        score = 0
        for w in PLAN_WORDS + DEADLINE_WORDS + ASK_WORDS:
            if w in text:
                score += 1
        if score:
            scored.append((score, m))
    scored.sort(key=lambda x: -x[0])
    picks = [m for _, m in scored[:4]]
    if not picks:
        return ("Nothing urgent happened overnight.",
                ["No plans, deadlines, or asks detected."])
    summary = " / ".join(f"{m['sender']}: {m['text']}" for m in picks[:2])
    points = [f"{m['sender']} ({m['time']}): {m['text']}" for m in picks]
    return (summary, points)


def local_model_digest(messages, model="llama3.2"):
    """Try a local Ollama endpoint; return None if it is not there."""
    prompt = ("Summarize this group chat overnight digest in two lines, "
              "then list key plans, deadlines, and asks as bullets. "
              "Chat:\n" + "\n".join(
                  f"{m['sender']} {m['time']}: {m['text']}" for m in messages))
    req = urllib.request.Request(
        "http://localhost:11434/api/generate",
        data=json.dumps({"model": model, "prompt": prompt,
                         "stream": False}).encode(),
        headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            return json.loads(resp.read())["response"]
    except Exception:
        return None


def main():
    if len(sys.argv) < 2:
        print("usage: python agent.py chat_export.json [--model NAME]")
        sys.exit(1)
    with open(sys.argv[1], encoding="utf-8") as f:
        messages = json.load(f)
    model = None
    if "--model" in sys.argv:
        model = sys.argv[sys.argv.index("--model") + 1]

    result = local_model_digest(messages, model) if model else None
    if result:
        print("☀️ Good morning — your 2-line digest (local model):\n")
        print(result)
        return
    summary, points = extractive_digest(messages)
    print("☀️ Good morning — your 2-line digest (on-device pass):\n")
    print(summary)
    print("\nKey points:")
    for p in points:
        print(f"  - {p}")
    print("\nGenerated locally. No messages left this device.")


if __name__ == "__main__":
    main()
