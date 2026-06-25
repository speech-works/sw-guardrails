# Use with any AI agent

`sw-guardrails` ships two skills, each a single Markdown `SKILL.md` under
[`skills/`](./skills):

- [`skills/sw-guardrails/SKILL.md`](./skills/sw-guardrails/SKILL.md) — the review
  ruleset (therapeutic integrity and brand voice).
- [`skills/sw-outreach/SKILL.md`](./skills/sw-outreach/SKILL.md) — drafting and
  reviewing outbound messages to the stuttering community.

Because each is plain Markdown under an MIT license, almost any AI agent or tool
can use it, either by loading the rules as instructions or by installing it
through a tool-specific mechanism.

## The universal entry point: the raw files

Every method below points at the same source of truth:

```text
https://raw.githubusercontent.com/speech-works/sw-guardrails/main/skills/sw-guardrails/SKILL.md
https://raw.githubusercontent.com/speech-works/sw-guardrails/main/skills/sw-outreach/SKILL.md
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

Both skills come with the plugin.

## Claude Code (any client), as skills

Clone the repo and copy the skill folders into a skills directory; Claude Code
finds each `SKILL.md` automatically.

User-level, available in all your projects:

```bash
git clone https://github.com/speech-works/sw-guardrails.git /tmp/sw-guardrails
cp -R /tmp/sw-guardrails/skills/* ~/.claude/skills/
```

Project-level, one repo (and shared with teammates if you commit it):

```bash
git clone https://github.com/speech-works/sw-guardrails.git /tmp/sw-guardrails
cp -R /tmp/sw-guardrails/skills/* .claude/skills/
```

Then, in a session:

```text
/sw-guardrails review path/to/file
/sw-outreach draft a reply to a community contact
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
```

Paste the output into your agent's instructions, or have the agent fetch the URL
at runtime. Each ruleset is self-contained: it states what to check and how to
report findings (severity, reason, suggested rewrite).

## About the format

Each `SKILL.md` uses the open Agent Skills layout: YAML frontmatter with `name`
and `description`, then Markdown instructions. There are no tool-specific
dependencies, so they work as plain context anywhere. Both are MIT licensed, so
you are free to copy or adapt them; attribution is appreciated.
