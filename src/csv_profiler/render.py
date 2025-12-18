from __future__ import annotations
from datetime import datetime

def render_markdown(report: dict) -> str:
    lines = []
    
    # العنوان والتاريخ
    lines.append("# CSV Profiling Report")
    lines.append(f"Generated: {datetime.now().isoformat(timespec='seconds')}\n")
    
    # الملخص
    lines.append("## Summary")
    lines.append(f"- **Rows:** {report['n_rows']}")
    lines.append(f"- **Columns:** {report['n_cols']}\n")
    
    # الجدول
    lines.append("## Columns Overview")
    lines.append("| Column | Type | Missing | Unique |")
    lines.append("|---|---|---|---|")
    
    for col in report["columns"]:
        name = col['name']
        ctype = col['type']
        miss = f"{col['missing']} ({col['missing_pct']:.1f}%)"
        uniq = col['unique']
        lines.append(f"| {name} | {ctype} | {miss} | {uniq} |")
    
    lines.append("")
    return "\n".join(lines)