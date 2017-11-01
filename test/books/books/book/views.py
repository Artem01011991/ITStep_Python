import datetime
from django.core.mail import send_mail, get_connection
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Book
from .forms import ContactForm

# Create your views here.
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
                connection=con
            )

            return HttpResponseRedirect('/contact/thanks/')
    else:
        form =ContactForm(
            initial={'subject':'I love your site!'}
        )

    return render(request, 'contact_form.html', {'form':form})

def search(request):
    errors = []
    if  'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'books/search_results.html',{'books':books,'query':q})
    return render(request, 'books/search_form.html', {'errors':errors, 'search': request.path})