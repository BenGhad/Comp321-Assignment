import random

count = 1

NEGATIVE_ONE_CHANCE = 0.2


def func(grid):
    R = len(grid)
    C = len(grid[0])
    blocker = [[-1 for _ in range(C)] for _ in range(R)]

    for c in range(C):
        stack = []
        for r in range(R - 1, -1, -1):
            if grid[r][c] == -1:
                blocker[r][c] = -1
                continue

            eff_r = grid[r][c] + (R - r - 1)

            while stack:
                k = stack[-1]
                eff_k = grid[k][c] + (R - k - 1)
                if eff_k >= eff_r:
                    break
                stack.pop()

            if not stack:
                blocker[r][c] = -1
            else:
                blocker[r][c] = stack[-1]
            stack.append(r)

    return blocker


def solve(grid, r, c, loc):
    global count
    res = func(grid)
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

DIMENSION_MIN = 2
DIMENSION_MAX = 5
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
DIMENSION_MAX = 25
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

DIMENSION_MIN = 2
DIMENSION_MAX = 25
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
DIMENSION_MAX = 25
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
DIMENSION_MAX = 25
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
