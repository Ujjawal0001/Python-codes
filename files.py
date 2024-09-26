f=open(r"C:\Users\ujjwl\Desktop\coding.c\2darray1.c","r")
lines=f.readlines()
for line in lines:
    print(line)
f.close()



# f = open("demofile.txt", "r")

# lines = f.readlines()
# newlines = []
# 
# for index, line in enumerate(lines):
#     newlines.append(line.upper())
# f.close()
# 
# print(newlines)
# 
# f = open("demofile.txt", "w")
# 
# for line in newlines:
#     f.writelines(line)
# f.close()

# 
# f = open("names.txt", "a+")
# print(f.tell())
# f.seek(0)
# lines = f.readlines()
# print(f.tell())
# print(lines)
# f.close()

# f = open("names.txt", "r")
# lines = f.readlines()
# print(lines)
# f.close()

# f = open("names.txt", "a+")
# f.seek(0)
# f.writelines("Priya")
# f.close()
# 
# f = open("names.txt", "r")
# lines = f.readlines()
# print(lines)
# print(f.tell())
# 
# f.close()

# f = open("names.txt", "a+")
# f.write("\nSonam")
# f.write("\nBhaiya")
# lines = f.readlines()
# print(lines)
# f.close()






f = open("names.txt", "r")
lines = f.readlines()
for line in lines:
    a = line.split(" - ")
    print(a[0])
    print(a[1])





a = "conditionals"
f = open("conditionals.txt", "w")
f.writelines(f"Topic - {a}")
f.close()