# DEV submission draft — Week 3: Slow and Steady
# Paste into a new DEV post using the official "Slow and Steady Submission Template".
# Fill in the [BRACKETS] on Monday after deploy.

---

# 🦥 SlothDigest: Your Group Chats, Read Overnight — Two Lines by Morning

## What I built

SlothDigest is a tiny overnight agent for group chats. While you sleep, it reads the night's messages and hands you a two-line morning digest: what was decided, what moved, and what someone needs from you. Everything else — the stickers, the 30-message side quests — quietly disappears.

Try it: [DEMO LINK — Render URL, fill in Monday](https://example.com)
Code: https://github.com/l28159363-cloud/sloth-digest

The demo simulates one night in a class group chat: 47 messages, one hotpot plan, one moved deadline, one forgotten charger. Hit "Run the overnight digest" and watch the sloth do its job. The repo also includes `agent.py`, which runs the same digest for real on an exported chat — with a local model when one is available (Ollama-compatible endpoint), and a lightweight on-device extractive pass otherwise.

## Why open innovation matters for this

This idea only works open, for three reasons:

1. **Privacy is the feature.** Group chats are the most personal data most people have. A cloud summarizer means handing your private conversations to someone else's server, forever. A small open-weight model running on your own machine makes the same feature private by construction — there is nothing to leak, sell, or subpoena.

2. **Zero marginal cost.** Once the model is downloaded, every nightly digest costs exactly $0. A closed API charges per message, which means the people who chat the most — students, families, community groups — pay the most. Open weights turn an AI feature into a utility you own.

3. **It works offline.** On a plane, on campus Wi-Fi that barely works, anywhere — the digest still runs, because nothing needs the cloud. Open models are what make "AI that just works" possible without a subscription.

## What I used

- A static front-end demo (HTML/CSS/JS, no build step) — deployed on Render
- `agent.py` — a Python script for the real local digest (local model optional, extractive fallback built in)
- Open-weight models via a local runtime (Ollama-compatible)

## Category

Best Use of Render — the demo is deployed on Render, and the whole point is a thing that runs while you sleep, on infrastructure that doesn't need babysitting.

## What I'd improve next

Real chat imports (WhatsApp/Telegram exports), per-group digest schedules, and a "digest before noon only" quiet mode — because the sloth way is to bother you as little as possible.
