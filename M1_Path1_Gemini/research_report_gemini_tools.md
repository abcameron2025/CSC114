# Building Domain-Specific AI Assistants and Agents with Google's Gemini Ecosystem: A Parallel Pathway to Claude for CSC-113 and CSC-114

## TL;DR
- **The Gemini path cleanly mirrors your Claude path and is genuinely lower-friction at the entry point:** a **Gemini Gem** (gemini.google.com) is the no-code, persona-plus-knowledge analog of a Claude Project, and **Google AI Studio + the Gemini API** (aistudio.google.com) is the developer-facing analog of the Anthropic Console — but unlike the Console, both Gems AND a working API key are reachable on a **free personal Google account with no credit card**, removing the billing-account hurdle your less-technical students stumble on.
- **Map for the pedagogy:** Gems are **assistants** (persona + up to 10 knowledge files, largely reactive, no custom tool-calling). True **agent** behavior — function calling, Google Search grounding, code execution, multi-step autonomy — lives in the Gemini API/AI Studio; the gentlest on-ramp to agent behavior with the least code is **Google Opal** (no-code "agent step," free Labs experiment) or AI Studio's built-in tool toggles before students touch the SDK.
- **Critical setup constraints to flag throughout:** students must **bring a personal Google account** (your college doesn't enable Workspace Gemini); the **13+ age minimum** applies to Gems on personal accounts (18+ for AI Studio and most paid/agentic features, and 18+ for all Gemini Apps in the EEA/UK/Switzerland); the once-generous **free 12-month Google AI Pro student offer has ended** (Google's student page now reads "Our previous student offer ended on March 11, 2026"; US final redemption was April 30, 2026); and on the **free tier Google may use prompts/uploads for product improvement and human review**, so students should never upload confidential material.

## Key Findings

### 1. Gemini Gems = the Claude Project analog (no-code assistant)
- A Gem is a saved, reusable custom version of Gemini with its own **name, instructions (system prompt), and an optional Knowledge base of uploaded files**. Functionally it is the direct counterpart to a Claude Project's "project instructions + uploaded knowledge."
- On the chatbot/assistant/agent spectrum, **Gems are assistants**: persona + knowledge, still largely reactive. They cannot perform genuine custom function-calling or run developer-defined tools. (They inherit whatever the Gemini app itself can do — image generation, Drive lookups when connected — but you cannot give a Gem custom tools/actions the way an agent uses them.)
- **Free personal-account users CAN create Gems and CAN upload Knowledge files** — confirmed against current official Google support pages (June 2026). Gems show a checkmark for "Without a Google AI plan" in Google's feature-availability table (support.google.com/gemini/answer/16275805), and the only stated requirement to create/use Gems on a personal account is being **13 or older**.

### 2. Free vs. paid — what actually changes for students
- **Gems are free.** This is a real advantage over OpenAI, where creating Custom GPTs requires the paid ChatGPT Plus plan. Anyone with a free Google account can create and use Gems.
- The **knowledge-file caps are identical on free and paid** — Google's Gemini Apps Help states verbatim: "Up to 10 files (subject to availability) can be uploaded in the same prompt. Each video can be up to 2 GB. All other supported file types can be up to 100 MB." The real free-vs-paid lever for a knowledge-heavy classroom Gem is the **context window**, not the file caps (see Details).
- **Pricing (current, mid-2026, post–Google I/O 2026):** the consumer tiers are **Google AI Plus $7.99/mo, Google AI Pro $19.99/mo, and Google AI Ultra starting at $99.99/mo**. Per The Decoder (May 19, 2026), at I/O 2026 "Google also cut the price of its previous top tier from $250 to $200," so a higher-limit Ultra tier now sits at **$199.99/mo**.
- **Model access:** free users get the current default Flash-class model and limited access to the Pro reasoning model; paid users (AI Pro/Ultra) get fuller access to the Pro model and the **1-million-token context window**.

### 3. Google AI Studio + Gemini API = the Anthropic Console analog (agent progression)
- **Google AI Studio (aistudio.google.com) is free**, browser-based, and accessible by signing in with a personal Google account — no credit card, no subscription. It is the "fastest way to build with Gemini" and is where students generate an **API key in a couple of clicks** ("Get API key" → "Create API key"; the key begins `AIza...`).
- The **Gemini API has a permanent free tier** (not a time-limited trial). A free key works against current Flash/Flash-Lite models. For the current default Flash model, PE Collective (citing Google's docs, May 2026) reports the free tier runs exactly **10 requests per minute, 250,000 tokens per minute, and 1,500 requests per day**, with the full 1M-token context window. Quotas are **per Google Cloud project, not per key**, and reset at midnight Pacific. **No billing account is required to start.**
- **Agent capabilities via the API:** function calling (custom tools), **Grounding with Google Search** (returns citations/groundingMetadata), **code execution** (Python sandbox, server-side, matplotlib for charts, no custom libraries, no extra charge beyond tokens), **URL context**, and structured outputs. For Gemini 3-class models, built-in tools can be **combined with custom function calls in a single turn** ("context circulation"). This is where genuine agent behavior lives.
- **Lowest-code path to real agent behavior:** For a non-technical-leaning student, the gentlest on-ramp is **Google Opal** (Google Labs, free) — a no-code visual workflow builder whose 2026 "agent step" (launched Feb 24, 2026, powered by Gemini 3 Flash) lets Gemini plan, pick tools, use persistent memory (via Google Sheets), and ask the user clarifying questions. Next rung up is flipping on built-in tools (Search grounding, code execution) right inside AI Studio. The full-code rung is Google's open-source **Agent Development Kit (ADK)**, which can run from an AI Studio API key.

### 4. Friction comparison — is Gemini lower-friction than the Anthropic Console?
**Yes, at the on-ramp.** The instructor's concern that the Anthropic Console "buy-in involves more effort than some less-technical students are comfortable with" is well-founded, and the Gemini path reduces it in two specific places:
- **Entry assistant:** Gem creation is free and requires nothing but a Google account (which most students already have). Claude Projects requires a Claude.ai account and, for meaningful use, typically a Claude Pro subscription.
- **Developer step:** A student can get a **working Gemini API key from a free personal account with no credit card and no billing setup**, and immediately test tool-use in AI Studio's playground. This is the single biggest friction reduction versus standing up the Anthropic Console for the first time.
- **Where Gemini friction still appears:** (a) the **18+ age requirement** for Google AI Studio and most agentic/paid features (vs. 13+ for Gems) can exclude some students; (b) moving beyond free-tier rate limits, removing the data-training clause, or using **Pro models in the API** requires **enabling Cloud billing** — Google removed the Pro series from the API free tier in 2026 (Gemini 2.5 Pro remains free-tier only at a trial-grade 5 RPM / 100 RPD); (c) the **API quota/billing model changed substantively in 2026** (prepaid billing for new accounts, Pro models behind billing), so any older tutorial will mislead.

### 5. Practical classroom and privacy notes
- **Bring-your-own personal Google account is required** (your college doesn't enable Workspace Gemini). Reinforce this in every handout.
- **Privacy:** on the **free consumer tier, Google may use prompts, uploaded files, and responses to improve products, and a subset of chats are human-reviewed** (reviewed data retained up to 3 years, disconnected from the account; default activity retention 18 months, changeable). Google's own notice says: "Please don't enter confidential information that you wouldn't want a reviewer to see or Google to use to improve our services." Paid consumer plans and Workspace accounts have stronger data handling. Students should treat classroom Gems as **public-facing** and never upload personal/sensitive documents.
- **Recent changes / deprecations to teach around:** Bard → Gemini rename (Feb 2024); MakerSuite → Google AI Studio rename; Gems went free for all users in 2025; the **Gemini student free-year offer has ended**; the API free tier was tightened and Pro models moved behind billing in 2026; Opal added its agentic "agent step" in Feb 2026.

## Details

### Gems — what they are and how to build one
A Gem is created at **gemini.google.com → sidebar → Gems → New Gem** (web only for creation; Gems can be *used* on mobile). The builder exposes:
- **Name** (descriptive, e.g., "CSC-113 Syllabus Helper").
- **Instructions** — the system prompt. Google recommends covering four areas: **Persona, Task, Context, and Format.** A "**Use Gemini to re-write instructions**" button (magic-wand) expands a one-line goal into structured instructions — useful for ESL/mixed-ability learners who can brain-dump a goal and have Gemini format it.
- **Knowledge** — "Add files" to upload reference docs (device, Google Drive, or a NotebookLM notebook). **Up to 10 files, each up to 100 MB** (videos up to 2 GB). An option to **"Disable knowledge citations"** exists. Drive uploads require Keep Activity on and Workspace connected.
- **Preview pane** — test prompts on the right before saving. (Previewing does NOT auto-save; students must click **Save**.)
- Five **premade Gems** (Brainstormer, Career Guide, Coding Partner, Learning Coach, Writing Editor) can be copied and modified as templates.

**Gems vs. Claude Projects (functional):** Both = persona + instructions + uploaded knowledge, no-code, reactive. Claude Projects emphasize a shared team knowledge base; Gems emphasize personal reuse and tight Google ecosystem/Drive integration. Neither is a true agent. A pedagogically clean classroom line: **"A Gem is to Gemini what a Project is to Claude — an assistant, not an agent."**

**Important free-tier nuance for knowledge-heavy Gems:** although free users can attach the full 10 files, the context window differs sharply by tier. Per 9to5Google quoting Google: "The context window on the free tier, which applies to all models, is 32,000 tokens or 'around 50 pages of text.' Google AI Pro and AI Ultra users get a long context window of 1 million tokens... equivalent to 1,500 pages of text or 30,000 lines of code." So a free Gem can only actively reason over ~50 pages at once. For a course Gem grounded in a long syllabus or textbook, this matters — a paid tier dramatically increases how much the Gem can "hold in mind." (For document-heavy study, **NotebookLM**'s free plan — 100 notebooks, 50 sources per notebook, up to 500,000 words per source — is often a better fit.)

### Google AI Studio and the Gemini API
- **Access:** sign in at aistudio.google.com with a personal Google account, accept the Generative AI terms, click **"Get API key" → "Create API key."** Treat the key as a password.
- **Free tier reality (2026):** AI Studio itself is always free; the API underneath has a free tier (Flash/Flash-Lite) and a paid tier. Quotas are **per Google Cloud project, not per key** (extra keys don't add quota), and reset at midnight Pacific. Free-tier traffic **may be used for product improvement and human review**; paid keys are not.
- **Models to recommend for students (2026):** the **Flash** class is the workhorse (good quality, cheap, generous limits — 10 RPM / 1,500 RPD free); **Flash-Lite** for high-throughput/cheap bulk tasks (higher RPM); **Pro** class for hard reasoning (tightly rate-limited; Gemini 2.5 Pro free-tier only at 5 RPM/100 RPD, and Gemini 3.x Pro is paid-only in the API). Token cost tradeoff: Flash-Lite is cheapest per million tokens; Pro is the most expensive. **Start students on Flash.**
- **Agent toolbox (API):** `google_search` grounding, `code_execution`, `url_context`, function calling for custom tools, and structured outputs. Built-in tools execute on Google's servers within one API call; custom tools/computer-use require the app to execute the function and return results.
- **Beyond the API:** **Opal** (no-code mini-apps + agent step, free Labs, now in 160+ countries), and the open-source **ADK** (Python/TypeScript/Go/Java; `adk run`/`adk web`; deployable to Google Cloud). ADK can authenticate with a simple AI Studio API key for getting-started use.

### Direct comparison table material

| Dimension | Gemini Gem | Claude Project | Google AI Studio / Gemini API | Anthropic Console / Claude API |
|---|---|---|---|---|
| Spectrum role | Assistant | Assistant | Agent platform | Agent platform |
| No-code? | Yes | Yes | AI Studio playground = no/low-code; API = code | Console playground = low-code; API = code |
| Account/billing friction | Lowest — free Google account, no card | Low — Claude account; Pro recommended | Low — free key, no card to start; billing for scale | Higher — Console + API key + billing for real use |
| Knowledge files | Up to 10 files, 100 MB each (video 2 GB) | Project knowledge uploads | File API / inline (up to 100 MB inline) | Files API |
| Tool / function calling | No (reactive) | No (Projects are reactive) | Yes — function calling, Search grounding, code exec | Yes — tool use, MCP, Managed Agents |
| Age min | 13+ (personal; 18+ in EEA/UK/CH) | per Anthropic terms | 18+ | per Anthropic terms |

### Friction specifics
- **Gemini's standout advantage:** a no-credit-card API key from a free account. This directly addresses the instructor's friction concern at the developer step.
- **Watch-outs:** 18+ for AI Studio; billing required to escape free-tier rate limits, to silence the data-training clause, or to use Pro models in the API; 2026 billing changes (prepaid, Pro-behind-billing) mean old tutorials are stale.

### Privacy and data handling
- **Free consumer Gemini:** prompts, uploads, and responses may be used to improve Google products; a subset is human-reviewed; reviewed data retained up to 3 years (disconnected from account); default activity retention 18 months (changeable). Google explicitly warns not to enter confidential info.
- **Paid consumer (AI Pro/Ultra):** data excluded from general model training by default, but human review can still occur for safety; retention still applies.
- **Workspace (not available to this college):** content not human-reviewed or used for training outside the domain without permission.
- **API:** free tier may be used for improvement and human review; paid tier inputs not used for training.

### Recent changes / deprecations (2025–2026)
- **Bard → Gemini** (Feb 2024).
- **MakerSuite → Google AI Studio** (renamed; AI Studio is the current developer entry point).
- **Gems went free for all users** in 2025 (previously a Gemini Advanced perk).
- **Knowledge-file uploads in Gems** originally launched (Nov 2024) restricted to Advanced/Workspace; now available to free personal accounts per current official docs.
- **Google AI Pro free 12-month student offer ENDED** (Google's student page: "Our previous student offer ended on March 11, 2026"; US final redemption April 30, 2026). No separate student price now; family sharing is the cheapest legitimate route (full AI Pro split up to 6 ways ≈ $3.33/person/month).
- **API free tier tightened**; Pro models moved behind billing; prepaid billing introduced for new accounts (2026).
- **Opal "agent step"** launched Feb 24, 2026 (Gemini 3 Flash-powered).

## Recommendations

**Stage 1 — CSC-113 entry (assistant, mirrors Claude Project):**
- Have every student create a personal Google account (if needed) and confirm **13+** (18+ if in the EEA/UK/Switzerland). Build a **domain-specific Gem** with instructions (Persona/Task/Context/Format) + 2–3 knowledge files. Use the magic-wand instruction re-writer for ESL/mixed-ability support. Teach the explicit lesson: **Gem = assistant, not agent.**
- Benchmark to advance: students can articulate why a Gem can't "take actions," and can show a Gem grounded in uploaded knowledge with citations on/off.

**Stage 2 — CSC-114 bridge (no-code agent):**
- Introduce **Google Opal** as the no-code agent rung. Students build a multi-step mini-app and add an **agent step** so Gemini plans, picks tools, and uses memory. This demonstrates agency (tool selection, multi-step, human-in-the-loop) without code. Confirm regional availability for each student.

**Stage 3 — CSC-114 developer step (true agent, mirrors Anthropic Console):**
- Students 18+ sign into **AI Studio**, generate a **free API key**, and test **function calling + Google Search grounding + code execution** in the playground first, then in minimal Python via the `google-genai` SDK. Start on **Flash**. Teach quota basics (per-project; 10 RPM / 1,500 RPD on free Flash; midnight-PT reset) and key security (never commit keys; restrict the key to the Generative Language API).
- Benchmark to advance: a student-built script where Gemini calls a custom function or grounds an answer in live Search with visible citations = genuine agent behavior achieved.

**Thresholds that change the plan:**
- If many students are **under 18**, keep the developer step to instructor-run demos and lean on Gems + Opal for hands-on work.
- If students **hit free-tier rate limits** (429 errors) or need Pro models, that's the signal to discuss enabling Cloud billing (and budget alerts) — but for a class, the free tier is sufficient for learning.
- If a knowledge-heavy Gem **misses details in large documents**, that's the free-tier 32K-token context ceiling; consider NotebookLM (free, larger source limits) for document-grounded study, or note where a paid tier (1M tokens) would help.

## Caveats
- **Fast-moving space.** Model names, prices, rate limits, and free-tier eligibility changed multiple times in 2025–2026 (notably the I/O 2026 subscription overhaul and the 2026 API billing changes). Re-verify pricing and limits against gemini.google/subscriptions, ai.google.dev, and support.google.com before each term.
- **Free-tier knowledge-file access for Gems** is confirmed by current official Google pages but is not stated in a single explicit "free users can upload knowledge files" sentence; it is inferred from the feature-availability table plus the absence of any paywall language, and Google appends "subject to availability." Some older third-party articles still claim it's paid-only — those are outdated.
- **Rate-limit numbers vary by source and date** because Google shows live, project-specific limits in AI Studio that depend on model, region, account age, and billing state. Treat any single published RPM/RPD figure as a starting point; the authoritative number is the one AI Studio shows for the student's own project.
- **Opal and ADK** are evolving (Opal is an experimental Labs product; ADK targets production/enterprise). Opal's regional availability and feature set may shift.
- This report assumes **personal accounts**; all Workspace-specific data protections do NOT apply to your students.