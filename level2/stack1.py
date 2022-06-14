def solution(progresses, speeds):
    answer = []
    day = 1
    count = 0
    
    while len(progresses) > 0:
        if progreses[0] + speeds[0]*day >= 100 :
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else :
            day += 1
            if count > 0 :
                answer.append(count)
                count = 0
        
    answer.append(count)
    return answer
