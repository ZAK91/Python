def count_substring(string, sub_string):
    res = [i for i in range(len(string)) if string.startswith(sub_string, i)]
    return len(res)
  


if __name__ == '__main__':
  
