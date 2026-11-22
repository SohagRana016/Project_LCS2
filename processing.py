
def get_clean_words(paragraph):
    clean_text = paragraph.lower().strip()
    words = clean_text.split()
    return words


def calculate_similarity(words1, words2, table):
    lcs_length = table[len(words1)][len(words2)]

    max_words = max(len(words1), len(words2))
    percentage = (lcs_length / max_words) * 100

    return lcs_length, percentage
