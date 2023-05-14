import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 5
        self.money = 100
        self.stependia = 10
        self.relationship = 10
        self.work = 15
        self.alive = True
    def to_getwork(self):
        print('пора працювати')
        self.gladness -= 3
        self.progress -= 3
        self.money += 10
    def to_uprelationship(self):
        print('почни спілкуватись')
        self.gladness += 3
        self.progressc -= 1
    def to_getstependia(self):
        print('Вчись, щоб отримувати степендію')
        self.gladness += 3
        self.progress += 3
    def to_upmoney(self):
        print('пора заробляти')
        self.gladness += 3
        self.progress -= 0.12
    def to_study(self):
        print('час навчатись')
        self.progress += 0.12
        self.gladness -= 3
        self.stependia +=10
    def to_chill(self):
        print('час відпочити')
        self.gladness += 5
        self.progress -= 0.1
        self.stependia -= 0.1
        self.relationship += 5
    def to_sleep(self):
        print('час спати')
        self.gladness += 3
        self.progress -= 0.1
    def is_alive(self):
        if self.progress <- 0.5:
            print('Відрахували!')
            self.alive = False
        elif self.gladness<=0:
            print('депресія(дед інсайд)')
            self.alive = False
        elif self.progress>5:
            print('Закінчив екстерном')
            self.alive=False
        elif self.money <= 0:
            print("Відраховано за неуплату, немає коштів!")
            self.alive = False
        elif self.stependia <= 1:
            print("в мене даже бабушка не степендії")
            self.alive = False
        elif self.relationship<=0:
            print('депресія(дед інсайд)')
            self.alive = False
        elif self.work <= 0:
            print('безробітний на маминих грошах')
    def end_of_day(self):
        print(f'gladness - {self.gladness}')
        print(f'Progress - {round(self.progress,2)}')
        print(f'Money - {self.gladness}')
        print(f'Stependia - {round(self.stependia,2)}')
        print(f'Relationship - {self.relationship}')
        print(f'Work - {self.work}')
    def live(self, day):
        day='Day ' + str(day) + ' of ' + self.name +' life'
        print(f'{day:-^50}')
        live_cube=random.randint(1,7)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        elif live_cube == 4:
            self.to_upmoney()
        elif live_cube == 5:
            self.to_getstependia()
        elif live_cube == 6:
            self.relationship()
        elif live_cube == 7:
            self.work()
        self.end_of_day()
        self.is_alive()

dick = Student(name="Dick")
for day in range(365):
    if dick.alive == False:
        break
    dick.live(day)
