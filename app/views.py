from email.message import EmailMessage
from pyexpat import model
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from account.forms import adminform, artist_Form,  artpost, artsForm, auth_Formuser, authForm, authHertiageFrom, authartFrom, authartscrafts, authcreationFrom, authfestivals, authmediaFrom, contactform, creationpost, dashForm, event_form, festivalForm, heriageForm, mediapost
from account.models import User
from app.models import artist_profile, authUser
from arts.models import art_post
from contact.models import admincontact, publiccontact

from event.models import addevent


# Create your views here.
import threading
from account.models import User
from functional_creation.models import creation_post
from heriage.models import arts_craft_post, heriage_post
from landingpage.models import copy_right, landind_page, logo, operate, quote
from mediaapp.models import media_post
# EmailThread is to speed up the send email
class EmailThread(threading.Thread):
     def __init__(self, email):
         self.email = email
         threading.Thread.__init__(self)
     def run(self):
         self.email.send(fail_silently=False)
from django.contrib.auth import get_user_model
def home(request):
    heriage= User.objects.filter(is_heriages=True).count()
    arts= User.objects.filter(is_arts=True).count()
    media= User.objects.filter(is_media=True).count()
    creation= User.objects.filter(is_creation=True).count()
    event = addevent.objects.filter(is_approved=True).order_by('-create_date')[:3]
    banner = landind_page.objects.all()
    logo_image = logo.objects.all()
    op = operate.objects.all()
    co = copy_right.objects.all()
    qo = quote.objects.all()
    context= {
        'heriage': heriage,
        'arts' : arts,
        'media' : media,
        'creation' : creation,
        'event': event,
        'banner':  banner,
        'logo_image':logo_image,
        'op': op,
        'co' : co,
        'qo' : qo,
        }
    return render(request, 'home.html', context)
  
    

def user_pro(request):
    submitted = False
    if request.method == "POST":
        form = authForm(request.POST, request.FILES)
        if form.is_valid():
            authUser = form.save(commit=False)
            authUser.user = request.user
            authUser.owner = request.user.id
            authUser.save()
            
            return render(request,'home.html')
    else:
        form = authForm
        if 'submitted' in request.GET:
            submitted = True  
    return render(request, 'userpro01.html', {
        'form': form , 'submitted': submitted
        })
   
def reject(request):
    return render(request, 'reject.html')

def approved(request):
    return render(request, 'approved.html')

# def editpro(request):
#     return render(request, 'editpro.html')

def profile(request):
    pro = None
    if artist_profile.objects.filter(user=request.user.id).exists():
        pro = artist_profile.objects.get(user=request.user.id)
    else:
     pro = None
   
    
    return render(request, 'profile.html',{'x': pro})

def artist(request):
    art = artist_profile.objects.all()
    return render(request, 'artisthome.html', {'artist_profile': art})
    

def proupdate(request):
    # instance = None
    # if artist_profile.objects.filter(user=request.user).exists():
    #     instance = artist_profile.objects.get(user=request.user)
    # else:
    #  instance = None
    try:
        instance= artist_profile.objects.get(user=request.user)
    except:
        instance=None
    print(instance)
    if request.method=="POST":
        if instance:
            form=artist_Form(request.POST,instance=instance)
        else:
            form=artist_Form(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=request.user
            obj.save()
            messages.success(request, ("Edit sucessful"))
            return redirect('approved')
    else:
        form=artist_Form(instance=instance)
    context={
        'form':form
    }
    return render(request,'proupdate.html',context)


  
def notapproved(request):
    submitted = False
    if request.method == "POST":
        form = auth_Formuser(request.POST, request.FILES)
        if form.is_valid():
            authUser = form.save(commit=False)
            authUser.user = request.user
            authUser.owner = request.user.id
            form.save()
            return render(request,'notapproved.html')
    else:
        form = auth_Formuser
        if 'submitted' in request.GET:
            submitted = True  
    return render(request, 'notapproved.html', {
        'form': form , 'submitted': submitted
        })

def editpro(request):
    submitted = False
    if request.method == "POST":
        form = artist_Form(request.POST, request.FILES)
        if form.is_valid():
            authUser = form.save(commit=False)
            authUser.user = request.user
            authUser.owner = request.user.id
            form.save()
            return render(request,'editpro.html')
    else:
        form = artist_Form
        if 'submitted' in request.GET:
            submitted = True  
    return render(request, 'editpro.html', {
        'form': form , 'submitted': submitted
        })

# opscan 01

def heriages(request): 
    submitted = False
    if request.method == "POST":
        form = heriageForm(request.POST, request.FILES)
        if form.is_valid():
            authUser = form.save(commit=False)
            authUser.user = request.user
            authUser.owner = request.user.id
            form.save()
            messages.success(request, ("Post Sucessful"))
            return render(request,'approved.html')
    
    else:
        return render(request,'heriages.html')
    
    return render(request, 'heriages.html', {'form': form , 'submitted': submitted })
    
def heritagenotauth(request):
    submitted = False
    if request.method == "POST":
        form = authHertiageFrom(request.POST, request.FILES)
        if form.is_valid():
            authHeritage = form.save(commit=False)
            authHeritage.user = request.user
            authHeritage.owner = request.user.id
            form.save()
            return render(request,'heritagenotauth.html')
    else:
        form = authHertiageFrom
        if 'submitted' in request.GET:
            submitted = True  
    return render(request, 'heritagenotauth.html', {
        'form': form , 'submitted': submitted
        })

def arts(request):
    submitted = False
    if request.method == "POST":
        form = artpost(request.POST, request.FILES)
        if form.is_valid():
            art_post = form.save(commit=False)
            art_post.user = request.user
            art_post.owner = request.user.id
            form.save()
            messages.success(request, ("Post Sucessful"))
            return render(request,'arts.html')
    
    else:
        return render(request,'arts.html')
    
    return render(request, 'arts.html', {'form': form , 'submitted': submitted })
    
   
def artauth(request):
    submitted = False
    if request.method == "POST":
        form = authartFrom(request.POST, request.FILES)
        if form.is_valid():
            authart = form.save(commit=False)
            authart.user = request.user
            authart.owner = request.user.id
            form.save()
            messages.success(request, ("Post Sucessful"))
            return render(request,'artauth.html')
    
    else:
        return render(request,'artauth.html')
    
    return render(request, 'artauth.html', {'form': form , 'submitted': submitted })



def media(request):
    submitted = False
    if request.method == "POST":
        form = mediapost(request.POST, request.FILES)
        if form.is_valid():
            media_post = form.save(commit=False)
            media_post.user = request.user
            media_post.owner = request.user.id
            form.save()
            messages.success(request, ("Post Sucessful"))
            return render(request,'media.html')
    
    else:
        return render(request,'media.html')
    
    return render(request, 'media.html', {'form': form , 'submitted': submitted })
    
def authme(request):
    submitted = False
    if request.method == "POST":
        form = authmediaFrom(request.POST, request.FILES)
        if form.is_valid():
            auth_media = form.save(commit=False)
            auth_media.user = request.user
            auth_media.owner = request.user.id
            form.save()
            messages.success(request, ("Post Sucessful"))
            return render(request,'authmedia.html')
    
    else:
        return render(request,'authmedia.html')
    
    return render(request, 'authmedia.html', {'form': form , 'submitted': submitted })

def creation(request):
    submitted = False
    if request.method == "POST":
        form = creationpost(request.POST, request.FILES)
        if form.is_valid():
            creation_post = form.save(commit=False)
            creation_post.user = request.user
            creation_post.owner = request.user.id
            form.save()
            messages.success(request, ("Post Sucessful"))
            return render(request,'functional_creation.html')
    
    else:
        return render(request,'functional_creation.html')
    
    return render(request, 'functional_creation.html', {'form': form , 'submitted': submitted })
    
def creationauth(request):
    submitted = False
    if request.method == "POST":
        form = authcreationFrom(request.POST, request.FILES)
        if form.is_valid():
            auth_creation = form.save(commit=False)
            auth_creation.user = request.user
            auth_creation.owner = request.user.id
            form.save()
            messages.success(request, ("Post Sucessful"))
            return render(request,'creationauth.html')
    
    else:
        return render(request,'creationauth.html')
    
    return render(request, 'creationauth.html', {'form': form , 'submitted': submitted })
     



# Create your views here.
def event(request):
    submitted = False
    if request.method == "POST":
        form = event_form(request.POST, request.FILES)
        if form.is_valid():
            auth_creation = form.save(commit=False)
            auth_creation.user = request.user
            auth_creation.owner = request.user.id
            auth_creation.save()
            messages.success(request, ("event Sucessful"))
            print("pass")
            return render(request,'event.html')
             
    else:
        print("fail")
        return render(request,'event.html')
    
    return render(request, 'event.html', {'form': form , 'submitted': submitted })
     
def eventupdate(request):
    try:
        instance= event.objects.get(user=request.user)
    except:
        instance=None
    print(instance)
    if request.method=="POST":
        if instance:
            form=event_form(request.POST,instance=instance)
        else:
            form=event_form(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=request.user
            obj.save()
            messages.success(request, ("Edit sucessful"))
            return redirect('approved')
    else:
        form=event_form(instance=instance)
    context={
        'form':form
    }
    return render(request,'eventupdate.html',context)


def showevent(request):
    event = addevent.objects.all().order_by('-create_date')
    return render(request, 'showevent.html', {'event': event})

def eventdetil(request, pk):
    event_list = addevent.objects.get(id=pk)
    return render(request, 'eventdetil.html',{'event_list': event_list})
from datetime import datetime

def contact_view(request, pk):
    eachProduct = addevent.objects.get(id=pk)

    form = contactform(instance=eachProduct)

    if request.method == 'POST':
        form = contactform(request.POST, instance=eachProduct)
        if form.is_valid():
            mail= form.cleaned_data['email']
            name = form.cleaned_data['first_name']
            last = form.cleaned_data['last_name']
            number = form.cleaned_data['phone']
            dis = form.cleaned_data['discription']
            c = publiccontact(event=eachProduct, email=mail, first_name=name, last_name =last, phone= number, discription=dis, submit_date=datetime.now())
            c.save()
            messages.success(request, ("Register Sucessful"))
            return redirect('home')
        else:
            print('form is invalid')    
    else:
        form = publiccontact()    


    context = {
        'form': form
    }

    return render(request, 'contact.html', context)



def aboutus(request):
    return render(request, 'aboutus.html')
    
def contactadmin(request):
    form = adminform()
    if request.method == 'POST':
        form = adminform(request.POST)
        if form.is_valid():
            mail= form.cleaned_data['email']
            name = form.cleaned_data['name']
            number = form.cleaned_data['phone']
            dis = form.cleaned_data['discription']
            c = admincontact( email=mail, name=name,  phone= number, discription=dis, submit_date=datetime.now())
            c.save()
            messages.success(request, ("Register Sucessful"))
            return redirect('home')
        else:
            print('form is invalid')    
    else:
        form = adminform()    


    context = {
        'form': form
    }

    return render(request, 'contactadmin.html', context)


def  industries(request):
    heriage= heriage_post.objects.all().order_by('-create_date')
    arts = art_post.objects.all()
    media= media_post.objects.all()
    creation= creation_post.objects.all()
    heriage_top = heriage_post.objects.filter().order_by('-create_date')[:1]
    context= {
        'heriage_top': heriage_top,
        'heriage': heriage,
        'arts' : arts,
        'media' : media,
        'creation' : creation,
        }
    return render(request, 'industry.html', context)

def artstype(request):
    heriage= User.objects.filter(is_heriages=True).count()
    arts= User.objects.filter(is_arts=True).count()
    media= User.objects.filter(is_media=True).count()
    creation= User.objects.filter(is_creation=True).count()
    logo_image = logo.objects.all()
    op = operate.objects.all()
    co = copy_right.objects.all()
    context= {
        'heriage': heriage,
        'arts' : arts,
        'media' : media,
        'creation' : creation,
        'logo_image': logo_image,
        'op': op,
        'co': co,
        }
    return render(request, 'artstype.html', context)

from django.core.paginator import Paginator
def artc(request):
    # event_list = arts_craft_post.objects.get(id=pk)
    artpost = arts_craft_post.objects.all()
    paginator = Paginator(artpost, per_page=8)
    page_object = request.GET.get('page')
    service = paginator.get_page(page_object)
    totalpage = service.paginator.num_pages
    
    context = {
        'service': service,
        'lastpage': totalpage,
        'totalpagelist':[n+1 for n in range(totalpage)],
        
    }
    return render(request, 'industry/heri/artc.html' , context)

def festival(request):

    return render(request, 'industry/heri/festival.html')
def cel(request):

    return render(request, 'industry/heri/cel.html')

def histo(request):

    return render(request, 'industry/heri/histo.html')

def muse(request):

    return render(request, 'industry/heri/muse.html')

def labri(request):

    return render(request, 'industry/heri/labri.html')

def achi(request):

    return render(request, 'industry/heri/achi.html')

def paint(request):

    return render(request, 'industry/art/paint.html')

def digi(request):

    return render(request, 'industry/art/digi.html')

def photo(request):

    return render(request, 'industry/art/photo.html')

def scul(request):

    return render(request, 'industry/art/scul.html')
def pott(request):

    return render(request, 'industry/art/pott.html')

def liv(request):

    return render(request, 'industry/art/liv.html')

def thea(request):

    return render(request, 'industry/art/thea.html')

def dan(request):

    return render(request, 'industry/art/dan.html')

def ope(request):

    return render(request, 'industry/art/ope.html')

def pup(request):

    return render(request, 'industry/art/pup.html')


def book(request):

    return render(request, 'industry/med/book.html')


def maga(request):

    return render(request, 'industry/med/maga.html')

def com(request):

    return render(request, 'industry/med/com.html')

def fil(request):

    return render(request, 'industry/med/fil.html')

def tele(request):

    return render(request, 'industry/med/tele.html')
def rad(request):

    return render(request, 'industry/med/rad.html')

def musv(request):

    return render(request, 'industry/med/musv.html')

def digicon(request):

    return render(request, 'industry/med/digicon.html')

def soft(request):

    return render(request, 'industry/med/soft.html')

def videogame(request):

    return render(request, 'industry/med/videogame.html')

def anima(request):

    return render(request, 'industry/med/anima.html')

def fas(request):

    return render(request, 'industry/fu/fas.html')

def jewe(request):

    return render(request, 'industry/fu/jewe.html')

def toy(request):

    return render(request, 'industry/fu/toy.html')

def inte(request):

    return render(request, 'industry/fu/inte.html')

def graph(request):

    return render(request, 'industry/fu/graph.html')


def arch(request):

    return render(request, 'industry/fu/arch.html')

def adver(request):

    return render(request, 'industry/fu/adver.html')

def creative(request):

    return render(request, 'industry/fu/creative.html')

def ser(request):

    return render(request, 'industry/fu/ser.html')

def digicreative(request):

    return render(request, 'industry/fu/digicreative.html')


# arts carfts
def artspost(request): 
    submitted = False
    if request.method == "POST":
        form = artsForm(request.POST, request.FILES)
        if form.is_valid():
            authUser = form.save(commit=False)
            authUser.user = request.user
            authUser.owner = request.user.id
            form.save()
            messages.success(request, ("Post Sucessful"))
            return render(request,'approved.html')
    
    else:
        return render(request,'industrytype/heritype/tra/artsdashboard.html')
    
    return render(request, 'artsdashboard.html', {'form': form , 'submitted': submitted })
    
def artsauth(request):
    submitted = False
    if request.method == "POST":
        form = authartscrafts(request.POST, request.FILES)
        if form.is_valid():
            authHeritage = form.save(commit=False)
            authHeritage.user = request.user
            authHeritage.owner = request.user.id
            form.save()
            return render(request,'industrytype/heritype/tra/artsauth.html')
    else:
        form = authartscrafts
        if 'submitted' in request.GET:
            submitted = True  
    return render(request, 'industrytype/heritype/tra/artsauth.html', {
        'form': form , 'submitted': submitted
        })

# festival

def festivalpost(request): 
    submitted = False
    if request.method == "POST":
        form = festivalForm(request.POST, request.FILES)
        if form.is_valid():
            authUser = form.save(commit=False)
            authUser.user = request.user
            authUser.owner = request.user.id
            form.save()
            messages.success(request, ("Post Sucessful"))
            return render(request,'approved.html')
    
    else:
        return render(request,'industrytype/heritype/tra/festivaldashboard.html')
    
    return render(request, 'festivaldashboard.html', {'form': form , 'submitted': submitted })
    
def festivalauth(request):
    submitted = False
    if request.method == "POST":
        form = authfestivals(request.POST, request.FILES)
        if form.is_valid():
            authHeritage = form.save(commit=False)
            authHeritage.user = request.user
            authHeritage.owner = request.user.id
            form.save()
            return render(request,'industrytype/heritype/tra/festivalauth.html')
    else:
        form = authfestivals
        if 'submitted' in request.GET:
            submitted = True  
    return render(request, 'industrytype/heritype/tra/festivalauth.html', {
        'form': form , 'submitted': submitted
        })

# celebrations 

def celepost(request): 
    submitted = False
    if request.method == "POST":
        form = dashForm(request.POST, request.FILES)
        if form.is_valid():
            authUser = form.save(commit=False)
            authUser.user = request.user
            authUser.owner = request.user.id
            form.save()
            messages.success(request, ("Post Sucessful"))
            return render(request,'approved.html')
    
    else:
        return render(request,'industrytype/heritype/tra/celedashboard.html')
    
    return render(request, 'celedashboard.html', {'form': form , 'submitted': submitted })
    
def celeauth(request):
    submitted = False
    if request.method == "POST":
        form = authForm(request.POST, request.FILES)
        if form.is_valid():
            authHeritage = form.save(commit=False)
            authHeritage.user = request.user
            authHeritage.owner = request.user.id
            form.save()
            return render(request,'industrytype/heritype/tra/celeauth.html')
    else:
        form = authForm
        if 'submitted' in request.GET:
            submitted = True  
    return render(request, 'industrytype/heritype/tra/celeauth.html', {
        'form': form , 'submitted': submitted
        })

# historical

def histopost(request): 
    submitted = False
    if request.method == "POST":
        form = dashForm(request.POST, request.FILES)
        if form.is_valid():
            authUser = form.save(commit=False)
            authUser.user = request.user
            authUser.owner = request.user.id
            form.save()
            messages.success(request, ("Post Sucessful"))
            return render(request,'approved.html')
    
    else:
        return render(request,'industrytype/heritype/tra/histodashboard.html')
    
    return render(request, 'celedashboard.html', {'form': form , 'submitted': submitted })
    
def histoauth(request):
    submitted = False
    if request.method == "POST":
        form = authForm(request.POST, request.FILES)
        if form.is_valid():
            authHeritage = form.save(commit=False)
            authHeritage.user = request.user
            authHeritage.owner = request.user.id
            form.save()
            return render(request,'industrytype/heritype/tra/histoauth.html')
    else:
        form = authForm
        if 'submitted' in request.GET:
            submitted = True  
    return render(request, 'industrytype/heritype/tra/celeauth.html', {
        'form': form , 'submitted': submitted
        })

# museum

def muspost(request): 
    submitted = False
    if request.method == "POST":
        form = dashForm(request.POST, request.FILES)
        if form.is_valid():
            authUser = form.save(commit=False)
            authUser.user = request.user
            authUser.owner = request.user.id
            form.save()
            messages.success(request, ("Post Sucessful"))
            return render(request,'approved.html')
    
    else:
        return render(request,'industrytype/heritype/tra/musdashboard.html')
    
    return render(request, 'musdashboard.html', {'form': form , 'submitted': submitted })
    
def musauth(request):
    submitted = False
    if request.method == "POST":
        form = authForm(request.POST, request.FILES)
        if form.is_valid():
            authHeritage = form.save(commit=False)
            authHeritage.user = request.user
            authHeritage.owner = request.user.id
            form.save()
            return render(request,'industrytype/heritype/tra/musauth.html')
    else:
        form = authForm
        if 'submitted' in request.GET:
            submitted = True  
    return render(request, 'industrytype/heritype/tra/musauth.html', {
        'form': form , 'submitted': submitted
        })

# labraries

def labpost(request): 
    submitted = False
    if request.method == "POST":
        form = dashForm(request.POST, request.FILES)
        if form.is_valid():
            authUser = form.save(commit=False)
            authUser.user = request.user
            authUser.owner = request.user.id
            form.save()
            messages.success(request, ("Post Sucessful"))
            return render(request,'approved.html')
    
    else:
        return render(request,'industrytype/heritype/tra/labdashboard.html')
    
    return render(request, 'labdashboard.html', {'form': form , 'submitted': submitted })
    
def labauth(request):
    submitted = False
    if request.method == "POST":
        form = authForm(request.POST, request.FILES)
        if form.is_valid():
            authHeritage = form.save(commit=False)
            authHeritage.user = request.user
            authHeritage.owner = request.user.id
            form.save()
            return render(request,'industrytype/heritype/tra/labauth.html')
    else:
        form = authForm
        if 'submitted' in request.GET:
            submitted = True  
    return render(request, 'industrytype/heritype/tra/labauth.html', {
        'form': form , 'submitted': submitted
        })

# archies


def archpost(request): 
    submitted = False
    if request.method == "POST":
        form = dashForm(request.POST, request.FILES)
        if form.is_valid():
            authUser = form.save(commit=False)
            authUser.user = request.user
            authUser.owner = request.user.id
            form.save()
            messages.success(request, ("Post Sucessful"))
            return render(request,'approved.html')
    
    else:
        return render(request,'industrytype/heritype/tra/archdashboard.html')
    
    return render(request, 'archdashboard.html', {'form': form , 'submitted': submitted })
    
def archauth(request):
    submitted = False
    if request.method == "POST":
        form = authForm(request.POST, request.FILES)
        if form.is_valid():
            authHeritage = form.save(commit=False)
            authHeritage.user = request.user
            authHeritage.owner = request.user.id
            form.save()
            return render(request,'industrytype/heritype/tra/archauth.html')
    else:
        form = authForm
        if 'submitted' in request.GET:
            submitted = True  
    return render(request, 'industrytype/heritype/tra/archauth.html', {
        'form': form , 'submitted': submitted
        })

# arts types

# painting


def paintpost(request): 
    submitted = False
    if request.method == "POST":
        form = dashForm(request.POST, request.FILES)
        if form.is_valid():
            authUser = form.save(commit=False)
            authUser.user = request.user
            authUser.owner = request.user.id
            form.save()
            messages.success(request, ("Post Sucessful"))
            return render(request,'approved.html')
    
    else:
        return render(request,'industrytype/arttype/varts/paintdashboard.html')
    
    return render(request, 'paintdashboard.html', {'form': form , 'submitted': submitted })
    
def paintauth(request):
    submitted = False
    if request.method == "POST":
        form = authForm(request.POST, request.FILES)
        if form.is_valid():
            authHeritage = form.save(commit=False)
            authHeritage.user = request.user
            authHeritage.owner = request.user.id
            form.save()
            return render(request,'industrytype/arttype/varts/paintauth.html')
    else:
        form = authForm
        if 'submitted' in request.GET:
            submitted = True  
    return render(request, 'industrytype/arttype/varts/paintauth.html', {
        'form': form , 'submitted': submitted
        })

# digital arts


def digitalpost(request): 
    submitted = False
    if request.method == "POST":
        form = dashForm(request.POST, request.FILES)
        if form.is_valid():
            authUser = form.save(commit=False)
            authUser.user = request.user
            authUser.owner = request.user.id
            form.save()
            messages.success(request, ("Post Sucessful"))
            return render(request,'approved.html')
    
    else:
        return render(request,'industrytype/arttype/varts/digitaldashboard.html')
    
    return render(request, 'digitaldashboard.html', {'form': form , 'submitted': submitted })
    
def digitalauth(request):
    submitted = False
    if request.method == "POST":
        form = authForm(request.POST, request.FILES)
        if form.is_valid():
            authHeritage = form.save(commit=False)
            authHeritage.user = request.user
            authHeritage.owner = request.user.id
            form.save()
            return render(request,'industrytype/arttype/varts/digitalauth.html')
    else:
        form = authForm
        if 'submitted' in request.GET:
            submitted = True  
    return render(request, 'industrytype/arttype/varts/digitalauth.html', {
        'form': form , 'submitted': submitted
        })

# photography

def photopost(request): 
    submitted = False
    if request.method == "POST":
        form = dashForm(request.POST, request.FILES)
        if form.is_valid():
            authUser = form.save(commit=False)
            authUser.user = request.user
            authUser.owner = request.user.id
            form.save()
            messages.success(request, ("Post Sucessful"))
            return render(request,'approved.html')
    
    else:
        return render(request,'industrytype/arttype/varts/photodashboard.html')
    
    return render(request, 'digitaldashboard.html', {'form': form , 'submitted': submitted })
    
def photoauth(request):
    submitted = False
    if request.method == "POST":
        form = authForm(request.POST, request.FILES)
        if form.is_valid():
            authHeritage = form.save(commit=False)
            authHeritage.user = request.user
            authHeritage.owner = request.user.id
            form.save()
            return render(request,'industrytype/arttype/varts/photoauth.html')
    else:
        form = authForm
        if 'submitted' in request.GET:
            submitted = True  
    return render(request, 'industrytype/arttype/varts/digitalauth.html', {
        'form': form , 'submitted': submitted
        })

# scul


def sculpost(request): 
    submitted = False
    if request.method == "POST":
        form = dashForm(request.POST, request.FILES)
        if form.is_valid():
            authUser = form.save(commit=False)
            authUser.user = request.user
            authUser.owner = request.user.id
            form.save()
            messages.success(request, ("Post Sucessful"))
            return render(request,'approved.html')
    
    else:
        return render(request,'industrytype/arttype/varts/sculdashboard.html')
    
    return render(request, 'sculdashboard.html', {'form': form , 'submitted': submitted })
    
def sculauth(request):
    submitted = False
    if request.method == "POST":
        form = authForm(request.POST, request.FILES)
        if form.is_valid():
            authHeritage = form.save(commit=False)
            authHeritage.user = request.user
            authHeritage.owner = request.user.id
            form.save()
            return render(request,'industrytype/arttype/varts/sculauth.html')
    else:
        form = authForm
        if 'submitted' in request.GET:
            submitted = True  
    return render(request, 'industrytype/arttype/varts/sculauth.html', {
        'form': form , 'submitted': submitted
        })

#  pottery

def potpost(request): 
    submitted = False
    if request.method == "POST":
        form = dashForm(request.POST, request.FILES)
        if form.is_valid():
            authUser = form.save(commit=False)
            authUser.user = request.user
            authUser.owner = request.user.id
            form.save()
            messages.success(request, ("Post Sucessful"))
            return render(request,'approved.html')
    
    else:
        return render(request,'industrytype/arttype/varts/potdashboard.html')
    
    return render(request, 'potdashboard.html', {'form': form , 'submitted': submitted })
    
def potauths(request):
    submitted = False
    if request.method == "POST":
        form = authForm(request.POST, request.FILES)
        if form.is_valid():
            authHeritage = form.save(commit=False)
            authHeritage.user = request.user
            authHeritage.owner = request.user.id
            form.save()
            return render(request,'industrytype/arttype/varts/potauth.html')
    else:
        form = authForm
        if 'submitted' in request.GET:
            submitted = True  
    return render(request, 'industrytype/arttype/varts/potauth.html', {
        'form': form , 'submitted': submitted
        })
# live video


def livepost(request): 
    submitted = False
    if request.method == "POST":
        form = dashForm(request.POST, request.FILES)
        if form.is_valid():
            authUser = form.save(commit=False)
            authUser.user = request.user
            authUser.owner = request.user.id
            form.save()
            messages.success(request, ("Post Sucessful"))
            return render(request,'approved.html')
    
    else:
        return render(request,'industrytype/arttype/parts/livedashboard.html')
    
    return render(request, 'livedashboard.html', {'form': form , 'submitted': submitted })
    
def liveauth(request):
    submitted = False
    if request.method == "POST":
        form = authForm(request.POST, request.FILES)
        if form.is_valid():
            authHeritage = form.save(commit=False)
            authHeritage.user = request.user
            authHeritage.owner = request.user.id
            form.save()
            return render(request,'industrytype/arttype/parts/liveauth.html')
    else:
        form = authForm
        if 'submitted' in request.GET:
            submitted = True  
    return render(request, 'industrytype/arttype/parts/liveauth.html', {
        'form': form , 'submitted': submitted
        })

# theater


def thepost(request): 
    submitted = False
    if request.method == "POST":
        form = dashForm(request.POST, request.FILES)
        if form.is_valid():
            authUser = form.save(commit=False)
            authUser.user = request.user
            authUser.owner = request.user.id
            form.save()
            messages.success(request, ("Post Sucessful"))
            return render(request,'approved.html')
    
    else:
        return render(request,'industrytype/arttype/parts/thedashboard.html')
    
    return render(request, 'thedashboard.html', {'form': form , 'submitted': submitted })
    
def theauth(request):
    submitted = False
    if request.method == "POST":
        form = authForm(request.POST, request.FILES)
        if form.is_valid():
            authHeritage = form.save(commit=False)
            authHeritage.user = request.user
            authHeritage.owner = request.user.id
            form.save()
            return render(request,'industrytype/arttype/parts/theauth.html')
    else:
        form = authForm
        if 'submitted' in request.GET:
            submitted = True  
    return render(request, 'industrytype/arttype/parts/theauth.html', {
        'form': form , 'submitted': submitted
        })

# dance

def dancepost(request): 
    submitted = False
    if request.method == "POST":
        form = dashForm(request.POST, request.FILES)
        if form.is_valid():
            authUser = form.save(commit=False)
            authUser.user = request.user
            authUser.owner = request.user.id
            form.save()
            messages.success(request, ("Post Sucessful"))
            return render(request,'approved.html')
    
    else:
        return render(request,'industrytype/arttype/parts/dancedashboard.html')
    
    return render(request, 'dancedashboard.html', {'form': form , 'submitted': submitted })
    
def danceauth(request):
    submitted = False
    if request.method == "POST":
        form = authForm(request.POST, request.FILES)
        if form.is_valid():
            authHeritage = form.save(commit=False)
            authHeritage.user = request.user
            authHeritage.owner = request.user.id
            form.save()
            return render(request,'industrytype/arttype/parts/danceauth.html')
    else:
        form = authForm
        if 'submitted' in request.GET:
            submitted = True  
    return render(request, 'industrytype/arttype/parts/danceauth.html', {
        'form': form , 'submitted': submitted
        })

# opera


def oppost(request): 
    submitted = False
    if request.method == "POST":
        form = dashForm(request.POST, request.FILES)
        if form.is_valid():
            authUser = form.save(commit=False)
            authUser.user = request.user
            authUser.owner = request.user.id
            form.save()
            messages.success(request, ("Post Sucessful"))
            return render(request,'approved.html')
    
    else:
        return render(request,'industrytype/arttype/parts/opdashboard.html')
    
    return render(request, 'opdashboard.html', {'form': form , 'submitted': submitted })
    
def opauth(request):
    submitted = False
    if request.method == "POST":
        form = authForm(request.POST, request.FILES)
        if form.is_valid():
            authHeritage = form.save(commit=False)
            authHeritage.user = request.user
            authHeritage.owner = request.user.id
            form.save()
            return render(request,'industrytype/arttype/parts/opauth.html')
    else:
        form = authForm
        if 'submitted' in request.GET:
            submitted = True  
    return render(request, 'industrytype/arttype/parts/opauth.html', {
        'form': form , 'submitted': submitted
        })

# pup


def puppost(request): 
    submitted = False
    if request.method == "POST":
        form = dashForm(request.POST, request.FILES)
        if form.is_valid():
            authUser = form.save(commit=False)
            authUser.user = request.user
            authUser.owner = request.user.id
            form.save()
            messages.success(request, ("Post Sucessful"))
            return render(request,'approved.html')
    
    else:
        return render(request,'industrytype/arttype/parts/pupdashboard.html')
    
    return render(request, 'pupdashboard.html', {'form': form , 'submitted': submitted })
    
def pupauth(request):
    submitted = False
    if request.method == "POST":
        form = authForm(request.POST, request.FILES)
        if form.is_valid():
            authHeritage = form.save(commit=False)
            authHeritage.user = request.user
            authHeritage.owner = request.user.id
            form.save()
            return render(request,'industrytype/arttype/parts/pupauth.html')
    else:
        form = authForm
        if 'submitted' in request.GET:
            submitted = True  
    return render(request, 'industrytype/arttype/parts/pupauth.html', {
        'form': form , 'submitted': submitted
        })


# bookes(media)

# pup


def bookpost(request): 
    submitted = False
    if request.method == "POST":
        form = dashForm(request.POST, request.FILES)
        if form.is_valid():
            authUser = form.save(commit=False)
            authUser.user = request.user
            authUser.owner = request.user.id
            form.save()
            messages.success(request, ("Post Sucessful"))
            return render(request,'approved.html')
    
    else:
        return render(request,'industrytype/arttype/med/bookdashboard.html')
    
    return render(request, 'bookdashboard.html', {'form': form , 'submitted': submitted })
    
def bookauth(request):
    submitted = False
    if request.method == "POST":
        form = authForm(request.POST, request.FILES)
        if form.is_valid():
            authHeritage = form.save(commit=False)
            authHeritage.user = request.user
            authHeritage.owner = request.user.id
            form.save()
            return render(request,'industrytype/arttype/med/bookauth.html')
    else:
        form = authForm
        if 'submitted' in request.GET:
            submitted = True  
    return render(request, 'industrytype/arttype/med/bookauth.html', {
        'form': form , 'submitted': submitted
        })

# maga
def magapost(request): 
    submitted = False
    if request.method == "POST":
        form = dashForm(request.POST, request.FILES)
        if form.is_valid():
            authUser = form.save(commit=False)
            authUser.user = request.user
            authUser.owner = request.user.id
            form.save()
            messages.success(request, ("Post Sucessful"))
            return render(request,'approved.html')
    
    else:
        return render(request,'industrytype/arttype/med/magadashboard.html')
    
    return render(request, 'magadashboard.html', {'form': form , 'submitted': submitted })
    
def magaauth(request):
    submitted = False
    if request.method == "POST":
        form = authForm(request.POST, request.FILES)
        if form.is_valid():
            authHeritage = form.save(commit=False)
            authHeritage.user = request.user
            authHeritage.owner = request.user.id
            form.save()
            return render(request,'industrytype/arttype/med/magaauth.html')
    else:
        form = authForm
        if 'submitted' in request.GET:
            submitted = True  
    return render(request, 'industrytype/arttype/med/magaauth.html', {
        'form': form , 'submitted': submitted
        })

# co
def compost(request): 
    submitted = False
    if request.method == "POST":
        form = dashForm(request.POST, request.FILES)
        if form.is_valid():
            authUser = form.save(commit=False)
            authUser.user = request.user
            authUser.owner = request.user.id
            form.save()
            messages.success(request, ("Post Sucessful"))
            return render(request,'approved.html')
    
    else:
        return render(request,'industrytype/arttype/med/comdashboard.html')
    
    return render(request, 'comdashboard.html', {'form': form , 'submitted': submitted })
    
def comauth(request):
    submitted = False
    if request.method == "POST":
        form = authForm(request.POST, request.FILES)
        if form.is_valid():
            authHeritage = form.save(commit=False)
            authHeritage.user = request.user
            authHeritage.owner = request.user.id
            form.save()
            return render(request,'industrytype/arttype/med/comauth.html')
    else:
        form = authForm
        if 'submitted' in request.GET:
            submitted = True  
    return render(request, 'industrytype/arttype/med/comauth.html', {
        'form': form , 'submitted': submitted
        })


# fil
def filpost(request): 
    submitted = False
    if request.method == "POST":
        form = dashForm(request.POST, request.FILES)
        if form.is_valid():
            authUser = form.save(commit=False)
            authUser.user = request.user
            authUser.owner = request.user.id
            form.save()
            messages.success(request, ("Post Sucessful"))
            return render(request,'approved.html')
    
    else:
        return render(request,'industrytype/arttype/med/fildashboard.html')
    
    return render(request, 'fildashboard.html', {'form': form , 'submitted': submitted })
    
def filauth(request):
    submitted = False
    if request.method == "POST":
        form = authForm(request.POST, request.FILES)
        if form.is_valid():
            authHeritage = form.save(commit=False)
            authHeritage.user = request.user
            authHeritage.owner = request.user.id
            form.save()
            return render(request,'industrytype/arttype/med/filauth.html')
    else:
        form = authForm
        if 'submitted' in request.GET:
            submitted = True  
    return render(request, 'industrytype/arttype/med/filauth.html', {
        'form': form , 'submitted': submitted
        })


# Tele
def telepost(request): 
    submitted = False
    if request.method == "POST":
        form = dashForm(request.POST, request.FILES)
        if form.is_valid():
            authUser = form.save(commit=False)
            authUser.user = request.user
            authUser.owner = request.user.id
            form.save()
            messages.success(request, ("Post Sucessful"))
            return render(request,'approved.html')
    
    else:
        return render(request,'industrytype/arttype/med/teledashboard.html')
    
    return render(request, 'teledashboard.html', {'form': form , 'submitted': submitted })
    
def teleauth(request):
    submitted = False
    if request.method == "POST":
        form = authForm(request.POST, request.FILES)
        if form.is_valid():
            authHeritage = form.save(commit=False)
            authHeritage.user = request.user
            authHeritage.owner = request.user.id
            form.save()
            return render(request,'industrytype/arttype/med/teleauth.html')
    else:
        form = authForm
        if 'submitted' in request.GET:
            submitted = True  
    return render(request, 'industrytype/arttype/med/teleauth.html', {
        'form': form , 'submitted': submitted
        })


# rad
def radpost(request): 
    submitted = False
    if request.method == "POST":
        form = dashForm(request.POST, request.FILES)
        if form.is_valid():
            authUser = form.save(commit=False)
            authUser.user = request.user
            authUser.owner = request.user.id
            form.save()
            messages.success(request, ("Post Sucessful"))
            return render(request,'approved.html')
    
    else:
        return render(request,'industrytype/arttype/med/raddashboard.html')
    
    return render(request, 'raddashboard.html', {'form': form , 'submitted': submitted })
    
def radauth(request):
    submitted = False
    if request.method == "POST":
        form = authForm(request.POST, request.FILES)
        if form.is_valid():
            authHeritage = form.save(commit=False)
            authHeritage.user = request.user
            authHeritage.owner = request.user.id
            form.save()
            return render(request,'industrytype/arttype/med/radauth.html')
    else:
        form = authForm
        if 'submitted' in request.GET:
            submitted = True  
    return render(request, 'industrytype/arttype/med/radauth.html', {
        'form': form , 'submitted': submitted
        })


# music video
def mvpost(request): 
    submitted = False
    if request.method == "POST":
        form = dashForm(request.POST, request.FILES)
        if form.is_valid():
            authUser = form.save(commit=False)
            authUser.user = request.user
            authUser.owner = request.user.id
            form.save()
            messages.success(request, ("Post Sucessful"))
            return render(request,'approved.html')
    
    else:
        return render(request,'industrytype/arttype/med/mvdashboard.html')
    
    return render(request, 'mvdashboard.html', {'form': form , 'submitted': submitted })
    
def mvauth(request):
    submitted = False
    if request.method == "POST":
        form = authForm(request.POST, request.FILES)
        if form.is_valid():
            authHeritage = form.save(commit=False)
            authHeritage.user = request.user
            authHeritage.owner = request.user.id
            form.save()
            return render(request,'industrytype/arttype/med/mvauth.html')
    else:
        form = authForm
        if 'submitted' in request.GET:
            submitted = True  
    return render(request, 'industrytype/arttype/med/mvauth.html', {
        'form': form , 'submitted': submitted
        })


# music video
def dcpost(request): 
    submitted = False
    if request.method == "POST":
        form = dashForm(request.POST, request.FILES)
        if form.is_valid():
            authUser = form.save(commit=False)
            authUser.user = request.user
            authUser.owner = request.user.id
            form.save()
            messages.success(request, ("Post Sucessful"))
            return render(request,'approved.html')
    
    else:
        return render(request,'industrytype/arttype/med/dcdashboard.html')
    
    return render(request, 'mvdashboard.html', {'form': form , 'submitted': submitted })
    
def dcauth(request):
    submitted = False
    if request.method == "POST":
        form = authForm(request.POST, request.FILES)
        if form.is_valid():
            authHeritage = form.save(commit=False)
            authHeritage.user = request.user
            authHeritage.owner = request.user.id
            form.save()
            return render(request,'industrytype/arttype/med/dcauth.html')
    else:
        form = authForm
        if 'submitted' in request.GET:
            submitted = True  
    return render(request, 'industrytype/arttype/med/dcauth.html', {
        'form': form , 'submitted': submitted
        })

# software
def softpost(request): 
    submitted = False
    if request.method == "POST":
        form = dashForm(request.POST, request.FILES)
        if form.is_valid():
            authUser = form.save(commit=False)
            authUser.user = request.user
            authUser.owner = request.user.id
            form.save()
            messages.success(request, ("Post Sucessful"))
            return render(request,'approved.html')
    
    else:
        return render(request,'industrytype/arttype/med/softdashboard.html')
    
    return render(request, 'softdashboard.html', {'form': form , 'submitted': submitted })
    
def softauth(request):
    submitted = False
    if request.method == "POST":
        form = authForm(request.POST, request.FILES)
        if form.is_valid():
            authHeritage = form.save(commit=False)
            authHeritage.user = request.user
            authHeritage.owner = request.user.id
            form.save()
            return render(request,'industrytype/arttype/med/softauth.html')
    else:
        form = authForm
        if 'submitted' in request.GET:
            submitted = True  
    return render(request, 'industrytype/arttype/med/softauth.html', {
        'form': form , 'submitted': submitted
        })

# video game
def vgpost(request): 
    submitted = False
    if request.method == "POST":
        form = dashForm(request.POST, request.FILES)
        if form.is_valid():
            authUser = form.save(commit=False)
            authUser.user = request.user
            authUser.owner = request.user.id
            form.save()
            messages.success(request, ("Post Sucessful"))
            return render(request,'approved.html')
    
    else:
        return render(request,'industrytype/arttype/med/vgdashboard.html')
    
    return render(request, 'vgdashboard.html', {'form': form , 'submitted': submitted })
    
def vgauths(request):
    submitted = False
    if request.method == "POST":
        form = authForm(request.POST, request.FILES)
        if form.is_valid():
            authHeritage = form.save(commit=False)
            authHeritage.user = request.user
            authHeritage.owner = request.user.id
            form.save()
            return render(request,'industrytype/arttype/med/vgauth.html')
    else:
        form = authForm
        if 'submitted' in request.GET:
            submitted = True  
    return render(request, 'industrytype/arttype/med/vgauth.html', {
        'form': form , 'submitted': submitted
        })


# animation
def anpost(request): 
    submitted = False
    if request.method == "POST":
        form = dashForm(request.POST, request.FILES)
        if form.is_valid():
            authUser = form.save(commit=False)
            authUser.user = request.user
            authUser.owner = request.user.id
            form.save()
            messages.success(request, ("Post Sucessful"))
            return render(request,'approved.html')
    
    else:
        return render(request,'industrytype/arttype/med/andashboard.html')
    
    return render(request, 'andashboard.html', {'form': form , 'submitted': submitted })
    
def anauths(request):
    submitted = False
    if request.method == "POST":
        form = authForm(request.POST, request.FILES)
        if form.is_valid():
            authHeritage = form.save(commit=False)
            authHeritage.user = request.user
            authHeritage.owner = request.user.id
            form.save()
            return render(request,'industrytype/arttype/med/anauth.html')
    else:
        form = authForm
        if 'submitted' in request.GET:
            submitted = True  
    return render(request, 'industrytype/arttype/med/anauth.html', {
        'form': form , 'submitted': submitted
        })


# fesion
def fepost(request): 
    submitted = False
    if request.method == "POST":
        form = dashForm(request.POST, request.FILES)
        if form.is_valid():
            authUser = form.save(commit=False)
            authUser.user = request.user
            authUser.owner = request.user.id
            form.save()
            messages.success(request, ("Post Sucessful"))
            return render(request,'approved.html')
    
    else:
        return render(request,'industrytype/fun/de/fedashboard.html')
    
    return render(request, 'fedashboard.html', {'form': form , 'submitted': submitted })
    
def authfe(request):
    submitted = False
    if request.method == "POST":
        form = authForm(request.POST, request.FILES)
        if form.is_valid():
            authHeritage = form.save(commit=False)
            authHeritage.user = request.user
            authHeritage.owner = request.user.id
            form.save()
            return render(request,'industrytype/fun/de/feauth.html')
    else:
        form = authForm
        if 'submitted' in request.GET:
            submitted = True  
    return render(request, 'industrytype/fun/de/feauth.html', {
        'form': form , 'submitted': submitted
        })


# jew
def jewpost(request): 
    submitted = False
    if request.method == "POST":
        form = dashForm(request.POST, request.FILES)
        if form.is_valid():
            authUser = form.save(commit=False)
            authUser.user = request.user
            authUser.owner = request.user.id
            form.save()
            messages.success(request, ("Post Sucessful"))
            return render(request,'approved.html')
    
    else:
        return render(request,'industrytype/fun/de/jewdashboard.html')
    
    return render(request, 'jewdashboard.html', {'form': form , 'submitted': submitted })
    
def authjew(request):
    submitted = False
    if request.method == "POST":
        form = authForm(request.POST, request.FILES)
        if form.is_valid():
            authHeritage = form.save(commit=False)
            authHeritage.user = request.user
            authHeritage.owner = request.user.id
            form.save()
            return render(request,'industrytype/fun/de/authjew.html')
    else:
        form = authForm
        if 'submitted' in request.GET:
            submitted = True  
    return render(request, 'industrytype/fun/de/authjew.html', {
        'form': form , 'submitted': submitted
        })

# toy
def toypost(request): 
    submitted = False
    if request.method == "POST":
        form = dashForm(request.POST, request.FILES)
        if form.is_valid():
            authUser = form.save(commit=False)
            authUser.user = request.user
            authUser.owner = request.user.id
            form.save()
            messages.success(request, ("Post Sucessful"))
            return render(request,'approved.html')
    
    else:
        return render(request,'industrytype/fun/de/toydashboard.html')
    
    return render(request, 'toydashboard.html', {'form': form , 'submitted': submitted })
    
def authtoy(request):
    submitted = False
    if request.method == "POST":
        form = authForm(request.POST, request.FILES)
        if form.is_valid():
            authHeritage = form.save(commit=False)
            authHeritage.user = request.user
            authHeritage.owner = request.user.id
            form.save()
            return render(request,'industrytype/fun/de/authtoy.html')
    else:
        form = authForm
        if 'submitted' in request.GET:
            submitted = True  
    return render(request, 'industrytype/fun/de/authtoy.html', {
        'form': form , 'submitted': submitted
        })
# set design

def setpost(request): 
    submitted = False
    if request.method == "POST":
        form = dashForm(request.POST, request.FILES)
        if form.is_valid():
            authUser = form.save(commit=False)
            authUser.user = request.user
            authUser.owner = request.user.id
            form.save()
            messages.success(request, ("Post Sucessful"))
            return render(request,'approved.html')
    
    else:
        return render(request,'industrytype/fun/de/setdeshboard.html')
    
    return render(request, 'setdeshboard.html', {'form': form , 'submitted': submitted })
    
def authset(request):
    submitted = False
    if request.method == "POST":
        form = authForm(request.POST, request.FILES)
        if form.is_valid():
            authHeritage = form.save(commit=False)
            authHeritage.user = request.user
            authHeritage.owner = request.user.id
            form.save()
            return render(request,'industrytype/fun/de/authset.html')
    else:
        form = authForm
        if 'submitted' in request.GET:
            submitted = True  
    return render(request, 'industrytype/fun/de/authset.html', {
        'form': form , 'submitted': submitted
        })

# graphic

def grapost(request): 
    submitted = False
    if request.method == "POST":
        form = dashForm(request.POST, request.FILES)
        if form.is_valid():
            authUser = form.save(commit=False)
            authUser.user = request.user
            authUser.owner = request.user.id
            form.save()
            messages.success(request, ("Post Sucessful"))
            return render(request,'approved.html')
    
    else:
        return render(request,'industrytype/fun/de/gradashboard.html')
    
    return render(request, 'gradashboard.html', {'form': form , 'submitted': submitted })
    
def authgra(request):
    submitted = False
    if request.method == "POST":
        form = authForm(request.POST, request.FILES)
        if form.is_valid():
            authHeritage = form.save(commit=False)
            authHeritage.user = request.user
            authHeritage.owner = request.user.id
            form.save()
            return render(request,'industrytype/fun/de/authgra.html')
    else:
        form = authForm
        if 'submitted' in request.GET:
            submitted = True  
    return render(request, 'industrytype/fun/de/authgra.html', {
        'form': form , 'submitted': submitted
        })

# architure

def archpost(request): 
    submitted = False
    if request.method == "POST":
        form = dashForm(request.POST, request.FILES)
        if form.is_valid():
            authUser = form.save(commit=False)
            authUser.user = request.user
            authUser.owner = request.user.id
            form.save()
            messages.success(request, ("Post Sucessful"))
            return render(request,'approved.html')
    
    else:
        return render(request,'industrytype/fun/cs/ardasboard.html')
    
    return render(request, 'ardasboard.html', {'form': form , 'submitted': submitted })
    
def autharc(request):
    submitted = False
    if request.method == "POST":
        form = authForm(request.POST, request.FILES)
        if form.is_valid():
            authHeritage = form.save(commit=False)
            authHeritage.user = request.user
            authHeritage.owner = request.user.id
            form.save()
            return render(request,'industrytype/fun/cs/authar.html')
    else:
        form = authForm
        if 'submitted' in request.GET:
            submitted = True  
    return render(request, 'industrytype/fun/cs/authar.html', {
        'form': form , 'submitted': submitted
        })

# advertisning

def adpost(request): 
    submitted = False
    if request.method == "POST":
        form = dashForm(request.POST, request.FILES)
        if form.is_valid():
            authUser = form.save(commit=False)
            authUser.user = request.user
            authUser.owner = request.user.id
            form.save()
            messages.success(request, ("Post Sucessful"))
            return render(request,'approved.html')
    
    else:
        return render(request,'industrytype/fun/cs/addashboard.html')
    
    return render(request, 'addashboard.html', {'form': form , 'submitted': submitted })
    
def authad(request):
    submitted = False
    if request.method == "POST":
        form = authForm(request.POST, request.FILES)
        if form.is_valid():
            authHeritage = form.save(commit=False)
            authHeritage.user = request.user
            authHeritage.owner = request.user.id
            form.save()
            return render(request,'industrytype/fun/cs/authad.html')
    else:
        form = authForm
        if 'submitted' in request.GET:
            submitted = True  
    return render(request, 'industrytype/fun/cs/authad.html', {
        'form': form , 'submitted': submitted
        })

# creative Rand D

def crdpost(request): 
    submitted = False
    if request.method == "POST":
        form = dashForm(request.POST, request.FILES)
        if form.is_valid():
            authUser = form.save(commit=False)
            authUser.user = request.user
            authUser.owner = request.user.id
            form.save()
            messages.success(request, ("Post Sucessful"))
            return render(request,'approved.html')
    
    else:
        return render(request,'industrytype/fun/cs/crddashboard.html')
    
    return render(request, 'crddashboard.html', {'form': form , 'submitted': submitted })
    
def authcrd(request):
    submitted = False
    if request.method == "POST":
        form = authForm(request.POST, request.FILES)
        if form.is_valid():
            authHeritage = form.save(commit=False)
            authHeritage.user = request.user
            authHeritage.owner = request.user.id
            form.save()
            return render(request,'industrytype/fun/cs/authcrd.html')
    else:
        form = authForm
        if 'submitted' in request.GET:
            submitted = True  
    return render(request, 'industrytype/fun/cs/authcrd.html', {
        'form': form , 'submitted': submitted
        })

# creative event service

def cespost(request): 
    submitted = False
    if request.method == "POST":
        form = dashForm(request.POST, request.FILES)
        if form.is_valid():
            authUser = form.save(commit=False)
            authUser.user = request.user
            authUser.owner = request.user.id
            form.save()
            messages.success(request, ("Post Sucessful"))
            return render(request,'approved.html')
    
    else:
        return render(request,'industrytype/fun/cs/cesdashboard.html')
    
    return render(request, 'cesdashboard.html', {'form': form , 'submitted': submitted })
    
def authce(request):
    submitted = False
    if request.method == "POST":
        form = authForm(request.POST, request.FILES)
        if form.is_valid():
            authHeritage = form.save(commit=False)
            authHeritage.user = request.user
            authHeritage.owner = request.user.id
            form.save()
            return render(request,'industrytype/fun/cs/authces.html')
    else:
        form = authForm
        if 'submitted' in request.GET:
            submitted = True  
    return render(request, 'industrytype/fun/cs/authces.html', {
        'form': form , 'submitted': submitted
        })
# digital sevices

def digpost(request): 
    submitted = False
    if request.method == "POST":
        form = dashForm(request.POST, request.FILES)
        if form.is_valid():
            authUser = form.save(commit=False)
            authUser.user = request.user
            authUser.owner = request.user.id
            form.save()
            messages.success(request, ("Post Sucessful"))
            return render(request,'approved.html')
    
    else:
        return render(request,'industrytype/fun/cs/digdashdoard.html')
    
    return render(request, 'digdashdoard.html', {'form': form , 'submitted': submitted })
    
def authdig(request):
    submitted = False
    if request.method == "POST":
        form = authForm(request.POST, request.FILES)
        if form.is_valid():
            authHeritage = form.save(commit=False)
            authHeritage.user = request.user
            authHeritage.owner = request.user.id
            form.save()
            return render(request,'industrytype/fun/cs/authdig.html')
    else:
        form = authForm
        if 'submitted' in request.GET:
            submitted = True  
    return render(request, 'industrytype/fun/cs/authdig.html', {
        'form': form , 'submitted': submitted
        })


