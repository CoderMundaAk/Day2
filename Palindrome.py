# def is_palindrome(word):
#     return word==word[::-1]

# print(is_palindrome("madam"))    # True
# print(is_palindrome("hello"))
def is_palindrome(word):
    left=0
    right=len(word)-1
    while left < right:
        if word[left]!=word[right]:
            return False
        left+=1
        right-=1
    return True
print(is_palindrome("hello"))

