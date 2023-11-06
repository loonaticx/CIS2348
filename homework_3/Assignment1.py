"""
Erica Miller
2031854

Prompt:
    The given program accepts as input a food item name, fat, carbs, and protein and the number of servings.
    It creates a food item using the constructor parameters' default values and a food item using the input values.
    The program outputs the nutritional information and calories per serving for both food items.
"""


class FoodItem:
    def __init__(self, name: str = "None", fat: float = 0.0, carbs: float = 0.0, protein: float = 0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def get_calories(self, num_servings: float) -> float:
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))


if __name__ == "__main__":
    defaultItem = FoodItem()

    item_name = input()
    if item_name == 'Water' or item_name == 'water':
        food_item = FoodItem(item_name)
        num_servings = 1.0
    else:
        amount_fat = float(input())
        amount_carbs = float(input())
        amount_protein = float(input())
        num_servings = float(input())
        food_item = FoodItem(item_name, amount_fat, amount_carbs, amount_protein)

    defaultItem.print_info()
    print(f'Number of calories for {num_servings:.2f} serving(s): {defaultItem.get_calories(1.0):.2f}\n')
    food_item.print_info()
    print(f'Number of calories for {num_servings:.2f} serving(s): {food_item.get_calories(num_servings):.2f}')
