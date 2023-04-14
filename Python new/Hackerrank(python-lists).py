if __name__ == '__main__':
    N = int(input())
    
    

    
my_list = []
for _ in range(N):
    cmd, *args = input().split()
    args = list(map(int, args))
    if cmd == 'append':
        my_list.append(*args)
    elif cmd == 'insert':
        my_list.insert(*args)
    elif cmd == 'remove':
        my_list.remove(*args)
    elif cmd == 'pop':
        my_list.pop()
    elif cmd == 'sort':
        my_list.sort()
    elif cmd == 'reverse':
        my_list.reverse()
    elif cmd == 'print':
                 
