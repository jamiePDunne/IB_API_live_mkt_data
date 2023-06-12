import asyncio
from ib_insync import IB, Contract, TickByTickAllLast

async def market_data():
    ib = IB()
    await ib.connectAsync('localhost', 4002, clientId=1)

    contract = Contract(conId=540729504, symbol='FDAX', secType='FUT', exchange='EUREX', currency='EUR')
    await ib.qualifyContractsAsync(contract)

    ticker = ib.reqTickByTickData(contract, 'AllLast')

    # Print the latest tick data immediately
    while True:
        await asyncio.sleep(2)
        print(ticker.time, ticker.last)

def main():
    asyncio.run(market_data())

if __name__ == '__main__':
    main()
