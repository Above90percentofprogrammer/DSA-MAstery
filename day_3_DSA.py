# ✅ Problem 1: Find the Missing Number in an Array
arr = [1,2,4,5]
n = 5
def find_missing(arr, n):
    total_sum = n * (n + 1) / 2
    actual_sum = sum(arr)
    num = int(total_sum - actual_sum)
    arr.append(num)
    arr.sort()
    print(arr)
find_missing(arr, n)

#Problem 2: Reverse an Integer (without converting to string)
def anyfunc(num):
    rev = 0
    if num < 0:
        num = -num
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    print(rev)

anyfunc(123)

# New concept today two pointer

str1 = "A man, a plan, a canal, Panama"
str1 = str1.lower()
speacial_char = ("~!@#$%^&*()_`= [';/.:>?<,]|\ ")
clean = "" 
for i in str1:
    if i in speacial_char:
        pass
    else:
        clean += i
print(clean)
left = 0
right = len(clean) - 1
def chck_2(clean):
    left = 0
    right = len(clean) - 1
    while left < right:
        if clean[left] != clean[right]:
            return False
        left += 1
        right -= 1
    if clean[left] == clean[right]:
        return True    
if chck_2(clean) == True:
    print("its a pellindrome//.....")
else:
    print("its not")

# Sorted Two Sum (Two Pointer)

nums = [1, 3, 4, 5, 7, 10, 11]
target = 9
def chk(nums , target):
    start = 0
    end = len(nums) - 1
    while start <end:
        sum = nums[start] + nums[end]
        if nums[start] + nums[end] == target:
            return True
        elif sum > target:
            end -= 1
        else:
            start += 1
    return False

    

if chk(nums , target):
    print("sum found")
else:
    print("not found")      