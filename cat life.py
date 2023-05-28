import random

class Cat:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.hungry = 5
        self.friend = 2
        self.walking = 2
        self.sleep = 3
        self.fithingbetweencats = 2
        self.healht = 10
        self.alive = True
    def to_gowalk(self):
        print('пора іти гуляти!')
        self.gladness += 3
        self.hungry += 1
        self.friend += 1
    def to_sleep(self):
        print('час лягати спатки')
        self.gladness += 3
        self.hungry += 1
        self.sleep += 2
        self.healht += 1
    def to_notohungry(self):
        print('Їж шоб не бути голодним')
        self.gladness += 3
        self.hungry -= 1
        self.healht +=1
    def to_getafriend(self):
        print('пора знайти друзів')
        self.gladness += 3
        self.walking += 1
    def to_fight(self):
        print('Пора начистити другим рожу!')
        self.healht - 0.5
        self.gladness -= 1
        self.walking +=10
        self.fithingbetweencats +=1
    def is_alive(self):
        if self.healht <- 0:
            print('Помер!')
            self.alive = False
        elif self.gladness<=0:
            print('депресія(дед інсайд)')
            self.alive = False
        elif self.hungry <= 0:
            print('Помер від голоду!')
            self.alive=False
        elif self.sleep <= 2:
            print("Жостке виснаження")
            self.alive = False
        elif self.fithingbetweencats >= 10:
            print("Забили на смерть")
            self.alive = False
        elif self.friend<=0:
            print('депресія(дед інсайд)')
            self.alive = False
        elif self.walking <= 0:
            print('Помер вдома від перевтоми')
    def end_of_day(self):
        print(f'Hungry - {self.hungry}')
        print(f'Friend - {self.friend}')
        print(f'Fighting - {self.fithingbetweencats}')
        print(f'Sleep - {self.sleep}')
        print(f'Health - {self.healht}')
        print(f'Walking - {self.walking}')
        print(f'Gladness - {self.gladness}')
    def live(self, day):
        day='hour - ' + str(day) + ' of ' + self.name +' day life'
        print(f'{day:_^50}')
        live_cube=random.randint(1,5)
        if live_cube == 1:
            self.to_fight()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_getafriend()
        elif live_cube == 4:
            self.to_notohungry()
        elif live_cube == 5:
            self.to_gowalk()
        self.end_of_day()
        self.is_alive()

myarchik = Cat(name="Myarchik")
for day in range(24):
    if myarchik.alive == False:
        break
    myarchik.live(day)
