import random

class Yatzy:
    def __init__(self):
        self.dice = [1] * 5  # Initialize 5 dice
        self.locked = [False] * 5  # Track locked state
        self.roll()  # Roll all dice on instantiation

    def roll(self):
        """Roll all unlocked dice."""
        for i in range(5):
            if not self.locked[i]:
                self.dice[i] = random.randint(1, 6)
        return self.dice

    def lock_die(self, index):
        """Lock a die at the given index (0-4)."""
        if 0 <= index < 5:
            self.locked[index] = True

    def unlock_die(self, index):
        """Unlock a die at the given index (0-4)."""
        if 0 <= index < 5:
            self.locked[index] = False

    def get_dice(self):
        """Return current dice values."""
        return self.dice

    # Scoring methods
    def Ones(self):
        return sum(d for d in self.dice if d == 1)

    def Twos(self):
        return sum(d for d in self.dice if d == 2)

    def Threes(self):
        return sum(d for d in self.dice if d == 3)

    def Fours(self):
        return sum(d for d in self.dice if d == 4)

    def Fives(self):
        return sum(d for d in self.dice if d == 5)

    def Sixes(self):
        return sum(d for d in self.dice if d == 6)

    def OnePair(self):
        counts = [self.dice.count(i) for i in range(1, 7)]
        for i in range(5, -1, -1):  # Check from 6 to 1
            if counts[i] >= 2:
                return (i + 1) * 2
        return 0

    def TwoPairs(self):
        counts = [self.dice.count(i) for i in range(1, 7)]
        pairs = [(i + 1) for i in range(5, -1, -1) if counts[i] >= 2]
        if len(pairs) >= 2:
            return (pairs[0] + pairs[1]) * 2
        return 0

    def ThreeAlike(self):
        for i in range(1, 7):
            if self.dice.count(i) >= 3:
                return i * 3
        return 0

    def FourAlike(self):
        for i in range(1, 7):
            if self.dice.count(i) >= 4:
                return i * 4
        return 0

    def Small(self):
        if sorted(self.dice) == [1, 2, 3, 4, 5]:
            return 15
        return 0

    def Large(self):
        if sorted(self.dice) == [2, 3, 4, 5, 6]:
            return 20
        return 0

    def FullCourse(self):
        counts = [self.dice.count(i) for i in range(1, 7)]
        if 2 in counts and 3 in counts:
            return 25
        return 0

    def Chance(self):
        return sum(self.dice)

    def Yatzy(self):
        if len(set(self.dice)) == 1:
            return 50
        return 0