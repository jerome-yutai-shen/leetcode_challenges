# -*- coding: utf-8 -*-
"""
Created on Oct 20 15:29:33 2023

@author: Jerome Yutai Shen

"""
import pandas as pd


def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by = ["id"], inplace = True)
    person.drop_duplicates(subset=['email'], keep = "first", inplace = True)
    return


if __name__ == "__main__":
    data = {'id': [3, 2, 1],
            'email': ["john@example.com", "bob@example.com", "john@example.com"]}
    df = pd.DataFrame(data=data)
    df = df.drop_duplicates(subset=['email'], keep = "first")
    print(df)