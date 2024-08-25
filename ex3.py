# # create a string using double quotes
# string1 = "ICT Department"
# print(string1)
# # create a string using single quotes
# string1 = ' ICT Department '
# print(string1)


#Access String Characters in Python
# string2 = '3EK1'
# # access 1st index element
# print(string2 [1])


# # Negative Indexing:
# # Python allows negative indexing for its strings. For example,
# string3 = 'ICT Department'
# # access 4th last element
# print(string3 [-4]) 


# string4 = 'ICT Department'
# # # access character from 1st index to 3rd index
# # print(string4[1:4])  
# print(string4[:2])
# print(string4[2:])

# message = 'ICT Department'
# message[0] = 'H'
# print(message)

# message = """
# ICT
# Department
# 3EK1
# """
# print(message)

# str1 = "ICT"
# str2 = "Department"
# str3 = "3EK1"
# # compare str1 and str2
# print(str1 == str2)
# # compare str1 and str3
# print(str1 == str3)

# greet = "ICT"
# name = "Department"
# # using + operator
# result = greet + name
# print(result)


# greet = 'ICT'
# # count length of greet string
# print(len(greet))

# print('a' in 'program') 
# print('at' not in 'battle') 


# message = 'python is fun'
# # convert message to uppercase
# print(message.upper())


# message = 'PYTHON IS FUN'
# # convert message to lowercase
# print(message.lower())


# text = 'CE Department'
# replaced_text = text.replace('CE', 'ICT')
# print(replaced_text)

# message = 'Python is a fun programming language'
# # check the index of 'fun'
# print(message.find('fun'))

# title = 'Python Programming   '
# result = title.rstrip()
# print(result)

# text = 'Python is fun'
# # split the text from space
# print(text.split())


# message = 'Python is fun'
# # check if the message starts with Python
# print(message.startswith('Python'))

# pin = "523"
# # checks if every character of pin is numeric 
# print(pin.isnumeric())

# text = 'shivam bhatt'
# # find the index of is
# result = text.index('bhatt')
# print(result)

# name = 'Cathy'
# country = 'UK'
# print(f'{name} is from {country}')

# str = "This is a \n normal string example" 
# print(str) 
# raw_str = r"This is a \n raw string example" 
# print(raw_str)


# #reverse
# str=input("enter a string")
# print(r"reverse string is:",str[::-1])
    
# #palindrome
# str=input("enter a string")
# if(str==str[::-1]):
#     print("string is palindrome")
# else:
#     print("string is not palindrome")

    
#check if string contains only numeric
# str=input("enter a string")
# print(str.isnumeric())


#length of last word
s="shivam bhatt"
sv=s.split()
v=sv[-1]
print(len(v))




# string = "programming with python"
# str = string.split()
# last = str[-1]
# print(len(last))


s = "shivam bhatt"
string = s.split()
print(string)
longest = max(string , key = len)
print("The longest word in the sentence is:", longest)




