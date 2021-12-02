import unittest
from ginrummy import *

class ginrummytest(unittest.TestCase):

    gin_rummy = ginrummy()

    def testGenerateDeck(self):
        self.assertEqual(52, len(self.gin_rummy.makedeck()))

    def testShuffleCards(self, deck=gin_rummy.makedeck()):
        self.assertNotEqual(deck, self.gin_rummy.shuffledeck(deck))

    def testHands(self, deck=gin_rummy.makedeck()):
        hands = self.gin_rummy.gethands(deck, 2)
        
        for hand in hands:
            self.assertEqual(7, len(hand))

    def test_input(self):
        self.assertEqual(2, self.gin_rummy.getplayers())

if __name__ == "__main__":
    unittest.main()

