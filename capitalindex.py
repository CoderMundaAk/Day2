def capitall(word):
    result=[]
    for i in range(len(word)-1):
        if word[i].isupper():
            result.append(i)
    return result
print(capitall("PytHon"))