def solution(participant, completion):
    # 알파벳 순으로 문자열 정렬
    participant.sort()
    completion.sort()

    while completion:
        PersonP = participant.pop()
        PersonC = completion.pop()

        if PersonP != PersonC: #완주한 선수 중 참가자가 없다면
            return PersonP #완주하지 못한 선수이다

    return participant.pop() #완주한 선수와 비교하고 나서도 참가자 중 못한 선수가 있을 수 있으므로
    #completion의 길이는 participant의 길이보다 1 작으므로 pop만 해주면 된다
