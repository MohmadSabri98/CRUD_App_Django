

from django.urls import path
from products.views import productindex,index,show,delete,UpdateProductView,CreateProductView
#,createproduct

urlpatterns = [
    path('all', productindex,name="products.all"),

    path('', index, name="products.index"),
    path("<int:id>", show, name="products.show"),
    path("delete/<id>", delete, name="products.delete"),
#    path("create", createproduct, name="products.create"),
    path("create", CreateProductView.as_view(), name="products.create"),

    path("edit/<int:pk>",UpdateProductView.as_view(),name="products.edit")


]
