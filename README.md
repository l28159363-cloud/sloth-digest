# 🦥 SlothDigest

**Your group chats, read overnight. Two lines by morning.**

Built for the [Hacktoberfest Open-Source AI Challenge](https://dev.to/devteam/join-the-hacktoberfest-open-source-ai-challenge-slow-and-steady-2850-in-prizes-across-21-3iee) — Week 3: **Slow and Steady** (build something with open-weight models or open-source AI that rewards laziness).

## The problem

Group chats don't sleep. You wake up to 47 messages and one decision buried in them. Reading everything is a chore; missing the one thing that matters is worse.

## What it does

SlothDigest runs overnight and hands you a two-line morning digest: what was decided, what moved, and what someone needs from you. Nothing else.

- **Decisions** — "hotpot Saturday 7pm" survives; the 30 sticker messages don't.
- **Deadlines** — "math assignment moved to Monday" surfaces even at 23:31.
- **Asks** — "bring a charger" becomes a checklist item, not a lost message.

## Try the demo

Open `index.html` in any browser — it simulates one night in a class group chat, then generates the morning digest. No build step, no server.

## Run it for real

`agent.py` runs the same digest on an exported chat, fully locally:

```bash
python agent.py chat_export.json
# with a local model (Ollama running on localhost:11434):
python agent.py chat_export.json --model llama3.2
```

Chat export format (JSON list):

```json
[{"sender": "Mia", "time": "23:14", "text": "hotpot saturday 7pm!"}]
```

Without a local model it uses a lightweight on-device extractive pass. Either way: **no messages leave the device, no API key, no bill.**

## Why open

This idea only works open. Group chats are the most personal data most people have — a cloud summarizer means handing your private conversations to someone else's server, forever, at a per-message price. An open-weight model running on your own machine turns the same feature into a utility you own: private by construction, free after download, and working offline on a plane.

## Deploy

The demo is a static page — deploy it anywhere. For the challenge's **Best Use of Render** category it runs on Render (free/static hosting).

## License

MIT. Sloths move slowly. So should your mornings.
