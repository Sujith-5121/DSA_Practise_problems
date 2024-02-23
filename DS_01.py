# Write a python program to find a pair with the given sum in an array:-

# Using Brute-Force:
def find_pair(n,target):
    for i in range(len(n)-1):
        for j in range(i+1,len(n)):
            if n[i]+n[j]==target:
                print("Pair found",(n[i],n[j]))
                return
    print("pair not found")
nums=[]
a=int(input("Enter the number: "))
for i in range(a):
    b=int(input("Enter the number: "))
    nums.append(b)
print(nums)
target=int(input("Enter the target number: "))
print(find_pair(nums,target))
