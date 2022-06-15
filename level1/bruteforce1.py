def solution(answers):
    answer = []
    
    solver1 = [1,2,3,4,5]
    solver2 = [2,1,2,3,2,4,2,5]
    solver3 = [3,3,1,1,2,2,4,4,5,5]
    
    count = [0 for i in range(3)]
    
    for i in range(len(answers)):
        if answers[i] == solver1[i%5]: #인덱스 범위를 초과하지 않기 위해서 모듈러 연산 적용
            count[0] += 1
        if answers[i] == solver2[i%8]:
            count[1] += 1
        if answers[i] == solver3[i%10]:
            count[2] += 1
    
    countMax = max(count)
    
    for i in range(len(count)):
        if countMax == count[i] :
            answer.append(i+1) #i에는 이미 다른 max 값이 있으므로
    
    return answer
