for a in range(3, 100 + 1):
    for b in range(2, a):

        if (a % b) == 0:
            break
    else:
        print(a)

