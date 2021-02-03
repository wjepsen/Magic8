import random
name = input("What is your name?\n")
question = input("Ask a yes or no question \n")
#question = "do I like peanuts?"
answer = "" 
random_number = random.randint(1,9)
if question == "":
    question = input("Ask a yes or no question \n")
print("Magic 8's Answer:")
if name == "":
# print(random_number)
  if random_number == 1:
    print("yes - definitely.")
  elif random_number == 2:
    print("It is decidedly so.")
  elif random_number == 3:
    print("Without a doubt.")
  elif random_number == 4:
    print("Reply hazy, try again.")
  elif random_number == 5:
    print("Ask again later.")
  elif random_number == 6:
    print("Better not tell you now.")
  elif random_number == 7:
    print("My sources say no.")
  elif random_number == 8:
    print("Outlook not so good.")
  elif random_number == 9:
    print("Very doubtful.")
else:
  print(name + ",")
  if random_number == 1:
    print("yes - definitely.")
  elif random_number == 2:
    print("It is decidedly so.")
  elif random_number == 3:
    print("Without a doubt.")
  elif random_number == 4:
    print("Reply hazy, try again.")
  elif random_number == 5:
    print("Ask again later.")
  elif random_number == 6:
    print("Better not tell you now.")
  elif random_number == 7:
    print("My sources say no.")
  elif random_number == 8:
    print("Outlook not so good.")
  elif random_number == 9:
    print("Very doubtful.")
