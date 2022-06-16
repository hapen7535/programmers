def solution(priorities, location):
    waiting = [i for i in range(len(priorities))]
    printlist = []
    
    while len(priorities) != 0 : #for 문 쓰면 pop 다했을 때 오류가 나는 수 있음
        if priorities[0] == max(priorities):
            printlist.append(waiting.pop(0))
            priorities.pop(0)
        else:
            priorities.append(priorities.pop(0))
            waiting.append(waiting.pop(0))
    
    return printlist.index(location) + 1
