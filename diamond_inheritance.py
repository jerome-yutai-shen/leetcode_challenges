# -*- coding: utf-8 -*-
"""
Created on Jan 18 21:02:15 2024

@author: Jerome Yutai Shen

"""




class Electrical(object):
    def chat(self):
        print('Chat with friend in electrical!')

    def watch_movie(self):
        print('Watch movie in electrical!')

    def game(self):
        print('Play game in electrical!')


class Phone(Electrical):
    def game(self):
        super().game()
        print('Play game in phone!')


class Computer(Electrical):
    def watch_movie(self):
        print('Watch movie in computer!')

    def game(self):
        super().game()
        print('Play game in computer!')


class HuaWei(Phone, Computer):
    pass
    #def game(self):
        # super().game()
     #   print('Play game in HuaWei!')


class Root:
    def ping(self):
        print(f"{self}.ping() in Root")
    def pong(self):
        print(f"{self}.pong() in Root")
    def __repr__(self):
        cls_name = type(self).__name__
        return f"<instance of {cls_name}>"
class A(Root):
    def ping(self):
        print(f"{self}.ping() in A")
        super().ping()
    def pong(self):
        print(f"{self}.pong() in A")
        super().pong()
class B(Root):
    def ping(self):
        print(f"{self}.ping() in B")
        super().ping()
    def pong(self):
        print(f"{self}.pong() in B")
class Leaf(A, B):
    def ping(self):
        print(f"{self}.ping() in Leaf")
        super().ping()


class AA:
    """A"""
    def who(self):
        print("who in AA is now being executed\n###\n")
        print('who() of AA is executed\n###\n')


class BB(AA):
    """This is BB, super is AA"""
    def who(self):
        print("who in BB is now being executed")
        super().who()
        print('who() of BB is executed\n###\n')


class CC(AA):
    """This is CC, super is AA"""
    def who(self):
        print("who in CC is now being executed")
        super().who()
        print('who() of CC is executed\n###\n')


class CC1(AA):
    """This is CC1, super is AA"""
    def who(self):
        print("who in CC1 is now being executed")
        super().who()
        print('who() of CC1 is executed\n###\n')


class CC2(AA):
    """This is CC2, super is AA"""
    def who(self):
        print("who in CC2 is now being executed")
        super().who()
        print('who() of CC2 is executed\n###\n')

class DD(BB, CC, CC1, CC2):
    def who(self):
        print("who in DD is now being executed")
        print(super().__doc__)
        super().who()
        # super().who()
        print('who of DD is executed', end = '\n###\n')



if __name__ == "__main__":
    d = DD()
    d.who()

    leaf = Leaf()
    leaf.ping()