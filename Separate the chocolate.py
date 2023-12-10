M, N, K = map(int, input().split())

sa = []
D = []
T = []
max_d = -1
max_t = -1

for i in range(M):
    sa.append(input())

if N > M:
    sa = list(map(''.join, zip(*sa)))
    N, M = M, N

if N == 1:
    sa = list(map(''.join, zip(*sa)))
    N, M = M, N

for i in range(M):
    s = sa[i][:N]
    sd = s
    st = s
    sd = sd.replace("U", "0")
    sd = sd.replace("D", "1")
    sd = sd.replace("T", "0")
    if int(sd, 2) != 0:
        max_d = i
    D.append(int(sd, 2))
    st = st.replace("U", "0")
    st = st.replace("D", "0")
    st = st.replace("T", "1")
    if int(sd, 2) != 0:
        max_t = i
    T.append(int(st, 2))

if (N % 2 == 0) and (M % 2 == 0):
    max_K = (N + M - 1)
else:
    max_K = (N + M + 1)
max_K = max(max_K, 4)
do_K = (K < max_K)


def transfer(prev_comb, comb_compact):
    temp_comb_compact = comb_compact
    comb = []
    for _ in range(N):
        comb.append(2 * (temp_comb_compact % 2) - 1)
        temp_comb_compact //= 2

    if prev_comb:
        label0_prev = -min(min(prev_comb), 0)
        label1_prev = max(max(prev_comb), 0)
    else:
        prev_comb = [0] * N
        label0_prev = 0
        label1_prev = 0

    N_full = N + label0_prev + label1_prev + 1
    N_half = N + label0_prev
    label = [0] * N_full
    adj = [[] for _ in range(N_full)]

    for i in range(N - 1):
        if comb[i] * comb[i + 1] > 0:
            adj[i].append(i + 1)
            adj[i + 1].append(i)
            if (prev_comb[i] * prev_comb[i + 1] > 0) and (comb[i] * prev_comb[i] > 0):
                return []

    for i in range(N):
        prev_level = prev_comb[i]
        if comb[i] * prev_level > 0:
            adj[i].append(N_half + prev_level)
            adj[N_half + prev_level].append(i)

    plus_label = 0
    minus_label = 0

    for i in range(N):
        if not label[i] and (comb[i] != 0):
            if comb[i] > 0:
                plus_label += 1
                current_label = plus_label
            elif comb[i] < 0:
                minus_label -= 1
                current_label = minus_label
            label[i] = current_label
            q = []
            q.append(i)
            while q:
                node = q.pop()
                for node_neighbour in adj[node]:
                    if not label[node_neighbour]:
                        label[node_neighbour] = current_label
                        q.append(node_neighbour)

    if (label0_prev > 0) and (max(label[N:N_half]) == 0) and (
            (label0_prev > 1) or ((label0_prev == 1) and (minus_label != 0))):
        return []
    if (label1_prev > 0) and (min(label[N_half + 1:N_full]) == 0) and (
            (label1_prev > 1) or ((label1_prev == 1) and (plus_label != 0))):
        return []

    return tuple(label[:N])


transfer_matrix = []
transfer_matrix_end = []
label_to_index = {}
number_of_comb = []
end_labels = []


def build_transfer_matrix():
    N_labels = 0
    pow2N = pow(2, N)
    queue_to_process = []

    for comb in range(pow2N):
        labeled_comb = transfer([], comb)
        if labeled_comb:
            label_to_index[labeled_comb] = N_labels
            if (max(labeled_comb) <= 1) and (min(labeled_comb) >= -1):
                end_labels.append(N_labels)
            queue_to_process.append([labeled_comb, N_labels])
            N_labels += 1
            transfer_matrix.append([])
            transfer_matrix_end.append([])
            if (comb & T[0] != 0) or (~comb & D[0] != 0):
                number_of_comb.append(0)
            else:
                number_of_comb.append(1)

    while queue_to_process:
        prev = queue_to_process.pop()
        prev_label = prev[0]
        prev_index = prev[1]

        for comb in range(pow2N):
            labeled_comb = transfer(prev_label, comb)
            if labeled_comb:
                if labeled_comb not in label_to_index:
                    label_to_index[labeled_comb] = N_labels
                    if (max(labeled_comb) <= 1) and (min(labeled_comb) >= -1):
                        end_labels.append(N_labels)
                    queue_to_process.append([labeled_comb, N_labels])
                    next_index = N_labels
                    N_labels += 1
                    transfer_matrix.append([])
                    transfer_matrix_end.append([])
                    number_of_comb.append(0)
                else:
                    next_index = label_to_index[labeled_comb]
                if (comb == 0) or (comb == pow2N - 1):
                    transfer_matrix_end[prev_index].append([next_index, comb])
                else:
                    transfer_matrix[prev_index].append([next_index, comb])


build_transfer_matrix()

if do_K:
    K_lt = [2 * bin(i).count("1") - N for i in range(pow(2, N))]
    prev_number_of_comb = number_of_comb
    number_of_comb = [[0] * (2 * max_K + 1) for _ in range(len(number_of_comb))]

    for comb in range(pow(2, N)):
        number_of_comb[comb][K_lt[comb] + max_K] = prev_number_of_comb[comb]

    for row in range(1, M):
        prev_number_of_comb = number_of_comb
        number_of_comb = [[0] * (2 * max_K + 1) for _ in range(len(number_of_comb))]
        for prev_id in range(len(transfer_matrix)):
            for K_id in range(2 * max_K + 1):
                if prev_number_of_comb[prev_id][K_id]:
                    for next_id, next_comb in transfer_matrix[prev_id]:
                        if (next_comb & T[row] == 0) and (~next_comb & D[row] == 0) and (
                                abs(K_id - max_K + K_lt[next_comb]) <= max_K):
                            number_of_comb[next_id][K_id + K_lt[next_comb]] += prev_number_of_comb[prev_id][K_id]

        if row == M - 1:
            for prev_id in range(len(transfer_matrix_end)):
                for K_id in range(2 * max_K + 1):
                    if transfer_matrix_end[prev_id]:
                        for next_id, next_comb in transfer_matrix_end[prev_id]:
                            if (next_comb & T[M - 1] == 0) and (~next_comb & D[M - 1] == 0) and (
                                    abs(K_id - max_K + K_lt[next_comb]) <= max_K):
                                number_of_comb[next_id][K_id + K_lt[next_comb]] += prev_number_of_comb[prev_id][K_id]

    final_sum = 0
    for end_id in end_labels:
        for K_id in range(2 * max_K + 1):
            if abs(K_id - max_K) <= K:
                final_sum += number_of_comb[end_id][K_id]
    print(final_sum)

else:
    for row in range(1, M):
        prev_number_of_comb = number_of_comb
        number_of_comb = [0] * len(number_of_comb)
        for prev_id in range(len(transfer_matrix)):
            if prev_number_of_comb[prev_id]:
                for next_id, next_comb in transfer_matrix[prev_id]:
                    if (next_comb & T[row] == 0) and (~next_comb & D[row] == 0):
                        number_of_comb[next_id] += prev_number_of_comb[prev_id]

        if row == M - 1:
            for prev_id in range(len(transfer_matrix_end)):
                if transfer_matrix_end[prev_id]:
                    for next_id, next_comb in transfer_matrix_end[prev_id]:
                        if (next_comb & T[M - 1] == 0) and (~next_comb & D[M - 1] == 0):
                            number_of_comb[next_id] += prev_number_of_comb[prev_id]

    final_sum = 0
    for end_id in end_labels:
        final_sum += number_of_comb[end_id]
    print(final_sum)
