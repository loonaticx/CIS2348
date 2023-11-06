"""
Erica Miller
2031854
"""


class Team:
    def __init__(self):
        self.name = 'none'
        self.wins = 0
        self.losses = 0

    def print_standing(self):
        if round(self.get_win_percentage()):
            print(f"Congratulations, Team {self.name} has a winning average!")
        else:
            print(f"Team {self.name} has a losing average.")

    def get_win_percentage(self):
        return self.wins / (self.wins + self.losses)


if __name__ == "__main__":
    team = Team()

    user_name = input()
    user_wins = int(input())
    user_losses = int(input())

    team.name = user_name
    team.wins = user_wins
    team.losses = user_losses

    team.print_standing()
