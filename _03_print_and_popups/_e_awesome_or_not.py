from tkinter import messagebox, simpledialog, Tk
import random

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Make a variable equal to a positive number less than 4 using random.randInt(0, 3)
    cat = random.randint(0, 3)
    # 2. Print your variable to the console
    print (cat)
    # 3. Get the user to enter something that they think is awesome
    what_is_awesome = simpledialog.askstring(title = "awesome", prompt = "what is something you think is awesome?")
    # 4. If your variable is  0
        # -- tell the user whatever they entered is awesome!
    if cat == 0:
        messagebox.showinfo(title = "awesome", message="that's awesome")
    # 5. If your variable is  1
        # -- tell the user whatever they entered is ok.
        if cat == 1:
            messagebox.showinfo(title = "awesome", message="that's ok")
    # 6. If your variable is  2
        # -- tell the user whatever they entered is boring.
        if cat == 2:
            messagebox.showinfo(title = "awesome", message="that's boring")
    # 7. If your variable is  3
        # -- invent your own message to give to the user (be nice).
        if cat == 3:
            messagebox.showinfo(title = "awesome", message="mega cat super hero kitties are so much better that that")
    # Run the window's .mainloop() method
    window.mainloop()
