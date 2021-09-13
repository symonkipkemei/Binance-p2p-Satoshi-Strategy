from subprograms import *
from motivation import *
import datetime


def checkifprofitable():
    buyPrice, amountBought, USDTBTC, BTCKES, amountSold = values()
    sellPrice = sellprice(USDTBTC, BTCKES)
    determine(buyPrice, sellPrice)
    diff = difference(buyPrice, sellPrice)
    percentage = differencepercentage(diff, buyPrice)
    amount(amountSold, percentage)


def addtofile():
    # get values and user information
    buyPrice, amountBought, USDTBTC, BTCKES, amountSold = values()
    sellPrice = sellprice(USDTBTC, BTCKES)
    sellPrice = round(sellPrice, 2)
    gain = determine(buyPrice, sellPrice)
    deviation = difference(buyPrice, sellPrice)
    deviation = round(deviation, 2)
    percentage = differencepercentage(deviation, buyPrice)
    percentage = round(percentage, 2)
    amountGainLoss = amount(amountSold, percentage)
    amountGainLoss = round(amountGainLoss, 2)

    tarehe = datetime.datetime.now()
    currentTime = tarehe - datetime.timedelta(microseconds=tarehe.microsecond)

    # create a csv file, do not overwrite if it exists
    tradeRecords = open("tradeRecords.csv", "a")
    record = "{0},{1},{2},{3},{4},{5},{6},{7},{8}\n".format(str(currentTime), str(buyPrice), str(amountBought),
                                                            str(sellPrice), str(amountSold), str(gain), str(deviation),
                                                            str(percentage), str(amountGainLoss))

    tradeRecords.write(record)
    tradeRecords.close()


def displaytrades():
    # open csv file
    tradeRecords = open("tradeRecords.csv", "r")
    for x in tradeRecords:
        print(x)


def main():
    correct = False
    while not correct:
        print("\nBinance p2p Satoshi Strategy\n"
              "(1)check if trade is profitable\n"
              "(2)Add trade to file\n"
              "(3)display all trades completed\n"
              "(4)close program\n")
        option = int(input("Choose option:"))

        if option == 1:
            checkifprofitable()

        elif option == 2:
            addtofile()
        elif option == 3:
            displaytrades()
        elif option == 4:
            correct = True
            print("\nThank you.")
            motivation()

        else:
            print("You might want to go back to kindergarten Symon. Try again")


main()
