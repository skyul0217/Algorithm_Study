"""
BOJ1931: 회의실 배정
한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다. 각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자. 단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다. 회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.
"""

# 그리디 알고리즘 - 활동 선택 문제

# 회의 개수
num_meetings = int(input())

confs = []  # 각 회의에 들어간 시간
for meeting in range(num_meetings):
    # 시작 시간 / 끝나는 시간
    start, end = map(int, input().split(" "))
    confs.append([start, end])

# 끝나는 시간 순서대로 우선 정렬
# 동일한 끝나는 시간의 경우 시작 시간을 기준으로 정렬
confs.sort(key=lambda x: (x[1], x[0]))
max_conf = 1

comp_conf = confs[0]
for conf in confs[1:]:
    if conf[0] >= comp_conf[1]:
        max_conf += 1
        comp_conf = conf

print(max_conf)
