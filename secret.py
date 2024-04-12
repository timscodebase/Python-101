secret = "apple"
guess = ""
guess_count = 0
guess_limit = 3

while guess != secret:
  if guess_count == guess_limit:
    print("You lose!")
    break
  guess = input("Enter your guess: ")
  guess_count += 1
  if guess == secret:
    print("You guessed it!")
  else:
    print("Wrong, try again.")