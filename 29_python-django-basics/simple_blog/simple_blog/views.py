from django.shortcuts import render


# BEGIN (write your solution here)
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')
# END
