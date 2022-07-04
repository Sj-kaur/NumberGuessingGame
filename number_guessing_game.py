target = int(input("Enter any number: "))
guess = 1
print("Total number of guesses will be only 9 times: ")
count = 0
while guess <= 9:
    n = int(input("Guess the number : "))
    count = count + 1
    if target < n :
        print("The number is greater than the required number")
    elif target > n:
        print("The number is less than the required number")
    else:
        print("YOU WON , The correct number is :", target)
        print("Number of guesses you took to guess :",count)
        break
    print("Number of guesses left : ", 9 - guess)
    guess = guess + 1
else:
    print("You Lose , The game is over")