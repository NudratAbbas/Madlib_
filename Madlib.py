# Mad Libs Game in Python
# This game asks the user for input and inserts it into a story template

def madlib():
    print("Welcome to the Mad Libs game!")
    print("Please provide the following words:\n")

    # Taking user input
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb (past tense): ")
    adverb = input("Enter an adverb: ")
    place = input("Enter a place: ")
    emotion = input("Enter an emotion: ")

    # Creating the story using f-strings
    story = f"""
    One day, a {adjective} {noun} was walking through {place}.
    Suddenly, it {verb} {adverb}, making everyone around feel {emotion}.
    It was a moment no one would ever forget!
    """

    # Printing the final madlib story
    print("\nHere is your Mad Libs story:")
    print(story)

# Run the function
if __name__ == "__main__":
    madlib()
