
class Tree:

    def __init__(self, tree_class):
        self.tree_class = tree_class

    def get_nested_dict(self):
        result = {}
        paths = self._path_lists()
        path_dicts = [self._dictify_path(path) for path in paths]
        for i in range(1, len(path_dicts) - 1):
            result.update(self._merge_dicts(path_dicts[i - 1], path_dicts[i]))
        return result

    def _path_lists(self):

        full_paths = []

        def recur(children, path):
            if children:
                for child in children:
                    children = self.tree_class.objects.filter(parent=child)
                    recur(children, path + [child.name])
            else:
                full_paths.append(path)

        top_categories = self.tree_class.objects.filter(parent=None)
        for category in top_categories:
            topcat = self.tree_class.objects.filter(name=category.name).first()
            children = self.tree_class.objects.filter(parent=topcat) 
            recur(children, [topcat.name])
        return full_paths

    def _dictify_path(self, path):
        if path:
            return {path[0]: self._dictify_path(path[1:])}
        return {}

    def _merge_dicts(self, dict_a, dict_b):
        for key in dict_b:
            if key in dict_a:
                self._merge_dicts(dict_a[key], dict_b[key])
            else:
                dict_a[key] = dict_b[key]
        return dict_a
