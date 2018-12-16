from django.shortcuts import render
from .models import timePick , timeTest
from .forms import MyTaskForm

# Create your views here.

def index(request):
   dt = timeTest.objects.all()


   return render(request, 'timeSet/index.html', {"dt":dt} )


def bookForm(request):


    if request.method == "POST":
        form = MyTaskForm(request.POST , request.FILES)
        if form.is_valid():

            tt = form.cleaned_data['name']
            tS = form.cleaned_data['holiday_date']
            tS.strftime('%Y-%m-%d')
            tS1 = form.cleaned_data['contact_time']
            tS1.strftime('%Y-%m-%d')

            tts = '%s %s' %(tS, tS1)

            tE = form.cleaned_data['holiday_date']
            tE.strftime('%Y-%m-%d')
            tE1 = form.cleaned_data['contact_time']
            tE1.strftime('%Y-%m-%d')

            tee = '%s %s' %(tE, tE1)

            u = '/'
            cN = 'default'


            timeTest.objects.create(title =tt ,timeStart = tts , timeEnd = tee , url = u , className = cN)


            form.save()
            #post.author = request.user
            #post.published_date = timezone.now()

            return render(request, 'timeSet/index.html', {} )
        else:
            return render(request, 'timeSet/index.html', {} )


    else:


        return render(request, 'timeSet/book.html', {"form":MyTaskForm()} )





