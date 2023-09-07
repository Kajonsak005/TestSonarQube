import unittest
import main


class TestRevertString(unittest.TestCase):
    def test_revert_string(self):
        self.assertEqual(main.revert_string(
            "Let's take LeetCode contest"), "s'teL ekat edoCteeL tsetnoc")


if __name__ == '__main__':
    unittest.main()
