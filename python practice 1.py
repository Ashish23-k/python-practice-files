#!/usr/bin/env python
# coding: utf-8

# In[3]:


#python
#Introduction to strings

#defining a string in python
x='python'
print(x)


# In[4]:


#using single quotes inside a string
x= "'Python'is the latest programming language "
print(x)


# In[5]:


#using both double and single quotes in a string
x=""" 'Raju' told me that "Recently many are using Python instead of older languages" """
print(x)


# In[6]:


#type of variable
type(x)


# In[7]:


#Using title case
Name='raju'
print(Name.title())


# In[8]:


#upper case and lower case
Name='Mahesh Kuri'
print(Name.upper())
print(Name.lower())


# In[10]:


#F-Strings
Name='suma'
Fav_fruit='mango'
print(f"{Name.title()} loves eating {Fav_fruit}")


# In[12]:


#string space
Fav_lang=' Python '

print(Fav_lang.lstrip())
print(Fav_lang.rstrip())
print(Fav_lang.strip())
#tab space before a string
print('\t Python')


# In[27]:


#using \n \t
print("""Men_clothing: \n\t 1.Shirts \n \t \t  i.Casual shirts \n\t\t ii.Formal shirts\n\t 2.Jeans \n \t \t  i.Torn jeans 
     \n \t \t ii.Faded jeans """)


# In[23]:


# list

#defning a list

Fav_colors=['red','blue','orange','violet','grey']
print(Fav_colors)
type(Fav_colors)
print(Fav_colors[0].upper())
print(f"I like {Fav_colors[1]} of all other colors")

#changing,adding,inserting and removing an element from/to a list

Fav_colors[2]='black'
print(Fav_colors)

#appending
Fav_colors.append('orange')
print(Fav_colors)


# In[24]:


#inserting
Fav_colors=['red','blue','orange','violet','grey']

Fav_colors.insert(3,'black')
print(Fav_colors)


# In[25]:


#removing
Fav_colors=['red','blue','orange','violet','grey']

Fav_colors.pop(4)
print(Fav_colors)


# In[30]:


#organinsing a list
cars=['bmw','audi','benz','jeep']
print(cars)
print('\n ')
cars.sort()
print(cars)


# In[32]:


#sort in reverse alphabetical order
cars=['bmw','audi','benz','jeep']
cars.sort(reverse=True)
print(cars)


# In[33]:


cars=['bmw','audi','benz','jeep']
len(cars)


# In[35]:


#Introdution to looping

#for loop
bikes=['yamaha','ducati','bmw','kawasaki']
for bike in bikes:
 print(f"{bike} is the best")


# In[36]:


#sum of numbers in list
nums=[2,3,4,5,6]
total=0
for num in nums:
    total=total+num
print(total)


# In[37]:


#slicing of strings

Dc_char=['superman','batman','flash','wonder women','joker']

Dc_heros=Dc_char[0:4]
print(Dc_heros)

Dc_villian=Dc_char[4:5]
print(Dc_villian)


# In[38]:


Dc_char=['superman','batman','flash','wonder women','joker']
#if not specified  the starting index number
print(Dc_char[:4])
#if not specified the ending index number
print(Dc_char[1:])


# In[39]:


#printing range of numbers
nums=list(range(1,50))
print(nums)


# In[40]:


#printing only even numbers(Providing the interval or increment)
eve_num=list(range(2,99,2))
print(eve_num)


# In[41]:


#Home work: Printing alternate elements of a list
Mahabharat_char=['ram','sita','lakshman','bharat','urmi','satrugna','kaikeyi','ravana','hanuma','garuda']
print(Mahabharat_char[0::2])


# In[42]:


#Duplicating a list
Mahabharat_char=['ram','sita','lakshman','bharat','urmi','satrugna','kaikeyi','ravana','hanuma','garuda']
Dup_char=Mahabharat_char[:]
print(Dup_char)


# In[43]:


#TUPLE
#it is an immutable list
dimensions=(200,50)
print(dimensions)


# In[44]:


dimensions=(200,50)

type(dimensions)


# In[46]:


dimensions=(200,50)

print(dimensions[0])

dimensions[0]=250


# In[47]:


#Introduction to Dictionary data type

alien_0={'color':'green','points':5}
print(alien_0)
type(alien_0)


# In[ ]:




