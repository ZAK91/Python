# Enter your code here. Read input from STDIN. Print output to STDOUT
''' x='-'
y='.|.'
m=int(input())
n=int(input())
for i in range(1, n, 2):
    print((y*i).center(m, x))
print("WELCOME".center(m, x))
for i in range(n, -1, -2):
    print((y*i).center(m,x))
'''
N, M = map(int, input().split())
for i in range(1):
    if i == N//2:
   
