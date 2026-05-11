def solution(numbers, hand):
    answer = ''
    distance = [[3,1]]
    if hand == 'right':
        hand = 'R'
    else:
        hand = 'L'
    for i in range(3):
        for j in range(3):
            distance.append([i,j])
    distance.append([3,0])
    distance.append([3,2])
    left_idx = 10
    right_idx = 11
    for n in numbers:
        if n == 1 or n == 4 or n == 7:
            answer += 'L'
            left_idx = n
        elif n == 3 or n == 6 or n == 9:
            answer += 'R'
            right_idx = n
        else:
            left = (abs(distance[left_idx][0] - distance[n][0]) + abs(distance[left_idx][1] - distance[n][1]))
            right = (abs(distance[right_idx][0] - distance[n][0]) + abs(distance[right_idx][1] - distance[n][1]))
            if left > right:
                answer += 'R'
                right_idx = n
            elif left < right:
                answer += 'L'
                left_idx = n
            else:
                answer += hand
                if hand == 'R':
                    right_idx = n
                else:
                    left_idx = n
    return answer