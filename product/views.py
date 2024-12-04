from django.shortcuts import render,get_object_or_404,redirect
from product.models import Product,Category,ProductSpecificationValue
from product_slider.models import Slider
from django.db.models import Q


def home(request):

    sliders = Slider.objects.all()
    special_products = Product.objects.filter(is_special=True).order_by('-discount')
    parent_category = Category.objects.filter(parent__isnull=True)
    new_products = Product.objects.all().order_by("created")[:5]
    many_sold = Product.objects.all().order_by("-count_sold")[:5]
    
    context = {
        "sliders":sliders,
        "special_products":special_products,
        "parent_category":parent_category,
        "new_products":new_products,
        "many_sold":many_sold
    }
    return render(request,"product/index.html",context)



def product_detail(request,uuid):
    product = get_object_or_404(Product,uuid=uuid)
    
    context = {
        "product":product
    }
    return render(request,"product/product.html",context)

def search(request):
    if request.method=='POST':
        search = request.POST['search']
        search = Product.objects.filter(Q(title__icontains=search) | Q(description__icontains=search))
        title = request.POST.get("search")
        if not search:
            return render(request,"product/search.html",{"title":title})
        else:
            return render(request,"product/search.html",{"search":search,"title":title})

    else:
        return render(request,"product/search.html",{})
