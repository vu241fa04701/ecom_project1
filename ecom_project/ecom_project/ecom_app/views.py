
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from .models import Product,Cart
def add_product(request):
    """
    this function will take the data from the client and save into the database
    :param request: data of the product from the form
    :return:
    """
    if request.method == "POST":
        p_name=request.POST.get('p_name')
        p_type=request.POST.get('p_type')
        p_price=request.POST.get('p_price')
        p_quantity=request.POST.get('p_quantity')
        data=Product.objects.create(
            p_name=p_name,
            p_type=p_type,
            p_price=p_price,
            p_quantity=p_quantity
        )
        return render(request,"success.html",{"message":"Product Added Successfully"})
    return render(request,"product_form.html")
def view_all_products(request):
    """
    this function will return the list of all the products
    :param request: no params
    :return: list of products
    """
    data=Product.objects.all().values()
    return render(request,"product_list.html",{"product_data":list(data)})
def delete_by_id(request, id):
    data = Product.objects.get(id=id)
    data.delete()
    return render(
        request,
        'success.html',
        {"message": "Product Deleted Successfully"}
    )
def add_to_cart(request, product_id):
    """
    :param request:
    :param product_id:
    :return:
    """

    data = Product.objects.get(id=product_id)

    Cart.objects.create(
        product_id = data.id,
        p_price = data.p_price
    )

    return render(
        request,
        "success.html",
        {"message":"Product Added to Cart Successfully"}
    )
def update_product(request, id):

    data = Product.objects.get(id=id)

    if request.method == "POST":

        data.p_name = request.POST.get('p_name')
        data.p_type = request.POST.get('p_type')
        data.p_price = request.POST.get('p_price')
        data.p_quantity = request.POST.get('p_quantity')

        data.save()

        return render(
            request,
            "success.html",
            {"message": "Product Updated Successfully"}
        )

    return render(
        request,
        "update_product.html",
        {"product": data}
    )
def remove_from_cart(request, id):

    data = Cart.objects.get(product_id=id)

    data.delete()

    return render(
        request,
        "success.html",
        {"message": "Product Removed From Cart Successfully"}
    )
def view_cart(request):

    cart_data = Cart.objects.all()

    return render(
        request,
        "cart_list.html",
        {"cart_items": cart_data}
    )