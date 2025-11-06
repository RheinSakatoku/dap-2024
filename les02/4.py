strs = input("Введи слова через пробел").split()

def solution(strs):
    shortest = min(strs, key=len)
    for i in range(len(shortest)):
        for j in range(len(strs)):
            if shortest[i] != strs[j][i]:
                return shortest[:i]
    return shortest
            
print(solution(strs))