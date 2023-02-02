### Hexlet tests and linter status:
[![Actions Status](https://github.com/olyavorobeva/python-project-49/workflows/hexlet-check/badge.svg)](https://github.com/olyavorobeva/python-project-49/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/c5be20bbe33e755776f4/maintainability)](https://codeclimate.com/github/olyavorobeva/python-project-49/maintainability)

# Пакет с игрой "Игры Разума".

## Первая игра: "Проверка на чётность"
Суть игры в следующем: пользователю показывается случайное число. И ему нужно ответить yes, если число чётное, или no — если нечётное

## Вторая игра: "Калькулятор"
Суть игры в следующем: пользователю показывается случайное математическое выражение, например 35 + 16, которое нужно вычислить и записать правильный ответ.

## Третья игра: "НОД"
Суть игры в следующем: пользователю показывается два случайных числа, например, 25 50. Пользователь должен вычислить и ввести наибольший общий делитель этих чисел.

## Четвертая игра: "Арифметическая прогрессия"
Суть игры в следующем: существует ряд чисел, образующий арифметическую прогрессию, одно число отсутствует и заменино двумя точками. Необходимо определить это число.

## Пятая игра: "Простое ли число?"
Суть игры в следующем: определить является ли число простым

## Установка и запуск игры:
* Установите python версии 3.6 или выше
* Удостоверьтесь, что у вас установлен свежий pip, вызвав ```python3 -m pip --version``` Потребуется версия 19 и выше. При необходимости обновите pip командой ```python3 -m pip install --upgrade --user pip```
* Установите пакетный менеджер poetry. В результате должна стать доступной команда poetry. Проверьте, что poetry имеет версию "1.2.0" и выше. Настройте poetry так, чтобы тот создавал виртуальные окружения в директории проекта (выполните команду poetry config virtualenvs.in-project true).
* Склонируйте созданный репозиторий проекта локально. ```git clone https://github.com/olyavorobeva/python-project-49.git```
В результате клонирования репозитория в вашей файловой системе появится корневая директория проекта — в ней будем размещать все файлы проекта. По умолчанию, имя этой директории будет таким же, как имя репозитория. Но, если захотите, вы сами можете выбрать имя (переименовать) для корневой директории.
* Соберите игру командой ```make build```
  и установите командой ```make package-install```
* Теперь можно играть набрав название одной из игр:
```
  brain-even
  brain-calc
  brain-gcd
  brain-progression
  brain-prime
```
## Демо игр
[Demo brain-even](https://asciinema.org/a/551628)
[Demo brain-calc](https://asciinema.org/a/eeizYaGRUYwDuGgT1iIdtrKvV)
[Demo brain-gcd](https://asciinema.org/a/dtWsqZ7BZy0KH41EIVbJnXwFJ)
[Demo brain-progression](https://asciinema.org/a/fdoRmzSK3fJZMcLI3GaLg9B6l)
[Demo brain-prime](https://asciinema.org/a/556206)
