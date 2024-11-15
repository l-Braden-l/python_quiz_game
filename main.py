#Braden Leach
#Nov 15 2024
#Python Quiz Game


# Function to ask a single question
def ask_question(question,answer):
    user_answer = input(question + "  ")
    if user_answer.lower() == answer.lower():
        return True 
    else:
        return False 
    
# Function to run the quiz 
def run_quiz():
    questions = [
        ('What is the fastest land animal?','cheetah'),
        ('Where is the Pyramid of Giza?','egypt'),
        ('What fish is used to make calamari?','squid'),
        ('How many Great Lakes are there?','5')
    ]

    # loop through the questions and ask each one 

    score = 0 
    for q in questions: 
        if ask_question(q[0],q[1]):
            print("Correct!")
            score += 1 
        else: 
            print('Incorrect answer! sorry!')

# calculate the score percentage 
    print(f'\nYour final score is; {score}/{len(questions)}')
    percentage = (score / len(questions)) * 100
    print(f'You Scored: {percentage:.1f}%')
    print('Goodbye!')

# main function to start the game 
def main():
    print('Welcome to my Python Quiz Game!')
    run_quiz()

# start the game 
if __name__ == "__main__":
    main()
