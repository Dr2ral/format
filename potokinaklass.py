from threading import Thread
from time import sleep
class Knight(Thread):
    def __init__(self, name, skill):
        super().__init__()
        self.name = name
        self.skill = skill

    def run(self):
        enemies = 100
        days = enemies // self.skill
        print(f'{self.name}: На нас напали!')
        for i in range(1, days + 1):
            enemies = enemies - self.skill
            print(f'{self.name} сражается {i}-й день(дня)..., осталось {enemies} воинов.')
            sleep(5)


#knight1 = Knight('Tural', 20)
#a = knight1.battle()
kn1 = Knight('Sir Arthur', 10)
kn1.start()
kn2 = Knight('Sir Garet  ', 20)


kn2.start()
print('Битва началась!')
kn1.join()
kn2.join()
print('Битва окончена!')