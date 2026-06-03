# CSC-114 Mini-Module: The Gemini Path to Assistants & Agents
## Instructor Guide

| Field | Value |
|-------|-------|
| Course | CSC-114 Artificial Intelligence I |
| Mini-module | The Gemini Path — a parallel to the Claude/Console path |
| Duration | 2 meetings, each a 2-hour block — **4 contact hours total** |
| Meeting structure | Hour 1 = lecture/demo, Hour 2 = lab *(provisional — adjust to the room)* |
| Platforms | Day 1: `gemini.google.com` (Gems). Day 2: `aistudio.google.com` (Google AI Studio) |
| Prerequisites | Students have built a Claude Project and seen the Anthropic Console; the chatbot/assistant/agent distinction is established |
| Student handouts | *Day 1 — Gemini Gem Study Bot*; *Day 2 — Domain Agent in Google AI Studio* |
| Account model | **Bring-your-own personal Google account** — our college does not enable Workspace Gemini |
| Status | DRAFT — first delivery; expect to tune pacing |

---

## Where This Mini-Module Sits

Students have already walked the assistant→agent ladder once, on Anthropic's stack: a Claude Project (assistant) and then the Console (agent). You observed that Console buy-in is more friction than some less-technical students are comfortable with. This mini-module walks the **same ladder on Google's stack**, where the on-ramp is lower-friction: Gems are free on any personal account, and a working agent in AI Studio needs **no billing setup and no API key**.

The pedagogical payoff is **tool-agnosticism**. Building the same two-rung climb on a second platform is how students separate the *transferable judgment* (writing constraints, testing, granting tools wisely) from the *platform mechanics*. It's the same move as "build the same bot twice" — applied across vendors instead of across one vendor's products.

Two-rung shape:

1. **Day 1 — Assistant.** A Gemini **Gem** study bot. Persona + knowledge + honesty rule. No actions.
2. **Day 2 — Agent.** A domain agent in **AI Studio** with **Google Search grounding** turned on. It takes an action and cites sources.

---

## Learning Targets

By the end, a student can:

1. **Place** Gems and AI Studio agents correctly on the chatbot/assistant/agent spectrum, and explain *why* a Gem is an assistant and a search-grounded AI Studio bot is an agent.
2. **Build** a Gem with instructions answering the three questions plus an honesty rule, grounded in their own knowledge files.
3. **Build** an AI Studio agent with five-part system instructions, a controlled knowledge document, and exactly the tools it needs.
4. **Validate** both with the three-test pattern (known-good/happy, known-bad/fallback, edge/trick) and **refine** using the one-change rule.
5. **Map** the Gemini path onto the Claude path they already know (Gem ↔ Project, AI Studio ↔ Console).
6. **Commit** their work to GitHub under `gemini-day1/` and `gemini-day2/` using their track's workflow.

---

## Instructor Pre-Work

Do this **before Day 1**.

- [ ] Confirm you have a personal Google account and have built **your own** sample Gem and **your own** AI Studio agent — you'll demo both live and you'll want a known failure to show.
- [ ] **Check the age gate.** Gems require 13+; **AI Studio requires 18+**. Quietly find out before Day 2 whether any enrolled students are under 18. If so, plan to run Day 2's build as an instructor-led demo with those students pairing on an 18+ classmate's screen, or doing the design work (knowledge doc + instructions) without operating AI Studio themselves. Handle this discreetly.
- [ ] Verify the **current Gemini model names** in both products the morning of class — Google renames models often. The labs say "the current Flash model" on purpose; fill in the live name for students.
- [ ] Re-confirm two facts that change fast: (a) Gems and their knowledge-file uploads are available on the **free** tier; (b) AI Studio runs in the playground **without** an API key or billing. Both were true as of mid-2026; verify before each term at `support.google.com/gemini` and `aistudio.google.com`.
- [ ] Prepare a small, **deliberately incomplete** knowledge document for your demos so a "known-bad" test fails naturally.
- [ ] Distribute both student handouts via Canvas.
- [ ] Decide your stance on the **privacy warning** and reinforce it verbally — students are on personal free accounts where inputs may be human-reviewed.

---

## Day 1 — Build a Gemini Gem Study Bot

### Hour 1: Lecture / Demo (≈60 min)

| Time | Segment | Talking points |
|------|---------|----------------|
| 5 min | **Framing** | "We've climbed the assistant→agent ladder once, with Claude. Today we climb the first rung on Google's ladder. The skills are the same; the buttons move." |
| 10 min | **What is a Gem?** | Google's Claude Project. Two parts: instructions + knowledge files. Create one live so they see the surface. Say plainly: **a Gem is an assistant, not an agent.** |
| 10 min | **Free + bring-your-own-account** | Gems are free on any personal Google account; our college accounts don't have Gemini. Everyone needs a personal Gmail. Hit the **privacy warning** here — no private uploads, humans may review free-tier data. |
| 15 min | **Three questions + honesty rule** | Build a sample instruction set live, taking answers from the class. The honesty rule is the conceptual heart — it gives the bot permission to say "I don't know." Show the magic-wand "re-write instructions" button as an ESL/accessibility aid. |
| 10 min | **Three tests + one-change rule** | Re-anchor known-good / known-bad / edge. Re-anchor the one-change rule from CSC-113/114. |
| 10 min | **Live demo: test and fix** | Run the three tests on your sample Gem. Make sure the known-bad test **fails** (bot bluffs). Fix with one change (add/strengthen honesty rule), re-test, narrate "failure is just exercise." |

**The one thing they must leave believing:** a Gem with three clear answers and one honesty rule behaves; a vague Gem bluffs.

### Hour 2: Lab (≈60 min)

Students work through *Day 1 — Gemini Gem Study Bot*, Steps 1–7.

- **Circulate.** The usual stall is the **known-bad test** — students pick a question their notes actually answer. Prompt: "What's something your notes definitely *don't* cover?"
- **Watch the rewrite reflex.** When a test disappoints, many rewrite everything. Stop them: one change, one re-test.
- **Free-tier context ceiling.** If a student's Gem "forgets" the back half of a long document, that's the ~50-page free-tier context window, not a bug. Coach them to use focused files.
- **Last 10 min — commit check.** Confirm `gemini-day1/` is committed. This is where **Prompt Masters** most need a hand — walk the drag-and-drop path and confirm the folder appears in the repo. Treat drag-and-drop as first-class.

**Circulating prompts:**
- "Show me your testing log. Which change made the biggest difference?"
- "Ask your bot something your notes don't cover. What does it do?"
- "In one sentence — why is this an *assistant* and not an *agent*?"

---

## Day 2 — Build a Domain Agent in Google AI Studio

### Hour 1: Lecture / Demo (≈60 min)

| Time | Segment | Talking points |
|------|---------|----------------|
| 5 min | **Debrief Day 1** | Surface a good "I don't know" response from a student's Gem on screen. Celebrate it. |
| 5 min | **The 18+ gate** | State it plainly and handle under-18 students per your pre-work plan. AI Studio is 18+. |
| 10 min | **What is AI Studio?** | Google's developer playground — the rough equivalent of the Anthropic Console. **Lower friction than the Console:** no API key, no billing for today's lab. Open it live. |
| 10 min | **The assistant→agent line** | The toggle that matters: **Google Search grounding**. Off = assistant. On = agent (it takes an action and cites sources). This is the conceptual heart of Day 2. |
| 10 min | **Tools = least privilege** | Re-anchor the Console tool-permission lesson: every tool left on is a tool the agent might misuse. Today, Search ON, everything else OFF, with a stated reason. |
| 10 min | **Knowledge doc vs. live search** | Controlled knowledge (the pasted document) vs. current knowledge (search). A good agent uses both and tells you which. |
| 10 min | **Live demo: agent that searches** | Demo a happy-path answer from your document, a clean fallback refusal, and a "current info" question that triggers search with visible sources. Make one test fail; fix with one change. |

**The one thing they must leave believing:** turning on a tool is what turns an assistant into an agent — and with that power comes the duty to scope tools and check sources.

### Hour 2: Lab (≈60 min)

Students work through *Day 2 — Domain Agent in Google AI Studio*, Steps 1–8.

- **No API key today.** If students start hunting for "Get API key," redirect them — the playground runs without it. (Note for you: API keys *are* free and need no card, but they're a later lesson about connecting Gemini to code. Keep today in the playground.)
- **Confirm the tool actually fired.** The most common silent failure: a student asks a "current info" question, gets a plausible answer with **no source links**, and assumes search ran. It didn't. Coach them to verify grounding by looking for citations.
- **Watch for over-toolings.** If someone flips on every tool "just in case," that's your least-privilege teaching moment.
- **Two change cycles.** Agents have more moving parts than Gems; expect (and require) at least two one-change cycles.
- **Last 10 min — commit check.** Confirm `gemini-day2/` is committed. Prompt Masters: drag-and-drop again.

**Circulating prompts:**
- "Did your agent actually search? Show me the sources it returned."
- "Why did you turn that tool on? Does your agent really need it?"
- "Ask it something completely off-topic. Does it refuse cleanly?"
- "What's one risk of letting this thing search the open web on its own?"

---

## Assessment Posture

Both days are **mostly formative**, graded **complete / re-do**, rewarding *process* over a perfect bot. Hold first-attempt expectations in the **Developing-to-Proficient** band. The graded artifacts are the committed files.

**Day 1 graded artifacts** (`gemini-day1/`): `gem-instructions.md` (three questions + honesty rule), `knowledge-sources.md`, `testing-log.md` (three tests + one documented change + reflection).

**Day 2 graded artifacts** (`gemini-day2/`): `knowledge-doc.md`, `system-instructions.md` (five parts + tool rationale), `testing-log.md` (three tests + two change cycles + reflection).

### Four-Category Rubric — How It Maps Here

| Category | Day 1 evidence | Day 2 evidence |
|----------|----------------|----------------|
| **AI Partnership Quality** | Three questions answered; honesty rule present | Five-part instructions; real knowledge doc; Search enabled with a reason |
| **Problem-Solving Process** | Three tests; one controlled change re-tested | Three tests; ≥2 controlled change cycles (not rewrites) |
| **Professional Communication** | Files under `gemini-day1/`; clear commit message | Files under `gemini-day2/`; tool-rationale note; clear commit message |
| **Critical Thinking & Ethics** | Noticed edge behavior; named one thing an assistant can't do | Explained *why* it's an agent; checked the agent's sources; named a live-search risk |

Keep grading light. The reflection prompts are where AI-partnership quality becomes observable — they explicitly ask what students asked their AI and whether they had to push back. Read those.

---

## Differentiation

**Code Builders vs. Prompt Masters.** The build and thinking are identical across tracks. The only divergence is how files reach GitHub:
- **Code Builders** use their normal Git workflow into `gemini-day1/` and `gemini-day2/`.
- **Prompt Masters** drag and drop files via the GitHub web client or Desktop. This is a deliberate, first-class accommodation — not a lesser path.

**Mixed ability and ESL.** Both labs target ~10th-grade reading and define jargon on first use. The magic-wand instruction re-writer (Day 1) is a genuine accessibility aid — let students brain-dump a goal and have Gemini structure it, then review. Pair faster students with slower ones during labs.

**Under-18 students (Day 2).** AI Studio's 18+ requirement is a hard external gate. Plan: they design the knowledge doc and system instructions (the real thinking), and either pair with an 18+ classmate to operate AI Studio or watch your instructor-led demo and submit the design artifacts. Don't make this a spectacle.

**Pacing.** The 1-hour-lecture / 1-hour-lab split is a starting guess. If the room flies through the build, shorten the lecture and let the lab breathe; if accounts and logins eat time, the reverse.

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| "I can't find Gemini on my school account." | College accounts don't have Gemini enabled. | They must use a **personal** Google account. Have them sign out and back in with personal Gmail. |
| "My Gem answers from general knowledge, not my files." | Honesty rule missing or weak. | Add/strengthen "use only my uploaded files; say so if it's not covered." Great live one-change demo. |
| "My Gem forgets the end of a long document." | Free-tier ~50-page context window. | Use shorter, focused files; this is expected, not a bug. |
| "Every test passed — nothing failed." | The known-bad question was actually answerable. | Coach a genuinely out-of-scope question. No failures = nothing learned. |
| "AI Studio is asking my age / won't let me in." | 18+ gate. | Apply the under-18 plan above. |
| "It's asking me for a credit card / API key." | Student wandered out of the playground. | Redirect to the chat playground; no key or billing is needed for this lab. |
| "My agent answered a 'current info' question with no sources." | Grounding didn't fire (or wasn't on). | Confirm the Search toggle is ON; verify by looking for citation links; re-ask. |
| "It turned on every tool." | Over-tooling. | Least-privilege teaching moment — turn off what the agent doesn't need and state why. |
| Prompt Master stuck on the commit | Unfamiliar with GitHub web/Desktop | Walk drag-and-drop; confirm the `gemini-dayN/` folder appears. |

**When to escalate.** Persistent account, age-gate, or access problems that are eating lab time can go to the designated escalation contacts (**Mallory Milstead, Andrew Norris**). Use this for blockers, not ordinary iteration struggles.

---

## Fast-Moving-Target Warnings

This is the most volatile material in the course. Re-verify before every term:

- **Model names** in both products (Google renames frequently — the labs say "current Flash model" deliberately).
- **Free-tier specifics:** that Gems + knowledge uploads remain free; that AI Studio's playground still needs no key/billing; the free context-window figure.
- **Age gates** (13+ Gems, 18+ AI Studio) and any regional differences (EU/UK/Switzerland is 18+ for Gemini Apps generally).
- **Privacy/data terms** on the free consumer tier (human review, retention) — the warning to students depends on this staying accurate.

If any of these have shifted, update the two student handouts before distributing.

---

## The Throughline

Same loop, second ladder:

> **Set your intentions → test them → change one thing → test again.**

Day 1 proves the loop transfers to a Gem. Day 2 proves the assistant→agent jump transfers to AI Studio. Across both, the lesson under the lesson is the one that outlasts every product rename: **the judgment is yours, not the platform's.** Which tools to grant, when to trust the output, and how to test whether the thing does what you intended — that's what students carry to whatever tool comes next.
