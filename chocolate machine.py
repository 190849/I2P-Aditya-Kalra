
Price = float(input("How much does your chocolate bar cost?"))
print("Please insert money")
Money = float(input("How much money did you insert?"))
print (Money - Price, "is your change")

Change = Money - Price

if Money < Price:
    print("Get out of here")

while Change >= 10:
    print("$10")
    break

while Change >= 5:
    print("$5")
    break
while Change >= 1:
    print("$1")
    break

