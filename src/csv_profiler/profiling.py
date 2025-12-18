def basic_profile(rows:list[dict[str,str]])->dict:
    """compute row count, column names, and missing values per column."""
    if not rows:
        return {"rows": 0, "columns": [], "missing": {}}
    row_count=len(rows)
    columns=list(rows[0].keys())

    # col =keys
    missing_counts = {col: 0 for col in columns}

    for row in rows:
        for col in columns:
            if row[col].strip() == "":
                missing_counts[col] += 1
    return{
        "rows": row_count,
        "columns": columns,
        "missing": missing_counts  
    }




def is_missing(value: str | None)->bool:
    """True for empyty / null . null-ish csv values."""
    if value is not None:
        value=value.strip().casefold()
    if value=="" or value=="na" or value=="none" or value=="nan" or value=="null"or value==None:
        return True
    else:
        return False
    

def try_float(value: str)-> float | None:
    """return float(value) or None if it fails."""
    try:
        return float(value)
    except ValueError:
        return None
    

def infer_type(values: list)->str:
    usable = [v for v in values if not is_missing(v)]
    if not usable:
        return "text"
    for v in usable:
        if try_float(v) is None:
            return "text"
    return "number"
    

def column_values(rows: list[dict[str,str]],col:str)-> list[str]:
    List=[]
    for row in rows:
        List.append(row.get(col,""))
    return List
def numeric_stats(values:list[str])->dict:
    """compute stats for nmeric column values (string)."""
    usable =[v for v in values if not is_missing]
    nums=[try_float(v) for v in usable]
        
    return 
def profile_rows(rows: list[dict[str, str]]) -> dict:
    if not rows:
        return {"n_rows": 0, "n_cols": 0, "column_names": [], "columns": []}
    
    n_rows = len(rows)
    names_column = list(rows[0].keys())
    col_profiles = []
    
    for col in names_column:        
        values = [row.get(col, "") for row in rows]
        usable = [v for v in values if not is_missing(v)]
        missing=len(values) - len(usable)
        missing_pct = (missing / n_rows * 100) if n_rows > 0 else 0

        state = {       
            'name': col, 
            'missing': missing,
            'missing_pct':missing_pct,
            'type': infer_type(usable),
            'unique': len(set(usable)),
            'max': None,
            'min': None,
            "mean": None,
            
        }

        if state['type'] == "number":
            nums = []
            for x in usable:
                v = try_float(x)
                if v is not None:
                    nums.append(v)
            if nums:
                state['min'] = min(nums)
                state['max'] = max(nums)
                state["mean"] = sum(nums) / len(nums)
            
        col_profiles.append(state)
                
    return {
        "n_rows": n_rows,
        "n_cols": len(names_column),
        "columns": col_profiles
    }
