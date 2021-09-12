# Binance p2p profit calculator

Determine if a trade you are about to undertake is
profitable or not and by what extent
 
## User
 A  frequent p2p trader who buys and sells amongst other
 p2p traders to make profit.
 
## trade currency
CRYPTO-FIAT 
 
## Parameters
1. Amount to be traded
2. Entry price
3. Selling price

## Expected Outcome
1. If trade is profitable or not
2. Percentage of profit or loss
3. Amount of profit or loss
4. Store data in a csv file


## Strategy

The strategy aims to minimise on risk and maximise on profit
by 
1. Avoiding transaction cost, use of equity bank as main mode of FIAT exchange
2. Trade BTCKES pair on bull markets only.
3. BTC converted to USDT as a store value at the end of daytrading.

Trades are intended to be one way profit, by selling btc .
BTC are bought by first buying USDTKES at market value and converting it into btc in fiat/spot wallet
before transferring the funds back to p2p wallet.This allows for ease of replenishing BTC once depleted 
thus the seed capital becomes constantly replenished.

The profit margin is  accrued from :
1. Difference of USDTKES (buy price) and BTCKES (buy price)
2. Instant replacement of seed capital in 20USDT bundles
3. Low profits but high frequency of trades.

## PROCEDURE


