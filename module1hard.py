# На вход даны следующие данные:
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students ={'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# Список grades содержит списки оценок для каждого ученика в алфавитном порядке.
# Множество students содержит неупорядоченную последовательность имён всех учеников в классе.

# srednyi_ball - список, в котором хранится средний балл студентов.
srednyi_ball = []
# jurnal - словарь, где ключ - имя ученика, а значение - его средний балл.
jurnal = {}

# spisok - cортированный по алфавиту список студентов
spisok_studentov = sorted(students)
# Проверка с помощью вывода на экран: 1) списка spisok;
# 2) типа данных, к которому относится относится список spisok.
print('Список студентов в алфавитном порядке: spisok_studentov: ', spisok_studentov, '.')
print('Объект spisok_studentov: относится к типу данных ', type(spisok_studentov), '.')

for i in range(len(grades)):
    # Вычисление среднего балла по оценкам каждого студента
    srednyi_ball.append(sum(grades[i])/len(grades[i]))

    # Объединение двух списков в словарь jurnal:
    # элементы списка spisok_studentov - ключи словаря jurnal;
    # элементы списка srednyi_ball - значения словаря jurnal.
    jurnal[spisok_studentov[i]] = srednyi_ball[i]

print('Средний балл студентов в соответствии со списком студентов в алфавитном порядке: ', srednyi_ball, '.')
print('Журнал преподавателя: ', jurnal, '.')




