from django.shortcuts import get_object_or_404, render
from .models import Tutorial, TutorialSeries,TutorialCategory
from django.http import HttpResponse

from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm


def home(request): 
    context = {'tutorialCategory': TutorialCategory.objects.all()}
    return render(request, 'blog/category.html',context)

def single_slug(request, single_slug):
    categories = [c.category_slug for c in TutorialCategory.objects.all()]   
  
    if single_slug in categories:
 
        matching_series = TutorialSeries.objects.filter(tutorial_category__category_slug=single_slug)
        series_urls = {}
        for tut in matching_series:
            tutorials = Tutorial.objects.filter(tutorial_series__series_slug=tut.series_slug).reverse()            
            for i in tutorials.reverse():                                             
                series_urls[tut] = i.tutorial_slug
                break         
        context = {'series_urls':series_urls}
        return render(request=request, template_name='blog/series.html', context=context)

    tutorials = [t.tutorial_slug for t in Tutorial.objects.all()]
    if single_slug in tutorials:
        this_tutorial = Tutorial.objects.filter(tutorial_slug=single_slug)
        tutorials_series_urls = 0
        
        for i in this_tutorial:
            tutorials_series_urls = Tutorial.objects.filter(tutorial_series__tutorial_series=i.tutorial_series)
        
        tutorial_index = list(tutorials_series_urls).index(this_tutorial[0])
        tutorial_next_slug = 0
        tutorial_back_slug = 0
        try:
            tutorial_next_slug = tutorials_series_urls[tutorial_index+1].tutorial_slug 
        except:
            tutorial_next_slug = "#Done"
        if tutorial_index+1 > 1:
            tutorial_back_slug = tutorials_series_urls[tutorial_index-1].tutorial_slug 

  
 
        context = {'tutorial':this_tutorial,
                   'tutorials_series_urls':tutorials_series_urls,
                   'tutorial_index':tutorial_index,
                   'tutorial_next_slug':tutorial_next_slug,
                   'tutorial_back_slug':tutorial_back_slug,
                   }
        return render(request=request, template_name='blog/tutorials.html',context=context)
    if single_slug == 'contact':
        print(request.method)
        sent = False
        name = ''
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                subject = form.cleaned_data['subject']
                message = form.cleaned_data['message']
                sender = settings.EMAIL_HOST_USER  # replace this with your email address

                from dotenv import dotenv_values
                recipient = []

                try:
                    env_vars = dotenv_values('.env')
                    recipient[0] = env_vars['EMAIL_HOST_USER']
                    send_mail(
                        subject,
                        'message from ' + email + ' ' + message,
                        sender,
                        recipient,
                        fail_silently=True,
                    )
                    sent = True
                    name = email.split('@')[0]
                except:
                        pass

        else:            
            form = ContactForm()
        return render(request, 'blog/contact.html', {'sent':sent,'name':name})
    if single_slug == 'privacy-policy':
        return render(request, 'blog/privacy_policy.html')
    if single_slug == 'about':
        return render(request, 'blog/about.html')
    if single_slug == 'blog':
        return render(request, 'blog/blog.html')

    return HttpResponse('404 not found ')

def tutorial_detail(request):
    return HttpResponse('this is sitemap')


 
         