# Write a python program to find sub-array with 0 sum:-

# Using Brute-Force:
def sub_array(n):
    for i in range(len(n)):
        sum=0
        for j in range(i,len(n)):
            sum += n[j]
            if sum==0:
                print("sublist:",(i,j))
nums=[]
a=int(input("Enter the number: "))
for i in range(a):
    b=int(input("Enter the number: "))
    nums.append(b)
print(nums)
print(sub_array(nums))
