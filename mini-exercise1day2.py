def is_missing(value: str | None)->bool:
    """True for empyty / null . null-ish csv values."""
    if value is not None:
        value=value.strip().casefold()
    if value=="" or value=="na" or value=="none" or value=="nan" or value=="null"or value==None:
        return True
    else:
        return False
    
print(is_missing("None"))