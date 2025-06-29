#3rd day of soving tiday 3 probs 2 revise and one new concept 

#1 Problem
def chk(str1):
    seem = set()
    for ch in str1:
        if ch in seem:
            return False
        seem.add(ch)
    return True
if chk("hello"):
    print("its unique")
else:
    print("its noot")
    
if chk("helo"):
    print("its unique")
else:
    print("its noot")

#2 fIND SUM IN SORTED LIST 
lsit1 = [1 , 6 ,7 , 4, 6]
lsit1.sort()
def find_sum(lsit1 , target):
    left = 0
    right = len(lsit1) - 1 
    while left < right:
        sum = lsit1[left] + lsit1[right]
        if sum == target:
            print(f"sum found at {left , right}")
            return True
        if sum < target:
            left += 1
        if sum > target:
            right -= 1 
    return False
if find_sum(lsit1 , 13):
    print("its found")
else:
    print("its not in list")

#3 Missing num in aa rnage
n = int(input("input the num tilll oyu wanna put : "))
random_num = int(input("input the num yopu wanna remove : "))
if random_num not in range(n + 1):
    raise ValueError("Please put num in given n number you gave till you wnated rEANGE")
def find_missing_num(n):
    array  = []
    for i in range(n + 1):
        array.append(i)
    array.remove(random_num)
    total_sum = n * (n + 1 ) // 2
    sum1 = sum(array)
    num = total_sum - sum1 
    print(f"missing num is : {num}")
find_missing_num(n)