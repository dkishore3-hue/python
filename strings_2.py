#isdigit()
#Returns True if all characters are digits(0-9)
'''
Returns False
1.It includes letters,spaces or symbols
2.The string is Empty
'''

# number="4250"
# new=number.isdigit()
# print(new)


# number="42 50"
# new=number.isdigit()
# print(new)



# number="python4250"
# new=number.isdigit()
# print(new)

# number=""
# new=number.isdigit()
# print(new)


# age=input("Enter your age:")
# if age.replace(" ","").replace(".","").isdigit():
#     print(f"Age is noted {age}")
# else:
#     print("Age must be numeric")


#sum of all digit characters
# number="a1b2c3"
# sum=0
# for i in number:
#     if i.isdigit():
#         sum+=int(i)
# print(sum)


#isalpha()
#Returns True if all characters in the string are letters(a-z,A-Z)
'''
Returns False if
1.The string contains numbers,spaces or symbols
2.The string Empty
'''

# text="python"
# new=text.isalpha()
# print(new)

# text="Python Life"
# new=text.isalpha()
# print(new)

# text="pyt$thon"
# new=text.isdigit()
# print(new)

# text="python123"
# new=text.isalpha()
# print(new)

# text=""
# new=text.isalpha()
# print(new)

# name=input("Enter your name:")
# if name.replace(" ","").isalpha():
#     print(f"validname:{name}")
# else:
#     print("your name is not properly Entered")



#isalnum()
#Returns True if all characters are alphanumeric(Letters or numbers)
'''
Returns False if:
1.The string conatin spaces or symbols
2.The string is empty

'''

# numbes="Python456"
# new=numbes.isalnum()
# print(new)

# number="Python 456"
# new=number.isalnum()
# print(new)

# numbers="456"
# new=numbers.isalnum()
# print(new)


# text="Python"
# new=text.isalnum()
# print(new)

# text=""
# new=text.isalnum()
# print(new)


# username=input("Enter your username:")
# if username.replace(" ","").isalnum():
#     print("username is valid")
# else:
#     print("Your username is must contain only letter or numbers")



#format

# text="hii {} tiffin chesara {}".format("suresh","bye")
# print(text)

# names=["ankit","varma","karuna","naresh","naveen","rajkumar","sowmya","surendra","farooq","venkatesh"]
# for i in names:
#     print("hii {} thinnara? {}".format(i,"bye"))



# names=["ankit","varma","karuna","naresh","naveen","rajkumar","sowmya","surendra","farooq","venkatesh"]
# for i in range(len(names)):
#     print("hii {} thinnara? {}".format(names[i],"bye"))


#split()
# text="This is September Python Batch"
# new=text.split()
# print(new)

# text="mahesh,pavan,tarak,arjun,charan"
# new=text.split(",")
# print(new)

# text="one-two-three-four"
# new=text.split("-")
# print(new)

# url="https://www.flipkart.com/product/item"
# splitting=url.split("/")
# print(splitting)
# print(splitting[2])
# print(splitting[3])

# path="C:/Python batches/sep_2025"
# splitting=path.split("/")
# print(splitting)
# print(splitting[2])


#join()
# names=["ankit","varma","karuna","naresh","naveen"]
# result=" ".join(names)
# print(result)


# text=["this","is","september","python","batch"]
# result="-".join(text)
# print(result)


# text=["this","is","september","python","batch"]
# separator="-"
# result=separator.join(text)
# print(result)


# folders=["C","Pythonbatches","sep2025"]
# path="/".join(folders)
# print(path)


# mails=["ramesh@gmail.com","suresh@gmail.com","mahesh@gmail.com"]
# mail_string=",".join(mails)
# print(mail_string)


# characters=["p","y","t","h","o","n"]
# word="".join(characters)
# print(word)


# tags=["Maheshabu ","Pavankalyan ","Ntr ","Prahas ","Alluarjun "]
# hastags="#".join(tags)
# print(hastags)
# print("#"+hastags)


# accountnolist=["****","*****","4895"]
# msgaccoutnumber="".join(accountnolist)
# print(msgaccoutnumber)


# accountnolist=["****","*****","4895"]
# accountnolist[0]="4569"
# accountnolist[1]="5074"
# print(accountnolist)



# accountnolist=["****","****","4895"]
# numbers=["4569","5074"]
# for i in range(len(accountnolist)):
#     if accountnolist[i]=="****":
#         accountnolist[i]=numbers.pop(0)
# print(accountnolist)
# msgaccountnumber="".join(accountnolist)
# print(msgaccountnumber)


# inputstring="Python Is To Learn"
# reversedstring="nohtyP sI oT nraeL"
# newlist=inputstring.split()
# print(newlist)
# emptylist=[]
# for i in newlist:
#     emptylist.append(i[::-1])
# print(emptylist)
# outputstr=" ".join(emptylist)
# print(outputstr)


# inputstring="Python Is To Learn"
# reversedstring="nohtyP sI oT nraeL"
# outpustr=" ".join([i[::-1] for i in inputstring.split()])
# print(outpustr)



#task 90
#ask the user to input a word and count how many vowels it contains
# word=input("Enter a word:")
# vowels="aeiouAEIOU"
# count=0
# for letter in word:
#     if letter in vowels:
#         count+=1
# print(f"The word {word} contains {count} vowels")


# word=input("Enter a word:")
# vowels="aeiou"
# for i in vowels:
#     count=word.lower().count(i)
#     if count>0:
#         print(f"{i}--->{count}")