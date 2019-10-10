#!/usr/bin/python

import argparse

# [2, 6, 3, 6]

# current_min_price = 2

# max_profit_so_far = 6-2


def find_max_profit(prices):
    # initialize first price
    current_min_price = prices[0]

    # initaliza first max profit
    max_profit_so_far = prices[1]-prices[0]

    for i in range(1, len(prices)):
        #
        if(prices[i] - current_min_price > max_profit_so_far):
            max_profit_so_far = prices[i] - current_min_price
        # reset curret_min_price
        if(prices[i] < current_min_price):
            current_min_price = prices[i]

    return max_profit_so_far


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
