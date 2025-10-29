import { defineConfig } from "vite";
import { ViteEjsPlugin } from "vite-plugin-ejs";
import { resolve } from "node:path";
import { readFile } from "node:fs/promises";

export default defineConfig({
  root: process.cwd(),
  publicDir: "public",
  plugins: [
    ViteEjsPlugin({
      rules: await readFile(resolve(__dirname, "rules.json"), "utf8").then(
        JSON.parse,
      ),
    }),
  ],
  build: {
    outDir: "dist",
    emptyOutDir: true,
    rollupOptions: {
      input: ["index", "rules", "help"].reduce(
        (acc, name) => ({
          ...acc,
          [name]: resolve(__dirname, `${name}.html`),
        }),
        {},
      ),
    },
  },
});
