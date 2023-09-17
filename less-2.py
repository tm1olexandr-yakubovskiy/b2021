import random

class my_life:
    def __init__(self, name):
        self.name = name
        self.mood = 50
        self.household_chores = 10
        self.chill = 10
        self.relationship_friend = 10
        self.relationship_Parents = 10
        self.evaluations = 11
        self.study = 0
        self.alive = True
    def to_getevaluations(self):
        print('пора вчитись')
        self.mood -= 1
        self.study += 3
        self.study += 3
    def to_uprelationship_friend(self):
        print('почни спілкуватись')
        self.mood += 3
        self.study -= 1
        self.relationship_friend += 3
    def to_uprelationship_parents(self):
        print('Налагодь відносини з батьками')
        self.mood += 3
        self.study += 3
        self.relationship_Parents += 3
    def to_upmood(self):
        print('Порадуйся')
        self.mood += 3
        self.chill += 3
    def to_study(self):
        print('час навчатись')
        self.mood += 3
        self.evaluations += 3
    def to_chill(self):
        print('час відпочити')
        self.mood += 5
        self.evaluations -= 2
        self.study -= 1
        self.relationship_Parents -= 2
        self.relationship_friend -= 2
    def to_household_chores(self):
        print('А поприбирати?')
        self.mood += 3
        self.evaluations -= 1
        self.relationship_Parents += 3
        self.relationship_friend -= 2
        self.chill -= 2
    def is_alive(self):
        if self.study <- 10:
            print('Відрахували!')
            self.alive = False
        elif self.mood<=0:
            print('депресія(дед інсайд)')
            self.alive = False
        elif self.study>5:
            print('Маладець')
            self.alive=True
        elif self.relationship_friend <= 0:
            print("Ізгой")
            self.alive = False
        elif self.relationship_Parents <= 1:
            print("з батьками посварився")
            self.alive = False
        elif self.chill<=0:
            print('замучений бідося')
            self.alive = False
        elif self.household_chores <= 0:
            print('я в свинарнику?')
            self.alive = False
    def end_of_day(self):
        print(f'mood - {self.mood}')
        print(f'study - {round(self.study,2)}')
        print(f'relationship - {self.mood}')
        print(f'evaluations - {round(self.evaluations,2)}')
        print(f'household_chores - {self.household_chores}')
        print(f'Chill - {self.chill}')
    def live(self, day):
        day='Day ' + str(day) + ' of ' + self.name +' life'
        print(f'{day:-^50}')
        live_cube=random.randint(1,7)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_upmood()
        elif live_cube == 3:
            self.to_chill()
        elif live_cube == 4:
            self.to_study()
        elif live_cube == 5:
            self.to_getevaluations()
        elif live_cube == 6:
            self.to_uprelationship_parents()
        elif live_cube == 7:
            self.to_uprelationship_friend()
        self.end_of_day()
        self.is_alive()

olexandr = my_life(name="Olexandr")
for day in range(90):
    if olexandr.alive == False:
        break
    olexandr.live(day)

