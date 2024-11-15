#Braden Leach
#Nov 15 2024
#Python Quiz Game


#Function to ask a single question
def ask_question(question,answer):
    user_answer = input(question + "  ")
    if user_answer.lower() == answer.lower():
        return True 
    else:
        return False 
    
#Function to run the quiz 
def run_quiz():
    questions = [
        ('What is the fastest land animal?','cheetah')
        ('Where is the Pyramid of Giza?','egypt')
        ('What fish is used to make calamari?','squid')
        ('How many Great Lakes are there?',5)

    ]
