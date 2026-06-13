# Use with any AI agent

`sw-guardrails` is a single Markdown file, [`SKILL.md`](./SKILL.md), holding the
full review ruleset. Because it is plain Markdown under an MIT license, almost
any AI agent or tool can use it, either by loading the rules as instructions or
by installing it through a tool-specific mechanism.

## The universal entry point: the raw file

Every method below points at the same source of truth:

```text
https://raw.githubusercontent.com/speech-works/sw-guardrails/main/SKILL.md
```

That URL always serves the latest rules from `main`. For stable, unchanging
behaviour, pin to a specific commit or tag instead:

```text
https://raw.githubusercontent.com/speech-works/sw-guardrails/<commit-or-tag>/SKILL.md
```

## Claude Code (terminal CLI), as a plugin

```text
/plugin marketplace add speech-works/sw-guardrails
/plugin install sw-guardrails@speechworks
```

## Claude Code (any client), as a skill

Clone the repo into a skills directory; Claude Code finds `SKILL.md`
automatically.

User-level, available in all your projects:

```bash
git clone https://github.com/speech-works/sw-guardrails.git ~/.claude/skills/sw-guardrails
```

Project-level, one repo (and shared with teammates if you commit it):

```bash
git clone https://github.com/speech-works/sw-guardrails.git .claude/skills/sw-guardrails
```

Then, in a session:

```text
/sw-guardrails review path/to/file
```

## Cursor, Windsurf, and other IDE agents

These tools use their own "rules" files rather than skills. Copy the contents of
[`SKILL.md`](./SKILL.md) into the tool's rules location, for example a project
`AGENTS.md`, a Cursor rule under `.cursor/rules/`, or the equivalent custom
instructions field. The agent then follows the same guardrails when it writes or
reviews content.

## Any other agent or LLM app

Fetch the file and include it in the agent's system prompt or context:

```bash
curl -sL https://raw.githubusercontent.com/speech-works/sw-guardrails/main/SKILL.md
```

Paste the output into your agent's instructions, or have the agent fetch the URL
at runtime. The ruleset is self-contained: it states what to check and how to
report findings (severity, reason, suggested rewrite).

## About the format

`SKILL.md` uses the open Agent Skills layout: YAML frontmatter with `name` and
`description`, then Markdown instructions. It has no tool-specific dependencies,
so it works as plain context anywhere. It is MIT licensed, so you are free to
copy or adapt it; attribution is appreciated.
