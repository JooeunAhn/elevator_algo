def solution(A, B, M, X, Y):

    if len(A) is 0:
        return 0

    for i in range(0, len(A)):
        if A[i] > Y and B[i] > M:
            A.pop(i)
            B.pop(i)

    move_count = 0
    move_weight = 0
    move_dic = {}
    move_dic[move_count] = []

    for i in range(0, len(A)):

        if len(move_dic[move_count]) == X or move_weight + A[i] > Y:
            move_count += 1
            move_weight = 0
            move_dic[move_count] = []

        move_dic[move_count].append(B[i])
        move_weight += A[i]

    def stop_counter(move_dic, move_count):
        stop_count = 0
        for i in range(0, move_count+1):
            stop_count += len(list(set(move_dic[i])))
        return stop_count + move_count + 1

    stop_count = stop_counter(move_dic, move_count)
    return stop_count


if __name__ == "__main__":
    A = [60, 80, 40]
    B = [2, 3, 5]
    M = 5
    X = 2
    Y = 200
    # 5
    print(solution(A, B, M, X, Y))

    A = [40, 40, 100, 80, 20]
    B = [3, 3, 2, 2, 3]
    M = 3
    X = 5
    Y = 200
    # 6
    print(solution(A, B, M, X, Y))

    A = [40, 190, 40, 40]
    B = [3, 3, 3, 4]
    M = 3
    X = 5
    Y = 200
    # 7
    print(solution(A, B, M, X, Y))
