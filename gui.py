import tkinter as tk

from result import check_copy_content


def create_gui():

    window = tk.Tk()
    window.title("Copy Content Detector (LCS Algorithm)")
    window.geometry("600x480")

    tk.Label(
        window,
        text="Copy Content Detector",
        font=("Arial", 16, "bold")
    ).pack(pady=10)

    tk.Label(
        window,
        text="Enter Original Content (Paragraph 1):",
        font=("Arial", 11)
    ).pack()

    box1 = tk.Text(window, height=6, width=65, font=("Arial", 10))
    box1.pack(pady=5)

    tk.Label(
        window,
        text="Enter Suspected Content (Paragraph 2):",
        font=("Arial", 11)
    ).pack()

    box2 = tk.Text(window, height=6, width=65, font=("Arial", 10))
    box2.pack(pady=5)

    result_label = tk.Label(
        window,
        text="Matched Percentage: 0.00% | LCS Length: 0 words",
        font=("Arial", 13, "bold"),
        fg="#137a4b"
    )
    result_label.pack(pady=10)

    match_btn = tk.Button(
        window,
        text="Match Content",
        font=("Arial", 12, "bold"),
        bg="#2b579a",
        fg="white",
        padx=15,
        pady=5,
        command=lambda: check_copy_content(box1, box2, result_label)
    )
    match_btn.pack(pady=15)

    window.mainloop()
