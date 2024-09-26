print("welcome to inspection !")
c_topics=["conditionals","loops","arrays","functions","string","pointer","pointer","dma"]
c_strong=[]
c_weak=[]
names=[]
n=int(input("Enter number of students : "))
def take_c_strong_topics(c_strong):
    #print("Enter topics in which you are strong or enter 0 to exit")
    a=1
    strong_topics=[]
    while a:
        a=input("Enter your strong topics or Enter 0 to exit : ")   
        if (a!="0"):
            strong_topics.append(a)
        else:
            a=int(a)
    print("strong topics are", strong_topics)
    c_strong.append(strong_topics)
    weak_topics=[]
    for i in range(len(strong_topics)):
        for j in range(len(c_topics)):
            if not strong_topics[i].lower()==c_topics[j].lower():
                weak_topics.append(c_topics[j])
    c_weak.append(weak_topics)
for i in range(n):
    names.append(input("Enter your name : "))
    take_c_strong_topics(c_strong)
    print("{}'s strong points is/are {} and weak points is/are {}".format(names,c_strong,c_weak))
for i in c_topics:
    for j in range(len(c_strong)):
        if i in c_strong[j]:
            print("{} will teach {}".format(names[j],c_strong[j]))