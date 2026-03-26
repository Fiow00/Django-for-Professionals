from django.contrib import admin
from .models import Book, Review, Category, Author, Order, OrderItem, Wishlist


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "status", "created")
    list_filter = ("status", "created")
    inlines = [OrderItemInline]


class BookAdmin(admin.ModelAdmin):
    inlines = [ReviewInline]
    list_display = ("title", "author", "category", "price", "inventory", "slug")
    list_filter = ("category", "author")
    search_fields = ("title", "author__name")


admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Wishlist)
admin.site.register(Book, BookAdmin)