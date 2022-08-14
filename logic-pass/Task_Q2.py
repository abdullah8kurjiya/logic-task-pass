##Q2/Write a program to find all prime numbers up to a given range of numbers?

## Answer

#Read user input(range)
min = int(input("Enter the min no. : "))
max = int(input("Enter the max no. : "))

for n in range(min,max + 1):
   if n > 1:
       for i in range(2,n):
           if (n % i) == 0:
               break
       else:
           print(n)