# -*- coding: utf-8 -*-
from random import randint

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.

ENLIGHTENMENT_CARMA_LEVEL = 777
my_carma = 0
carma_path = 'carma_log.txt'

class IamGodError(Exception):
    pass
class DrunkError(Exception):
    pass
class CarCrashError(Exception):
    pass

class GluttonyError(Exception):
    pass
class DepressionError(Exception):
    pass
class SuicideError(Exception):
    pass


def one_day():
    carma = randint(1,7)
    dice = randint(1,13)
    print(dice)
    if dice == 1:
        raise IamGodError('Оказывается я не Бог')
    elif dice ==2:
        raise DrunkError('Я слишком пьян, для этого дерьма')
    elif dice ==3:
        raise CarCrashError('Разбился на уличных гонках')
    elif dice ==4:
        raise GluttonyError('Я обожрался и не могу ходить')
    elif dice ==5:
        raise DepressionError('У меня депрессия')
    elif dice ==6:
        raise SuicideError('Прощай бренный мир')
    return carma

with open(carma_path, 'w', encoding='UTF-8') as log:
    while my_carma < ENLIGHTENMENT_CARMA_LEVEL:
        try:
            my_carma += one_day()
            print(f'My carma = {my_carma}')
        except IamGodError as exc:
            print("IamGodError")
            log.write(str(exc) + '\n')
        except DrunkError as exc:
            print("DrunkError")
            log.write(str(exc) + '\n')
        except CarCrashError as exc:
            print("CarCrashError")
            log.write(str(exc) + '\n')
        except GluttonyError as exc:
            print("GluttonyError")
            log.write(str(exc) + '\n')
        except DepressionError as exc:
            print("DepressionError")
            log.write(str(exc) + '\n')
        except SuicideError as exc:
            print("SuicideError")
            log.write(str(exc) + '\n')



# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError



# https://goo.gl/JnsDqu
