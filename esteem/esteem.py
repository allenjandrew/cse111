print()

def main():
    input("This is the Rosenberg self-esteem scale.\nPlease rate your answers from 0 to 3 based on how well you agree with the statement.\nType '0' for 'Strongly Disagree', '1' for 'Disagree', '2' for 'Agree', or '3' for 'Strongly Agree'.\nPress ENTER or RETURN to begin.")
    print()

    questions = [
        (1, 'I feel that I am a person of worth, at least on an equal plane with others.'),
        (2, 'I feel that I have a number of good qualities.'),
        (3, 'All in all, I am inclined to feel that I am a failure.'),
        (4, 'I am able to do things as well as most other people.'),
        (5, 'I feel I do not have much to be proud of.'),
        (6, 'I take a positive attitude toward myself.'),
        (7, 'On the whole, I am satisfied with myself.'),
        (8, 'I wish I could have more respect for myself.'),
        (9, 'I certainly feel useless at times.'),
        (10, 'At times I think I am no good at all.')
        ]
    
    points = 0
    for question in questions:
        if question_is_positive(question[0]):
            rating = ask(question[1] + ' ')
        else:
            rating = 3 - ask(question[1] + ' ')
        points += rating
    print()
    print(f'Your score: {points} out of 30 points')
    print(what_result(points))

def ask(question):
    return int(input(question))

def question_is_positive(number):
    if number in (1,2,4,6,7):
        return True
    else:
        return False

def what_result(score):
    if score >= 25:
        return 'Looks good! You have very high self-esteem.'
    if score >= 20:
        return 'You got this! Keep working on yourself. I believe in you!'
    if score >= 15:
        return 'You could use some improvement in this area. No worries! Start small - you can do it!'
    if score >= 10:
        return 'You really are just a cotton-headed ninnymuggins.'
    return 'Looks like you have low self-esteem. Remember that God loves you no matter what! He will help you succeed!'

if __name__ == '__main__':
    main()

print()