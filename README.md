# Игра угадай число от 1 до 10

Очень простая игра, где нужно вводить в терминал числа от 1 до 10, пытаясь угадать, какое конкретно загадал компьютер.
Он будет выдавать подсказки, чтобы помочь.

Тренировалась с docker, создала образ с помощью Dockerfile, загрузила его на Docker hub.
теперь игру можно запустить как просто через Run в интерпретаторе, так и через Docker
c помощью команды:

docker run -it asayaru/number-guess:1.0.0
