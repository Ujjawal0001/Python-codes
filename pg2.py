print("welcome to inspection !")
c_topics=["conditionals","loops","arrays","functions","string","pointer","pointer","dma"]
p_topics=["list","sets","tuple","dict"]
p_strong=[]
p_weak=[]
c_strong=[]
c_weak=[]
names=[]
n=int(input("Enter number of students : "))
def take_c_strong_topics(c_strong):
    #print("Enter topics in which you are strong or enter 0 to exit")
    a=1
    strong_topics=[]
    while a:
        a=input("Enter your strong topics of C or enter 0 to exit : ")   
        if (a!="0"):
            strong_topics.append(a)
        else:
            a=int(a)
    print("strong topics of C is/are", strong_topics)
    c_strong.append(strong_topics)
    weak_topics=[]
    for i in range(len(strong_topics)):
        for j in range(len(c_topics)):
            if not strong_topics[i].lower()==c_topics[j].lower():
                weak_topics.append(c_topics[j])
    c_weak.append(weak_topics)
def take_p_strong_topics(p_strong):
    #print("Enter topics in which you are strong or enter 0 to exit")
    a=1
    strong_topic=[]
    while a:
        a=input("Enter your strong topics of python or enter 0 to exit : ")   
        if (a!="0"):
            strong_topic.append(a)
        else:
            a=int(a)
    print("strong topics of python is/are", strong_topic)
    p_strong.append(strong_topic)
    weak_topic=[]
    for i in range(len(strong_topic)):
        for j in range(len(p_topics)):
            if not strong_topic[i].lower()==p_topics[j].lower():
                weak_topic.append(p_topics[j])
    p_weak.append(weak_topic)
for i in range(n):
    names.append(input("Enter your name : "))
    take_c_strong_topics(c_strong)
    take_p_strong_topics(p_strong)
    print("{}'s strong points in C is/are {} and weak points in C is/are {}".format(names,c_strong,c_weak))
    print("{}'s strong points in python is/are {} and weak points in python is/are {}".format(names,p_strong,p_weak))

for i in c_topics:
    for j in range(len(c_strong)):
        if i in c_strong[j]:
            print("{} will teach {}".format(names[j],c_strong[j]))
for i in p_topics:
    for j in range(len(p_strong)):
        if i in p_strong[j]:
            print("{} will teach {}".format(names[j],p_strong[j]))
            
            

            
