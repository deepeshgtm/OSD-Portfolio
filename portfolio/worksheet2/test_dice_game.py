import unittest
from dice_game import DiceGame

class TestDiceGame(unittest.TestCase):
    def setUp(self):
        """Create a new DiceGame instance before each test."""
        self.game = DiceGame()

    def set_dice(self, values):
        """Helper to set dice values for testing."""
        if len(values) != 5:
            raise ValueError("Must provide exactly 5 dice values")
        self.game.dice = values[:]  # Copy to avoid mutating input
        self.game.locked = [False] * 5  # Reset locks

    def test_roll_dice(self):
        """Test that rolling produces 5 dice with values between 1 and 6."""
        dice = self.game.roll_dice()
        self.assertEqual(len(dice), 5)
        self.assertTrue(all(1 <= d <= 6 for d in dice))

    def test_initial_roll(self):
        """Test that instantiation rolls all dice."""
        dice = self.game.get_dice_values()
        self.assertEqual(len(dice), 5)
        self.assertTrue(all(1 <= d <= 6 for d in dice))

    def test_lock_and_roll(self):
        """Test that locking a die prevents it from changing on roll."""
        self.set_dice([1, 2, 3, 4, 5])
        self.game.lock_dice(0)  # Lock first die (value 1)
        self.game.roll_dice()
        self.assertEqual(self.game.dice[0], 1)  # Locked die stays the same
        self.assertTrue(all(1 <= self.game.dice[i] <= 6 for i in range(1, 5)))

    def test_score_ones(self):
        """Test ScoreOnes scoring."""
        self.set_dice([1, 1, 2, 3, 4])
        self.assertEqual(self.game.ScoreOnes(), 2)

    def test_score_twos(self):
        """Test ScoreTwos scoring."""
        self.set_dice([2, 2, 2, 3, 4])
        self.assertEqual(self.game.ScoreTwos(), 6)

    def test_single_pair(self):
        """Test SinglePair scoring."""
        self.set_dice([3, 3, 4, 4, 5])
        self.assertEqual(self.game.SinglePair(), 8)  # Pair of 4s

    def test_double_pairs(self):
        """Test DoublePairs scoring."""
        self.set_dice([3, 3, 4, 4, 5])
        self.assertEqual(self.game.DoublePairs(), 14)  # Pairs of 3s and 4s

    def test_triple_match(self):
        """Test TripleMatch scoring."""
        self.set_dice([2, 2, 2, 3, 4])
        self.assertEqual(self.game.TripleMatch(), 6)

    def test_quad_match(self):
        """Test QuadMatch scoring."""
        self.set_dice([5, 5, 5, 5, 1])
        self.assertEqual(self.game.QuadMatch(), 20)

    def test_small_straight(self):
        """Test SmallStraight scoring."""
        self.set_dice([1, 2, 3, 4, 5])
        self.assertEqual(self.game.SmallStraight(), 15)

    def test_large_straight(self):
        """Test LargeStraight scoring."""
        self.set_dice([2, 3, 4, 5, 6])
        self.assertEqual(self.game.LargeStraight(), 20)

    def test_full_set(self):
        """Test FullSet scoring."""
        self.set_dice([2, 2, 3, 3, 3])
        self.assertEqual(self.game.FullSet(), 25)

    def test_total_sum(self):
        """Test TotalSum scoring."""
        self.set_dice([1, 2, 3, 4, 5])
        self.assertEqual(self.game.TotalSum(), 15)

    def test_all_same(self):
        """Test AllSame scoring."""
        self.set_dice([4, 4, 4, 4, 4])
        self.assertEqual(self.game.AllSame(), 50)

if __name__ == "__main__":
    unittest.main()