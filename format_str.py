team1_name = "'Мастера кода'"
team2_name = "'Волшебники данных'"
team1_num = int(input()) #5
team2_num = int(input()) #6
score_1 = int(input()) #40
score_2 = int(input()) #42
team1_time = int(input()) #1552.512
team2_time = int(input()) #2153.31451
challenge_result = ''
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total

#Использование %:
print("В команде %s участников: %d ! " % (team1_name, team1_num))
print("Итого сегодня в командах участников: %s и %s !" % (team1_num, team2_num))

#Использование format():
print("Команда {} решила задач: {} !".format(team2_name, score_2))
print("{} решили задачи за {} с !".format(team2_name, team1_time))

#Использование f-строк:
print(f"Команды решили {score_1} и {score_2} задач.")
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    print(f'Победа команды {team1_name}!')
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    print(f'Победа команды {team2_name}!')
else:
    print("Ничья!")
print(f"Сегодня было решенно {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.")