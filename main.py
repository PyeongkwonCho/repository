def positive(l):
    result = []
    for i in l:
        if i > 0:
            result.append(i)
    return result

print(positive([-3,-5,0,5,7]))