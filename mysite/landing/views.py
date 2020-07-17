from django.shortcuts import render
from .forms import SubscriberForm


# Create your views here.
def landing(request):
    name = "CodingMedved"
    current_day = "03.01.2017"
    form = SubscriberForm(request.POST or None)
    print(form)
    if request.method == "POST" and form.is_valid():
        SubscriberForm.name=request.POST.name
        print("ready")
        return render(request, 'landing/landing.html', locals())
    return render(request, 'landing/landing.html', locals())