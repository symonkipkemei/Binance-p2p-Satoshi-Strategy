# Binance p2p Satoshi strategy

The satoshi strategy is a mirror of the bottom up economic model being advanced in Kenya.
Just as coined from its name , Satoshi, the strategy envisions to trade small amounts of BTCKES infinite times, as long as the BTCKES market 
remains profitable buy a margin of 0.2%.

where do we get this BTC from at a cheaper price?


## User
 A  frequent p2p trader who buys and sells amongst other
 p2p traders to make profit.
 
## trade currency
CRYPTO-FIAT 
 

## Parameters

1. Entry price in KES (USDTKES)
2. The amount bought (in KES) Note that the minimum conversion limit is 20 USDT
3. Sell price(To be calculated)
   (The sell price is unknown because we will be trading BTC in BTCKES market, yet we have bought it from USDTKES )
   We will need the following to calculate
   1. The USDTBTC exchange rate (To be obtained from btc spot trading during conversion).
      To avoid the tedious task of imputing many repetitive zeros, you will only input the last 4 dynamic digits.
   2. The BTCKES exchange rate (To be obtained from the advertiser's trade)
      The 50 has already been imputed, just insert the rest of the figures.The first two figures
      will be updated periodically according to the market movements.
4. The Amount sold (in KES)

A trade cycle is complete if the amount  bought is equal to the amount sold.

## Expected Outcome

1. If trade is profitable or not
2. Percentage of profit or loss
3. Amount of profit or loss
4. Store data in a csv file
5. Get some motivation at end of successful trade.


## Strategy

The strategy aims to minimise on risk and maximise on profit
by 
1. Avoiding transaction cost, use of equity bank as main mode of FIAT exchange
2. Trade BTCKES pair on bull markets only.
3. BTC converted to USDT as a store value at the end of daytrading.

Trades are intended to be one way profit, by selling btc .
BTC are bought by first buying USDTKES at market value and converting it into btc in fiat/spot wallet
before transferring the funds back to p2p wallet.This allows for ease of replenishing BTC once depleted 
thus the seed capital becomes constantly replenished.It is funny how we have managed to circumvent the 
strongest point in civic books , the lack of capital .

The profit margin is  accrued from :
1. Difference of USDTKES (buy price) and BTCKES (buy price-from the perspective of an advertiser it becomes the Sell price )
2. Instant replacement of seed capital in 20USDT bundles
3. Low profits but high frequency of trades.

## PROCEDURE


