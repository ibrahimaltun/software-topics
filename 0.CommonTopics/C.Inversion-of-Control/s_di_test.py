"""
unittest ile UserService'i mock bir repository ile test
"""
import unittest
from s_di_exam import GreetingService, User


class FakeUserRepo:
    def __init__(self):
        self.called = False

    def get_user(self, user_id: int):
        self.called = True
        if user_id == 1:
            return User(1, "TestUser")
        return None


class GreetingServiceTest(unittest.TestCase):
    def test_greet_found(self):
        repo = FakeUserRepo()
        svc = GreetingService(repo)
        res = svc.greet_user(1)
        self.assertEqual(res, "Hello, TestUser!")
        self.assertTrue(repo.called)

    def test_greet_not_found(self):
        repo = FakeUserRepo()
        svc = GreetingService(repo)
        res = svc.greet_user(99)
        self.assertEqual(res, "User not found")


if __name__ == "__main__":
    unittest.main()
