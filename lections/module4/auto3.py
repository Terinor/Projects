
def format_ingredients(items):
    if len(items) == 1:
        receit = items[0]
    else:
        receit = ", ".join(items[ :-1]) + " and " + items[-1]
    print (receit)
    return receit

items = ['2 eggs', '1 liter sugar', '1 tsp salt', 'vinegar']
format_ingredients(items)

items = [ '1 tsp salt', 'vinegar']
format_ingredients(items)

items = ['vinegar']
format_ingredients(items)

