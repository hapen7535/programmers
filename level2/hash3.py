def solution(clothes):
    answer = 1
    closet = {}
    
    for cloth, kind in clothes:
        if kind in closet:
            closet[kind] += 1
        else:
            closet[kind] = 1
    
    for key, value in closet.items():
        answer *= (value + 1)
    
    return answer-1
