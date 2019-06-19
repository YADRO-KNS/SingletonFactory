import unittest
from uuid import *
import SingletonFactory


class Foo(object):
    def __init__(self):
        self.uuid = uuid4()



class Resources(SingletonFactory.ResourceProvider):
    def get_foo(self, recreate: bool = False):
        if self.is_in(Foo) is False or recreate is True:
            self.add(exemplar=Foo())
        return self.get(Foo)


class TestSingletonFactory(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.resource = Resources()


class TestSingletonFactoryCreation(TestSingletonFactory):
    def test_creation_success(self):
        self.assertIsNotNone(self.resource)
        self.assertIsInstance(self.resource, Resources)


class TestSingletonFactorResources(TestSingletonFactory):
    def test_instance_creation(self):
        result = self.resource.get_foo()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, Foo)

    def test_instance_recreation(self):
        result_1 = self.resource.get_foo()
        result_2 = self.resource.get_foo(recreate=True)

        self.assertIsNotNone(result_1)
        self.assertIsNotNone(result_2)
        self.assertIsInstance(result_1, Foo)
        self.assertIsInstance(result_2, Foo)

        self.assertNotEqual(result_1.uuid, result_2.uuid)