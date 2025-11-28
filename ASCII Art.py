import sys
import math


allChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ?" # a string of all the accepted characters

l = int(input())    # GAMEINPUT
h = int(input())    # GAMEINPUT
t = input()         # GAMEINPUT > text to transform
print("Debug messages...    l,h,t",l,", ",h,", ",t, file=sys.stderr, flush=True)

full_input = [] #to store the entire input to reach from

for i in range(h):  # GAMEINPUT
    row = input()
    # print("Debug messages...    rowInput:: ", row, file=sys.stderr, flush=True)
    full_input.append(row)

# for i in range(len(full_input)): # To Visually Check the input
#     print("Debug messages... (full_input[i]): ", (full_input[i]), file=sys.stderr, flush=True)

def extractLetter(letter: str) -> list[list[str]]: # for creating the ASCII version for each letter
    """takes a string and extracts the given CHAR if it exists on the input to a 2-d matrix"""
    if (letter.upper() in allChars): # if written lowercase
        letter = letter.upper()
    elif letter not in allChars:     # if not an accepted letter
        letter = "?"
    letterIndex = allChars.index(letter)
    letterStart = (letterIndex * l) # where the character starts in all length
    letterEnds  = (letterStart + l) # where the character ends
    extracted_char = []
    for h in range(len(full_input)):
        new_row = (full_input[h][letterStart : letterEnds])
        extracted_char.append(new_row)

    return extracted_char

def showResults(inputWord: str) -> None: # for printing the results
    matrices = [extractLetter(ch) for ch in inputWord]

    # for each row of the final output, concatenate the corresponding row
    # from every character's matrix and print it
    for row_idx in range(h):
        out_line = ''.join(matrix[row_idx] for matrix in matrices)
        print(out_line)

showResults(t)


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
# print("answer")