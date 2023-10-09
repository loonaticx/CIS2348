"""
Erica Miller
2031854
"""


def exact_change(user_total):
    user_dollars = user_total // 100
    user_total %= 100
    user_quarters = user_total // 25
    user_total %= 25
    user_dimes = user_total // 10
    user_total %= 10
    user_nickels = user_total // 5
    user_pennies = user_total % 5
    return user_dollars, user_quarters, user_dimes, user_nickels, user_pennies


if __name__ == '__main__':
    input_val = int(input())

    if input_val <= 0:
        print("no change")
    else:
        num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)

        if num_dollars > 0:
            print(f"{num_dollars} {'dollar' if num_dollars == 1 else 'dollars'}")
        if num_quarters > 0:
            print(f"{num_quarters} {'quarter' if num_quarters == 1 else 'quarters'}")
        if num_dimes > 0:
            print(f"{num_dimes} {'dime' if num_dimes == 1 else 'dimes'}")
        if num_nickels > 0:
            print(f"{num_nickels} {'nickel' if num_nickels == 1 else 'nickels'}")
        if num_pennies > 0:
            print(f"{num_pennies} {'penny' if num_pennies == 1 else 'pennies'}")
