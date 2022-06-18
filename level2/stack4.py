def solution(prices):
    answer = []
    
    for i in range(len(prices)):
        count = 0
        for j in range(i, len(prices)-1):
            if prices[i] > prices[j]:
                break
            else:
                count += 1
        answer.append(count)
        
    return answer
