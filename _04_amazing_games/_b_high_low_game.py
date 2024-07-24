from tkinter import messagebox, simpledialog, Tk
import sys
import random

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # 1. Change this line to give you a random number between 1 - 100.
    number = random.randint(1, 100)
    count = 1

    # 2. Print out the random variable that you made in step #1
    #print('Random number:', number)

    # 3. Code a for loop to run steps 4-10, 10 times
    for _ in range(10):
        # 4. Ask the user for a guess using a pop-up window, and save their response
        guess = simpledialog.askinteger(title='Guess the number', prompt='Enter a number between 1-100:')
        count+=1

        # Ensure the user input is within the valid range
        if guess is None:
            sys.exit(0)  # Exit if user cancels

        # 5. If the guess is correct
        if guess == number:
            # 6. Win. Use 'sys.exit(0)' to end the program
            messagebox.showinfo('Correct!', f'Congratulations! You guessed the number {number}!')
            sys.exit(0)

        # 7. if the guess is high
        elif guess > number:
            # 8. Tell them it's too high
            messagebox.showinfo(title="too high", message='Your guess is too high. Try again. You have ' +str(count)+ ' guesses left')
            count+=1

        # 9. Else if the guess is low
        else:
            # 10. Tell them it's too low
            messagebox.showinfo(title='Too Low', message='Your guess is too low. Try again. You have ' +str(count)+ ' guesses left')
            count+=1

    # 11. Outside of the loop, tell the user they lost
    messagebox.showinfo('Game Over', f'Sorry, you ran out of guesses. The number was {number}.')

    window.mainloop()
