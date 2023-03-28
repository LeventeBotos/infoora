def inp(prompt, type):
    print(prompt)
    ret = input()
    if type == "int":
        try:
            ret = int(ret)
        except ValueError:
            print("type error")
    elif type == "float":
        try:
            ret = float(ret)
        except ValueError:
            print("type error")
    elif type == "bool":
        try:
            ret = bool(ret)
        except ValueError:
            print("type error")

    return ret
