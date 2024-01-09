#Sum of all even numbers up to 50
sum = 0
for i in range(1,51):
 if i % 2 == 0:
    sum = sum + i
print("The sum of all even numbers up to 50 =" , sum)

# Write first 20 numbers and their squared
for i in range (1,21):
    print(i,"Square Numbers",i**2)

#A number is Divisible by 8 or 12 up to 100 numbers

for i in range(1,100):
 if i % 8 == 0 and i % 12 == 0:
   print(i)
     
#Write a program to create a billing system at supermarket.
while True:
    name = input("Enter Customer Name:")
    total = 0
    while True:
       print("enter the amount and quantity")
       amount = float(input("enter amount:"))
       quantity = float(input("enter quantity:"))
       total +=  amount * quantity
       repeat = input("do you want to add or more items? (Yes/No) :")
       if repeat == "No" or repeat == "no":
          break
    print("-"*40)
    print("Name: ",name)
    print("Amount to be paid:" , total)
    print("-"*40)
    print("******************Happy Shopping************")

    repeat1 = input("Do you want to go to next customer? (Yes/No):")

    if repeat1 == "No" or repeat1 =="no" :
       break
