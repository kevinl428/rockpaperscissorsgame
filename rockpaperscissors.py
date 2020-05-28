import random
import sys

# def draw_sit():
# 	draw_response = input("It is a draw. Play again? Type Y for yes or N for no. ")
# 	draw_choice = "You chose {}".format(draw_response)
# 	if draw_response is Y:
# 		return choice
# 	else:
# 		quit()

def rockPaperScissors():
	
# Intro to rock paper scissors
	choice = int(input("Hello!. Do you choose rock, paper, or scissors? Type 1 for rock, 2 for paper, or 3 for scissors. "))

	if choice is 1:
		print("You chose rock.")
	elif choice is 2:
		print("You chose paper.")
	else:
		print("You chose scissors.")


	# response = "You chose {}".format(choice)
	# print(response)


	# Random choice by computer (import random)
	pc_choice = random.randint(1, 4)
	if pc_choice is 1:
		print("I chose rock.")
	elif pc_choice is 2:
		print("I chose paper.")
	else:
		print("I chose scissors.")

	# I have chosen _______ and you chose ________. j
	if choice > pc_choice:
		print("Congratulations, you win!")
	elif choice < pc_choice:
		print("Sorry, but I am the winner!")
	else:
		print("It is a tie! We both win.")

rockPaperScissors()

play_again = str(input("Would you like to play again? Enter Y for yes, or N for no. "))
if play_again == "Y":
	rockPaperScissors()
else:	
	sys.exit()

	#draw_sit()

# if choice is rock:
# 	if pc_choice is 1:
# 		draw_sit()
# 		# if draw_response = Y new game
# 		# else: quit program

# 	elif pc_choice is 2:
# 		print("Since paper beats rock, I win!")

# 	else:
# 		print("Since rock beats scissors, you win!")

# elif choice is paper:
# 	if pc_choice is 1:
# 		print("Since paper beats rock, you win!")
# 	elif pc_choice is 2:
# 		draw_sit()
# 	else:
# 		print("Since scissors beats paper, I win!")

# elif choice is scissors:
# 	if pc_choice is 1:
# 		print("Since rock beats scissors, I win!")
# 	elif pc_choice is 2:
# 		print("Since paper beats scissors, you win!")
# 	else:
# 		draw_sit()





# if choice is P:

# if choice is S"
# Since _______ beats _________ you/I win.

# Would you like to play again? If yes, restart. If no, quit.