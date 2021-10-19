#author: DMH 10/19/21

q = int(input("Enter the day of the date: "))
m = int(input("Enter the month of the date: "))
y = int(input("Enter the year of the date: "))

if m == 1:
    m = 13
    y = y - 1
if m == 2:
    m = 14
    y = y - 1


j = y // 100
k = y % 100

h = ((q + ((26 * (m + 1)) / 10) + k + (k / 4) + (j / 4) + (5 * j)) % 7) 

h = h // 1

if m == 13:
    m = 1
if m == 14:
    m = 2


if h == 0:
    print(str(m) + "/" + str(q) + "/" + str(y) + " was a Saturday")
if h == 1:
    print(str(m) + "/" + str(q) + "/" + str(y) + " was  a Sunday")
if h == 2:
    print(str(m) + "/" + str(q) + "/" + str(y) + " was  a Monday")
if h == 3:
    print(str(m) + "/" + str(q) + "/" + str(y) + " was  a Tuesday")
if h == 4:
    print(str(m) + "/" + str(q) + "/" + str(y) + " was  a Wednesday")
if h == 5:
    print(str(m) + "/" + str(q) + "/" + str(y) + " was  a Thursday")
if h == 6:
    print(str(m) + "/" + str(q) + "/" + str(y) + " was  a Friday")

