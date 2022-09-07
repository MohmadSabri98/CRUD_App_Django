from django.db import models
from django.shortcuts import reverse
# Create your models here.
class product(models.Model):
    #here is our propreties
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=200,null=True)
    image=models.CharField(max_length=200,null=True)
    no_of_item=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name
    def get_show_url(self):
        return reverse("products.show",kwargs={"id":self.id})
    def get_all_url(self):
        return reverse("products.index")
    def get_delete_url(self):
        return reverse("products.delete",kwargs={"id":self.id})

    def get_edit_url(self):
        return reverse("products.edit", kwargs={"pk": self.id})

