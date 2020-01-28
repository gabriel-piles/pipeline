from random import random
from unittest import TestCase


class Test(TestCase):
    def test_info(self):
        if random() > 0.5:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

