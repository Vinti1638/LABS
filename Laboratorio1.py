import csv
file = open('lab1.csv')
l=0
for line in file:
    l+=1
print(l)
n=0

with open('lab1.csv',newline= '') as csvfile:
    reader = csv.DictReader(csvfile,delimiter=";")
    for row in reader:
        if len(row['Book-Title'])>30:
          n+=1
    print(n)

print('введите имя автора: ')
k=0
x=input(str)
with open('lab1.csv',newline= '') as csvfile:
    reader = csv.DictReader(csvfile,delimiter=";")
    for row in reader:
        if row['Book-Author'] == x:
            if row['Year-Of-Publication']=='2014' or row['Year-Of-Publication']=='2016' or row['Year-Of-Publication'] =='2017':
                print(row['Book-Title'])
                k+=1
    if k==0:
        print('Автор не найден')

import random
m=1
u=1
d=0
filepath = r"lab1.csv"
f = open("gg.txt", "w")
while d<20:
    file = open(filepath, "r", newline="")
    i = random.randint(1, 9410)
    for row in file:
        a = row.split(';')
        if m == i:
            f.write(str(u)+') ')
            f.write(a[2] + '.' + a[1] + '-' + a[3] + '; \n')
            u+=1
        m+=1
    m=1
    d+=1
    file.close()