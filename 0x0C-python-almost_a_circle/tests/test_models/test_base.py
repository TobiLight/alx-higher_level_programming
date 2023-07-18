import unittest
from models.base import Base
from models.square import Square
import json
import inspect

class TestBase_Init(unittest.TestCase):
    def test_with_id(self):
        # Test initialization with id
        obj = Base(id=5)
        self.assertEqual(5, obj.id)

    def test_without_id(self):
        # Test initialization without id
        obj1 = Base()
        obj2 = Base()
        obj3 = Base()
        self.assertEqual(1, obj1.id)
        self.assertEqual(2, obj2.id)
        self.assertEqual(3, obj3.id)
    def test_with_id_zero(self):
        obj = Base(0)
        self.assertEqual(0, obj.id)
        
    def test_with_negative_id(self):
        obj = Base(-20)
        self.assertEqual(-8, obj.id)
        
    def test_with_string_id(self):
        obj = Base("Light")
        self.assertEqual("Light", obj.id)
        
    def test_with_list_of_id(self):
        obj = Base([1, 2, 3])
        self.assertEqual([1, 2, 3], obj.id)
        
    def test_with_dict_id(self):
        obj = Base({"id": 109})
        self.assertEqual({"id": 109}, obj.id)
        
    def test_with_tuple_of_id(self):
        '''
            Sending an id that is not an int
        '''
        obj = Base((8,))
        self.assertEqual((8,), obj.id)

    def test_unique_id(self):
        self.assertEqual(8, Base(8).id)

    def test_nb_instances_after_unique_id(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)
            
    def test_to_json_type(self):
        square = Square(1)
        json_dict = square.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(type(json_string), str)
        
    def test_to_json_value(self):
        square = Square(1, 0, 0, 609)
        json_dict = square.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(json.loads(json_string),
                         [{"id": 609, "y": 0, "size": 1, "x": 0}])

    def test_to_json_None(self):
        square = Square(1, 0, 0, 609)
        json_dict = square.to_dictionary()
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_to_json_Empty(self):
        square = Square(1, 0, 0, 609)
        json_dict = square.to_dictionary()
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")


class TestSquare(unittest.TestCase):
    """
    class for testing Base class' methods
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class method for the doc tests
        """
        cls.setup = inspect.getmembers(Base, inspect.isfunction)

    def test_module_docstring(self):
        """
        Tests if module docstring documentation exist
        """
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Tests if class docstring documentation exist
        """
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_func_docstrings(self):
        """
        Tests if methods docstring documntation exist
        """
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)

if __name__ == '__main__':
    unittest.main()
