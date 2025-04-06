import unittest

class TestTranslator(unittest.TestCase):
    def test_translation(self):
        self.assertEqual(translate("hello"), "hallo")
        self.assertEqual(translate("goodbye"), "auf Wiedersehen")

if __name__ == '__main__':
    unittest.main()