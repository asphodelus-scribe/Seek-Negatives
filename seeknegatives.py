#for input i search set s for its opposite starting at i, at each step decrement n by the current value c in the set and replace that value with n\
# at each step replace the current value s[index(c)]=c+n and n+=c
print("enter i value:")
i = int(input())
n = i
c = i
s = []

limit = 15
count = 0

print("enter number of ints to count forward from i:")
f = int(input())
print("enter number of ints to count backward from i:")
b = int(input())

for j in range(i-b,i+f+1):
     s.append(j)
     print("setbuild:",s)
print("preset: ",s)

print("enter start index: ")
x = int(input())
while( (x < 0) or (x > len(s)) ):
    print("enter start index: ")
    x = int(input())

while c != -i:
    print("idx:",x)
    print("c:",c)
    print("n:",n)
    n -= c
    s[x] = n
    print("iterset:",s)
    if x == len(s)-1:
        x = 0
    else:
        x += 1
    c = s[x]
    count += 1
    if count == limit:
        print("limit reached ",end='')
        break

print("final set:",s)