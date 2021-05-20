from tree.tree import Tree
from category.models import Category


def categories_to_dropdown_options():
    tree = Tree(Category)
    return list(reversed(flatten(tree.get_tree())))


def flatten(dict, prefix='', separator='—'):
    items = []
    for k, v in dict.items():
        items.extend(flatten(v, prefix + separator))
        items.append((k[0], prefix + ' ' + str(k[1])))
    return items
