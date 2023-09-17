
class Soda:
    def __init__(self, добавка=None):
        if isinstance(добавка, str):
            self.добавка=добавка
        else:
            self.добавка = None

    def show_my_drink(self):
        if self.добавка:
            print(f"Газировка та {self.добавка}")
        else:
            print("Звичайна газировка")


soda1 = Soda("лайм")
soda2 = Soda(None)


soda1.show_my_drink()
soda2.show_my_drink()