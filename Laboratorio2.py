import turtle
import random
import csv
import os

def esc(code):
    return f'\u001b[{code}m'


def array_init(array_in, st):
    for i in range(10):
        for j in range(10):
            if j == 0:
                array_in[i][j] = st * (8 - i) + st
            if i == 9:
                array_in[i][j] = j
    return array_in


def array_fill(array_fi, res, st):
    for i in range(9):
        for k in range(10):
            if abs(array_fi[i][0] - res[9 - k]) < st:
                for j in range(9):
                    if 8 - j == k:
                        array_fi[i][j + 1] = 1
    return array_fi


def print_plot(plot):
    for i in range(9):
        line = ''
        for j in range(10):
            if j == 0:
                line += white + str(plot[i][j])
            if plot[i][j] == 0:
                line += '  '
            elif plot[i][j] == 1:
                line += black + '  ' + white
        line += end
        print(line)
    print(white + '0 1 2 3 4 5 6 7 8 9' + end)

red = esc(41)
blue = esc(44)
white = esc(47)
end = esc(0)
black = esc(40)
green = esc(42)
print(red + ' ' * 10 + end + '\n' + white + ' ' * 10 + end + '\n' + blue + ' ' * 10 + end + '\n')

i = turtle.Turtle()
i.speed(100)
g = random.randint(1,5)
for j in range(g):
    i.right(60)
    i.forward(100)
    i.right(120)
    i.color('white')
    i.forward(50)
    i.color('black')
    i.right(120)
    i.forward(100)
    i.right(60)
    i.right(60)
    i.forward(100)
    i.right(120)
    i.color('white')
    i.forward(50)
    i.color('black')
    i.right(120)
    i.forward(100)
    i.right(60)
turtle.done()

array_plot = [[0 for col in range(10)] for row in range(10)]
result = [0 for i in range(10)]

for i in range(10):
    result[i] = i * 2
step = 2

array_init(array_plot, step)
array_fill(array_plot, result, step)
print_plot(array_plot)
print('\n')

m = 0
with open('lab1.csv',newline= '') as csvfile:
    reader = csv.DictReader(csvfile,delimiter=";")
    for row in reader:
        if int(row['Year-Of-Publication']) <= 1995:
            m +=1
x = round(m / 9409 * 100, 1)
y = 100 - x

if x < y:
    print(white + str(y) + '  '*4 + black + ' '*3 + white + ' '*1 + end)
    print(white + '  '*6 + black + ' '*3 + white + ' '*1 + end)
    print(white + str(x) + black + ' '*3 + white + ' '*5 + black + ' '*3 + white + ' '*1   + end)
    print(white + '  '*2 + black + ' '*3 + white + ' '*5 + black + ' '*3 + white + ' '*1 + end)
    print(white + ' до 1995   после' + end)
if x > y:
    print(white + str(x) + '  '*4 + black + ' '*3 + white + ' '*1 + end)
    print(white + '  '*6 + black + ' '*3 + white + ' '*1 + end)
    print(white + str(y) + black + ' '*3 + white + ' '*5 + black + ' '*3 + white + ' '*1   + end)
    print(white + '  '*2 + black + ' '*3 + white + ' '*5 + black + ' '*3 + white + ' '*1 + end)
    print(white + ' до 1995   после' + end)
if x == y:
    print(white + str(x) + black + ' '*3 + white + ' '*5 + black + ' '*3 + white + ' '*1 + end)
    print(white + '  ' * 2 + black + ' ' * 3 + white + ' ' * 5 + black + ' ' * 3 + white + ' ' * 1 + end)
    print(white + ' до 1995   после' + end)

os.system("clear")
print('         ' + green + ' '*6 + end)
print('       ' + green + ' '*14 + end)
print('       ' + green + ' '*9 + end)
print('       ' + black + ' '*9 + end)
os.system("clear")
print('         ' + green + ' '*6 + end)
print('       ' + green + ' '*14 + end + ' '*2 + white + ' '*3 + end)
print('       ' + green + ' '*9 + end)
print('       ' + black + ' '*9 + end)
os.system("clear")
print('         ' + green + ' '*6 + end)
print('       ' + green + ' '*14 + end + ' '*6 + white + ' '*3 + end)
print('       ' + green + ' '*9 + end)
print('       ' + black + ' '*9 + end)