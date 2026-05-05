from tkinter import *

# Flashcards (Question, Answer)
flashcards = [
    ("Capital of India?", "New Delhi"),
    ("2 + 2 = ?", "4"),
    ("Largest planet?", "Jupiter"),
    ("Python is?", "Programming Language"),
    ("Color of sky?", "Blue")
]

index = 0
showing_answer = False
score = 0

def update_card():
    global showing_answer
    showing_answer = False
    label.config(text=flashcards[index][0])
    score_label.config(text=f"Score: {score}")

def show_answer():
    global showing_answer, score
    if not showing_answer:
        label.config(text=flashcards[index][1])
        showing_answer = True
        score += 1
        score_label.config(text=f"Score: {score}")

def next_card():
    global index
    index = (index + 1) % len(flashcards)
    update_card()

def prev_card():
    global index
    index = (index - 1) % len(flashcards)
    update_card()

# GUI
root = Tk()
root.title("Flashcard Quiz App")
root.geometry("450x350")

label = Label(root, text="", font=("Arial", 18), wraplength=350)
label.pack(pady=40)

score_label = Label(root, text="Score: 0", font=("Arial", 12))
score_label.pack()

Button(root, text="Show Answer", command=show_answer).pack(pady=5)
Button(root, text="Next", command=next_card).pack(pady=5)
Button(root, text="Previous", command=prev_card).pack(pady=5)

update_card()
root.mainloop()