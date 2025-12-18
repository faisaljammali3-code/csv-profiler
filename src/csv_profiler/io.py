from __future__ import annotations

from csv import DictReader
from pathlib import Path

def read_csv_rows(path:str | Path) -> list[dict[str,str]]:
    """read a csv as list of rows (each row is a dict of strings)."""
    path=Path(path)
    if not path.exists():
        raise FileNotFoundError("fill not found")
    with path.open(mode='r',newline="",encoding="utf-8")as file:
        csv_reader=DictReader(file)
        
        rows= [dict(row) for row in csv_reader]
        if not rows:
            raise ValueError("csv has no rows")
        return rows
    

filePath = r'C:/Users/faisal_333/bootcamp/csv-profiler/data/sample.csv'
print(read_csv_rows(filePath))