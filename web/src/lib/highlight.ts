import { createHighlighter, type Highlighter } from "shiki";

/* Pewarnaan kode dilakukan saat build, jadi browser tidak perlu mengunduh pustaka pewarna. */

const LANGS = ["java", "python", "sql", "ts", "tsx", "js", "jsx", "html", "css", "scss", "bash", "json", "yaml",
  "toml", "dart", "kotlin", "swift", "xml", "markdown", "graphql", "hcl", "dockerfile", "ini", "gherkin", "jinja"] as const;
const ALIAS: Record<string, string> = { docker: "dockerfile", conf: "ini", django: "jinja", shell: "bash", sh: "bash", py: "python" };

export const LABEL: Record<string, string> = {
  dart: "Dart", kotlin: "Kotlin", java: "Java", python: "Python", sql: "SQL", ts: "TypeScript", js: "JavaScript", jsx: "JSX",
  html: "HTML", css: "CSS", bash: "Terminal", yaml: "YAML", json: "JSON", markdown: "Markdown", swift: "Swift", xml: "XML",
  toml: "TOML", excel: "Spreadsheet", docker: "Dockerfile", hcl: "Terraform", text: "Teks", tsx: "TSX", scss: "SCSS",
  graphql: "GraphQL", django: "Template Django", conf: "Konfigurasi", gherkin: "Gherkin",
};

let hl: Promise<Highlighter> | null = null;
function get() {
  hl ??= createHighlighter({ themes: ["github-light-default", "github-dark-default"], langs: [...LANGS] });
  return hl;
}

const esc = (s: string) => s.replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[c]!);

/** HTML <pre> berwarna untuk tema terang dan gelap sekaligus (CSS memilih lewat variabel). */
export async function highlight(code: string, lang = "text"): Promise<string> {
  const l = ALIAS[lang] ?? lang;
  if (!(LANGS as readonly string[]).includes(l)) return `<pre class="shiki plain" tabindex="0"><code>${esc(code)}</code></pre>`;
  const h = await get();
  return h
    .codeToHtml(code, { lang: l, themes: { light: "github-light-default", dark: "github-dark-default" }, defaultColor: false })
    // warna komentar tema terang dipergelap sedikit agar kontrasnya lolos WCAG AA (4.5:1)
    .replaceAll("--shiki-light:#6E7781", "--shiki-light:#57606A");
}
