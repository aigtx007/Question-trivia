from Question import Question
questionnaire = [
"What is the most tallest mountain on Earth?\na. Lhotse\nb. Kangchenjunga\nc. Mt. Everest\nd. K2\n",

"What is the most venomous animal on Earth?\na. Snake \nb. Frog \nc. Scorpion \nd. Snail \n",

"Who is the tallest person in the world right now?\na. Shaquil O'Neal \nb. Yao Ming "
"\nc. Sultan Kosen \nSd. ultan Mobdal \n",

"Who is the No 1 intelligent person in the world? \na. Albert Einstein \nb. Thomas Edison \n Marie Curie\nd. Isaac Newton \n",

"Who is the richest person in the world? \na. Jac Ma \nb. Sergey Brin \nc. Jeff Bezos \nd. Elon Musk \n",

"How long is an Olympic swimming pool (in meters)? \na. 70 meters \nb. 60 meters \nc. 80 meters \nd. 50 meters \n",
]

questions = [
    Question(questionnaire[0],'c'),
    Question(questionnaire[1],'d'),
    Question(questionnaire[2],'c'),
    Question(questionnaire[3],'c'),
    Question(questionnaire[4],'c'),
    Question(questionnaire[5],'c'),
    ]
def run_test(questions):
    score = 0
    attempts = 3
    count = 0
    while attempts > 0:

        for question in questions:
            answer = input(question.prompt)
            count +=1
            if answer == question.answer:
                score +=1
                print(f'You got a correct answer')
                print(f'You got {score} out of {count} You have {attempts} left.')
            else:
                attempts -= 1
                print(f'You got a wrong answer')

                print(f'You got {score} out of {count} You have {attempts} left.')
            break
        print(f'You got {score} out of {count} You have {attempts} left.')






run_test(questions)
