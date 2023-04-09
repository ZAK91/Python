from collections import defaultdict
d = defaultdict(list)

n, m = map(int, input().split())

for i in range(n):
   a = input()
    d[a].append(i+1)



for i in range(m):
    b = input()
    if len(d[b]) > 0:
        print(*d[b])
        
    
