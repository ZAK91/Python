def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    w = "".join(l)
    return w
    

if __name__ == '__main__':
  
