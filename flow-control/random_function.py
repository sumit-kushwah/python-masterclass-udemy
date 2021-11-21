import random

answer = random.randint(1, 10)

for i in range(5):
  print(answer)
  random.seed(23)