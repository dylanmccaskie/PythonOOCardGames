import unittest
import sys
import io
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

    def testOutputHand(self, deck=gin_rummy.makedeck()):
        hand = self.gin_rummy.gethands(deck, 2)[0]
        expected_output = ' '.join(hand)
        print("OUTPUT: ", expected_output)
        redirected_output = io.StringIO()
        
        # Redirect console output 
        sys.stdout = redirected_output

        # Call function and check that value matches expected value
        self.gin_rummy.output_hand(hand)
        self.assertEqual(redirected_output.getvalue().strip(), expected_output)
        
        # Reset redirect
        sys.stdout = sys.__stdout__
        print("passed")

if __name__ == "__main__":
    unittest.main()

