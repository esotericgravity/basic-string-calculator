def parse_calc(str):
    for i in range(len(str)):
        if str[i]=='+':
            try:
                a=int(str[:i]) + int(str[i+1:])
                print(int(str[:i]))
            except ValueError:
                a="invalid, string cannot be converted to integer."
            return a
        if str[i]=='-':
            try:
                a=int(str[:i]) - int(str[i+1:])
                print(int(str[:i]))
            except ValueError:
                a="invalid, string cannot be converted to integer."
            return a
        if str[i]=='*':
            try:
                a=int(str[:i]) * int(str[i+1:])
                print(int(str[:i]))
            except ValueError:
                a="invalid, string cannot be converted to integer."
            return a
        if str[i]=='/':
            try:
                a=int(str[:i]) / int(str[i+1:])
                print(int(str[:i]))
            except ValueError:
                a="invalid, string cannot be converted to integer."
            return a
        if str[i]=='^':
            try:
                a=int(str[:i]) ** int(str[i+1:])
                print(int(str[:i]))
            except ValueError:
                a="invalid, string cannot be converted to integer."
            return a        
    return "invalid, string does not contain an operator"

if __name__ == '__main__':
    print(parse_calc(""))
