import unittest
from yatzy import Yatzy

class TestYatzy(unittest.TestCase):
    def setUp(self):
        """Create a new Yatzy instance before each test."""
        self.game = Yatzy()

    def set_dice(self, values):
        """
        Helper to set dice values for testing.
        Resets locks and sets dice directly (since roll is random).
        """
        if len(values) != 5:
            raise ValueError("Must provide exactly 5 dice values")
        self.game.dice = values[:]  # Copy to avoid mutating input
        self.game.locked = [False] * 5  # Reset locks

    def test_roll(self):
        """Test that rolling produces 5 dice with values between 1 and 6."""
        dice = self.game.roll()
        self.assertEqual(len(dice), 5)
        self.assertTrue(all(1 <= d <= 6 for d in dice))

    def test_initial_roll(self):
        """Test that instantiation rolls all dice."""
        dice = self.game.get_dice()
        self.assertEqual(len(dice), 5)
        self.assertTrue(all(1 <= d <= 6 for d in dice))

    def test_lock_and_roll(self):
        """Test that locking a die prevents it from changing on roll."""
        self.set_dice([1, 2, 3, 4, 5])
        self.game.lock_die(0)  # Lock first die (value 1)
        self.game.roll()
        self.assertEqual(self.game.dice[0], 1)  # Locked die stays the same
        self.assertTrue(all(1 <= self.game.dice[i] <= 6 for i in range(1, 5)))

    def test_unlock_and_roll(self):
        """Test that unlocking a die allows it to change on roll."""
        self.set_dice([1, 2, 3, 4, 5])
        self.game.lock_die(0)
        self.game.unlock_die(0)
        self.game.roll()
        self.assertTrue(all(1 <= d <= 6 for d in self.game.dice))

    def test_invalid_lock_index(self):
        """Test that locking an invalid index doesn't raise an error."""
        try:
            self.game.lock_die(5)  # Out of bounds
            self.game.lock_die(-1)  # Negative
        except IndexError:
            self.fail("lock_die raised IndexError unexpectedly")

    def test_ones(self):
        """Test Ones scoring."""
        self.set_dice([1, 1, 2, 3, 4])
        self.assertEqual(self.game.Ones(), 2)
        self.set_dice([2, 3, 4, 5, 6])
        self.assertEqual(self.game.Ones(), 0)

    def test_twos(self):
        """Test Twos scoring."""
        self.set_dice([2, 2, 2, 3, 4])
        self.assertEqual(self.game.Twos(), 6)
        self.set_dice([1, 3, 4, 5, 6])
        self.assertEqual(self.game.Twos(), 0)

    def test_threes(self):
        """Test Threes scoring."""
        self.set_dice([3, 3, 3, 1, 2])
        self.assertEqual(self.game.Threes(), 9)
        self.set_dice([1, 2, 4, 5, 6])
        self.assertEqual(self.game.Threes(), 0)

    def test_fours(self):
        """Test Fours scoring."""
        self.set_dice([4, 4, 1, 2, 3])
        self.assertEqual(self.game.Fours(), 8)
        self.set_dice([1, 2, 3, 5, 6])
        self.assertEqual(self.game.Fours(), 0)

    def test_fives(self):
        """Test Fives scoring."""
        self.set_dice([5, 5, 5, 1, 2])
        self.assertEqual(self.game.Fives(), 15)
        self.set_dice([1, 2, 3, 4, 6])
        self.assertEqual(self.game.Fives(), 0)

    def test_sixes(self):
        """Test Sixes scoring."""
        self.set_dice([6, 6, 1, 2, 3])
        self.assertEqual(self.game.Sixes(), 12)
        self.set_dice([1, 2, 3, 4, 5])
        self.assertEqual(self.game.Sixes(), 0)

    def test_one_pair(self):
        """Test OnePair scoring."""
        self.set_dice([3, 3, 4, 4, 5])
        self.assertEqual(self.game.OnePair(), 8)  # Pair of 4s (highest)
        self.set_dice([1, 2, 3, 4, 5])
        self.assertEqual(self.game.OnePair(), 0)

    def test_two_pairs(self):
        """Test TwoPairs scoring."""
        self.set_dice([3, 3, 4, 4, 5])
        self.assertEqual(self.game.TwoPairs(), 14)  # Pairs of 3s and 4s: (3 + 4) * 2
        self.set_dice([3, 3, 3, 3, 5])
        self.assertEqual(self.game.TwoPairs(), 0)  # Only one value
        self.set_dice([1, 2, 3, 4, 5])
        self.assertEqual(self.game.TwoPairs(), 0)  # No pairs

    def test_three_alike(self):
        """Test ThreeAlike scoring."""
        self.set_dice([2, 2, 2, 3, 4])
        self.assertEqual(self.game.ThreeAlike(), 6)
        self.set_dice([1, 2, 3, 4, 5])
        self.assertEqual(self.game.ThreeAlike(), 0)

    def test_four_alike(self):
        """Test FourAlike scoring."""
        self.set_dice([5, 5, 5, 5, 1])
        self.assertEqual(self.game.FourAlike(), 20)
        self.set_dice([5, 5, 5, 1, 2])
        self.assertEqual(self.game.FourAlike(), 0)

    def test_small(self):
        """Test Small straight scoring."""
        self.set_dice([1, 2, 3, 4, 5])
        self.assertEqual(self.game.Small(), 15)
        self.set_dice([1, 2, 3, 4, 4])
        self.assertEqual(self.game.Small(), 0)

    def test_large(self):
        """Test Large straight scoring."""
        self.set_dice([2, 3, 4, 5, 6])
        self.assertEqual(self.game.Large(), 20)
        self.set_dice([1, 2, 3, 4, 5])
        self.assertEqual(self.game.Large(), 0)

    def test_full_course(self):
        """Test FullCourse (full house) scoring."""
        self.set_dice([2, 2, 3, 3, 3])
        self.assertEqual(self.game.FullCourse(), 25)
        self.set_dice([2, 2, 2, 2, 3])
        self.assertEqual(self.game.FullCourse(), 0)

    def test_chance(self):
        """Test Chance scoring."""
        self.set_dice([1, 2, 3, 4, 5])
        self.assertEqual(self.game.Chance(), 15)
        self.set_dice([6, 6, 6, 6, 6])
        self.assertEqual(self.game.Chance(), 30)

    def test_yatzy(self):
        """Test Yatzy scoring."""
        self.set_dice([4, 4, 4, 4, 4])
        self.assertEqual(self.game.Yatzy(), 50)
        self.set_dice([4, 4, 4, 4, 5])
        self.assertEqual(self.game.Yatzy(), 0)

if __name__ == "__main__":
    unittest.main()