from collections import deque


def solution(n, delivery):
    answer = ''
    result = [0] * (n + 1)
    delivery.sort(key=lambda x: -x[2])
    print(delivery)
    # 0은 모른다. 1은 있다. 2는 없다.

    for i in range(len(delivery)):
        item_1, item_2, is_ok = delivery[i]
        if is_ok == 1:  # 배송 성공
            result[item_1], result[item_2] = 1, 1
        else:  # 배송 실패
            # 만약 둘 중에 하나라도 있으면 나머지 하나는 없다.
            if result[item_1] == 1:
                result[item_2] = 2
            elif result[item_2] == 1:
                result[item_1] = 2

    for i in range(1, n + 1):
        if result[i] == 0:
            answer += '?'
        elif result[i] == 1:
            answer += 'O'
        else:
            answer += 'X'
    return answer


print(solution(7, [[5, 6, 0], [1, 3, 1], [1, 5, 0], [7, 6, 0], [3, 7, 1], [2, 5, 0]]))
