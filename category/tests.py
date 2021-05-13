from django.test import TestCase

from tree.tree import Tree
from .models import Category


class CategoryTestCase(TestCase):
    def setUp(self):
        self.medieval = Category.objects.create(name="Medieval")
        self.byzantine_empire = Category.objects.create(name="Byzantine Empire", parent=self.medieval)
        self.roman_empire = Category.objects.create(name="Roman Empire", parent=self.medieval)
        self.baden_gulden = Category.objects.create(name="Baden gulden", parent=self.roman_empire)
        self.rhenish_guilder = Category.objects.create(name="Rhenish guilder", parent=self.roman_empire)

        self.circulating = Category.objects.create(name="Circulating")
        self.usd = Category.objects.create(name="United States dollar", parent=self.circulating)
        self.british_pound = Category.objects.create(name="British pound", parent=self.circulating)
        self.libyan_dinar = Category.objects.create(name="Libyan dinar", parent=self.circulating)


    def test_top_categories(self):
        top_categories = Category.objects.filter(parent=None)
        category_names = [category.name for category in top_categories]
        self.assertEqual(["Medieval", "Circulating"], category_names)

    def test_tree(self):
        tree = Tree(Category)
        expected = {
            (self.medieval.id, "Medieval"): {
                (self.byzantine_empire.id, "Byzantine Empire"): {},
                (self.roman_empire.id, "Roman Empire"): {
                    (self.baden_gulden.id, "Baden gulden"): {},
                    (self.rhenish_guilder.id, "Rhenish guilder"): {}
                }
            },
            (self.circulating.id, "Circulating"): {
                (self.usd.id, "United States dollar"): {},
                (self.british_pound.id, "British pound"): {},
                (self.libyan_dinar.id, "Libyan dinar"): {}
            }
        }
        self.assertEqual(expected, tree.get_tree())
