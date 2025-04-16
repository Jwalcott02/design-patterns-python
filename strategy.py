class Strategy:
    def do_algorithm(self, data):
        raise NotImplementedError
    
class NormalSotrtingStragety(Strategy):
    def do_algorithm(self, data):
        return sorted(data)
        

class ReverseSotrtingStragety(Strategy):
   def do_algorithm(self, data): 
        return sorted(data, reverse= True)
   
class UpperCaseSortingStragety(Strategy):
    def do_algorithm(self, data): 
        return [item.upper() for item in data]
    

class Context:
    def __init__(self, stragety):
        self._stragety = stragety

    def set_stragety(self, stragety):
        self._stragety = stragety

    def execute_stragety(self, data):
        print("context: Sorting data using the stragety (not sure how it'll do it)")
        result = self._stragety.do_algorithm(data)
        print(" ,".join(result))

#usuage
data = ["a" , "b" , "c" , "d" ,"e"]

context = Context(NormalSotrtingStragety())
print("Client: Stragety is set to normal sorting")
context.execute_stragety(data)

context = Context(ReverseSotrtingStragety())
print("Client: Stragety is set to reverse sorting")
context.execute_stragety(data)

context = Context(UpperCaseSortingStragety())
print("Client: Stragety is set to uppercase sorting")
context.execute_stragety(data)
