import sys

print(sys.argv)
print(sys.argv[0])
sum=0
for i in range(1,len(sys.argv)):
    sum+=i

print(sum)
