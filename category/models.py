from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=256)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
        # full_path = [self.name]                  
        # k = self.parent_id
        # while k is not None:
        #     full_path.append(k.name)
        #     k = k.parent_id
        # return ' -> '.join(full_path[::-1])
