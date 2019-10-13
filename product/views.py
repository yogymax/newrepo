from django.shortcuts import render

# Create your views here.
from .models import Product
from django.http.response import HttpResponse
def dummy_product():
    return Product(id=0,name='',qty=0,price=0.0,category='',
                   vendor='',brand='',remarks='')

def welcome_product_page(req):
    return render(req,'product.html',{'prod':dummy_product(),"products":Product.objects.all()})

    '''
    if req.method=='GET':
        return render(req,'product.html',{'prod':dummy_product(),"products":Product.objects.all()})
    return HttpResponse("Invalid Method Type...cannot show Landing page..!")
    '''


def save_or_update_product(req):
    print(req.POST)
    if int(req.POST['pid'])==0:
        prod = Product(name=req.POST['pnm'],
                   qty=req.POST['pqu'],
                   price=req.POST['ppr'],
                   category=req.POST['pca'],
                   vendor=req.POST['pve'],
                   brand=req.POST['pbr'],
                   remarks=req.POST['pre'])
        amsg = "Product <{}> Record Saved Successfully..."
    else:
        prod = Product(id=req.POST['pid'],name=req.POST['pnm'],
                       qty=req.POST['pqu'],
                       price=req.POST['ppr'],
                       category=req.POST['pca'],
                       vendor=req.POST['pve'],
                       brand=req.POST['pbr'],
                       remarks=req.POST['pre'])
        amsg = "Product <{}> Record updated Successfully..."
    prod.save()
    return render(req,'product.html',
                  {'prod':dummy_product(),
                   "products":Product.objects.all(),
                   "msg":amsg.format(prod.id)
                   })

def fetch_product_for_edit(req,pid):
    return render(req,'product.html',{'prod':Product.objects.get(id=pid),"products":Product.objects.all()})

def remove_product_record(req,pid):
    Product.objects.get(id=pid).delete()
    return render(req,'product.html',{
        'prod':dummy_product(),
        "products":Product.objects.all(),
        "msg":"Product <{}> record removed from database".format(pid)
    })
