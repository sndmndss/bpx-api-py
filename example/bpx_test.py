from bpx.bpx import *

if __name__ == '__main__':
    bpx = BpxClient()

    bpx.init("T/NyhImyTeSHIUwblbxCGi9GhQHuwIPchW5Uqv91CFc=", "")

    print(bpx.depositAddress('Bitcoin'))
    #
    # print(bpx.balances())
    # print(bpx.deposits())
    # #
    # print(bpx.withdrawals(10, 0))

    bpx.debug = True

    # print(bpx.withdrawal("", "USDC", "Solana", "600"))

    # print(bpx.orderQuery('SOL_USDC', '111948072781414400'))
    # print(bpx.ordersQuery(''))

    # print(bpx.orderCancel('SOL_USDC','111947854837907456'))
    # print(bpx.ordersCancel('SOL_USDC'))

    #
    # print(bpx.orderHistoryQuery('SOL_USDC', 10, 0))
    # print(bpx.fillHistoryQuery('SOL_USDC', 10, 0))
    # bpx.proxies = {'http': 'http://127.0.0', 'https': 'http://127.0.0.'}
    #
    # print(bpx.ExeOrder('SOL_USDC', 'Bid', 'Limit', 'IOC', '0.1', '116.35'))
    # print(bpx.ExeOrder('SOL_USDC', 'Bid', 'Limit', '', '1', '13'))
    #
