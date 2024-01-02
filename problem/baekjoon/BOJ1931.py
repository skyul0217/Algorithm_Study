"""
BOJ1931: 회의실 배정
한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다. 각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자. 단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다. 회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.
"""


def debug(rooms, confs):
    binary_list = [bin(num).replace("0b", "") for num in rooms]
    print(binary_list)
    print(confs)


# 회의 개수
num_meetings = int(input())

rooms = [0]  # 회의 경우의 수
confs = [0]  # 각 회의에 들어간 시간
num_startend = 0  # 시작하자마자 끝나는 회의 시간의 수
for meeting in range(num_meetings):
    # 시작 시간 / 끝나는 시간
    start, end = input().split(" ")
    start, end = int(start), int(end)
    if start == end:
        num_startend += 1
        continue

    # 시작 시간과 끝나는 시간을 비트로 취급
    mask = 2**end - 2**start

    idx = 0
    while idx < len(rooms):
        # mask: 시작 시간 ~ 끝나는 시간 = 1
        # rooms[idx] ^ mask: 시작 시간 ~ 끝나는 시간과 XOR, 겹치면 그 부분은 0이 된다.
        # mask와 AND 시 mask와 동일하면 겹치지 않은 것.
        if mask & (rooms[idx] ^ mask) == mask:
            rooms[idx] |= mask
            confs[idx] += 1
            break
        idx += 1

    # 모든 회의 경우의 수와 겹치면 새롭게 경우의 수 창작
    if idx == len(rooms):
        rooms.append(mask)
        confs.append(1)

    # debug(rooms, confs)

print(max(confs) + num_startend)

# Brute Force: O(N^2) -> 최적화 문제 발생
