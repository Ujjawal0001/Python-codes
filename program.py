print("Welcome to the Inspection!")

c_topics = ["Variables", "Data Types", "Input", "Output","Conditionals", "Functions", "loops","arrays","Pointers","String","DMA","Structure","Union","Linked List"]

n = int(input("How many of you are there?"))
 
names = []
c_strong = []
c_weak = []

def take_c_strong_topics(c_strong):
    print("Please enter your strong topics. Please enter 0 to exit")
    a = 1
    strong_topics =  []
    while a:
        a = input("Your topic please. Enter 0 to exit.")
        if(a != "0"):
            strong_topics.append(a)
        else:
            a = int(a)
    print(f"strong topics : {strong_topics}")    
    c_strong.append(strong_topics)
    weak_topics =  []
    for i in range(len(strong_topics)):
        for j in range(len(c_topics)):
            if not strong_topics[i].lower() == c_topics[j].lower():
                weak_topics.append(c_topics[j])
    c_weak.append(weak_topics)            
            
    
    
    
# def take_c_weak_topics(c_weak):
#     print("Please enter your weak topics. Please enter 0 to exit")
#     a = 1
#     weak_topics =  []
#     while a:
#         a = input("Your topic please. Enter 0 to exit.")
#         if(a != "0"):
#             weak_topics.append(a)
#         else:
#             a = int(a)    
#     print(f"weak topics : {weak_topics}")        
#     c_weak.append(weak_topics)
    
 
# iterate through strong points - topic, teacher
# dict
# topic - []
# 

for i in range(n):
    names.append(input("Enter your name: "))
    take_c_strong_topics(c_strong)
    print(f" {names}'s strong points are : {c_strong} and weak points are : {c_weak}")
    
for i in range(len(c_strong)):
    print(f"{names[i]} : {c_strong[i]}")
    
    
    
for i in c_topics:
    for j in range(len(c_strong)):
        if i in c_strong[j]:
            print(f"{names[j]} will teach {c_strong[j]}")
