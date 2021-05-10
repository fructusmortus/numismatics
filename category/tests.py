from django.test import TestCase
from .models import Category
from tree.tree import Tree


class CategoryTestCase(TestCase):
    def setUp(self):
        с1 = Category.objects.create(name="Modern")
        с2 = Category.objects.create(name="Medieval")
        Category.objects.create(name="Austria", parent=с1)
        с3 = Category.objects.create(name="USSR", parent=с1)
        Category.objects.create(name="Greece", parent=с2)
        Category.objects.create(name="1920-1950 series", parent=с3)
        Category.objects.create(name="1950-1980 series", parent=с3)


    def test_top_categories(self):
        top_categories = Category.objects.filter(parent=None)
        category_names = [category.name for category in top_categories]
        self.assertEqual(["Modern", "Medieval"], category_names)

    # def test_path_lists(self):
    #     tree = Tree(Category)
    #     expected = [['Modern', 'Austria'], 
    #                 ['Modern', 'USSR', '1920-1950 series'], 
    #                 ['Modern', 'USSR', '1950-1980 series'], 
    #                 ['Medieval', 'Greece']]
    #     self.assertEqual(expected, tree.path_lists())

    def test_temporary(self):
        tree = Tree(Category)
        print(tree.get_nested_dict())