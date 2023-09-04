age = int(input("How old are you?"))

if age < 18:
  print("You can't drink.")
elif age >= 18 and age <= 35:  # and는 앞의 조건이 True면 반드시 뒤에 조건도 같아야 함, False 면 뒤에 조건도 같아야함
  print("You dirnk beer!")
elif age == 60 or age == 70:  # or 는 둘 중에 하나만 True 여도 됨
  print("Birthday party!")
else:
  print("Go ahead!")

True and True == True
False and True == False
True and False == False
False and False == False

True or True == True
True or False == True
False or True == True
False or False == False
