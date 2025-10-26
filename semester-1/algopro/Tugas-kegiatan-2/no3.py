print("Program snack drink & snack drink.")
print("Dibuat oleh Ahmad")

for i in range(1, 15):
    if i % 2 & i % 3 == 0:
        print(i, "snack and drink")
    elif i % 2:
        print(i, "drink")
    elif i % 3:
        print(i, "snack")