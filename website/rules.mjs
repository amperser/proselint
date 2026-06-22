#! /usr/bin/env node

import { readdir, readFile, writeFile } from "node:fs/promises";
import { resolve, relative } from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = fileURLToPath(new URL(".", import.meta.url));

function extractFrontmatter(fileContent) {
  return Object.fromEntries(
    (fileContent.match(/^"""([\s\S]*?)"""/m)?.[1] ?? "")
      .split("\n")
      .map((line) => line.split(":").map((part) => part.trim()))
      .filter(([key, value]) => key && value),
  );
}

async function collectMetadata(directoryPath, rootDirectory = directoryPath) {
  const entries = await readdir(directoryPath, { withFileTypes: true });

  const results = await Promise.all(
    entries.map(async (entry) => {
      const entryPath = resolve(directoryPath, entry.name);

      if (entry.isDirectory()) return collectMetadata(entryPath, rootDirectory);
      if (!entry.name.endsWith(".py") || entry.name === "__init__.py")
        return [];

      const fileContent = await readFile(entryPath, "utf8");
      const metadata = extractFrontmatter(fileContent);

      return Object.keys(metadata).length
        ? [{ ...metadata, __file__: relative(rootDirectory, entryPath) }]
        : [];
    }),
  );

  return results.flat();
}

const checksDirectory = resolve(__dirname, "..", "proselint", "checks");
const outputPath = resolve(__dirname, "public", "rules.json");

try {
  const rules = await collectMetadata(checksDirectory);
  await writeFile(outputPath, JSON.stringify(rules, null, 2));
  console.log("generated rules");
} catch (error) {
  console.error("couldn't generate rules", error);
  process.exit(1);
}
