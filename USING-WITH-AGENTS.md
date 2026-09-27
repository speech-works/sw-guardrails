# Use with any AI agent

`sw-guardrails` ships three skills, each with a Markdown `SKILL.md` under
[`skills/`](./skills):

- [`skills/sw-guardrails/SKILL.md`](./skills/sw-guardrails/SKILL.md) — the review
  ruleset (therapeutic integrity and brand voice).
- [`skills/sw-outreach/SKILL.md`](./skills/sw-outreach/SKILL.md) — drafting and
  reviewing outbound messages to the stuttering community.
- [`skills/sw-program-writing/SKILL.md`](./skills/sw-program-writing/SKILL.md):
  writing and auditing Speechworks programs in plain English. Its
  `references/` and `scripts/` folders come with it, so load the whole
  folder, not only `SKILL.md`.

Because each is plain Markdown under an MIT license, almost any AI agent or tool
can use it, either by loading the rules as instructions or by installing it
through a tool-specific mechanism.

## The universal entry point: the raw files

Every method below points at the same source of truth:

```text
https://raw.githubusercontent.com/speech-works/sw-guardrails/main/skills/sw-guardrails/SKILL.md
https://raw.githubusercontent.com/speech-works/sw-guardrails/main/skills/sw-outreach/SKILL.md
https://raw.githubusercontent.com/speech-works/sw-guardrails/main/skills/sw-program-writing/SKILL.md
```

Those URLs always serve the latest rules from `main`. For stable, unchanging
behaviour, pin to a specific commit or tag instead:

```text
https://raw.githubusercontent.com/speech-works/sw-guardrails/<commit-or-tag>/skills/sw-guardrails/SKILL.md
```

## Claude Code (terminal CLI), as a plugin

```text
/plugin marketplace add speech-works/sw-guardrails
/plugin install sw-guardrails@speechworks
```

All three skills come with the plugin.

## Claude Code (any client), as skills

Do not copy these skills into a project's `.claude/skills` or `.agents/skills`.
This repo is the single source of truth for Speechworks skills, and a copy goes
stale (sw-blog's copies did). Install the plugin once at user level instead:

```bash
claude plugin marketplace add speech-works/sw-guardrails   # or a local path to this repo
claude plugin install sw-guardrails@speechworks
```

After you change a skill here, refresh the installed plugin:

```bash
claude plugin marketplace update speechworks
claude plugin update sw-guardrails@speechworks
```

## Cursor, Windsurf, and other IDE agents

These tools use their own "rules" files rather than skills. Copy the contents of
the relevant `SKILL.md` (the reviewer, the outreach writer, or both) into the
tool's rules location, for example a project `AGENTS.md`, a Cursor rule under
`.cursor/rules/`, or the equivalent custom instructions field. The agent then
follows the same guidance when it writes or reviews content.

## Any other agent or LLM app

Fetch the file you need and include it in the agent's system prompt or context:

```bash
curl -sL https://raw.githubusercontent.com/speech-works/sw-guardrails/main/skills/sw-outreach/SKILL.md
https://raw.githubusercontent.com/speech-works/sw-guardrails/main/skills/sw-program-writing/SKILL.md
```

Paste the output into your agent's instructions, or have the agent fetch the URL
at runtime. Each ruleset is self-contained: it states what to check and how to
report findings (severity, reason, suggested rewrite).

## About the format

Each `SKILL.md` uses the open Agent Skills layout: YAML frontmatter with `name`
and `description`, then Markdown instructions. There are no tool-specific
dependencies, so they work as plain context anywhere. Both are MIT licensed, so
you are free to copy or adapt them; attribution is appreciated.
