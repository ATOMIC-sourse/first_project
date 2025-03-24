from django.template.context_processors import request

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'bread': {
        'мука, г': 500,
        'соль, щепоть': 1,
        'вода, л': 0.2,
        'масло, г': 30,
    },
    'cereal': {
        'кукурузные хлопья, г': 100,
        'молоко, л': 0.3,
    }
}

# recipe = 'omlet'
# value = DATA.values()
# for dish in DATA.keys():
#     if recipe == dish:
#         print(DATA.values())
servings = input()
recipe = DATA.get('bread')
# scaled_recipe = {ingredient: amount * servings for ingredient, amount in recipe.items()}
print(recipe)
