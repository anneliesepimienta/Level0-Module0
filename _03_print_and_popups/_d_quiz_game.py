from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    score = 0
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
    question_1 = simpledialog.askstring(title = "#1", prompt = "who is the traitor in hawkwing's journey warriors book?")
    #      // 3.  Use an if statement to check if their answer is correct
    if question_1 == "darktail":
        messagebox.showinfo(message="your answer was correct.")
        score = score + 1
    #      // 4.  if the user's answer was correct, add one to their score 
    else:
        messagebox.showinfo(message="Your answer was incorrect. Correct answer: Darktail")
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
    question_2 = simpledialog.askstring(title = "#2", prompt = "Who never came back to the clan after the rogoue battle in the gorge in hawkwing's journey warriors book?")
    #make the if statement.
    if question_2 == "frecklewish and sandynose":
        messagebox.showinfo(message="Your answer was correct.")
        score = score + 1
    # make the else statement.
    else:
        messagebox.showinfo(message="Your answer was incorrect. Correct answer: frecklewish and sandynose.")
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    messagebox.showinfo(message="your total score is " + str(score))
    # Run the window's .mainloop() method
    window.mainloop()
