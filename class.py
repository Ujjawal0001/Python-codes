class Coffee:
    def _init_(s, type, base, sugarfree):
        print("creating coffee object")
        s.type = type
        s.base = base
        s.sugarfree = sugarfree
        
    def make_americano(ujjwal):
        print("making americano")
 
    def make_latte(self):
        # print(self)
        print("making latte")
    
    def init():
        print("making tea")
     
        
# cold_coffee = Coffee("cold", "milk", True)  
# print(cold_coffee.type)
# print(cold_coffee.base)
# print(cold_coffee.sugarfree)


# hot_coffee = Coffee("hot", "water", False)  
# print(hot_coffee.type)
# print(hot_coffee.base)
# print(hot_coffee.sugarfree)

# print(id(hot_coffee))

# hot_coffee.make_americano()
# hot_coffee.make_latte()
# Coffee.init()



class ChildCoffee(Coffee):
    def _init_(self, price, type, base, sugarfree):
        print("making child coffee")
        self.price = price
        self.type=t
        super()._init_(type, base, sugarfree)
    
    def make_latte(self):
        # print(self)
        print("making cold latte")    

c_coffee = ChildCoffee(230, "cold", "milk", False)   
c_coffee.make_latte()

print(c_coffee.type)
