fizz_buzz1=input("n= ")
n=int(fizz_buzz1)

if (n % 3 == 0) and (n % 5 == 0):
    print("FizzBuzz")
elif n % 5 == 0:
    print ("Buzz")
elif n % 3 == 0:
    print("Fizz")
else:
    print(n)