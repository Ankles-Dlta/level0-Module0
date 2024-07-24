from tkinter import messagebox, simpledialog, Tk
import random

# Create an if-main code block
if __name__ == '__main__':
    # Make a new window variable
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()

    # 1. Make a variable equal to a positive number less than 4 using random.randint(0, 3)
    random_number = random.randint(0, 4)

    # 2. Print your variable to the console
    print('Random number:', random_number)

    # 3. Get the user to enter something that they think is awesome
    user_input = simpledialog.askstring(title='Input', prompt='Enter something you think is awesome:')

    # 4. If your variable is 0
    if random_number == 0:
        # -- tell the user whatever they entered is awesome!
        messagebox.showinfo('Feedback', f'{user_input} is not awesome and he is bad at everything he does except glaze people!')

    # 5. If your variable is 1
    elif random_number == 1:
        # -- tell the user whatever they entered is ok.
        messagebox.showinfo('Feedback', f'{user_input} is a hater.')

    # 6. If your variable is 2
    elif random_number == 2:
        # -- tell the user whatever they entered is boring.
        messagebox.showinfo('Feedback', f'{user_input} is boring and anoying.')

    # 7. If your variable is 3
    elif random_number == 3:
        # -- invent your own message to give to the user (be nice).
        messagebox.showinfo('Feedback', f'Wow, {user_input} does not sound interesting!')

    elif random_number == 4:
    # -- invent your own message to give to the user (be nice).
        messagebox.showinfo('Feedback', f'Wow, {user_input} is amazing!')

    # Run the window's .mainloop() method
    window.mainloop()
