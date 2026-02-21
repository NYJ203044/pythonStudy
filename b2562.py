import sys
input = sys.stdin.readline

max_val=0
max_index=0

for i in range(9):
    n=int(input())
    if n>max_val:
        max_val=n
        max_index=i+1

print(max_val)
print(max_index)