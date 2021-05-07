from django.test import TestCase
from .models import Category

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

        def recur(children, path):
            if children:
                for child in children:
                    children = Category.objects.filter(parent=child)
                    recur(children, path + [child.name])
            else:
                print(path)

        top_categories = Category.objects.filter(parent=None)
        for category in top_categories:
            topcat = Category.objects.filter(name=category.name).first()
            children = Category.objects.filter(parent=topcat) 
            recur(children, [topcat.name])

        # category_names = [category.name for category in top_categories]
        # self.assertEqual(["Modern", "Medieval"], category_names)
