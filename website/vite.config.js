import { defineConfig } from "vite";
import { ViteEjsPlugin } from "vite-plugin-ejs";
import { resolve } from "node:path";
import { readFile, readdir } from "node:fs/promises";

const rules = await readFile(
  resolve(__dirname, "public", "rules.json"),
  "utf8",
);

const pages = (await readdir(resolve(__dirname, "src"))).filter((x) =>
  x.endsWith(".html"),
);

export default defineConfig({
  root: "src",
  publicDir: "public",
  plugins: [
    ViteEjsPlugin({
      rules: JSON.parse(rules),
      apiURL: "http://localhost:8000",
    }),
  ],
  build: {
    outDir: "../dist",
    emptyOutDir: true,
    rollupOptions: {
      input: Object.fromEntries(
        pages.map((x) => [x, resolve(__dirname, "src", x)]),
      ),
    },
  },
});
