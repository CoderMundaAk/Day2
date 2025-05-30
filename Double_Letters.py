def d_char(charr):
    for c in range(len(charr)-1):
        if charr[c]==charr[c+1]:
            return True
    return False
print(d_char("banana"))