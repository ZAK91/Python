from collections import defaultdict
d = defaultdict(list)

n, m = map(int, input().split())

for i in range(n):
   a = input()
    d[a].append(i+1)



for i in range(m):
