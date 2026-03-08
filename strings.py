'''
This is String topic 
'''

# cities='''
#     1.Hyderabad
#     2.Banglore
#     3.Chennai
#     4.Pune
#     5.Mumbai

# '''
# print(cities)


#single quoutes
#double quotes
#triple quotes


# text='''today is Thursday
# we are discussing
# "string" topic

# '''
# print(text)


# name="Python Life"
#variable[index]
#print(name[4])
# print(name[-2])
# print(name[8])
# print(name[6])


#slicing
#my_string="India is Developing Country"
# print(my_string[3:7])
# print(my_string[8:2:-1])
#print(my_string[::-1])


#Palindrome

# while True:
#     number=input("Enter a number/Text:")
#     if number==number[::-1]:
#         print(f"{number} is a Palindrome")
#     else:
#         print(f"{number} is not a Palindrome")


#replace
# original_string="India is Developing Country"
# change=original_string.replace("is","are")
# print(original_string)
# print("-"*25)
# print(change)


# print("India is Developing Country".replace("is","are"))

# orginal_string="India is Developing Country"
# change=orginal_string.replace("is","are").replace("India","Indians").replace("Country","People")
# print(orginal_string)
# print("-"*25)
# print(change)


#upper()
# my_string="September Batch students are very sincere"
# up_case=my_string.upper()
# print(up_case)

# answer=input("Do you agree?YES?NO:")
# if answer.upper()=="YES":
#     print("You agreed...")

#lower()
# my_string="SePTemBEr PyTHoN LiVe BaTcH"
# low_case=my_string.lower()
# print(low_case)

# answer=input("Do you agre?Enter yes or no:")
# if answer.lower()=="yes":
#     print("you agreed....")


#count()
#text="This is String class"
# print(text.count("i"))
#print(text.count("is"))

#len() --->built in function
# text="PythonLife"
# print(len(text))


#strip()
# text="   This is Python live class   "
# print(text)
# print(len(text))
# print("-"*25)
# trimmed_string=text.strip()
# print(trimmed_string)
# print(len(trimmed_string))


#lstrip()
# text="   This is Python live class   "
# print(text)
# print(len(text))
# print("-"*25)
# trimmed_string=text.lstrip()
# print(trimmed_string)
# print(len(trimmed_string))


#rstrip()
# text="   This is Python live class   "
# print(text)
# print(len(text))
# print("-"*25)
# trimmed_string=text.rstrip()
# print(trimmed_string)
# print(len(trimmed_string))


# name="   Python Life  "
# print(name)
# result=name.replace(" ","")
# print(result)


#startswith()
# text="PythonLife"
# new_string=text.startswith("P")
# print(new_string)

# text="PythonLife"
# new_string=text.startswith("Python")
# print(new_string)

# user_input="Hello,I need Your Help"
# if user_input.lower().startswith("hello"):
#     print("Hii,How Can I Help You Today...")


#endswith()
# text="PythonLife"
# new_string=text.endswith("e")
# print(new_string)

# text="PythonLife"
# new_string=text.endswith("Life")
# print(new_string)

# maillist=["abhi@gmail.com","harshita@outlook.com","karuna@gmail.com","varma@hotmail.com","naresh@yahoo.com","niranjan@gmail.com"]
# gmailist=[]
# for i in maillist:
#     if i.endswith("@gmail.com"):
#         gmailist.append(i)
# print(gmailist)


#find() method
#syntax:stirng.find(sub,start,end)

# text="Python programming is fun"
# print(text.find("pro"))
# print(text.find("m"))
# print(text.find("o"))
# print(text.find("o",5,10))
# print(text.find("m",14,17))
# print(text.find("o",5))#finds "o"from index 5
# print(text.find("n",6))
# print(text.find("java"))#it returns -1


#index()
#syntax:string.index(sub,start,end)
#text="Python programming is fun"
#print(text.index("pro"))
#print(text.index("m"))
#print(text.index("o"))
# print(text.index("o",5,10))
# print(text.index("m",14,17))
# print(text.index("o",5))#finds "o"from index 5
#print(text.index("n",6))
#print(text.index("java"))#valueError:substring not found


#text="hello world"
# print(text.find("z")) #output:-1
#print(text.index("z"))#ValueError: substring not found

#sentence="Data science and data anlysis are related"
#print(sentence.find("data"))#17
#print(sentence.lower().find("data"))
#print(sentence.index("science"))


# word="banana"
# print(word.find("a"))
# print(word.index("a"))
 

# word="banana"
# char="a"
# for i in range(len(word)):
#     if word[i]==char:
#         print(f"Found {char} at position {i}")


# word="banana"
# char="a"
# index=word.find(char)
# while index!=-1:
#     print(f"Found at index:{index}")
#     index=word.find(char,index+1)


#captilize()
#converts the first character of the string to uppercase and rest to the lower case
# text="thIs Is PytHon CLASS"
# new=text.capitalize()
# print(new)

# user_input="your PACkaGe HaS BEEn SHIpped"
# new=user_input.capitalize()
# print(new)

#title()
# text="tHis iS pYtHoN cLaSS"
# new=text.title()
# print(new)

# user_input="yoUR paCkAGe haS bEEn shIPPed"
# new=user_input.title()
# print(new)