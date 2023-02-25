#!/usr/bin/env python
# coding: utf-8

# # 1 Take values of the length & breadth of a rectangle from user input and check if it is square or not.

# In[1]:


length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

if length == breadth:
    print("The rectangle is a square.")
else:
    print("The rectangle is not a square.")


# # 2 Take three integer values from the user and print the greatest among them.
# 

# In[2]:


# Prompt the user to enter three integers
num1 = int(input(" Enter your 1st Number: "))
num2 = int(input(" Enter your 2nd Number: "))
num3 = int(input(" Enter your 3rd Number: "))

if (num1>=num2) and (num1>=num3):
    largest =num1
    
elif (num2>=num1) and (num2>=num3):
    largest = num2
    
else:
    largest = num3
         
# Print the greatest integer
print("The greatest value: ", largest)


# # 3  student will not be allowed to sit in an exam if his/her attendance is less than 75%.

# In[3]:


#the user to enter the total number of classes held and the number of classes attended
total_class = int(input("Enter the total number of class: "))
attended_class = int(input("Enter the number of class attended: "))

# Calculate the attendance percentage
attended_percent = (attended_class/total_class)*100

# Check if the attendance percentage is greater than or equal to 75%
if attended_percent >= 75:
    print("student will be allowed to sit in an exam")
else:
    print("student will not be allowed to sit in an exam")
    
    
    


# # 4. A school has the following rules for the grading system

# In[4]:


# the user to enter the marks
marks = int(input("Enter your marks: "))

# condition apply here

if marks < 25:
    grade = "F"
elif marks < 45:
    grade = "E"
elif marks < 50:
    grade = "D"
elif marks < 60:
    grade = "C"
elif marks < 80:
    grade = "B"
elif marks < 90:
    grade = "A"
else:
    grade = "A+"

# print the grade you've got
print("Your grade is:", grade)


# # 5 Print the following pattern using for and while loop.

# In[5]:


#using for loop

for i in range(7, 0 ,-1):  # loop from 7 to 1 in steps of -1
    for j in range(1, i+1):  # loop from 1 to i
        print(j, end=' ')  # print j and space
    print()  # print newline


# In[6]:


#using while loop

i = 7  # set initial value of i
while i >= 1:
    j = 1  # set initial value of j
    while j <= i:
        print(j, end=' ')
        j += 1  # increment j by 1
    print()
    i -= 1  # decrement i by 1


# # 6 Display numbers from -100 to -10 using for loop.

# In[7]:


for i in range(-100, -9):
    print(i)


# # 7 Write a program to sum all prime numbers within a range of 10 to 1000.

# In[8]:


# Function to check if a number is prime or not
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Main code
start = 10
end = 1000
sum_primes = 0

for num in range(start, end+1):
    if is_prime(num):
        sum_primes += num

print("Sum of all prime numbers between", start, "and", end, "is:", sum_primes)


# # 8 ind the factorial of an n! (Hint, n=7: 7*6*5*4*3*2*1) 

# In[9]:


n = 7
factorial = 1
for i in range(1, n+1):
    factorial *= i
print(factorial)


# # 9 Reverse a given integer number 27956240710.

# In[10]:


number = 27956240710

#Convert the integer to a string
number_str = str(number)

# Reverse the string
reversed_str = number_str[:-1]

#Convert the reversed string back to an integer
reversed_number = int(reversed_str)

print(reversed_number)


# # 11 Display the Fibonacci series of 15 elements using the for and while loop.

# In[11]:


# using a for loop
n = 15
fibonacci = [0, 1]
for i in range(2, n):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
print(fibonacci)


# In[12]:


# using a while loop
n = 15
fibonacci = [0, 1]
i = 2
while i < n:
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    i += 1
print(fibonacci)


# # 12 Remove 2 and add 3 to the list and replace True with False.

# In[13]:


Li = [1, 3, 5, [2, 3], True]
Li[3][0] = 3   # replace 2 with 3 in the sublist
Li[-1] = False # replace True with False at the end of the list
print(Li)


# # 13 Find the intersection (common) of two sets.
# 

# In[14]:


S1 = {1,4,6,8}
S2 = {True, 1,2,10}
result = S1.intersection (S2) #just use intersection 
print(result)


# # 15. Rename the key of a dictionary.

# In[15]:


Dict = { "name": "Shakil", "age":27, "city": "Berlin", "country": "Germany" }
# Renaming the key 'country' to 'region'
Dict['region'] = Dict.pop('country')
# Printing the updated dictionary
print(Dict)


# # 16 Creating a data frame using the list.

# In[16]:


#import pandas library
import pandas as pd

num = [10, 100, 300]
#creating data from list
df = pd.DataFrame({'number': num})
print(df)


# # 17 Change the value of a key in a given dictionary.

# In[17]:


Dict = {"name": "Shakil", "age": 27, "city": "Berlin", "country": "Germany"}

# Changing the value of the key 'age' to 28
Dict['age'] = 28

# Printing the updated dictionary
print(Dict)


# In[ ]:




