# Amount to be traded, buy price and sell price
tradeAmount = float(input("Insert intended trade amount: "))
buyPrice = float(input("Buying Price: "))
sellPrice = float(input("selling Price: "))


# establishing if trade is profitable or not

def determine():
    if buyPrice > sellPrice:
        print("Loss")
    elif sellPrice > buyPrice:
        print("profit")
    else:
        print("zero rate")


# establishing the percentage difference

def difference():
    diff = float(buyPrice - sellPrice)
    print(diff)
    return diff


def differencePercentage():
    diff = float(buyPrice - sellPrice)
    percentage = ((diff / buyPrice) * 100)
    print(str(percentage) + "%")


def amount():
    diff = float(buyPrice - sellPrice)
    percentage = ((diff / buyPrice) * 100)
    amountDiff = ((percentage/100) * tradeAmount)
    print(str(round(amountDiff, 2)) + "ksh")



determine()
difference()
differencePercentage()
amount()
