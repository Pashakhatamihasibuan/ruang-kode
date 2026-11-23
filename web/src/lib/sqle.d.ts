export interface SqlResultRows { kind: "rows"; cols: string[]; rows: unknown[][]; type?: string; sql?: string }
export interface SqlResultMsg { kind: "msg"; msg: string; type?: string; sql?: string }
export type SqlResult = SqlResultRows | SqlResultMsg;
export interface SqlTable { name: string; view?: boolean; rows?: number; cols: { name: string; type?: string }[] }
export declare const SQLE: {
  create(seed: string): unknown;
  exec(db: unknown, sql: string): SqlResult[];
  schema(db: unknown): SqlTable[];
  fmt(v: unknown): string;
};
export declare const SEED: Record<string, string>;
