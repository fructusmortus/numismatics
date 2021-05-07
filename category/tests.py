from django.test import TestCase
from .models import Category

class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name="Modern")
        Category.objects.create(name="Medieval")
        Category.objects.create(name="Austria", parent_id=1)
        Category.objects.create(name="USSR", parent_id=1)
        Category.objects.create(name="Greece", parent_id=2)
        Category.objects.create(name="1920-1950 series", parent_id=4)
        Category.objects.create(name="1950-1980 series", parent_id=4)


    def test_top_categories(self):
        top_categories = Category.objects.filter(parent_id=None)
        category_names = [category.name for category in top_categories]
        self.assertEqual(["Modern", "Medieval"], category_names)
