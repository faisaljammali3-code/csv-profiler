class ColumnProfiler:
    def __init__(self,name:str,inferred_type:str,total:int,missing:int,unique:int):
        self.name = name
        self.inferred_type = inferred_type
        self.total = total
        self.missing = missing
        self.unique = unique

    @property
    def missing_pct(self)->float:
        pct=(self.missing/self.total)*100
        return 0.0 if self.total <=0.0 else pct if pct<=100 else 100
    
#فيه غلط في السلايدات عندي معدله وفي عندي غلط بعد لو اجمعهم يطلع الصح

c =ColumnProfiler('faisal',"str",300,2,3)
print(c.missing_pct)

