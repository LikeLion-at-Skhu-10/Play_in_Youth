from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request, 'base.html')

def main(request):
    return render(request, 'main.html')

def category(request):
    return render(request, 'category.html')

def write(request):
    return render(request, 'write.html')

def edit(request):
    return render(request, 'edit.html')

# category_detail
def gardening(request):
    return render(request, 'category_detail/gardening.html')

def farming(request):
    return render(request, 'category_detail/farming.html')

def yoga(request):
    return render(request, 'category_detail/yoga.html')

def bicycle(request):
    return render(request, 'category_detail/bicycle.html')

def cooking(request):
    return render(request, 'category_detail/cooking.html')

def go(request):
    return render(request, 'category_detail/go.html')

def hiking(request):
    return render(request, 'category_detail/hiking.html')

def knitting(request):
    return render(request, 'category_detail/knitting.html')

def fishing(request):
    return render(request, 'category_detail/fishing.html')