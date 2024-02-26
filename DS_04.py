# Write a python program to find the duplicate element in the limited range array:-

# Using Brute-Force:
def duplicate_elements(n):
    for i in range(len(n)-1):
        for j in range(i+1,len(n)):
            if n[i]==n[j]:
                print("The duplicate element is:")
                return n[i]
    print("The duplicate elements not found")
num=[1,2,3,4,2]
print(duplicate_elements(num))
