def try_float(value: str)-> float | None:
    """return float(value) or None if it fails."""
    try:
        return float(value)
    except ValueError:
        return None

print(try_float('32.32'))