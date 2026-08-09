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
            l_range, r_range = get_valid_range()
            ans = guess_number(l_range, r_range)
            print(ans)
        elif play_game.lower() == "no":
            print(f"You played {game} game(s).")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            pass
        
    
    

def choose_difficulty(range_size):
    '''
    Prompt the user for a range formatted as "low-high" (e.g. "1-50").
    Reprompts on any input that can't be split and parsed into two
    integers. Returns the two bounds as (l_range, r_range); does not
    itself guarantee l_range < r_range — guess_number() handles that.
    '''   
    
    difficulty = range_size.split("-")
    r_range = int(difficulty[-1])
    l_range = int(difficulty[0])
           
    return (l_range, r_range)
        

def get_valid_range():
    
    while True:
        try:
            val = input("Enter a range e.g. 50-100, 1-200: ").strip()
            l_range, r_range = choose_difficulty(val)
            return l_range, r_range
        except ValueError:
            continue
        
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
        
        try:
            guess = input(f"Guess a number between {l_numb} and {r_numb}: ") 
            guess = int(guess)
            ans = check_guess(guess, number)
            guess_numb += 1  # Increment the number of attempts            
            
            if ans == "Correct":
                return f"{ans} that was attempt number {guess_numb -1}."
                
            elif guess_numb > 7  :
                return f"You lost, that was attempt number {guess_numb - 1}."
            else: 
                continue
        except ValueError:
            print("Please enter a valid integer.")
            continue
        
    
def check_guess(guess, number):
    '''
    Compare the player's guess to the target number and return feedback.
    Returns "too high" if the guess is greater than the target, "too low"
    if less, and "correct" if equal. This function is not strictly necessary
    but can be useful for testing or future extensions.
    '''
    if guess > number:
        return "Too High"
    elif guess < number:
        return "Too Low"
    else:
        return f"Correct"   
    
             
if "__main__" == __name__:
    main()