# GitHub Basics · Day 5 — The Everyday Workflow (Part 2 of 3)

Part 2 of the **3-part GitHub mini-track** (Days 4–6). Part 1 gave the *why* and the mental model;
today is **hands-on**: the four commands students will run every day for the rest of the course —
**`status` → `add` → `commit` → `push`** — plus `.gitignore` (which keeps their AI-track API keys
safe) and `pull`.

> Arc: **Day 4 — Why &amp; What** → **Day 5 — The Everyday Workflow** (this deck) →
> **Day 6 — Branching &amp; Collaboration**.

## How to present it
Self-contained `index.html` (no install). Command blocks use a dark terminal style; the workflow
diagram is **inline SVG**.
1. Double-click **`index.html`** → press **F** for fullscreen.
2. **→ / Space / click-right** = next · **← / click-left** = back · **Home/End** = jump.

~20 min. Ideally run it right before giving students the in-session time to push their Day-4 folder.

## Slide flow + speaker notes
13 slides.

| # | Slide | Talk about / ask the room |
|--:|-------|---------------------------|
| 1 | Title | "Yesterday the why; today the loop you'll run a thousand times." |
| 2 | Recap + goal | One-line callback to Day 4. Reassure: not about memorising, it becomes automatic. |
| 3 | The 3 areas | ⭐ The concept beginners trip on. Use the **parcel analogy**: edit → box (stage) → seal+label (commit) → ship (push). |
| 4 | Pipeline SVG | Walk the arrows left→right. Emphasise: add/commit are *local*; only **push** hits the internet. |
| 5 | One-time setup | `git config` once per machine; then `git init` (new) or `git clone` (existing). Don't dwell — point them at the cheat sheet. |
| 6 | The daily 4 steps | The heart of the deck. Read each line + its comment aloud. |
| 7 | `git status` | "When lost, run status." Show it literally prints the next command. No downside to running it. |
| 8 | Commit messages | The "This commit will…" trick. Read the bad vs good columns aloud — gets a laugh, sticks. |
| 9 | `.gitignore` | ⚠️ **The safety slide.** Hammer `.env` → never commit API keys. This prevents a real disaster in the AI track. |
| 10 | `git pull` | pull → work → commit → push. Start in sync, end in sync. |
| 11 | Cheat sheet | The four commands one more time. Tell them to screenshot it. |
| 12 | **GitHub Action** | Give 10–15 min in-session; TA floats. First push is always bumpy — that's fine. |
| 13 | Close | Tease Day 6: branches + pull requests. |

## Teaching tips
- **Do it live.** If you have a projector, run the four commands on a throwaway repo while you talk.
  Watching `git status` change after `add` is the lightbulb moment.
- **The first push will hurt** (auth, remote URL, default branch). Pre-warn them it's normal; have the
  TA ready. Once it works once, it works forever.
- **Don't introduce branches yet** — that's Day 6. Keep today to the linear loop so it lands cleanly.
- **`.gitignore` is non-negotiable** before the AI track. Make every student add `.env` to it today,
  even though they have no keys yet — build the reflex before the keys exist.
- Common stumbles to name: forgetting `git add` before commit; committing then forgetting to push
  ("it's not on GitHub!"); trying to commit with no message.

## Today's GitHub Action
**Push the Day-4 loops folder to a new GitHub repo:** `git init` → add a `.gitignore` → `add` →
`commit -m "..."` → create the repo on github.com → `push`. End state: their code is live online.
≤15 min, TA-supported.

## Editing
All inline in `index.html` (shared Softpro template + `.cmd` terminal blocks and `.diagram` SVG
wrapper). Copy any `<section class="slide">…</section>` to add a slide; counter/progress auto-update.

➡ Next: **[Day 6 — Branching &amp; Collaboration](../../Day-06-Data-Structures/github-basics/)**
