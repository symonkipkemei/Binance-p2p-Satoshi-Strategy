# Amount to be traded, buy price and sell price
def values():
    buyPrice = float(input("Buying Price: "))
    amountBought = float(input("Amount Bought: "))
    USDTBTC = float("0.0000" + str(input("USDT to BTC Rate: ")))
    BTCKES = float(input("BTC to KES Rate: "))
    amountSold = float(input("Amount Sold: "))
    val = (buyPrice, amountBought, USDTBTC, BTCKES, amountSold)
    return val


def sellprice(USDTBTC, BTCKES):
    # Sell price is equal to USDTBTC * BTCKES
    sellPrice = USDTBTC * BTCKES
    print(round(sellPrice, 2))
    return sellPrice


# Establishing if trade is profitable or not
def determine(buyPrice, sellPrice):
    if buyPrice > sellPrice:
        print("loss")
        return "loss"
    elif sellPrice > buyPrice:
        print("profit")
        return "profit"
    else:
        print("zero rate")
        return "zero rate"


# Establishing the difference between the buy and sell price (Go getter)
def difference(buyPrice, sellPrice):
    diff = float(sellPrice-buyPrice)
    print(round(diff, 4), "Sx")
    return diff


# Establishing the percentage difference
def differencepercentage(diff, buyPrice):
    percentage = ((diff / buyPrice) * 100)
    print(str(round(percentage, 2)) + "%")
    return percentage


# Determine the amount lost or gained
def amount(amountSold, percentage):
    amountDiff = ((percentage / 100) * amountSold)
    print(str(round(amountDiff, 2)) + "ksh")
    return amountDiff
