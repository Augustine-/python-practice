"""
Implement a class NonRepeatingRandom that includes a method to generate a sequence of random numbers.
Each number should be unique and from a specified range.
Once all possible numbers from the range have been generated, the method should reset and begin generating new numbers without repetition.

Requirements:

    Class Name: NonRepeatingRandom

    Method Name: generate

    Input Parameters:
        start: An integer specifying the start of the range (inclusive).
        finish: An integer specifying the end of the range (inclusive).
        N: An integer specifying the number of random numbers to generate.

    Output: A list of N random numbers.
    The sequence should not repeat any number until all unique numbers from the specified range have been used.
    Once every number has been generated, the sequence can start repeating numbers from the range.

Example Usage:

    Given the range (1, 3) and N = 6,
    a valid sequence could be [2, 1, 3, 2, 3, 1], but [1, 1, 3, 2, 1, 3] would be invalid.
"""
import random

class NonRepeatingRandom:
    def __init__(self, start, end) -> None:
        self.pool = list(range(start, end + 1))
        self.w = len(self.pool) - 1

    def generate(self, n):
        out = []
        for _ in range(n):
            if self.w < 0:
                self.w = len(self.pool) - 1
            r = random.randint(0, self.w)
            out.append(self.pool[r])
            self.pool[r], self.pool[self.w] = self.pool[self.w], self.pool[r]
            self.w -= 1

        return out

nrr = NonRepeatingRandom(1, 3)

print(nrr.generate(9))