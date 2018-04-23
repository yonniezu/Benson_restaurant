from django.shortcuts import render

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        Order = request.POST.get('Order')
        address = request.POST.get("address")

        print(Order * 10)
        return render(request, 'waimai/home_page.html', {'Order': Order, 'address': address})

    return render(request, 'waimai/home_page.html')