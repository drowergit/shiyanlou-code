i = 0
while i<100:
    i += 1
    if i % 7 == 0 or i % 10 == 7 or i in range(70, 80):
        continue
    else:
        print(i)
