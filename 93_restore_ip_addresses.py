# -*- coding: utf-8 -*-
"""
Created on Jun 08 11:36:42 2022

@author: Jerome Yutai Shen

"""
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if not s:
            return []
        ip = []
        result = []
        self.findIPs(s, 0, 1, ip, result)
        self.findIPs(s, 0, 2, ip, result)
        self.findIPs(s, 0, 3, ip, result)
        return result

    def findIPs(self, s, start_index, split_length, ip, result):
        if start_index > len(s):
            return

        if start_index == len(s):
            if len(ip) != 4:
                return
            ip_adress = ""
            for i in ip:
                ip_adress += str(i)
                ip_adress += "."
            ip_adress = ip_adress[:-1]
            if ip_adress not in result:
                result.append(str(ip_adress))
            return

        if len(ip) == 4 or (s[start_index] == '0' and split_length > 1):
            return

        address = int(s[start_index:start_index + split_length])
        if address > 255:
            return
        ip.append(address)
        for i in range(1, 4):
            self.findIPs(s, start_index + split_length, i, ip, result)
        ip.pop()