# Day 1 Lab: Build a Gemini Gem Study Bot

**Course:** CSC-114 Artificial Intelligence I
**Module:** Domain Assistants & Agents — The Gemini Path
**Today's build:** A custom study assistant on Google Gemini
**Where it lives:** `gemini.google.com` (no code, runs in your browser)

---

## Before You Start: What You'll Need

- [ ] A **personal Google account** (a Gmail address). Our college accounts do **not** have Gemini turned on, so you must bring your own. If you don't have one, make a free one at `accounts.google.com`.
- [ ] You must be **13 or older** to use Gems on a personal account. (If you are in the EU, UK, or Switzerland, the minimum is 18.)
- [ ] Two or three of your own **study documents** — class notes, a study guide, a chapter summary, a review sheet. PDF, Word, or plain text all work.
- [ ] Your CSC-114 GitHub repository, ready to receive files.

> **Privacy warning — read this.** On a free Google account, Google may use what you type and upload to improve their products, and a small number of chats get read by human reviewers. **Do not upload anything private** — no medical info, no financial info, no other people's personal information. Use study material you'd be comfortable showing the class.

---

## Words You'll See Today

| Word | What it means here |
|------|--------------------|
| **Gem** | A saved, reusable custom version of Gemini. You give it a name, instructions, and reference files. It's Google's version of a Claude Project. |
| **Assistant** | An AI that follows a persona and uses knowledge you give it, but does **not** take actions on its own. A Gem is an assistant. |
| **Instructions** | The "system prompt" — the standing rules that tell your Gem who it is and how to behave. |
| **Knowledge files** | The reference documents you attach so your Gem answers from *your* material, not just the open internet. |
| **The honesty rule** | An instruction that gives your bot permission to say "I don't know" instead of making something up. |

---

## What We're Building (and What We're Not)

You're building a **study bot**: a Gem that quizzes you, explains your notes in plain language, and helps you review for a topic *you* choose.

This is an **assistant**, not an agent. It reads, it explains, it answers — but it can't go *do* things in the world (it can't send email, run code, or look things up in a live database with tools you control). Knowing that boundary is part of today's lesson. Tomorrow you'll cross it.

> **The big idea:** This is the same loop you already know — **write your intentions → test them → change one thing → test again.** Only the platform is new.

---

## Step 1 — Open the Gem Builder

1. Go to `gemini.google.com` and sign in with your personal Google account.
2. In the left sidebar, find **Gems** and click **New Gem**.
3. You'll see two main boxes: a **Name** field and an **Instructions** field, with an **Add files** area for Knowledge, and a **preview** panel on the right.

---

## Step 2 — Name Your Gem

Give it a clear, specific name. Not "Study Helper" — name the *subject*.

**Good examples:**
- `Cellular Respiration Study Coach`
- `Spanish 101 Verb Drill Bot`
- `IPv4 Subnetting Review Buddy`

Write your Gem name here: `______________________________`

---

## Step 3 — Write the Instructions (The Three Questions + The Honesty Rule)

Answer these three questions in plain sentences. This is your system prompt.

**Question 1 — Who is the bot?**
> Example: "You are a patient study coach for a community college biology student. You explain ideas simply and never lecture for more than a few sentences before checking that I understand."

**Question 2 — Who am I (the user)?**
> Example: "I am a student reviewing cellular respiration for an exam. English is my second language, so use simple words and define any technical term the first time you use it."

**Question 3 — What do we accomplish together?**
> Example: "Help me review by quizzing me one question at a time, explaining my notes when I'm stuck, and summarizing a topic when I ask."

**Now add the honesty rule. This is required.**
> Copy this in, adjusting as needed:
> "Only answer using the study files I have given you. If something is not in my files, say: 'That's not in your notes — want me to explain it from general knowledge instead?' Never make up facts and pretend they came from my notes."

> **Why the honesty rule matters:** Without it, your bot will confidently invent answers when your notes don't cover something. The honesty rule gives it permission to say *"I don't know."* That single sentence is the most important one in your whole prompt.

**Optional helper:** If writing instructions feels hard, type a one-line goal into the Instructions box and click the **"Use Gemini to re-write instructions"** (magic wand) button. It expands your goal into a full draft. Then read it carefully and fix anything that's wrong — *you* are still in charge.

---

## Step 4 — Add Your Knowledge Files

1. In the **Knowledge** area, click **Add files**.
2. Upload **2–3 of your study documents** from your device or Google Drive.
3. Limits to know: up to **10 files**, each up to **100 MB** (videos can be larger). You won't get near those limits today.

> **Heads-up about the free tier:** On a free account, your bot can only actively "hold in mind" about 50 pages of text at once. If you upload a giant document and it seems to forget the later parts, that's why — not a bug. Keep your study files focused.

---

## Step 5 — Test With Three Questions

Use the preview panel on the right. Run **exactly these three kinds of tests** and write down what happens.

| Test | What to ask | What *should* happen |
|------|-------------|---------------------|
| **Known-good** | A question your notes clearly answer | It answers correctly, from your notes |
| **Known-bad** | A question your notes do **not** cover at all | It uses the honesty rule — says it's not in your notes |
| **Edge case** | Something tricky or near the boundary of your notes | You observe *how* it behaves at the edge |

> **The known-bad test is the one everyone gets wrong.** Make sure you ask something your notes genuinely don't cover. If every test "passes," your test was too easy and you learned nothing.

---

## Step 6 — Change ONE Thing (The One-Change Rule)

Look at your three test results. Find the **single biggest problem.** Change **only that one thing** in your instructions. Save. Test again.

> Do **not** rewrite the whole prompt because one test disappointed you. Change one thing, re-test, see what that one change did. That's controlled experimentation — the same discipline real engineers and scientists use. **Failure is just exercise.**

Repeat until your bot behaves the way you intend (at least one full change-and-retest cycle is required).

---

## Step 7 — Save and Submit to GitHub

Create a folder in your CSC-114 repo called `gemini-day1/` and add these three files.

**File 1 — `gem-instructions.md`**
Paste your final Gem name and the full instructions text (all three questions + the honesty rule).

**File 2 — `knowledge-sources.md`**
List the study files you uploaded and one sentence on what each one covers.

**File 3 — `testing-log.md`** — use this exact template:

```markdown
# Gemini Gem Testing Log — Day 1

## My Gem: [name]

| Test # | Type | What I asked | What it did | Pass/Fail | Notes |
|--------|------|--------------|-------------|-----------|-------|
| 1 | Known-good | [question] | [what happened] | [P/F] | |
| 2 | Known-bad | [question] | [what happened] | [P/F] | |
| 3 | Edge case | [question] | [what happened] | [P/F] | |

## The one change I made
**Before:** [what my instructions said]
**Change:** [the single thing I changed]
**After:** [what happened when I re-tested]

## Reflection (3–4 sentences)
- What did I ask the bot to do, in my own words?
- Did I have to push back on or correct the bot at any point? What did I do?
- What is one thing a Gem (an assistant) clearly *cannot* do?
```

**How to submit:**
- **Code Builders:** add, commit, and push the `gemini-day1/` folder using your normal Git workflow. Use a descriptive commit message (e.g., `Add Day 1 Gemini Gem study bot + testing log`).
- **Prompt Masters:** drag and drop the three files into a `gemini-day1/` folder using the GitHub website or GitHub Desktop. This is a real, valid way to submit — not a shortcut.

---

## Before You Leave — Checklist

- [ ] My Gem exists and has a clear, subject-specific name.
- [ ] My instructions answer all three questions **and** include the honesty rule.
- [ ] I uploaded 2–3 focused study files.
- [ ] I ran all three test types (known-good, known-bad, edge case).
- [ ] I made one controlled change and re-tested it.
- [ ] All three files are in `gemini-day1/` in my GitHub repo.

---

## What Just Happened

Today you built an **assistant**: a custom Gemini that follows a persona and answers from *your* knowledge, with an honesty rule keeping it truthful. You used the same loop you've used all along — **intend, test, change one thing, test again** — on a brand-new platform. You also saw the ceiling of an assistant: it reads and explains, but it can't take actions.

**Tomorrow** you'll move to Google AI Studio and give a bot the ability to *do* things — that's the jump from assistant to **agent**.

> **Stuck on accounts or access?** If a login or platform problem is eating your lab time (not ordinary bot-tweaking struggles), let your instructor know — they can escalate to Mallory Milstead or Andrew Norris.

---

## Grading: What "Complete" Looks Like

This is **complete / re-do** grading. You're not chasing a perfect bot — you're showing the *process*. Your work maps to the four-category rubric:

| Category | What earns "complete" |
|----------|----------------------|
| **AI Partnership Quality** | Instructions answer all three questions; honesty rule is present and clear. |
| **Problem-Solving Process** | Three tests run; one controlled change made and re-tested (not a full rewrite). |
| **Professional Communication** | Three files, organized under `gemini-day1/`, with a clear commit message. |
| **Critical Thinking & Ethics** | Your reflection shows you noticed *how* the bot behaves at its edge — and named one thing an assistant can't do. |
