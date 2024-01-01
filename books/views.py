from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def books(request):
    books = Book.objects.all()
    print(books)

    context = {"page_title": "Books", "books": books}

    return render(request, "homepage.html", context)


def book(request, pk):
    book = Book.objects.get(id=pk)

    context = {"page_title": "Book", "book": book}
    print(context)
    return render(request, "book.html", context)


@login_required(login_url="login")
def addBook(request):
    form = BookForm()

    if request.method == "POST":
        Book.objects.create(
            title=request.POST.get("title"),
            book_id=request.POST.get("book_id"),
            author=request.POST.get("author"),
            description=request.POST.get("description"),
            publishedby_year=request.POST.get("publishedby_year"),
            rating=request.POST.get("rating"),
            posted_by=request.user,
        )
        return redirect("/")
    context = {"page_title": "Create Book", "form": form}

    return render(request, "book_form.html", context)


@login_required(login_url="login")
def updateBook(request, pk):
    book = Book.objects.get(id=pk)
    form = BookForm(instance=book)

    if book.posted_by != request.user:
        return render(request, "not_authorized.html")

    if request.method == "POST":
        book.title = request.POST.get("title")
        book.book_id = request.POST.get("book_id")
        book.author = request.POST.get("author")
        book.description = request.POST.get("description")
        book.publishedby_year = request.POST.get("publishedby_year")
        book.rating = request.POST.get("rating")

        book.save()

        return redirect("/")

    context = {"page_title": "Update Book", "form": form}

    return render(request, "book_form.html", context)


@login_required(login_url="login")
def deleteBook(request, pk):
    book = Book.objects.get(id=pk)

    if book.posted_by != request.user:
        return render(request, "not_authorized.html")

    if request.method == "POST":
        book.delete()
        return redirect("/")

    context = {
        "book": book,
    }

    return render(request, "delete.html", context)


def loginPage(request):
    page = "login"
    print(request.user)
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            print("User does not exist")
            return redirect("login")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            print("Username or password is incorrect")

    context = {"page": page}

    return render(request, "login_register.html", context)


def logoutUser(request):
    logout(request)
    return redirect("/")


def registerUser(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            login(request, user)

            return redirect("/")
        else:
            print("Error in registration")

    context = {"page_title": "Register Here", "form": form}

    return render(request, "login_register.html", context)
