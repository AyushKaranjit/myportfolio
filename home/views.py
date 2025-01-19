from django.shortcuts import render
from home.models import Education
from .forms import ContactUsForm
# Create your views here.


def home(request):
    myeducations = Education.objects.all()
    contactus_form = ContactUsForm()
    context = {
        'educations': myeducations,
        'contactus_form': contactus_form
    }
    return render(request, 'home.html',context)
