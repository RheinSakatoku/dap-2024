x = int(input("Введи число"))

def solution(x):
    if x > 0:
        n = x
        rev = 0
        while x > 0:
            rev = rev*10 + (x % 10)
            x = x // 10
        if rev == n:
            return True
        else:
            return False
    else:
        return False

print(solution(x))