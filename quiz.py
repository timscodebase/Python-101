from Question import Question
from chalky import sty, fg

red = sty.bold & fg.red
green = sty.bold & fg.green

questions_prompt = [
  "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
  "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
  "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

question = [
  Question(questions_prompt[0], "a"),
  Question(questions_prompt[1], "c"),
  Question(questions_prompt[2], "b"),
]

def run_test(questions):
  score = 0
  for question in questions:
    answer = input(question.prompt)
    if answer == question.answer:
      score += 1
  print("You got ")
  print(red | str(score))
  print("/")
  print(green |str(len(questions)))
  print(" correct")

run_test(question)