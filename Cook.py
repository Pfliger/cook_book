from pprint import pprint


with open('recipes.txt', encoding='utf-8') as f:
    recipes = f.read()
    recipes = recipes.split('\n\n')

def cook_book (recipes):
  Cook_Book = {}
  for dish in recipes:
    dish = dish.split('\n')
    name = dish[0]
    components = []
    for a in dish[2:]:
      ingredient = a.split('|')
      ing_list = {'ingredient_name': ingredient[0], 'quantity': ingredient[1], 'measure': ingredient[2]}
      components.append(ing_list)
    Cook_Book[name] = components
  return Cook_Book

pprint(cook_book(recipes))


def get_shop_list_by_dishes(dishes, number_of_people):
  result = {}
  ing_list = []
  for dish in dishes:
    ing_list += (cook_book(recipes).get(dish))
  for dish in ing_list:
    name = dish['ingredient_name']
    ingredients = result.setdefault(name,{'measure': dish['measure'], 'quantity': 0})
    ingredients['quantity'] = int(ingredients['quantity']) + int(dish['quantity']) * number_of_people
    result[name] = ingredients
  return result

pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))
