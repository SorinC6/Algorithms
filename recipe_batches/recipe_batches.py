#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    result = -1
    if len(recipe) > len(ingredients):
        return 0

    for r in recipe:
        #print(f"RECIPE: {r}")
        for i in ingredients:
            #print(f"INGREDIENTS: {i}")
            # if the ingrediants matching
            if r == i:
                # calculate how many we have
                if(recipe[r] <= ingredients[i]):
                    lot = ingredients[i] // recipe[r]
                    if lot < result or result == -1:
                        result = lot
                # if we don't have enough ingredients for the recipe
                else:
                    result = 0
                    break

    return result


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
