def format():
    x = "Yooo {} Is just so much {} {}.{}"
    # x = "Yooo {1} Is just so much {0} {2}."

    print(x)
    print(x.format("TypeScript", "better", "period", 19))

    for i in range(3):
        print("works")
