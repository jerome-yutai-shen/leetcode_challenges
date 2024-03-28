# -*- coding: utf-8 -*-
"""
Created on Dec 28 03:28:03 2023

@author: Jerome Yutai Shen

"""
class Solution:
    months = {
        'Jan': '01', "Feb": '02', "Mar": '03',
        "Apr": '04', "May": '05', "Jun": '06',
        "Jul": '07', "Aug": '08', "Sep": '09',
        "Oct": '10', "Nov": '11', "Dec": '12'}

    def reformatDate(self, date: str) -> str:
        day, month, year = date.split()
        day = day[:-2].zfill(2)
        return f"{year}-{self.months.get(month)}-{day}"


if __name__ == "__main__":
    _ = Solution()
    print(_.reformatDate("20th Oct 2052"))
    print(_.reformatDate("6th Jun 1933"))
    print(_.reformatDate("26th May 1960"))