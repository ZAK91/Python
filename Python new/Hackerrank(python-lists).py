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
    
