# -*- coding: utf-8 -*-
"""
Created on Sep 16 01:49:04 2023

@author: Jerome Yutai Shen

"""


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

# binary search
class Solution:
    def guessNumber(self, n: int) -> int:
        start, end = 1, n # 此处跟模版不一样
        while start + 1 < end:
            my_guess = (start + end) // 2
            if_hit = guess(my_guess)
            if if_hit < 0:
                end = my_guess
            elif if_hit > 0:
                start = my_guess # my_guess + 1
            else:
                end = my_guess # my_guess - 1

        if guess(start) == 0:
            return start
        if guess(end) == 0:
            return end

"""The guess API is defined in the parent class GuessGame.
   @param num, your guess
   @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
      int guess(int num); 
public class Solution extends GuessGame {
    public int guessNumber(int n) {
        int low = 1;
        int high = n;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            int res = guess(mid);
            if (res == 0)
                return mid;
            else if (res < 0)
                high = mid - 1;
            else
                low = mid + 1;
        }
        return -1;
    }
}
"""
def guessNumber2(n: int) -> int:
    low, high = 1, n  # 此处跟模版不一样
    while low <= high:
        mid = (low + high) // 2
        res = guess(mid)
        if res == 0:
            return mid
        elif res < 0:
            high = mid - 1
        else:
            low = mid + 1

    return -1


