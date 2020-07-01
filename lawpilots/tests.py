import unittest
import time

from .tasks import say_hello


class TestTasks(unittest.TestCase):
    def setUp(self):
        self.name = "Nader"

    def test_say_hello(self):
        self.assertEqual(say_hello(self.name), f"Hello {self.name}")

    def test_task_status(self):
        task = say_hello.delay(self.name)
        while not task.ready():
            time.sleep(0.1)
        self.assertEqual(task.status, "SUCCESS")


if __name__ == "__main__":
    unittest.main()
