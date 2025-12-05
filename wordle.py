from pathlib import Path
import random

directory = Path("/Users/leonm/Downloads/5-Letter-words-main")
filepath = directory / "words.txt"

with open(filepath, 'r') as file:
    word = [line for line in file]
    
GREEN = "\033[42m"    
YELLOW = "\033[43m"   
RESET = "\033[0m"
def choosing_word():
    while True:
        chosen = random.choice(word)
        chosen = [i for i in chosen]
        del chosen[-1]
        if len(set(chosen)) == len(chosen): # SETS HAVE UNIQUE STRINGS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            print(chosen)
            return chosen
        else:
            continue
        
def print_grid(grid):
    for row in grid:
        print(",".join(row))
        
def ask_4_word():
    current_word = input("Enter your word: ")
    current_word = [i for i in current_word]
    return current_word
    
def check_for_word(word, chosen):
    indicator = []
    for index, letter in enumerate(word):
        if (letter == chosen[index]) and (word.index(letter) == chosen.index(letter)): 
            indicator.append(1)
        elif letter in chosen:
            indicator.append(2)
        else:
            indicator.append(3)
    return indicator

def iteration(indicator, turn, grid, word):           
    for index,value in enumerate(indicator):
        x = index
        if value == 1: # GREEN
            grid[turn][x] = f"{GREEN}{word[x]}{RESET}"
        elif value == 2: # YELLOW
            grid[turn][x] = f"{YELLOW}{word[x]}{RESET}"
        else:
            grid[turn][x] = word[x] # NONE
            
def check_grid(turn, chosen, grid, word):
    if turn == 4:
        print(f"You lost! The chosen word was {"".join(chosen)}")
        return True
    elif "".join(word) == "".join(chosen):
        print(f"You won! The word was {chosen}")
        return True
    else:
        return False         
def main():
    turn = 0
    grid = [
        ["▢", "▢", "▢", "▢", "▢"],
        ["▢", "▢", "▢", "▢", "▢"],
        ["▢", "▢", "▢", "▢", "▢"],
        ["▢", "▢", "▢", "▢", "▢"],
        ["▢", "▢", "▢", "▢", "▢"],
    ]

    while True:
        if turn == 0:
            chosen = choosing_word()
        else:
            pass
        print_grid(grid=grid)
        word = ask_4_word()
        indicator = check_for_word(word=word, chosen=chosen)
        iteration(indicator=indicator, turn=turn, grid=grid, word=word)
        if check_grid(turn=turn,word=word, grid=grid, chosen=chosen):
            return False
        turn += 1
              
main()
    
    

        