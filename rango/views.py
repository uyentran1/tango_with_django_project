from django.shortcuts import render, redirect
from django.http import HttpResponse
from rango.forms import CategoryForm
from rango.models import Category, Page

def index(request):
    # Retrieve top 5 most liked categories
    category_list = Category.objects.order_by('-likes')[:5] # -like: desceding order
    # Retrieve top 5 most viewed pages
    page_list = Page.objects.order_by('-views')[:5] # -views: desceding order

    context_dict = {
        'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!',
        'categories': category_list,
        'pages': page_list
    }

    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'name': 'Uyen'}
    return render(request, 'rango/about.html',context=context_dict)

def secret(request):
    context_dict = {
        'secret1': 'Hello this is secret number 1.', 
        'secret2': 'Hello this is secret number 2.'
        }
    return render(request, 'rango/secret.html', context=context_dict)

def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context=context_dict)

def add_category(request):
    form = CategoryForm()

    # If the user submitted data via the form
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect('/rango/')
        else:
            print(form.errors)
            
    return render(request, 'rango/add_category.html', {'form': form})

    
