# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.
class NotNameError(Exception):
    pass

class NotEmailError(Exception):
    pass


analized_file = 'registrations.txt'
good_data = 'registrations_good.log'
bad_data = 'registrations_bad.log'
errors = 0

with open(analized_file, 'r', encoding='utf-8') as file, \
        open(good_data, 'w', encoding='utf-8') as gooddata, open(bad_data, 'w', encoding='utf-8') as baddata:
    for line in file:
        try:
            name, email, age = line.split(' ')
            if 10 > int(age) or int(age) > 99:
                raise ValueError('Не корректный возраст')
            if not name.isalpha():
                raise NotNameError('Не корректное имя')
            if not '@' or not '.' in email:
                raise NotEmailError
            gooddata.write(line)

        except ValueError as exc:
            if 'unpack' in exc.args[0]:
                baddata.write(line)
                errors += 1
                # print(f"Не хватает операндов {exc}")
            elif 'int' in exc.args[0]:
                baddata.write(line)
                errors += 1
                # print(f"Возраст не число: {age}")

            else:
                baddata.write(line)
                errors += 1
                # print(f"{exc} в строке {line}")

        except NotNameError as exc:
            baddata.write(line)
            errors += 1
            # print(exc, name)

        except NotEmailError as exc:
            baddata.write(line)
            errors += 1
            # print(f'Не корректная почта {email}')

print(f'Проверка завершена, количество ошибок: {errors}')
