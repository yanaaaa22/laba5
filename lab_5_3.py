roster = ('понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье')
x = int(input('сколько хотите выходных?: '))
x = len(roster) - x
print('рабочие дни: ', *roster[0:x])
print('выходные дни: ', *roster[x:len(roster)+1])



