def md_table_header()->list[str]:
    return [
        "| Column | Type | Missing | Unique |",
        "|---|---:|---:|---:|"
        ]
def md_col_row(name: str, typ: str, missing: int, missing_pct: float, unique: int) -> str:
    return f"| {name} | {typ} | {missing} ({missing_pct:.1%}) | {unique} |"

print(md_table_header())