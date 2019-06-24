n=input()
n=n.split(" ")
a=[]
for i in range(0,len(n)):
    a.append(n[i])
for i in range(0,len(a)+1):
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
            a.remove(a[j])
print(len(a))
