import random

class Unit:
    id_counter = 0

    def __init__(self, team):
        self.id = Unit.id_counter
        Unit.id_counter += 1
        self.team = team

class Soldier(Unit):
    def follow_hero(self, hero):
        print(f"Солдат {self.id} следует за героем {hero.id}")

class Hero(Unit):
    def __init__(self, team):
        super().__init__(team)
        self.level = 1

    def increase_level(self):
        self.level += 1
        print(f"Уровень героя {self.id} увеличен до {self.level}")

def main():
    # Создаем по одному герою для каждой команды
    hero_team_1 = Hero(team=1)
    hero_team_2 = Hero(team=2)

    soldiers_team_1 = []
    soldiers_team_2 = []

    count_team_1 = 0
    count_team_2 = 0

    # Генерируем солдат и распределяем их по командам случайным образом
    for _ in range(100):  # предположим, генерируем 100 солдат
        team = random.choice([1, 2])
        soldier = Soldier(team)
        if team == 1:
            soldiers_team_1.append(soldier)
            count_team_1 += 1
        else:
            soldiers_team_2.append(soldier)
            count_team_2 += 1

    # Выводим количество солдат в каждой команде
    print(f"Команда 1: {count_team_1} солдат")
    print(f"Команда 2: {count_team_2} солдат")

    # Увеличиваем уровень героя, принадлежащего команде с большим количеством солдат
    if count_team_1 > count_team_2:
        hero_team_1.increase_level()
    elif count_team_2 > count_team_1:
        hero_team_2.increase_level()

    # Отправляем одного из солдат первого героя следовать за ним
    if soldiers_team_1:
        soldier_to_follow = soldiers_team_1[0]
        soldier_to_follow.follow_hero(hero_team_1)
        print(f"Солдат {soldier_to_follow.id} из команды 1 следует за героем {hero_team_1.id}")
    elif soldiers_team_2:
        soldier_to_follow = soldiers_team_2[0]
        soldier_to_follow.follow_hero(hero_team_2)
        print(f"Солдат {soldier_to_follow.id} из команды 2 следует за героем {hero_team_2.id}")

if __name__ == "__main__":
    main()
