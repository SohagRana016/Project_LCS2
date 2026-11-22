import tkinter as tk
from tkinter import messagebox

from lcs import build_lcs_table
from processing import get_clean_words, calculate_similarity


def check_copy_content(box1, box2, result_label):

    para1 = box1.get("1.0", tk.END)
    para2 = box2.get("1.0", tk.END)

    words1 = get_clean_words(para1)
    words2 = get_clean_words(para2)

    if len(words1) == 0 or len(words2) == 0:
        messagebox.showwarning(
            "Empty Input",
            "Please enter text in both boxes!"
        )
        return

    dp_table = build_lcs_table(words1, words2)

    lcs_len, match_percent = calculate_similarity(
        words1, words2, dp_table
    )

    if match_percent >= 50:
        result_label.config(
            text=f"Matched Percentage: {match_percent:.2f}% | LCS Length: {lcs_len} words",
            fg="red"
        )
    else:
        result_label.config(
            text=f"Matched Percentage: {match_percent:.2f}% | LCS Length: {lcs_len} words",
            fg="green"
        )
