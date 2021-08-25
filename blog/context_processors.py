from blog.models import Category

def getCategories(request):
    return {"categories":Category.objects.all()}