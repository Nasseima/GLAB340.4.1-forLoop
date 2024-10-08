# Problem 1
n = int(input("Enter a positive integer (n): "))
sum_of_natural_numbers = 0

for i in range(1, n + 1):
    sum_of_natural_numbers += i

print (f"the sum of the first {n} natural numbers is: {sum_of_natural_numbers}")

# Problem 2
number = int(input("Enter a number: "))
num_str = str(number)
reversed_str = num_str[::-1]

if num_str == reversed_str:
    print(f"{number} is a palindrome number.")
else:
    print(f"{number} is not a palindrome number.")    
