from random import randint

print("Welcome to Python Casino")
pc_choice = randint(1, 50)

playing = True

while playing:
  user_choice = int(input("Choose number:"))
  if user_choice == pc_choice:
    print("You won!")
    playing = False
  elif user_choice > pc_choice:
    print("Lower!")
  elif user_choice < pc_choice:
    print("Higher!")

# 멈춤을 주지 않으면 무한 반복
# dictance 가 20보다 작으면 True로 반복.
# 임포트는 파이썬의 공구주머니에서 공구를 가지고 와서 사용하는 것.