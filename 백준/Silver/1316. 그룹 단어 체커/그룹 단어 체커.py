# 1316 그룹 단어 체커

N = int(input())

count = 0
for _ in range(N):
    vocab = input()

    if len(vocab) == 1: # baseline
        count += 1
        continue

    dup_ck = set()
    dup_ck.add(vocab[0])

    for i in range(1, len(vocab)):
        if i != len(vocab) - 1:

            if vocab[i] == vocab[i - 1]: # 이전 알파벳과 동일하면 pass
                continue

            if vocab[i] not in dup_ck: # 새로운 알파벳이 등장하면 리스트에 추가
                dup_ck.add(vocab[i])
                continue

            break

        else: # 마지막까지 조건 만족하면 단어 개수 추가
            if vocab[i] == vocab[i - 1] or vocab[i] not in dup_ck:
                count += 1

print(count)        