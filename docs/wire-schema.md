# Wire Schema

Proselint has a stable, versioned, structured output for programmatic usage.
This is available via the `--output-format json` flag, and the output schema is
modelled below.

```ts
interface CheckResult {
    check_path: string;
    message: string;
    span: [number, number];
    replacements: string | null;
}

interface LintResult extends CheckResult {
    pos: [number, number];
}

enum ErrorCode {
    Unknown = -31999,
    FileError = -31998,
    LintError = -31997,
}

interface ResponseError {
    code: ErrorCode;
    message: string;
    data?: any;
}

interface SuccessFileOutput {
    diagnostics: LintResult[];
}

interface ErrorOutput {
    error: ResponseError;
}

type FileOutput = SuccessFileOutput | ErrorOutput;

interface SuccessProselintOutput {
    result: Record<string, FileOutput>;
}

type ProselintOutput = SuccessProselintOutput | ErrorOutput;
```

Every invocation of `proselint`  produces exactly one `ProselintOutput` object.
Both `ProselintOutput` and `FileOutput` are tagged unions. This means that
`ProselintOutput` will always contain one of `result` or `error`, but never
both, and the same applies to `diagnostics` and `error` for `FileOutput`.
