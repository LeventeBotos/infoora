def inp(prompt, type):
    print(prompt)
    ret = input()
    if type == "int":
        try:
            ret2 = int(ret)
        except:
            print("type error")
    elif type == "float":
        try:
            ret2 = float(ret)
        except:
            print("type error")
    elif type == "bool":
        try:
            ret2 = bool(ret)
        except:
            print("type error")

    return ret2
