from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406429014',
        'name': 'Rochelle Marchia Arisandi',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)