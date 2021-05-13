class Tree:
    def __init__(self, tree_class):
        self.tree_class = tree_class

    def get_tree(self):
        """
        Returns tree as a nested dict. Key consists of (id, name).
        Example:
        {
            (1, 'Medieval'): {
                (2, 'Byzantine Empire'): {},
                (3, 'Roman Empire'): {
                    (4, 'Baden gulden'): {},
                    (5, 'Rhenish guilder'): {}
                }
            },
            (6, 'Circulating'): {
                (7, 'United States dollar'): {},
                (8, 'British pound'): {},
                (9, 'Libyan dinar'): {}
            }
        }
        """
        tree = {}
        current = {}
        for path in [self._dictify_path(path) for path in self._path_lists()]:
            current = self._merge_dicts(current, path)
            tree.update(current)
        return tree

    def _path_lists(self):
        """
        Returns flattened paths.
        Example:
        [
            [(1, 'Medieval'), (2, 'Byzantine Empire')],
            [(1, 'Medieval'), (3, 'Roman Empire'), (4, 'Baden gulden')],
            [(1, 'Medieval'), (3, 'Roman Empire'), (5, 'Rhenish guilder')],
            [(6, 'Circulating'), (7, 'United States dollar')],
            [(6, 'Circulating'), (8, 'British pound')],
            [(6, 'Circulating'), (9, 'Libyan dinar')]
        ]
        """
        def add_path(children, path):
            if children:
                for child in children:
                    children = self.tree_class.objects.filter(parent=child)
                    add_path(children, path + [(child.id, child.name)])
            else:
                full_paths.append(path)

        full_paths = []
        for category in self.tree_class.objects.filter(parent=None):
            children = self.tree_class.objects.filter(parent=category)
            add_path(children, [(category.id, category.name)])
        return full_paths

    def _dictify_path(self, path):
        """
        Transforms path from list to dict.
        Example input:
        [
            (1, 'Medieval'),
            (3, 'Roman Empire'),
            (4, 'Baden gulden')
        ]
        Example output:
        {
            (1, 'Medieval'): {
                (3, 'Roman Empire'): {
                    (4, 'Baden gulden'): {}
                }
            }
        }
        """
        if path:
            return {path[0]: self._dictify_path(path[1:])}
        return {}

    def _merge_dicts(self, dict_a, dict_b):
        """
        Merges two dicts.
        Example input:
        dict_a = {
            (1, 'Medieval'): {
                (3, 'Roman Empire'): {
                    (4, 'Baden gulden'): {}
                }
            }
        }

        dict_b = {
            (1, 'Medieval'): {
                (3, 'Roman Empire'): {
                    (5, 'Rhenish guilder'): {}
                }
            }
        }
        Example output:
        {
            (1, 'Medieval'): {
                (3, 'Roman Empire'): {
                    (4, 'Baden gulden'): {},
                    (5, 'Rhenish guilder'): {}
                }
            }
        }
        """
        for key in dict_b:
            if key in dict_a:
                self._merge_dicts(dict_a[key], dict_b[key])
            else:
                dict_a[key] = dict_b[key]
        return dict_a
