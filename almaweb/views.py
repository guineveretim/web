from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Article 


def home(request):
  return render(request, 'information/home.html')


def Journal(request):
    articles = Article.objects.all()  # Fetching all articles from the database
    return render(request, 'information/journals.html', {'articles': articles})  # Passing the articles to the template
  
def download_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    response = HttpResponse(article.document, content_type='application/pdf')  # Change content_type if necessary
    response['Content-Disposition'] = f'attachment; filename="{article.document.name}"'
    return response

def Consultancy(request):
  return render(request, 'information/consultancy_unit.html')


def Payment(request):
  return render(request, 'information/home.html')


def About(request):
  return render(request, 'information/about_us.html')


def Agribusiness(request):
  return render(request, 'programs/agri_business.html')



def MBA(request):
  return render(request, 'programs/mba.html')


def CLM(request):
  return render(request, 'programs/clm.html')


def BTLGS(request):
  return render(request, 'programs/btlgs.html')


def ILF(request):
  return render(request, 'programs/ilf.html')




