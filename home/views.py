from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact, Blog
import math
from .forms import BooksForm
from .models import Books
from django.db.models import Q

# Create your views here.
def home(request):
    # return HttpResponse("this is my home page")
    context = {'name': 'Ajeet', 'course': 'Django'}
    return render(request, 'home.html', context)


def about(request):
    # return HttpResponse("this is my about page ")
    return render(request, 'about.html')


def projects(request):
    # return HttpResponse("this is my project page")
    return render(request, 'projects.html')


def contact(request):
    if request.method == "POST":
        print("congrats")
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        ins = Contact(name=name, email=email, phone=phone, desc=desc)
        ins.save()
    # return HttpResponse("this is my contact page")
    return render(request, 'contact.html')


def blog(request):
    nop = 3
    page = request.GET.get('page')
    if page is None:
        page = 1
    else:
        page = int(page)
    blogs = Blog.objects.all()
    length = len(blogs)
    blogs = blogs[(page - 1) * nop: page * nop]

    if page > 1:
        prev = page - 1
    else:
        prev = None

    if page < math.ceil(length / nop):
        nxt = page + 1
    else:
        nxt = None
    context = {'blogs': blogs, 'prev': prev, 'nxt': nxt}
    return render(request, 'blog.html', context)
    '''
    1:0-3
    2:3-6
    3:6-9
    1:0-0+nop
    2:nop to nop+nop
    3:nop+nop to nop+nop+nop
    pg-1 *nop to pg*nop
    '''


def blogpost(request, slug):
    blog = Blog.objects.filter(slug=slug).first()
    context = {'blog': blog}
    return render(request, 'blogpost.html', context)


def search(request):
    search_query=request.GET['search']
    search_result=Blog.objects.filter(Q(title__contains = search_query) | Q(desc__contains = search_query) | Q(content__contains = search_query))
    context={'result':search_result}
    return render(request, 'search.html',context)

def wdp1(request):
    return render(request, 'wdp1.html')


def mbook(request):
    if request.method == "POST":
        form = BooksForm(request.POST)
        if form.is_valid():
                form.save()
                return redirect('/show')

    else:
        form = BooksForm()
    return render(request, 'bindex.html', {'form': form})


def show(request):
    book = Books.objects.all()
    return render(request, "bshow.html", {'book': book})


def edit(request, bname):
    books = Books.objects.get(bname=bname)
    return render(request, 'bedit.html', {'books': books})


def update(request, bname):
    books = Books.objects.get(bname=bname)
    form = BooksForm(request.POST, instance=books)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'bedit.html', {'books': books})


def destroy(request, bname):
    books = Books.objects.get(bname=bname)
    books.delete()
    return redirect("/show")

