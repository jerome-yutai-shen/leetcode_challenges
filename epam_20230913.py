# -*- coding: utf-8 -*-
"""
Created on Sep 13 14:30:54 2023

@author: Jerome Yutai Shen

"""


def find_5_top_most_used_words(paragraph: str):
    all_words = paragraph.split(" ")
    words_freq = dict()

    for idx in range(len(all_words)):
        word = all_words[idx]
        if word[-1] in (",", "."):
            word = word[:-1]
        all_words[idx] = word.lower()

    for word in all_words:
        if word not in words_freq:
            words_freq[word] = 1
        else:
            words_freq[word] += 1

    sorted_list = [(k, words_freq.get(k)) for k in words_freq]
    sorted_list2 = sorted(sorted_list, key=lambda x: x[-1], reverse = True)
    print(sorted_list2[:5])
    return sorted_list2


def run_try_except(a: float, b: float) -> float:
    try:
        c = a/b
    except ZeroDivisionError:
        print(f"b: {b}")
    except ValueError:
        print(f"type of a: {type(a)}, type of b: {type(b)}")
    except TypeError:
        print("a and b must be float or int")
    else:
        print(f"a{a} / b {b} equals c {c}")
    finally:
        # c = a / b
        print(c)





if __name__ == "__main__":
    run_try_except(12, "abc")
    paragraph = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum"""
    _ = find_5_top_most_used_words(paragraph)
    print(_)

