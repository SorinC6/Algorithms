#!/usr/bin/python

import sys


def rock_paper_scissors(n):
   # define a list with R-P-S options and
    # list to contain the results
    choice = ['rock', 'paper', 'scissors']
    result = []

    # helper funciton to pass number of round 
    # and a list that contains results from previous rounds
    def helper(rounds, saved_arr):
        # end condition
        if rounds == 0:
            # if we're at 0 rounds, append list to the resulting list
            result.append(saved_arr)
            return

        # for every option in rps add the option to the list and run the fn again
        for i in choice:
            # run this function 3 times for every 'rock', 'paper', 'scissors' rounds number of times
            new_arr = saved_arr + [i]
            helper(rounds-1, new_arr)
    helper(n, [])
    return result


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
