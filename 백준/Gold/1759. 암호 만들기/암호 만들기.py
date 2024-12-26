#1759
from itertools import combinations

L, C = map(int, input().split())
alphabet = list(input().split())

alphabet.sort() # 알파벳 순서로 미리 정렬 -> 추후 따로 정렬할 필요 없음.
vowels = {'a', 'e', 'i', 'o', 'u'} # 모음 집합 생성

for combination in combinations(alphabet, L):
    moum = 0
    jaum = 0
    for i in combination:
        if i in vowels:
            moum += 1
        else:
            jaum += 1
    if moum >= 1 and jaum >=2 :
        print(*combination, sep='')