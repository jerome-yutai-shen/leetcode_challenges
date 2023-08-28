# -*- coding: utf-8 -*-
"""
Created on Jun 26 19:39:26 2023

@author: Jerome Yutai Shen

"""


class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._msg_dict = { }

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        """
        if message not in self._msg_dict:
            # case 1). add the message to print
            self._msg_dict[message] = timestamp
            return True

        if timestamp - self._msg_dict[message] >= 10:
            # case 2). update the timestamp of the message
            self._msg_dict[message] = timestamp
            return True
        else:
            return False


if __name__ == "__main__":
    messages = [[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]
    logger = Logger()
    for ts_msg in messages[1:]:
        ts, msg = ts_msg
        print(logger.shouldPrintMessage(ts, msg))