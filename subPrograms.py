# Amount to be traded, buy price and sell price
def values():
    tradeAmount = float(input("Insert intended trade amount: "))
    buyPrice = float(input("Buying Price: "))
    sellPrice = float(input("selling Price: "))
    val = (tradeAmount, buyPrice, sellPrice)
    return val


# Establishing if trade is profitable or not
def determine(buyprice, sellprice):
    if buyprice > sellprice:
        print("loss")
        return "loss"
    elif sellprice > buyprice:
        print("profit")
        return "profit"
    else:
        print("zero rate")
        return "zero rate"


# Establishing the difference between the buy and sell price (Go getter)
def difference(buyprice, sellprice):
    diff = float(buyprice - sellprice)
    print(diff)
    return diff


# Establishing the percentage difference
def differencePercentage(diff, buyprice):
    percentage = ((diff / buyprice) * 100)
    print(str(percentage) + "%")
    return percentage


# Determine the amount lost or gained
def amount(tradeamount, percentage):
    amountDiff = ((percentage / 100) * tradeamount)
    print(str(round(amountDiff, 2)) + "ksh")