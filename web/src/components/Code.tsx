import { highlight, LABEL } from "@/lib/highlight";
import { CopyButton } from "./CopyButton";

/** Panel kode berwarna (diwarnai saat build). */
export async function Code({ code, lang = "text", label, copy = true }: { code: string; lang?: string; label?: string; copy?: boolean }) {
  const html = await highlight(code, lang);
  return (
    <div className="code">
      <div className="code-h">
        <span>{label ?? LABEL[lang] ?? "Kode"}</span>
        {copy && <CopyButton text={code} />}
      </div>
      <div dangerouslySetInnerHTML={{ __html: html }} />
    </div>
  );
}

export function Out({ text, label = "Keluaran" }: { text: string; label?: string }) {
  return (
    <div>
      <div className="out-l">{label}</div>
      <pre className="out">{text}</pre>
    </div>
  );
}
