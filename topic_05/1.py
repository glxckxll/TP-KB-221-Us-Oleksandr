import random

class Game:
    def __init__(self, rounds, difficulty):
        self.rounds = rounds
        self.difficulty = difficulty

    def play(self):
        self.results = {}
        for i in range(self.rounds):
            self.player_gesture = input("Виберіть ваш жест(камінь, ножиці, папір): ")
            self.computer_gesture = self.get_computer_gesture(self.difficulty, self.player_gesture)
            self.results[i] = self.get_winner(self.player_gesture, self.computer_gesture)

        self.print_results()

    def get_computer_gesture(self, difficulty, player_gesture):
        if difficulty == "нормально":
            return random.choice(["камінь", "ножиці", "папір"])
        elif difficulty == "складно":
            if player_gesture == "камінь":
                return "папір"
            elif player_gesture == "ножиці":
                return "камінь"
            else:
                return "ножиці"

    def get_winner(self, player_gesture, computer_gesture):
        if player_gesture == computer_gesture:
            return "Нічия"
        elif (player_gesture, computer_gesture) in {("камінь", "ножиці"), ("ножиці", "папір"), ("папір", "камінь")}:
            return "Перемога гравця"
        else:
            return "Перемога комп'ютера"

    def print_results(self):
        for i, result in enumerate(self.results.values()):
            print(f"Раунд {i + 1}: {result}")
        if self.get_winner(self.player_gesture, self.computer_gesture) == "Перемога гравця":
            print("Ви перемогли!")
        elif self.get_winner(self.player_gesture, self.computer_gesture) == "Перемога комп'ютера":
            print("Комп'ютер переміг!")
        else:
            print("Нічія!")


def main():
    rounds = int(input("Введіть кількість раундів: "))
    difficulty = input("Виберіть складність(нормально/складно): ")
    game = Game(rounds, difficulty)
    game.play()


if __name__ == "__main__":
    main()