def make_juice(fruit):
  return f"{fruit}+🥤"


def add_ice(juice):
  return f"{juice}+🧊"


def add_sugar(ice_juice):
  return f"{ice_juice}+🧂"


my_juice = make_juice("🍉")
cold_juice = add_ice(my_juice)
magic_juice = add_sugar(cold_juice)

print(magic_juice)
