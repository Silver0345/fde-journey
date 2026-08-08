import random

def main():
    '''
    Repeatedly ask the user whether to play a round of the guessing game.
    Tracks how many rounds were played and reports that total when the
    user answers "no". Delegates difficulty selection to choose_difficulty()
    and the actual round to guess_number().
    '''
    game = 0
    while True:
        
        play_game = input("Do you want to play the guessing game? (yes/no): ").strip()
        if play_game.lower() == "yes":
            game +=1
            l_range, r_range = choose_difficulty()
            guess_number(l_range, r_range)
        elif play_game.lower() == "no":
            print(f"You played {game} game(s).")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            pass

def choose_difficulty():
    '''
    Prompt the user for a range formatted as "low-high" (e.g. "1-50").
    Reprompts on any input that can't be split and parsed into two
    integers. Returns the two bounds as (l_range, r_range); does not
    itself guarantee l_range < r_range — guess_number() handles that.
    '''
    while True:
        try:
            range_size = input("Choose a range size: 1-50 vs 1-200: ")
            difficulty = range_size.split("-")
            r_range = int(difficulty[-1])
            l_range = int(difficulty[0])
           
            return l_range, r_range
        
        except ValueError:
            print("Invalid input. Please enter a valid integer range.")
            pass
        
def guess_number(l_numb, r_numb):
    '''
    Pick a random target between l_numb and r_numb (bounds may be given
    in either order; a reversed range is corrected automatically, an
    equal range is rejected). Give the player up to 7 attempts to guess
    the target, printing "too high"/"too low" feedback on each miss,
    and report the attempt count on a win or a loss.
    '''
    guess_numb = 1  # Initialize the number of attempts
    if l_numb > r_numb:
        number = random.randint(r_numb,l_numb)  # The number to guess
    elif l_numb < r_numb:
        number = random.randint(l_numb, r_numb)  # The number to guess
    else:
        print("Invalid range. Please choose a valid range.")
        return

    while True:
        if guess_numb > 7:
            print(f"You lost, that was attempt number {guess_numb - 1}.")
            break
        try:
            guess = input(f"Guess a number between {l_numb} and {r_numb}: ") 
            guess = int(guess)
            
            if guess > number:
                print("Too high! Try again.")
                guess_numb += 1
            elif guess < number:
                print("Too low! Try again.")
                guess_numb += 1
            else:
                print(f"Congratulations! You guessed the number {guess} in {guess_numb} attempts.")
                guess_numb += 1
                break
        except ValueError:
            print("Please enter a valid integer.")
            continue
            
    
main()