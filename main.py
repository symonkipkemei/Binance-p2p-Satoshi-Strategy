from subPrograms import *


def checkIfProfitable():
    tradeAmount, buyPrice, sellPrice = values()
    determine(buyPrice, sellPrice)
    diff = difference(buyPrice, sellPrice)
    percentage = differencePercentage(diff, buyPrice)
    amount(tradeAmount, percentage)


def addtoFile():
    # get values and user information
    tradeAmount, buyPrice, sellPrice = values()
    gain = determine(buyPrice, sellPrice)
    deviation = difference(buyPrice, sellPrice)
    percentage = differencePercentage(deviation, buyPrice)
    amountGainLoss = amount(tradeAmount, percentage)

    # create a csv file, do not overwrite if it exists
    tradeRecords = open("tradeRecords.csv", "a")
    record = str(buyPrice) + "," + str(sellPrice) + "," + str(gain) + "," + \
             str(deviation) + "," + str(percentage) + "," + str(amountGainLoss) + "\n"
    tradeRecords.write(record)
    tradeRecords.close()


def displaytrades():
    # open csv file
    tradeRecords = open("tradeRecords.csv", "r")
    for x in tradeRecords:
        print(x)


def main():
    print("Binance p2p calculator\n"
          "choose option\n"
          "(1)check if trade is profitable\n"
          "(2)Add trade to file\n"
          "(3)display all trades completed\n"
          "(4)close program\n")
    option = int(input("option:"))

    if option == 1:
        checkIfProfitable()
    elif option == 2:
        addtoFile()
    elif option == 3:
        displaytrades()
    elif option == 4:
        print("good progress")


main()
