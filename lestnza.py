def recurs(i, step=[]):
    if i > 10:
        i = 10
    step.append(i)
    if i >= 10:
        print(step)
        return True

    arr = [1, 2, 3, 4, 5]
    for a in arr:
        recurs(i + a, step.copy())


recurs(1)
