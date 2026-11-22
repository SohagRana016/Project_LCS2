
def build_lcs_table(words1, words2):
    rows = len(words1) + 1
    cols = len(words2) + 1

    table = []
    for i in range(rows):
        table.append([0] * cols)

    for i in range(1, rows):
        for j in range(1, cols):
            if words1[i - 1] == words2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

    return table
