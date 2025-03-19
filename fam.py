import time
def square():
    n = 1 
    a = int(input("Enter the number from where to print square: "))
    for i in range(n, a):
        sqr = n * n
        print(f"{n}. {sqr}")
        n += 1
        time.sleep(1)

def string():
    str = "Thank you"
    a = 1
    n = int(input("Enter times to print: "))
    for i in range(a, n):
        print(f"{a}. {str}")
        a += 1
        time.sleep(1)

print("1. Square of infinite numbers")
print("2. Printing a string in speific time intervals and specific times to print")
while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        square()
    
    elif choice == 2:
        string()

    elif choice == 3:
        break