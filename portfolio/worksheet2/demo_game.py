from dice_game import DiceGame

def play_demo_game():
    game = DiceGame()
    print("Initial roll:", game.get_dice_values())
    
    # Simulate a turn
    game.lock_dice(0)  # Lock first die
    game.roll_dice()
    print("After locking die 0 and rolling:", game.get_dice_values())
    
    # Show scoring options
    scores = {
        "ScoreOnes": game.ScoreOnes(),
        "ScoreTwos": game.ScoreTwos(),
        "ScoreThrees": game.ScoreThrees(),
        "ScoreFours": game.ScoreFours(),
        "ScoreFives": game.ScoreFives(),
        "ScoreSixes": game.ScoreSixes(),
        "SinglePair": game.SinglePair(),
        "DoublePairs": game.DoublePairs(),
        "TripleMatch": game.TripleMatch(),
        "QuadMatch": game.QuadMatch(),
        "SmallStraight": game.SmallStraight(),
        "LargeStraight": game.LargeStraight(),
        "FullSet": game.FullSet(),
        "TotalSum": game.TotalSum(),
        "AllSame": game.AllSame(),
    }
    
    print("\nScoring options:")
    for category, score in scores.items():
        print(f"{category}: {score}")

if __name__ == "__main__":
    play_demo_game()