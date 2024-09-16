print("Welcome to my quiz game!!!")

playing = input("Do you want to start the game? ")

if playing.lower() != "yes":
    quit()

print("Let's begin!")
score = 0

answer = input("What is the largest planet in our solar system? ")
if answer.lower() == "jupiter":
    print("You got it right!")
    score += 1
else:
    print("That's incorrect :(")

answer = input("Which country is home to the kangaroo? ")
if answer.lower() == "australia":
    print("You got it right!")
    score += 1
else:
    print("That's incorrect :(")

answer = input("What is the largest organ in the human body? ")
if answer.lower() == "skin":
    print("You got it right!")
    score += 1
else:
    print("That's incorrect :(")

answer = input("What is the hardest natural material known? ")
if answer.lower() == "diamond":
    print("You got it right!")
    score += 1
else:
    print("That's incorrect :(")

print("Now it's time to kick things up a notch with more challenging questions. ")

answer = input("What number does the prefix 'giga-' represent in computing? ")
if answer.lower() == "billion":
    print("You got it right!")
    score += 1
else:
    print("That's incorrect :(")

answer = input("Who is credited with inventing the World Wide Web? ")
if answer.lower() == "Berners-Lee":
    print("You got it right!")
    score += 1
else:
    print("That's incorrect :(")

answer = input("What is the rarest blood type in humans? ")
if answer.lower() == "AB-":
    print("You got it right!")
    score += 1
else:
    print("That's incorrect :(")

answer = input("What year did the Titanic sink? ")
if answer.lower() == "1912":
    print("You got it right!")
    score += 1
else:
    print("That's incorrect :(")
    

print("You have " + str(score) + " questions correct!")
print("You have " + str((score / 8) *100) + "%.")

