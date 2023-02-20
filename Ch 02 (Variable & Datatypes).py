#!/usr/bin/env python
# coding: utf-8

# In[5]:


a = "sohail"
A = "KIAAN" #variables names are case sensitive
b = 786
c = 66.67
_d = False #variable name can start with underscore
e = None #variable name cannot start with digit

#Printing type of variable

print(type(a))
print(type(A))
print(type(b))
print(type(c))
print(type(_d))
print(type(e))


# In[9]:


#Arithmatic Operators

a = 5
b = 4
print("The value of",a,"+",b,"is", a+b)
print("The value of",a,"-",b,"is", a+b)
print("The value of",a,"x",b,"is", a*b)
print("The value of",a,"/",b,"is", a/b)


# In[14]:


#Assignment Operators

a = 34
a += 12
print(a)

b = 38
b -= 10
print(b)

c = 35
c *= 15
print(c)

d = 100
d /= 5
print(d)


# In[19]:


#Comparison operators

b = (14>7)
print(b)

c = (100<50)
print(c)

d = (14<=15)
print(d)

e = (15>=16)
print(e)

f = (16!=10)
print(f)


# In[22]:


#Logical operators

bool1 = True
bool2 = False
print("The value of bool1 and bool2 is",bool1 and bool2)
print("The value of bool1 or bool2 is",bool1 or bool2)
print("The value of not bool2 is",not bool2)


# In[26]:


#Typecasting
a = "3534"
print(type(a))

a = int(a) #Python will TRY to convert it into int
print(a+5)


# In[28]:


#Input Function

a = input("Enter your name = ")
print("Welcome to the world of programming",a)
print(type(a))


# In[ ]:


#Input will always be in the form of string


# In[33]:


b = input("Enter your age in years = ")
print(type(b))
b = int(b)
print(type(b))
print("Your age is", b)


# In[ ]:


#Practice Set


# In[34]:


# Pr 01 Add 2 numbers

a = 30
b = 5
print("The sum of a and b is",a+b)


# In[36]:


# pr 02 remainder

a = 45
b = 4
print("The remainder when a is divided by b is",a%b)


# In[38]:


# pr 03 type of variable assigned using input function

a = input("Enter your favorite actor's name = ")
print("Your fav actor is",a)
print(type(a))


# In[42]:


# pr 04 
a = int(input("Enter a number a : "))
b = int(input("Enter a number b : "))
c = (a>b)
print("Is a > b ?",c)


# In[43]:


# pr 05 finding the avg of 2 entered numbers

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
print("The average of two numbers is",(a+b)/2)


# In[44]:


# pr 06 To find the square of entered number

a = int(input("Enter a number for calculating square : "))
print("The square of this number is",a*a)

