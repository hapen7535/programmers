def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number: #자기 자신 제외하고 본인과 같은 접두어가 있는지 다른 전화번호 확인
                return False
    return answer
