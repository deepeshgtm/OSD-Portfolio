from yatzy import Yatzy

def play_dice_game():
    game = Yatzy()
    print("Initial roll:", game.get_dice())
    
    # Simulate a turn
    game.lock_die(0)  # Lock first die
    game.roll()
    print("After locking die 0 and rolling:", game.get_dice())
    
    # Show scoring options
    scores = {
        "Ones": game.Ones(),
        "Twos": game.Twos(),
        "Threes": game.Threes(),
        "Fours": game.Fours(),
        "Fives": game.Fives(),
        "Sixes": game.Sixes(),
        "OnePair": game.OnePair(),
        "TwoPairs": game.TwoPairs(),
        "ThreeAlike": game.ThreeAlike(),
        "FourAlike": game.FourAlike(),
        "Small": game.Small(),
        "Large": game.Large(),
        "FullCourse": game.FullCourse(),
        "Chance": game.Chance(),
        "Yatzy": game.Yatzy(),
    }
    
    print("\nScoring options:")
    for category, score in scores.items():
        print(f"{category}: {score}")

if __name__ == "__main__":
    play_dice_game()