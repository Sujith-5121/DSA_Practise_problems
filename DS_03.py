# Write a python program to sort binary array in linear time:-

# sort binary array in linear time using while loop function:
def Sort(a):
    zeros=a.count(0)
    k=0
    while zeros:
        a[k]=0
        zeros -= 1
        k += 1
    for k in range(k,len(a)):
        a[k]=1
num=[0,1,0,1,0,0,1,0,1,1]
Sort(num)
print(num)

# sort binary array in linear time using for loop function:
def Sort(a):
    k=0
    for i in range(len(a)):
        if a[i]==0:
            a[k]=0
            k=k+1
    for k in range(k,len(a)):
        a[k]=1
num=[0,1,0,1,0,0,1,0,1,1]
Sort(num)
print(num)
