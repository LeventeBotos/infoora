def inp(prompt, type):
    print(prompt)
    ret = input()
    if type == "int":
        try:
            ret = int(ret)
        except ValueError:
            print("Type error.")
    elif type == "float":
        try:
            ret = float(ret)
        except ValueError:
            print("Type error.")
    elif type == "bool":
        try:
            ret = bool(ret)
        except ValueError:
            print("Type error.")
    elif type == "str" or type == "string":
        try:
            ret = ret
        except ValueError:
            print("Type error")

    return ret
