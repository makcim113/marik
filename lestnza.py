def recurs(i, step=[]):
    step.append(i)
    if i >= 10:
        print(step)
        return True

    arr = [1, 2, 3, 4, 5]
    for a in arr:
        if i + a <= 10:
            recurs(i + a, step.copy())


recurs(1)
