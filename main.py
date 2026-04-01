class AzulGame:
    def __init__(self, num_players):
        self.num_players = num_players
        self.players = []
        self.factories = []
        self.center = []
        self.bag = []
        self.discard_pile = []
        self.current_player = 0

    def setup_game(self):
        print(f"Setting up Azul for {self.num_players} players...")
        self.create_bag()
        self.create_factories()

    def create_bag(self):
        colors = ["Blue", "Yellow", "Red", "Black", "White"]
        for color in colors:
            self.bag.extend([color] * 20)
        print("Bag created with 100 tiles.")

    def create_factories(self):
        if self.num_players == 2:
            factory_count = 5
        elif self.num_players == 3:
            factory_count = 7
        elif self.num_players == 4:
            factory_count = 9
        else:
            raise ValueError("Azul supports 2 to 4 players only.")

        self.factories = [[] for _ in range(factory_count)]
        print(f"{factory_count} factories created.")

    def start_game(self):
        self.setup_game()
        print("Game started.")

if __name__ == "__main__":
    game = AzulGame(2)
    game.start_game()
