class Coin:
    def __init__(self, value):
        self.value = value

    def show_value(self):
        print(f"This coin is worth {self.value}")

my_coin = Coin(25)
my_coin.show_value()