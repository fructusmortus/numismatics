from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    categories = {
        "USSR": {
            "1920-1950": {
                "1920-1930": {},
                "1930-1950": {
                    "1930": {},
                    "1950": {}   
                }
            }

        },
        "Austria": {
            "1910": {},
            "1920": {
                "Shilling coins": {},
                "Shilling banknotes": {
                    "Mint": {},
                    "Fair": {}
                }
            }
        },
        "Netherlands": {
            "Modern euros": {},
            "Old guldens": {}
        }
    }
    return render(request, 'home/dashboard.html', {'categories': categories})


def about(request):
    print(request)
    return render(request, 'home/about.html')
