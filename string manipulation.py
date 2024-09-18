str = input("enter a string")

def reversed_str(string):
    string = list(str)
    string.reverse()
    return "".join(string)
print(reversed_str(str))
