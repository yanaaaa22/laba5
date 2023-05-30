import random
a = ['Смирнов', 'Орлов', 'Птичкин', 'Рубцов']
b = ['Иванов', 'Петров', 'Козлов', 'Сизов']
a1 = random.sample(a, 2)
b1 = random.sample(b, 2)
team = tuple(a1) + tuple(b1)
if 'Иванов' in team:
    print('Иванов в команде встречается', team.count('Иванов'), 'раз')
else:
    print('Иванова нет в команде')

print('Одногруппники :', a)
print('Другая группа :', b)
print('Спортивная команда :', team)
print('В команде', len(team), 'человека')
