def climbSteps(n: int) -> int:

    if n == 1 or n == 2:
        return n
    prevPrev = 1
    prev = 2
    current = 0
    for step in range(3, n + 1):
        current = prevPrev + prev
        prevPrev = prev
        prev = current
    print('Способы подняться по лестнице',climbStairs(n))
    return current


def climbStairs(n: int) -> list:
    if n == 1:
        return [[1]]
    elif n == 2:
        return [[1, 1], [2]]

    result = []
    for way in climbStairs(n - 1):
        result.append(way + [1])
    for way in climbStairs(n - 2):
        result.append(way + [2])
           
    return result

if __name__ == "__main__":
    n=6
    print('Количество вариантов как подняться по лестнице: ',climbSteps(n))