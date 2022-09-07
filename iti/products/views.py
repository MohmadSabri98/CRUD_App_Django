from django.shortcuts import render,redirect
from django.http import HttpResponse
from products.models import product
# Create your views here.
from products.forms import ProductForm
from django.views.generic.edit import UpdateView, CreateView
def productindex(request):
    allproducts = [
        {"id": 1, "name": "product1", "image": 'product1.png'},
        {"id": 2, "name": "product2", "image": 'product2.png'},
        {"id": 3, "name": "product3", "image": 'product3.png'}]
    return render(request,"products/allproducts.html",context={"products":allproducts})
    #return HttpResponse("this my product index")
def index(request):
    allproducts = product.objects.all()
    return render(request,"products/index.html",context={"products":allproducts})
    #return HttpResponse("this my product index")
def show (request,id):
    item=product.objects.get(pk=id)
    #return HttpResponse(item)
    return render(request,"products/show.html",context={"product":item})
def delete (request,id):
    item=product.objects.get(pk=id)
    item.delete()
    return redirect("/products")

# def createproduct(request):
#     # request may be get request
#     if request.POST:
#         # return HttpResponse("POST request ")
#         # I want to get the data received with the request ?
#         # return HttpResponse(request.POST["name"])
#         item = product()
#         item.name = request.POST["name"]
#         item.image = request.POST["image"]
#         item.no_of_item= request.POST["no_of_item"]
#         item.description = request.POST["description"]
#         item.save()
#         return redirect('/products')
#
#     myform = ProductForm()
#     return render(request, "products/create.html", context={"form":myform})

#class based views
class UpdateProductView(UpdateView):
    model = product
    form_class = ProductForm
    template_name ='products/edit.html'
    success_url = "/products"
class CreateProductView(CreateView):
    model = product
    form_class = ProductForm
    template_name ='products/create.html'
    success_url = "/products"