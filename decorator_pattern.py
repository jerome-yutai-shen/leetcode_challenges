# -*- coding: utf-8 -*-
"""
Created on Jan 20 16:27:44 2024

@author: Jerome Yutai Shen

"""
class ICoffee:
    def makeCoffee(self):
        pass


class OriginalCoffee(ICoffee):
    def makeCoffee(self):
        print("原味咖啡 ", end="")


class CoffeeDecorator(ICoffee):
    def __init__(self, coffee: OriginalCoffee):
        self.coffee = coffee

    def makeCoffee(self):
        self.coffee.makeCoffee()


class MilkDecorator(CoffeeDecorator):
    def __init__(self, coffee: OriginalCoffee):
        super().__init__(coffee)

    def makeCoffee(self):
        super().makeCoffee()
        self.addMilk()

    def addMilk(self):
        print("加奶 ", end="")


class SugarDecorator(CoffeeDecorator):
    def __init__(self, coffee: OriginalCoffee):
        super().__init__(coffee)

    def makeCoffee(self):
        super().makeCoffee()
        self.addSugar()

    def addSugar(self):
        print("加糖", end="")


if __name__ == "__main__":
    coffee = OriginalCoffee()
    coffee.makeCoffee()
    print("")

    coffee = MilkDecorator(coffee)
    coffee.makeCoffee()
    print("")

    coffee = SugarDecorator(coffee)
    coffee.makeCoffee()