import random

count = 1

NEGATIVE_ONE_CHANCE = 0.2


def func(grid, r, c):
    res = [[-1 for _ in range(c)] for _ in range(r)]

    for j in range(c - 1, -1, -1):
        mono = []
        for i in range(r - 1, -1, -1):
            while mono and grid[mono[-1]][j] - mono[-1] < grid[i][j] - i:
                mono.pop()
            if mono:
                res[i][j] = mono[-1]
            mono.append(i)

    return res


def solve(grid, r, c, loc):
    global count
    res = func(grid, r, c)
    toWrite = []
    for i in range(r):
        line = []
        for j in range(c):
            line.append(res[i][j])
        toWrite.append(" ".join(map(str, line)) + "\n")

    with open(f"../data/{loc}/{count}.ans", "w") as f:
        f.writelines(toWrite)
    count += 1


# SAMPLE INPUTS

DIMENSION_MIN = 3
DIMENSION_MAX = 3
HEIGHT_MIN = 1
HEIGHT_MAX = 10

for _ in range(3):
    toWrite = []
    r = random.randint(DIMENSION_MIN, DIMENSION_MAX)
    c = random.randint(DIMENSION_MIN, DIMENSION_MAX)
    toWrite.append(f"{r} {c}\n")

    matrix = [[0 for _ in range(c)] for _ in range(r)]

    for i in range(r):
        line = []
        for j in range(c):
            value = -1
            if random.random() > NEGATIVE_ONE_CHANCE:
                value = random.randint(HEIGHT_MIN, HEIGHT_MAX)
            matrix[i][j] = value
            line.append(value)
        toWrite.append(" ".join(map(str, line)) + "\n")

    with open(f"../data/sample/{count}.in", "w") as f:
        f.writelines(toWrite)

    solve(matrix, r, c, "sample")

# SECRET CASES FOR TLE

DIMENSION_MIN = 430
DIMENSION_MAX = 430
HEIGHT_MIN = 4
HEIGHT_MAX = 4

for _ in range(1):
    toWrite = []
    r = random.randint(DIMENSION_MIN, DIMENSION_MAX)
    c = random.randint(DIMENSION_MIN, DIMENSION_MAX)
    toWrite.append(f"{r} {c}\n")

    matrix = [[0 for _ in range(c)] for _ in range(r)]

    value = random.randint(HEIGHT_MIN, HEIGHT_MAX)
    for i in range(r):
        line = []
        for j in range(c):
            matrix[i][j] = value
            line.append(value)
        toWrite.append(" ".join(map(str, line)) + "\n")

    with open(f"../data/secret/{count}.in", "w") as f:
        f.writelines(toWrite)

    solve(matrix, r, c, "secret")

# SECRET CASES FOR NORMAL

DIMENSION_MIN = 2
DIMENSION_MAX = 25
HEIGHT_MIN = 1
HEIGHT_MAX = 100

for _ in range(4):
    toWrite = []
    r = random.randint(DIMENSION_MIN, DIMENSION_MAX)
    c = random.randint(DIMENSION_MIN, DIMENSION_MAX)
    toWrite.append(f"{r} {c}\n")

    matrix = [[0 for _ in range(c)] for _ in range(r)]

    for i in range(r):
        line = []
        for j in range(c):
            value = -1
            if random.random() > NEGATIVE_ONE_CHANCE:
                value = random.randint(HEIGHT_MIN, HEIGHT_MAX)
            matrix[i][j] = value
            line.append(value)
        toWrite.append(" ".join(map(str, line)) + "\n")

    with open(f"../data/secret/{count}.in", "w") as f:
        f.writelines(toWrite)

    solve(matrix, r, c, "secret")

# SECRET CASES FOR COMPLICATED RANDOM

DIMENSION_MIN = 2
DIMENSION_MAX = 25
HEIGHT_MIN = 1
HEIGHT_MAX = 3

for _ in range(4):
    toWrite = []
    r = random.randint(DIMENSION_MIN, DIMENSION_MAX)
    c = random.randint(DIMENSION_MIN, DIMENSION_MAX)
    toWrite.append(f"{r} {c}\n")

    matrix = [[0 for _ in range(c)] for _ in range(r)]

    offset = 0
    for i in range(r):
        line = []
        for j in range(c):
            value = -1
            if random.random() > NEGATIVE_ONE_CHANCE:
                value = random.randint(HEIGHT_MIN, HEIGHT_MAX) + offset
            matrix[i][j] = value
            line.append(value)
        toWrite.append(" ".join(map(str, line)) + "\n")
        offset += 5

    with open(f"../data/secret/{count}.in", "w") as f:
        f.writelines(toWrite)

    solve(matrix, r, c, "secret")


# SECRET CASES FOR EDGE CASES

# SINGLE ROW

DIMENSION_MIN = 2
DIMENSION_MAX = 10
HEIGHT_MIN = 1
HEIGHT_MAX = 3

for _ in range(1):
    toWrite = []
    r = 1
    c = random.randint(DIMENSION_MIN, DIMENSION_MAX)
    toWrite.append(f"{r} {c}\n")

    matrix = [[0 for _ in range(c)] for _ in range(r)]

    for i in range(r):
        line = []
        for j in range(c):
            value = -1
            if random.random() > NEGATIVE_ONE_CHANCE:
                value = random.randint(HEIGHT_MIN, HEIGHT_MAX)
            matrix[i][j] = value
            line.append(value)
        toWrite.append(" ".join(map(str, line)) + "\n")

    with open(f"../data/secret/{count}.in", "w") as f:
        f.writelines(toWrite)

    solve(matrix, r, c, "secret")


# SINGLE COLUMN

DIMENSION_MIN = 10
DIMENSION_MAX = 20
HEIGHT_MIN = 1
HEIGHT_MAX = 3

for _ in range(2):
    toWrite = []
    r = random.randint(DIMENSION_MIN, DIMENSION_MAX)
    c = 1
    toWrite.append(f"{r} {c}\n")

    matrix = [[0 for _ in range(c)] for _ in range(r)]

    for i in range(r):
        line = []
        for j in range(c):
            value = -1
            if random.random() > NEGATIVE_ONE_CHANCE:
                value = random.randint(HEIGHT_MIN, HEIGHT_MAX)
            matrix[i][j] = value
            line.append(value)
        toWrite.append(" ".join(map(str, line)) + "\n")

    with open(f"../data/secret/{count}.in", "w") as f:
        f.writelines(toWrite)

    solve(matrix, r, c, "secret")

# EVERYONE BLOCKS EVERYONE

DIMENSION_MIN = 2
DIMENSION_MAX = 10
HEIGHT_MIN = 1
HEIGHT_MAX = 3

for _ in range(2):
    toWrite = []
    r = random.randint(DIMENSION_MIN, DIMENSION_MAX)
    c = random.randint(DIMENSION_MIN, DIMENSION_MAX)
    toWrite.append(f"{r} {c}\n")

    matrix = [[0 for _ in range(c)] for _ in range(r)]

    value = random.randint(HEIGHT_MIN, HEIGHT_MAX)
    for i in range(r):
        line = []
        for j in range(c):
            matrix[i][j] = value
            line.append(value)
        toWrite.append(" ".join(map(str, line)) + "\n")
        value += 50

    with open(f"../data/secret/{count}.in", "w") as f:
        f.writelines(toWrite)

    solve(matrix, r, c, "secret")

# NO ONE BLOCKS ANYONE

DIMENSION_MIN = 2
DIMENSION_MAX = 10
HEIGHT_MIN = 70
HEIGHT_MAX = 100

for _ in range(2):
    toWrite = []
    r = random.randint(DIMENSION_MIN, DIMENSION_MAX)
    c = random.randint(DIMENSION_MIN, DIMENSION_MAX)
    toWrite.append(f"{r} {c}\n")

    matrix = [[0 for _ in range(c)] for _ in range(r)]

    value = 150
    for i in range(r):
        line = []
        for j in range(c):
            matrix[i][j] = value
            line.append(value)
        toWrite.append(" ".join(map(str, line)) + "\n")
        value -= 5

    with open(f"../data/secret/{count}.in", "w") as f:
        f.writelines(toWrite)

    solve(matrix, r, c, "secret")

# 1X1 BOARD

HEIGHT_MIN = 1
HEIGHT_MAX = 25

for _ in range(1):
    toWrite = []
    r = 1
    c = 1
    toWrite.append(f"{r} {c}\n")

    matrix = [[0 for _ in range(c)] for _ in range(r)]

    for i in range(r):
        line = []
        for j in range(c):
            value = random.randint(HEIGHT_MIN, HEIGHT_MAX)
            matrix[i][j] = value
            line.append(value)
        toWrite.append(" ".join(map(str, line)) + "\n")

    with open(f"../data/secret/{count}.in", "w") as f:
        f.writelines(toWrite)

    solve(matrix, r, c, "secret")

# 1X1 BOARD WITH EMPTY SEAT

HEIGHT_MIN = 1
HEIGHT_MAX = 25

for _ in range(1):
    toWrite = []
    r = 1
    c = 1
    toWrite.append(f"{r} {c}\n")

    matrix = [[0 for _ in range(c)] for _ in range(r)]

    for i in range(r):
        line = []
        for j in range(c):
            value = -1
            matrix[i][j] = value
            line.append(value)
        toWrite.append(" ".join(map(str, line)) + "\n")

    with open(f"../data/secret/{count}.in", "w") as f:
        f.writelines(toWrite)

    solve(matrix, r, c, "secret")

# ALL EMPTY SEATS

HEIGHT_MIN = 1
HEIGHT_MAX = 25

for _ in range(1):
    toWrite = []
    r = 3
    c = 3
    toWrite.append(f"{r} {c}\n")

    matrix = [[-1 for _ in range(c)] for _ in range(r)]

    for i in range(r):
        line = []
        for j in range(c):
            line.append(value)
        toWrite.append(" ".join(map(str, line)) + "\n")

    with open(f"../data/secret/{count}.in", "w") as f:
        f.writelines(toWrite)

    solve(matrix, r, c, "secret")

# ALL SAME HEIGHT

HEIGHT_MIN = 1
HEIGHT_MAX = 25

for _ in range(1):
    toWrite = []
    r = 7
    c = 7
    toWrite.append(f"{r} {c}\n")

    matrix = [[0 for _ in range(c)] for _ in range(r)]

    for i in range(r):
        line = []
        for j in range(c):
            value = 2
            matrix[i][j] = value
            line.append(value)
        toWrite.append(" ".join(map(str, line)) + "\n")

    with open(f"../data/secret/{count}.in", "w") as f:
        f.writelines(toWrite)

    solve(matrix, r, c, "secret")
