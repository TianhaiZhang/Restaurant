from django.shortcuts import render

# Create your views here.
def home_page(request):

	if request.method == 'POST':
		item = request.POST.get('item')
		address = request.POST.get("address")

		return render(request, 'waimai/home_page.html')
	return render(request, 'waimai/home_page.html')