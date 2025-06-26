"""# Check if a num is prime or not
num = int(input("whats the num : "))
def prime_check(num):
    for i in range(2 , num - 1):
        if num % i == 0:
            return False
    return True
if prime_check(num):
    print("it is ")
else:
    print("it is not")

#Second method:
num = int(input("whats the num : "))
if num < 10:
    raise ValueError("Please put value above then 10 bcause under  1- 2 , 3 , 5 , 7 are prime")

primes = [2 , 3 , 5 , 7 , ]
def prime_check(num):
    for i in  range(2 , 11):
        if num % i == 0:
            return False
    return True

if prime_check(num):
    print("it is a prime a number")
else:
    print("Its not a prime num")

# Problem 2: Remove Duplicates from a Sorted List

Nums = [1 , 1 , 2 , 2 ,3 ,5 ,6 ,7 , 6 ,8 ,8]
Nums.sort()
idx = []
count = 0
for i in range(len(Nums)):
    count += 1
    if i == 0:
        pass
    elif Nums[i] == Nums[i - 1]:
        idx.append(i)
    else:
        pass

print(idx)

for i in reversed(idx):
    del Nums[i]
print(Nums)

# Check if Two Strings Are Anagrams updated version
def two_annagram_chk(str1 , str2):
    str1 = sorted(str1.lower())
    str2 = sorted(str2.lower())
    if str1 == str2:
        return True
    else:
        return False
if two_annagram_chk("madam" , "damma") :
    print("they are annagram")
else:
    print("They are not")"""

# Palindrome Checker with cleanup
specialcharacter = "!@#$%^&*(())_+=?></.,\| " or [" " , ","]
string = "A man, a plan, a canal, Panama"
string = string.lower()
clean = ""
for i in string:
    if i in specialcharacter:
        pass
    else:
        clean += i

sreversed = "" 
for i in clean:
    sreversed = i + sreversed
if sreversed == clean:
    print("it is a pellindrome")
else:
    print("it is not")

# First Non-Repeating Character
s = "asdbfjhkdfaghasdfghjklasdfghjkldgfbahds"
def nonrepeaterchekcer(s):
    for i in s:
        if s.count(i) == 1:
            return i
    return None
print(nonrepeaterchekcer(s))
