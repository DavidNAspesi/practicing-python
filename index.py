# # print("hello world")
# # print(2 ** 3)

# a = 5
# a = "Hello World"

# b = "ABRACADABRA he yelled"

# c = {"key1":"name","key2":"age"}

# d = {"k1":1,"k2":[0,1,2],"k3":{"anotherKey":100}}

# e = (1,"two",4.5)

# with open("myfile.txt") as myfile:
#     contents = myfile.readlines()

# with open("abdcd.txt", mode="w") as f:
#     f.write("Just created this file!")

# with open("abdcd.txt", mode="r") as l:
#     stuff = l.read()

# # print(a[::-1])
# # print(b.split())


# # print("this is a string {1} {0}".format("also inserted", "inserted"))

# # print(f'this is a new string {b}')

# # print(c["key1"])

# # print(d["k3"]["anotherKey"])

# # print(e.count("two"))

# # print(1 > 2)

# print(contents)
# print(stuff)

# print(2 == 2)
# print("2" == 2)
# print (2.1 > 2)
# print(3 != 2)

# print( 1 < 2 and 2 < 3)
# print(1 < 2 or 2 > 3)
# print(not 2 > 3)

# if 4 < 3:
#     print("its true!")
# else:
#     print("whoops")
# new_list = []
# my_iterable = "a string"
# for item_name in my_iterable:
#     new_list.append(item_name)

# print(new_list)

# my_iterable = [0,1,2,3,4,5,6,7,8,9,10]
# for num in my_iterable:
#     if num % 2 == 0:
#         print(num)
#     else:
#         print(f"Odd number: {num}")

# mylist = [(1,2),(3,4),(5,6),(7,8)]
# for a,b in mylist:
#     print(a)
#     print(b)

# while_number = 0
# while while_number < 10:
#     while_number += 1
#     print (while_number)

# for num in range(3,10,2):
#     print(num)



# word = "abcde"
# for index,item in enumerate(word):
#     print(item)

# list1 = [1,2,3]
# list2 = ["a","b","c"]

# for item in zip(list1, list2):
#     print(item)

mylist = [1,2,4,654,84,3]
print(min(mylist))
print(max(mylist))

from random import shuffle

mylist2 = [1,2,3,4,5,6,7,8,9]
shuffle(mylist2)

print(mylist2)