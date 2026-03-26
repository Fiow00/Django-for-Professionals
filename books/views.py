from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.views.generic import ListView, DetailView

from django.db.models import Q

from .models import Book, Author, Category

# Create your views here.
class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = "books/book_list.html"
    context_object_name = "book_list"
    login_url = "account_login"
    queryset = Book.objects.select_related("author", "category").prefetch_related("reviews__author")

class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Book
    template_name = "books/book_detail.html"
    context_object_name = "book"
    login_url = "account_login"
    permission_required = "books.special_status"
    queryset = Book.objects.select_related("author", "category").prefetch_related("reviews__author")

class SearchResultsListView(ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "books/search_results.html"
    
    def get_queryset(self):
        query = self.request.GET.get("q")
        return Book.objects.select_related("author", "category").filter(
            Q(title__icontains=query) | Q(author__name__icontains=query) | Q(category__name__icontains=query)
        )
