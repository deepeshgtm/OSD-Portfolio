import random

class DiceGame:
    def __init__(self):
        self.dice = [1] * 5  # Initialize 5 dice
        self.locked = [False] * 5  # Track locked state
        self.roll_dice()  # Roll all dice on instantiation

    def roll_dice(self):
        """Roll all unlocked dice."""
        for i in range(5):
            if not self.locked[i]:
                self.dice[i] = random.randint(1, 6)
        return self.dice

    def lock_dice(self, index):
        """Lock a die at the given index (0-4)."""
        if 0 <= index < 5:
            self.locked[index] = True

    def unlock_dice(self, index):
        """Unlock a die at the given index (0-4)."""
        if 0 <= index < 5:
            self.locked[index] = False

    def get_dice_values(self):
        """Return current dice values."""
        return self.dice

    # Scoring methods
    def ScoreOnes(self):
        return sum(d for d in self.dice if d == 1)

    def ScoreTwos(self):
        return sum(d for d in self.dice if d == 2)

    def ScoreThrees(self):
        return sum(d for d in self.dice if d == 3)

    def ScoreFours(self):
        return sum(d for d in self.dice if d == 4)

    def ScoreFives(self):
        return sum(d for d in self.dice if d == 5)

    def ScoreSixes(self):
        return sum(d for d in self.dice if d == 6)

    def SinglePair(self):
        counts = [self.dice.count(i) for i in range(1, 7)]
        for i in range(5, -1, -1):  # Check from 6 to 1
            if counts[i] >= 2:
                return (i + 1) * 2
        return 0

    def DoublePairs(self):
        counts = [self.dice.count(i) for i in range(1, 7)]
        pairs = [(i + 1) for i in range(5, -1, -1) if counts[i] >= 2]
        if len(pairs) >= 2:
            return (pairs[0] + pairs[1]) * 2
        return 0

    def TripleMatch(self):
        for i in range(1, 7):
            if self.dice.count(i) >= 3:
                return i * 3
        return 0

    def QuadMatch(self):
        for i in range(1, 7):
            if self.dice.count(i) >= 4:
                return i * 4
        return 0

    def SmallStraight(self):
        if sorted(self.dice) == [1, 2, 3, 4, 5]:
            return 15
        return 0

    def LargeStraight(self):
        if sorted(self.dice) == [2, 3, 4, 5, 6]:
            return 20
        return 0

    def FullSet(self):
        counts = [self.dice.count(i) for i in range(1, 7)]
        if 2 in counts and 3 in counts:
            return 25
        return 0

    def TotalSum(self):
        return sum(self.dice)

    def AllSame(self):
        if len(set(self.dice)) == 1:
            return 50
        return 0