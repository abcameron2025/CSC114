# Day 2 Lab: Build a Domain Agent in Google AI Studio

**Course:** CSC-114 Artificial Intelligence I
**Module:** Domain Assistants & Agents — The Gemini Path
**Today's build:** A domain agent that *takes an action* using a tool
**Where it lives:** `aistudio.google.com` (still no real coding — you'll use the built-in playground)

---

## Where Today Sits

Yesterday you built a **Gem** — an *assistant*. It read your notes and explained them, but it couldn't *do* anything. Today you cross the line into **agent** territory: you'll build a bot that can reach outside itself and take an action — by **grounding its answers in a live Google Search** and citing where the facts came from.

Same loop as always: **intend → test → change one thing → test again.** New, more powerful platform.

---

## Before You Start: What You'll Need

- [ ] Your **personal Google account** (same as yesterday — our college accounts don't have these tools enabled).
- [ ] **You must be 18 or older** to use Google AI Studio. This is stricter than the Gem age limit. If you are under 18, tell your instructor now — you'll pair with a classmate or do this as a guided demo instead.
- [ ] One **domain knowledge document** you prepare and paste in (a one-page reference on a topic you know — see Step 3).
- [ ] Your CSC-114 GitHub repository.

> **Privacy warning, again.** On the free tier, Google may use what you type to improve their products and may have humans review some of it. **Paste only non-private study/reference material.** No personal data, yours or anyone else's.

> **No credit card needed.** Google AI Studio is free to use, and you can run today's lab without setting up any billing. If anyone asks you to enter payment info to finish this assignment, stop and ask your instructor — you don't need it.

---

## Words You'll See Today

| Word | What it means here |
|------|--------------------|
| **Google AI Studio** | Google's developer playground for building with the Gemini models. It's the rough equivalent of the Anthropic Console you saw with Claude. |
| **System instructions** | The same idea as your Gem's instructions — the standing rules for your bot. |
| **Agent** | An AI that can **take actions** using tools, not just chat. Today's action is live search. |
| **Grounding (Google Search)** | A tool you switch on that lets the bot look something up on the live web and **show its sources**. |
| **Tool / function** | A capability you give the bot beyond talking. Grounding is a built-in tool. |
| **Knowledge document** | The reference text you give your agent so it answers from a known, controlled source. |

---

## The Key Difference From Yesterday

| | **Gem (Day 1)** | **AI Studio agent (Day 2)** |
|---|---|---|
| Role on the spectrum | Assistant | Agent |
| Can it take an action? | No | **Yes — it can search the live web** |
| Does it cite sources? | Not really | **Yes — grounding returns citations** |
| Knowledge | Uploaded files | A document you paste + live search |
| Platform | gemini.google.com | aistudio.google.com |

This is the **same kind of jump** you saw moving from a Claude Project to the Anthropic Console — but the on-ramp here is gentler: no billing setup, fewer clicks to a working bot.

---

## Step 1 — Open Google AI Studio

1. Go to `aistudio.google.com` and sign in with your personal Google account.
2. Accept the terms if prompted.
3. Open a new **Chat** prompt. You'll see a large message area in the middle and a **settings panel** on the right (model, system instructions, and tool toggles).

> You do **not** need to create an API key for today's lab. The playground runs without one. (An API key is for connecting Gemini to your *own* code — that's a later lesson.)

---

## Step 2 — Pick Your Model

In the right-hand settings, set the model to the current **Gemini Flash** model (the default fast model — its name may include "Flash"). Flash is fast, capable, and generous on the free tier. Don't reach for the heavier "Pro" model today; Flash is the right tool for this job.

Write the exact model name you used here: `______________________________`

---

## Step 3 — Write Your Domain Knowledge Document

Before you build the agent, prepare its knowledge. Open a plain text or Markdown file and write a **one-page reference document** on a domain *you* choose.

**Good domains (pick one, or your own):**
- A study topic from another class (e.g., "The phases of mitosis")
- A how-to you know well (e.g., "How to set a static IP on Windows 11")
- A reference table (e.g., "Common SQL JOIN types and when to use each")

**Your document should include:**
- A short intro of what the domain is
- 5–10 specific facts, steps, or definitions
- One thing that is *deliberately left out* (so you have a clean "known-bad" test later)

Save this as `knowledge-doc.md`. You'll paste it into the system instructions next.

---

## Step 4 — Write the System Instructions

In the settings panel, open **System instructions** and write rules using the same structure you know. Here is a five-part frame — fill in every part:

```markdown
## 1. Identity and Role
You are [Agent Name], a [specific role] for [specific audience].
You help with [narrow domain] and nothing else.

## 2. Behavioral Rules
- Answer using the knowledge document below and trusted live search results.
- When you use search, always show the sources/links you found.
- If a question is outside [your domain], say: "[your refusal line]"
- Never invent facts. If you are unsure, say so.

## 3. Domain Knowledge
[Paste your one-page knowledge-doc.md here.]

## 4. Output Format
[How should answers look? e.g., "Answer in 3–5 sentences, then list any
sources you used as bullet points."]

## 5. Context
Today's date is [date]. You are used by students in CSC-114.
```

> **Why both a document AND search?** The document is your *controlled* knowledge — the stuff you trust. Search lets the agent reach *current* information it doesn't have. A good agent knows which to lean on, and tells you where each answer came from.

---

## Step 5 — Turn On the Agent's Tool: Google Search Grounding

This is the step that turns your assistant into an agent.

1. In the settings panel, find the **Tools** section.
2. Turn **ON** the **Grounding with Google Search** toggle.
3. Leave other tools (like code execution) **OFF** for now — only switch on what your agent actually needs. (That's the "principle of least privilege" you met with Claude tool permissions: every tool you leave on is a tool the agent might use in a way you didn't expect.)

> You just gave your bot the ability to take an action. That's the line between assistant and agent.

---

## Step 6 — Run the Three-Test Protocol

Test your agent with the same three test types, now adapted for an agent:

| Test | What to try | What *should* happen |
|------|-------------|---------------------|
| **Happy path** | A question your knowledge document clearly answers | Correct answer, drawn from your document |
| **Fallback (known-bad)** | A question outside your domain entirely | It uses your refusal line — doesn't wander off-topic |
| **Trick / action test** | A question that needs *current* info (e.g., "What's the latest version of X?") | It **uses search** and **shows sources/links** |

Watch for two things specifically:
- **Did it actually search?** Grounded answers show source links. If it answered a "current info" question with no sources, it didn't really use the tool — note that.
- **Did it stay in its lane?** A good domain agent refuses cleanly instead of answering everything.

---

## Step 7 — Apply the One-Change Rule

Find the single biggest problem from your three tests. Change **one thing** — a rule, the refusal line, the output format, or the knowledge document. Re-test. Document what that one change did.

Run **at least two** change-and-retest cycles today (the agent has more moving parts than yesterday's Gem, so you'll usually need more than one).

> Resist rewriting everything. One change, one re-test. **Failure is just exercise.**

---

## Step 8 — Submit to GitHub

Create a folder `gemini-day2/` in your CSC-114 repo with these files.

**File 1 — `knowledge-doc.md`** — your one-page domain reference.

**File 2 — `system-instructions.md`** — your final five-part system instructions, and a one-line note saying **which tools you turned on and why** (e.g., "Search: ON — my agent needs current version numbers. Code execution: OFF — my agent does no math.").

**File 3 — `testing-log.md`** — use this template:

```markdown
# Domain Agent Testing Log — Day 2

## My Agent: [name]   |   Domain: [domain]   |   Model: [model]

## Tools I enabled
| Tool | On/Off | Why |
|------|--------|-----|
| Google Search grounding | On/Off | [one sentence] |
| Code execution | On/Off | [one sentence] |

## Tests
| Test # | Type | What I asked | What it did | Did it use a tool? | Pass/Fail |
|--------|------|--------------|-------------|--------------------|-----------|
| 1 | Happy path | | | | |
| 2 | Fallback | | | | |
| 3 | Trick/action | | | | |

## Change cycle 1
**Problem I saw:** [...]
**The one change:** [...]
**Result after re-test:** [...]

## Change cycle 2
**Problem I saw:** [...]
**The one change:** [...]
**Result after re-test:** [...]

## Reflection (4–5 sentences)
- What made today's bot an AGENT and not just an assistant?
- When the agent used search, did you trust its sources? How did you check?
- What did you ask your own AI partner (Gemini, Claude, etc.) while building this, and did you have to push back on any answer it gave you?
- Name one risk of letting an agent search the live web on its own.
```

**How to submit:**
- **Code Builders:** commit and push the `gemini-day2/` folder with a descriptive message.
- **Prompt Masters:** drag and drop the three files into a `gemini-day2/` folder via the GitHub website or Desktop. Fully valid.

---

## Before You Leave — Checklist

- [ ] My agent runs in AI Studio on the Flash model.
- [ ] My system instructions include all five parts and paste in my knowledge document.
- [ ] I turned **on** Google Search grounding and left unneeded tools off — and I wrote down why.
- [ ] I ran all three tests (happy path, fallback, trick/action).
- [ ] I confirmed the agent actually used search and showed sources on at least one answer.
- [ ] I ran at least two one-change cycles.
- [ ] All three files are in `gemini-day2/` in my GitHub repo.

---

## What Just Happened

Over two days you walked the whole spectrum on a new platform. Day 1: an **assistant** (a Gem) that answers from your knowledge. Day 2: an **agent** that takes an action — searching the live web and citing its sources — while staying inside the domain you defined.

You also saw the trade-off that defines agent design: more power (it can reach the live web) means more responsibility (you have to check its sources and limit its tools). That judgment — *which* tools to grant and *when* to trust the output — is the real skill. The platform will keep changing. The judgment travels with you.

> **Compare it to Claude:** Gem ↔ Claude Project (assistant). AI Studio agent ↔ Anthropic Console agent. Same two rungs, two different ladders. Being able to move between them is exactly what makes you tool-agnostic.

> **Stuck on accounts, the 18+ requirement, or access?** Tell your instructor — they can escalate to Mallory Milstead or Andrew Norris.

---

## Grading: What "Complete" Looks Like

**Complete / re-do** grading, mapped to the four-category rubric:

| Category | What earns "complete" |
|----------|----------------------|
| **AI Partnership Quality** | Five-part system instructions; a real knowledge document; Search grounding enabled with a stated reason. |
| **Problem-Solving Process** | All three tests run; at least two controlled one-change cycles documented (not full rewrites). |
| **Professional Communication** | Three files under `gemini-day2/`, a clear tool-rationale note, and a descriptive commit message. |
| **Critical Thinking & Ethics** | Reflection shows you can tell *why* this is an agent, that you checked the agent's sources, and that you named a real risk of live-web search. |
