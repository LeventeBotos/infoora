def settle_debts(participants):
    n = len(participants)
    total = sum(p["amount"] for p in participants)
    avg = total / n

    for p in participants:
        p["balance"] = round(p["amount"] - avg, 2)
  
    creditors = sorted([p for p in participants if p["balance"] > 0], key=lambda x: -x["balance"])
    debtors = sorted([p for p in participants if p["balance"] < 0], key=lambda x: x["balance"])

    transactions = []

    i = j = 0
    while i < len(debtors) and j < len(creditors):
        debtor = debtors[i]
        creditor = creditors[j]

        amount = min(-debtor["balance"], creditor["balance"])
        amount = round(amount, 2)

        transactions.append(f"{debtor['name']} fizet {amount} Ft-ot {creditor['name']}-nak/nek")

        debtor["balance"] += amount
        creditor["balance"] -= amount

        if abs(debtor["balance"]) < 1e-6:
            i += 1
        if abs(creditor["balance"]) < 1e-6:
            j += 1

    return transactions



mode = input("Válassz módot (1: fájlból beolvasás, 2 manuális input): ")
if mode == "1":
    file_path = input("Add meg a fájl elérési útját: ")
    with open(file_path, 'r') as file:
        lines = file.readlines()
        participants = []
        for line in lines:
            name, amount = line.strip().split(",")
            participants.append({"name": name.strip(), "amount": float(amount.strip())})
        result = settle_debts(participants)
        for r in result:
            print(r)
elif mode == "2":
    participants = []
    while True:
        name = input("Név (vagy 'vége' a befejezéshez): ")
        if name.lower() == "vége":
            break
        amount = float(input("Összeg: "))
        participants.append({"name": name, "amount": amount})
    result = settle_debts(participants)
    for r in result:
        print(r)

## Használtam ChatGPT-t, de csak egy példát tudott adni, hogyan hasznéljam az algoritmust.
## prompt: Solve this problem with python please