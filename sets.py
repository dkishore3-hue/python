#set---->{}
#set is mutable
#duplicates not allowed
#set elements must be of type immutable
#unordered
#no indexing

# numbers={}
# print(type(numbers))

# numbers=set()
# print(numbers)
# print(type(numbers))

# numbers=set({4,5,8})
# print(numbers)

# my_set={5,3.5,True,"sai",2+5j,(4,9)}
# print(my_set)


# my_set={5,3.5,True,"sai",2+5j,[4,9]}
# print(my_set)#Type Error


# my_set={5,3.5,True,"sai",2+5j,{"name":"sai","rollno":5}}
# print(my_set)#Type Error


# my_set={5,3.5,True,"sai",2+5j,{8,15}}
# print(my_set)#Type Error


# numbers={4,56,4,5,6,4,5,6,4,5,6,4,5,6,4,5,6,4,5,6}
# print(numbers)


# my_set={5,3.5,True,"sai",2+5j}
# print(my_set[3])


# #add()
# numbers={52,15,89,76,19}
# numbers.add("mahesh")
# print(numbers)


#update()
# numbers={52,15,89,76,19}
# numbers.update([100,"suresh",200])
# print(numbers)


# numbers={52,15,89,76,19}
# numbers.update((100,"suresh",200))
# print(numbers)


# numbers={52,15,89,76,19}
# numbers.update({100,"suresh",200})
# print(numbers)


#clear()
# numbers={52,15,89,76,19}
# numbers.clear()
# print(numbers)


#copy()
# set_1={52,15,89,76,19}
# set_2=set_1.copy()
# print(set_1)
# print("-"*25)
# print(set_2)


#remove()
# numbers={52,15,89,76,19}
# numbers.remove(89)
# print(numbers)

# numbers={52,15,89,15,76,15,19,15}
# numbers.remove(15)
# print(numbers)


# numbers={52,15,89,15,76,15,19,15}
# numbers.remove(200)
# print(numbers)#keyError


#discard()
# numbers={52,15,89,76,19}
# numbers.discard(89)
# print(numbers)


# numbers={52,15,89,28,76,28,19,28}
# numbers.discard(28)
# print(numbers)


# numbers={52,15,89,76,19}
# numbers.discard(200)
# print(numbers)


#pop()
# numbers={52,15,89,76,19}
# numbers.pop()
# print(numbers)


# gmails=["abc@gmail.com","gcd@gmai.com","abc@gmail.com","bcd@gmail.com"]
# uniqueemails=set(gmails)
# for i in uniqueemails:
#     print(f"sending email to {i}")


#union

# A={1,2,3,4,5}
# B={6,7,4,8,9}
# print(A.union(B))


# A={1,2,3,4,5}
# B={6,7,4,8,9}
# print(A|B)


#intersection

# A={1,2,3,4,5}
# B={6,7,4,5,9,8}
# print(A.intersection(B))


# A={1,2,3,4,5}
# B={6,7,4,5,9,8}
# print(A&B)


#difference

# A={1,2,3,4,5}
# B={6,7,4,5,9,8}
# print(A.difference(B))
# print("-"*25)
# print(A-B)


# A={1,2,3,4,5}
# B={6,7,4,5,9,8}
# print(B.difference(A))
# print("-"*25)
# print(B-A)


#symmetricdifference

# A={1,2,3,4,5}
# B={6,7,4,5,9,8}
# print(A.symmetric_difference(B))
# print("-"*25)
# print(A^B)

#disjoint
# A={1,2,3}
# B={4,5,6}
# print(A.isdisjoint(B))


# A={1,2,3}
# B={4,5,3,6}
# print(A.isdisjoint(B))


#subset
# A={1,2,3,4,5,6}
# B={4,6,2}
# print(B.issubset(A))
# print("-"*25)
# print(A.issubset(B))


# A={6,4,2}
# B={4,6,2}
# print(B.issubset(A))
# print("-"*25)
# print(A.issubset(B))

#supeset
# A={1,2,3,4,5,6}
# B={4,5,2}
# print(A.issuperset(B))


#frozenset()
# list_1=[2,3.5,98,45,15]
# my_frozenset=frozenset(list_1)
# print(my_frozenset)
# print(type(my_frozenset))


# tuple_1=(2,3.5,98,45,15)
# my_frozenset=frozenset(tuple_1)
# print(my_frozenset)
# print(type(my_frozenset))


# my_dictionary={1:"mahesh",2:"suresh"}
# d=frozenset(my_dictionary.items())
# print(d)

# fs1=frozenset({1,2,3})
# fs2=frozenset({4,5,6})
# my_set={45,fs1,fs2,20}
# print(my_set)


#frozenset iterable
# fs=frozenset([1,2,3,4])
# for i in fs:
#     print(i)
