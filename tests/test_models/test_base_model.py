"""
Unit tests for BaseModel class.
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test cases for BaseModel class.
    """
    def test_attributes(self):
        """
        Test initialization of attributes.
        """
        my_model = BaseModel()
        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))

    def test_str_method(self):
        """
        Test __str__ method.
        """
        my_model = BaseModel()
        self.assertEqual(str(my_model), f"[BaseModel] ({my_model.id}) {my_model.__dict__}")

    def test_save_method(self):
        """
        Test save method.
        """
        my_model = BaseModel()
        prev_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(prev_updated_at, my_model.updated_at)

    def test_to_dict_method(self):
        """
        Test to_dict method.
        """
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        self.assertTrue(isinstance(my_model_dict, dict))
        self.assertTrue("__class__" in my_model_dict)
        self.assertTrue("created_at" in my_model_dict)
        self.assertTrue("updated_at" in my_model_dict)


if __name__ == '__main__':
    unittest.main()
