import random
number = random.randint(1,50)
i=0
hearts = 5
for i in range(5):
  i = i + 1
  
  guess =  int(input("Enter a number between 1 to 50: "))
  
  
  if guess > 50 or guess < 0:
     print("No cheating! That's -1 attempt. Attempts left:",5-i)
  
  elif guess == number:
     print("Hooray!, you guessed right!")
     break
  elif guess > number :
     print("Guess is too high! Attempts left:",5-i)
  elif guess < number:
     print("Guess is too low! Attempts left:",5-i)
  
if i == 5:
    print("No more hearts! The random number guessed was",number)

   

    
