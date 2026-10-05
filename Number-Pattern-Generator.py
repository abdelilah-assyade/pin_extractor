def number_pattern(n):
    if type(n) is not int:
        return "Argument must be an integer value."
    if n < 1 :
        return "Argument must be an integer greater than 0."
    num=""
    for i in range (1,n+1):
        num+=str(i)+" "
    return num.strip()
print(number_pattern(4))