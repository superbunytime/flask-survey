class Question:
    """Question on a questionnaire."""

    def __init__(self, question, choices=None, allow_text=False):
        """Create question (assume Yes/No for choices."""

        if not choices:
            choices = ["Yes", "No"]

        self.question = question
        self.choices = choices
        self.allow_text = allow_text


class Survey:
    """Questionnaire."""

    def __init__(self, title, instructions, questions):
        """Create questionnaire."""

        self.title = title
        self.instructions = instructions
        self.questions = questions


satisfaction_survey = Survey(
    "Customer Satisfaction Survey",
    "Please fill out a survey about your experience with us.",
    [
        Question("Have you shopped here before?"),
        Question("Did someone else shop with you today?"),
        Question("On average, how much do you spend a month on frisbees?",
                 ["Less than $10,000", "$10,000 or more"]),
        Question("Are you likely to shop here again?"),
    ])

personality_quiz = Survey(
    "Rithm Personality Test",
    "Learn more about yourself with our personality quiz!",
    [
        Question("Do you ever dream about code?"),
        Question("Do you ever have nightmares about code?"),
        Question("Do you prefer porcupines or hedgehogs?",
                 ["Porcupines", "Hedgehogs"]),
        Question("Which is the worst function name, and why?",
                 ["do_stuff()", "run_me()", "wtf()"],
                 allow_text=True),
    ]
)

surveys = {
    "satisfaction": satisfaction_survey,
    "personality": personality_quiz,
}

#these are a bunch of (now functional) loops for iterating over the questions class object
#very cool, thank you Victor for helping me understand it better.

# accessing the first question inside of the satisfaction survey

# print(satisfaction_survey.questions[0].question)

# accessing all questions inside of the satisfaction survey
# not dynamic

# for x in range (len(satisfaction_survey.questions)):
#   print(satisfaction_survey.questions[x].question)

# not sure why this line doesn't work

# for index, x in enumerate(satisfaction_survey.questions):
#     print(index + 1, x.question, x.choices, x.allow_text)
    # print(x)

# questions = [{"title": "have you shopped here before", "number": 0}, {"title":"Did someone else shop with you today?", "number": 1}]

# for val in questions:
#     print(val["title"])

# l1 = ["a", "b", "c"]

# for ltr in l1:
#     print(ltr)
