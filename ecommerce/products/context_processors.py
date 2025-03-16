from .models import Category

# load for all pages
def categories(request):
    return {
        'categories': Category.objects.all()
    }