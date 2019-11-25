#from search_views.search import SearchListView

from django.shortcuts import render
from django.http import HttpResponse#import httpresponse class from http module of django package
from.models import Products,Offer
from.forms import Productform,Offerform,Signupform,Loginform,ProductSearchForm

# Create your views here.


def index(request): #a function normally given the name index to specify what the user gets on the main page
    product=Products.objects.all()#fetch all products from the Products model
    #return HttpResponse('Hellow world')
    return render(request,'index.html',{'product':product})#return a dictionary of items in the product objects

def displayoffer(request):
    offers=Offer.objects.all()
    return HttpResponse(request,'specialoffer.html',{'offers':offers})

def create(request): #a function defined to create a view for product form to specify what the user gets on the main page
    form=Productform(request.POST or None)
    if form.is_valid():
        form.save()
    form = Productform()
    context={'form':form}
    return render(request,'product_create.html',context)#return a dictionary of items in the product objects


def offer(request): #a function defined to create a view for product form to specify what the user gets on the main page
    form=Offerform(request.POST or None)
    if form.is_valid():
        form.save()
    form = Offerform()
    context={'form':form}
    return render(request,'create_offer.html',context)#return a dictionary of items in the product objects

def signup(request):
    form=Signupform(request.POST or None)
    if form.is_valid():
        form.save()
        form=Signupform()
    context={'form':form}
    return render(request,'registration/signup.html',context)#return a dictionary of items in the product objects

def login(request):
    form=Loginform(request.POST or None)
    if form.is_valid():
        form = Loginform()

    return render(request,'registration/login.html')

def logout(request):
    return render(request,'registration/logout.html')

def SearchProduct(request):
    queryset=Products.objects.all()
    context={
        "object_list":queryset
    }
    return render(request,'productsearch.html',context)



#..class ProductSearchView(SearchListView):
   # model = Products
    #paginate_by = 30
    #template_name = "mysearch.html"
    #form_class = ProductSearchForm
    #filter_class = ProductsFilter..
