
min_val = 10
max_val = 100
a, b = 0, 1
c=0
fibonacci_list = []

while a <= max_val:
    if a >= min_val:
        fibonacci_list.append(a)
   #a, b = b, a + b    
    c=a+b
    a=b
    b=c

print(f"Fibonacci numbers in range {min_val} to {max_val}: {fibonacci_list}")
