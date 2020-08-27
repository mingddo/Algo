#
# import sys
# #sys.stdin = open("input.txt", "r")
# #중복 된 값 지우는 함수
# def test (words):
#     i = 0
#     l = len(words)
#     while True:
#         if i >= (l - 1):
#             return words
#             break
#         if words[i] == words[i+1]:
#             words.pop(i+1)
#             words.pop(i)
#             l = len(words)
#         else:
#             i += 1
#
# def test_words(words):
#     for j in range(len(words)-1):
#         if words[j] == words[j+1]:
#             return words
#     return len(words)
#
#
#
#
# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     words = list(input())
#     while True:
#         words = test(words)
#         result = test_words(words)
#         if type(result) is int:
#             break
#
#     print(f'#{test_case} {result}')

def dfs(word):
    l = len(word)
    for i in range(l-1):
        if word[i] == word[i + 1]:
            word.pop(i + 1)
            word.pop(i)
            return dfs(word)
    return l


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    words = list(input())
    result = dfs(words)

    print('#{} {}'.format(test_case, result))

