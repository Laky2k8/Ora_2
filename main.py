def recursive(i):
    print(i)
    if i > 0:
        i -= 1
        recursive(i)
    else:
        print("\n Done!")

def factorial(j,k):
    if j > 1:
        j -= 1
        k = k * j
        factorial(j,k)
    else:
        print("\n Done!", num2, "'s factorial is:", k)

def fibonacci(i,j,k):
    if(k<1000):
        k= j
        j = i+j
        i = k
        print(j)
        fibonacci(i,j,k)



num1 = int(input("Hello! Give me a number: "))
print("This will be a recursive function, so brace yourselves. \n")
recursive(num1)

print("\n \n")
print("TASK 2 \n")
print("FACTORIAL GENERATOR")
num2 = int(input("Give me another number! I will calculate it's factorial: "))
factorial(num2,num2)

print("\n \n")
print("TASK 3 \n")
print("FIBONACCI GENERATOR")
numA = int(input("Give me the first number: "))
numB = int(input("Give me the second number: "))
numC = int(input("Give me the third number: "))
fibonacci(numA, numB, numC)


