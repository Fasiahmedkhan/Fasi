
n = int(input("Enter a noneger: "))

if n < 0:
    print("Please enteger.")
else:
  
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    
  
    print("Factorial of",  ":", factorial)
