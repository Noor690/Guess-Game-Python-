secret_word = "Lion"
guess = ""
guess_count = 0
guess_limit = 5
out_of_guesses = False

while guess != secret_word:
    if guess_count < guess_limit:
        guess = input("Enter a guess:")
        guess_count += 1
    else:
        out_of_guesses = True
        print("You lost!")
        break

if guess == secret_word:
    print("You won")
