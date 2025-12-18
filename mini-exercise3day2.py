from datetime import datetime

def md_header(source:str)->list[str]:
    """return lines for the top of the report."""
    List=[]
    List.append("# CSV Profiling Report")
    List.append(source)
    List.append(datetime.now().isoformat(timespec='seconds'))
    return List
print(md_header("sourse"))
