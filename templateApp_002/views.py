from django.shortcuts import render

# Create your views here.
def simple_temp(request):
    return render(request, 'templateApp_002/simple_temp.html',)

def dynamic_temp(request):
    data = {'Name': 'Shiv', 'Address': 'Kailash Parvat'}
    return render(request, 'templateApp_002/dynamic_temp.html', data)

def show_data(request):
    # show static data like image
    return render(request, 'templateApp_002/show_img.html')
