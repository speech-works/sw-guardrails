#!/usr/bin/env node
/**
 * Extract a program's reader-facing copy into one Markdown file per day, so
 * the plain-English checker, the boilerplate scan and the blind readers can
 * read it.
 *
 * Reads the compiled seed in sw-be-2 (dist/), the same way
 * scripts/packDepthReport.cjs does. Run `npm run build` in sw-be-2 first.
 * Read only. It never writes into sw-be-2.
 *
 * Usage (from anywhere):
 *   node extract_program.cjs --repo=/path/to/sw-be-2 --program=art_of_disclosure --out=/tmp/aod
 *   node extract_program.cjs --repo=/path/to/sw-be-2 --all --out=/tmp/programs
 *
 * Output: <out>/<catalogKey>/day-01.md ... plus <out>/<catalogKey>/program.md
 * (title and description). With --all, one folder per program.
 *
 * Shared promises from src/seed/pack/sharedCopy.ts are replaced by a marker
 * such as [SHARED:SKIP_IS_A_CHOICE], because they are meant to be identical in
 * every program and would drown the boilerplate scan.
 */
const fs = require("fs");
const path = require("path");

const args = process.argv.slice(2);
const arg = (name) => (args.find((a) => a.startsWith(`--${name}=`)) || "").split("=").slice(1).join("=");
const repo = path.resolve(arg("repo") || process.cwd());
const only = arg("program");
const all = args.includes("--all");
const out = path.resolve(arg("out") || "program-copy");

if (!only && !all) {
  console.error("Pass --program=<catalogKey> or --all.");
  process.exit(2);
}
const distPack = path.join(repo, "dist/seed/pack/index.cjs");
if (!fs.existsSync(distPack)) {
  console.error(`${distPack} is missing. Run \`npm run build\` in sw-be-2 first.`);
  process.exit(2);
}

// The seed imports entities with circular requires. The warnings are noise.
process.removeAllListeners("warning");
process.on("warning", () => {});

const { PackSeed } = require(distPack);
const { ProgramQuizQuestions } = require(path.join(repo, "dist/seed/question/programQuiz.cjs"));
let shared = {};
try {
  shared = require(path.join(repo, "dist/seed/pack/sharedCopy.cjs"));
} catch (_) {
  /* older builds have no sharedCopy */
}

const questions = new Map(ProgramQuizQuestions.map((q) => [q.shortId, q]));
const markShared = (text) => {
  let t = String(text ?? "");
  for (const [name, value] of Object.entries(shared)) {
    if (typeof value === "string" && value.length > 20) t = t.split(value).join(`[SHARED:${name}]`);
  }
  return t;
};

const programs = PackSeed.filter((p) => p.catalogKey && (all || p.catalogKey === only));
if (!programs.length) {
  console.error(`No sellable program with catalogKey "${only}".`);
  process.exit(1);
}

const ACTIVITY_FIELDS = [
  "titleOverride",
  "descriptionOverride",
  "instructionsOverride",
  "encouragementOverride",
  "completionPromptOverride",
  "completionPlaceholderOverride",
];

for (const p of programs) {
  const dir = path.join(out, p.catalogKey);
  fs.mkdirSync(dir, { recursive: true });
  fs.writeFileSync(
    path.join(dir, "program.md"),
    `# ${p.title}\n\n${markShared(p.description)}\n`,
  );
  for (const m of [...p.modules].sort((a, b) => a.dayIndex - b.dayIndex)) {
    const L = [`# ${m.title}`, "", markShared(m.description), ""];
    for (const b of [...m.blocks].sort((a, c) => a.orderIndex - c.orderIndex)) {
      const c = b.content || {};
      const tag = [b.orderIndex, b.type, c.role || c.mode || c.refId || ""].filter(Boolean).join(" ");
      L.push(`<!-- block ${tag}${c.sources ? ` sources: ${c.sources.join(", ")}` : ""} -->`, "");
      if (b.type === "TEXT") L.push(markShared(c.markdown), "");
      if (b.type === "ACTIVITY" || b.type === "FORM") {
        for (const f of ACTIVITY_FIELDS) if (c[f]) L.push(markShared(c[f]), "");
      }
      if (b.type === "GOALS" && c.prompt) L.push(markShared(c.prompt), "");
      if (b.type === "WEEK_REVIEW") L.push(...[c.title, c.intro].filter(Boolean).map(markShared), "");
      if (b.type === "QUIZ") {
        for (const key of c.questionKeys || []) {
          const q = questions.get(key);
          if (!q) {
            L.push(`MISSING QUESTION ${key}`, "");
            continue;
          }
          L.push(`**${key}** ${q.text}`, "");
          for (const o of q.options || []) {
            L.push(`- ${o.isCorrect ? "(right) " : ""}${o.text}`, `  ${o.explanation || "NO EXPLANATION"}`);
          }
          L.push("");
        }
      }
    }
    const name = `day-${String(m.dayIndex).padStart(2, "0")}.md`;
    fs.writeFileSync(path.join(dir, name), L.join("\n"));
  }
  console.log(`${p.catalogKey}: ${p.modules.length} days -> ${dir}`);
}
