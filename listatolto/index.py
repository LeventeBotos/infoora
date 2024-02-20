def ask_question(question):
    return input(question)

async def lista_tolto():
    name = ask_question("Add meg a lista nevét: ")

    num = int(ask_question("Hány tagú lesz a lista?: "))

    lista = []
    for i in range(num):
        element = ask_question(f"Add meg a(z) {i + 1}. elemet: ")
        lista.append(element)

    print(f"A {name} listád elemei: {', '.join(lista)}")
    print(lista)


lista_tolto()
