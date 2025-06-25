"""✅ Contains Duplicate

✅ Valid Anagram

✅ Two Sum

✅ Intersection of Two Arrays

✅ Missing Number
"""

#to find duplicate in strings and list 
"""list1 = []
str1 = ""
n = int(input("HOW Much words you wanna add in list : "))
for i in range(n):
    lst = int(input("what you wanna add in it "))
    list1.append(lst)
print(list1)

set1 = set(list1)

if len(set1) == len(list1):
    print("it doesnt have any duplicate")
else:
    print("it have")


str1 = "strin"
str2 = "srint"

def chck(str1,str2):
    if str1.sort() == str2.sort():
        print("its annagram")
    else:
        print("its not ")    
"""
"""
string = "zurriyat"
strempty = ""
for i in range(len(string)-1 , -1 , -1):
    strempty += i 

print(strempty)
    """
"""string = "zurriyat"
strempty = ""
for char in string:
    reversedchr = char + strempty
    

print(reversedchr)"""

"""str1 = input("tell word : ")
strempty = ""
for char in str1:
    strempty = char + strempty
if str1 == strempty:
    print("it is a pellindrome")
else:
    print("its not")"""

list1 = [1 , 2 ,3 ,5 ,5 , 3]
onceseen = []
duplicate = []
count = 0
dup_idx = []
for i in list1:
    count += 1
    if i in onceseen and i not in duplicate :
        duplicate.append(i)
        dup_idx.append(f"so duplicsate is at {count - 1}")
    else:
        onceseen.append(i)

print(f"duplcate nums are : {duplicate}")
print(f"total duplicates are {dup_idx}")