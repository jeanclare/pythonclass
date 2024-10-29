#python script that checks of a number is even or an odd number

num=int(input("Enter a number: "))
if num%2==0:
    print(f"{num} is even number")
else:
    print(f"{num} is odd number")



#create a program that prints the largest of three numbers

num2=int(input("Enter the first number: "))
num3=int(input("Enter the second number: "))
num4=int(input("Enter the third number: "))

def find_largest(num1, num2, num3):
    if (num1 >= num2) and (num1 >= num3):
        largest = num1
    elif (num2 >= num1) and (num2 >= num3):
        largest = num2
    else:
        largest = num3
    return largest

# Call the function and print the result
largest_number = find_largest(num1, num2, num3)
print(f"The largest number is: {largest_number}")