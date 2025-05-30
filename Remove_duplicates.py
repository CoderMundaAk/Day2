def remove_dub(word):
    seen=set()
    result=''
    for i in word:
        if i not in seen:
            seen.add(i)
            result+=i
    return result


print(remove_dub("banana"))   # Output: "ban"
print(remove_dub("hello"))   
