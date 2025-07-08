def get_num_words(text):
    return len(text.split())

def get_num_chars(text):
    dic = {}

    for char in text.lower():        
        if(char in dic):
            dic[char] += 1
        else:
            dic[char] = 1

    return dic

def sort_chars(e):
    return e["num"]

def get_sorted_dics(dic_chars):
    unsorted = []

    for char in dic_chars:
        if(char.isalpha()):
            unsorted.append({"char":char, "num": dic_chars[char]})

    unsorted.sort(reverse=True, key=sort_chars)
    
    return unsorted

