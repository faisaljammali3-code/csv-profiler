class person:
    def __init__(self,firstname:str, age: int)->None:
        self.firstname=firstname
        self.age=age

    @property
    def age(self)->int:
        return self._age
    
    @age.setter
    def age(self,value:int)->None:
        assert 0<= value <= 200
        self._age=value
    
    def __repr__(self):
        return f"person(firstname={self.firstname}, age={self.age})"

    def __eq__(self,other)->bool:
        return self.firstname==other.firstname and self.age==other.age

    


faisal=person("faisal",22)
faisal.age=30
print(faisal)