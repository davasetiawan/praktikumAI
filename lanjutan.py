#data types

# cast from str to int
str_numbers = "456"
str_numbers_to_int = int(str_numbers)
print("Before casting:", str_numbers, ", the data type is", type(str_numbers))
print("After casting :", str_numbers_to_int, ", the data type is", type(str_numbers_to_int))
print("="*50)

# casting from int to str
integer = 12345
integer_to_str = str(integer)
print("Before casting :", integer, ", the data type is", type(integer))
print("After casting :", integer_to_str, ", the data type is", type(integer_to_str))
print("="*50)

# casting from int to bool
num_int = 1
num_bool = bool(num_int)
print(num_bool, type(num_bool))

num_int = 0
num_bool = bool(num_int)
print(num_bool, type(num_bool))
print("="*50)


#operators
print("8 == 8 :", 8 == 8)
print("8 != 9 :", 8 != 9)
print("8 > 9  :", 8 > 9)
print("8 < 9  :", 8 < 9)
print("8 <= 9 :", 8 <= 9)
print("9 >= 9 :", 9 >= 9)
print("="*50)


# logic operators
a = True
b = True
print(a and b)
print(a or b)
print(not b)

# logic with numbers
print(5 > 6 and 6 < 7)
print("="*50)


# arithmetic operators  
e = 8
f = 2

# Summation
sum_ = e + f
print(f"The sum of e with f is : {sum_}\n")

# Reduction
red = e - f
print(f"The reduction of e with f is : {red}\n")

# Multiplication
multi = e * f
print(f"The multiplication of e with f is : {multi}\n")

# Division
divi = e / f
print(f"The quotient of e with f is : {divi}\n")

# Modulo
mod = e % f
print(f"The remainder of e with f is : {mod}\n")

# Power
pow_ = e ** f
print(f"The power of e of f is : {pow_}\n")
print("="*50)



# Koding Input Output
# Input
name = str(input("What is your name : "))
age = int(input("What's your age : "))
print("Name: ", name)
print("Age: ", age)

# Output
print('Hi all! I am', name, 'age', age, 'years old')
print(f'Hi all! I am {name} age {age} years old')
print('Hi all! I am %s age %d years old' % (name, age))

print(30*"=")
print("Temperature Calculator Program")
print(30*"=")
print("="*50)



# Koding Conditionals & Exception Handling

try:
    your_GPA = float(input("Enter your GPA: "))
    if 4.0 >= your_GPA >= 0.0:
        if 4.0 >= your_GPA >= 3.80:
            print(f"Damn you've got a magna cumlaude with your {your_GPA} GPA")
        elif 3.50 <= your_GPA < 3.80:
            print(f"Cool!! You've got a cumlaude with your {your_GPA} GPA")
        elif 3.00 <= your_GPA < 3.50:
            print("You've got a stable GPA tho")
        elif your_GPA < 3.0:
            print("You need a stable GPA")
    else:
        print(f"Sorry, your GPA {your_GPA} is out of range and invalid")
except:
    print("Please enter a valid GPA")
print("="*50)



# Using match case

try:
    status_code = int(input("Enter your status code: "))
    print("Your code means:")
    match status_code:
        case 200:
            print("Success!")
        case 400:
            print("Bad Request")
        case 401:
            print("Unauthorized")
        case 402:
            print("Payment Required")
        case 403:
            print("Forbidden")
        case 404:
            print("Not Found")
        case 500:
            print("Internal Server Error")
        case _:
            print("Unknown status code")
except:
    print("Please enter a valid status code")
print("="*50)



# Ternary Operator

a = 3
b = "Even Numbers" if a % 2 == 0 else "Odd Numbers"
print(b)
print("="*50)



# Using Loops

for i in range(5):
    print(i)

print(50*"=")

# For loop with range
for i in range(5):
    print("Data science is easy!")

print(50*"=")

for i in range(1, 5, 2):
    print("Data science is easy!")

print("="*50)

word = "I want to master data science"
for letter in word:
    print(letter)

print("="*50)

# Using enumerate
for m, n in enumerate(word):
    print(f"Index {m}. {n}")