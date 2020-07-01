import unittest

from .tasks import say_hello


class TestTasks(unittest.TestCase):
    def test_say_hello(self):
        name = "Nader"
        self.assertEqual(say_hello(name), f"Hello {name}")


if __name__ == "__main__":
    unittest.main()
