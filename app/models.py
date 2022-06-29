
from email.message import EmailMessage
from django.db import models

from django.db import models

from account.models import User



class authUser(models.Model):
   SELECT = 'select'
   BHUTAN = 'Bhutan'
   INDIA = 'India'
   USA = 'USA'
   
   STATUS = [
       (SELECT, ('---select Countries---')),
       (BHUTAN, ('Bhutan')),
       (INDIA, ('India')),
       (USA, ('USA')),
       
   ]
#    dzongkha

   SELECT = 'select'
   BUMTHANG='Bumthang'
   CHUKHA='Chukha'
   DAGANA='Dagana'
   GASA='Gasa'
   HAA = 'Haa'
   LHUNTSE='Lhuntse'
   MONGAR='Mongar'
   PARO = 'Paro'
   PAMAGATSHEL='Pemagatshel'
   PUNAKHA='Punakha'
   SAMDRUP_JONGKHAR='Samdrup Jongkhar '
   SAMTSE='Samtse'
   SARPANG='Sarpang'
   THIMPHU = 'Thimphu'
   TRASHIGANG = 'Trashigang'
   TRASHIYANGTSE='Trashiyangtse'
   TRONGSA='Trongsa'
   TSIRANG='Tsirang'
   WANGDUE='Wangdue Phodrang'
   ZHEMGANG='Zhemgang'
   
   
   STATUS2 = [
       (SELECT, ('---select Dzongkhag---')),
       (BUMTHANG,('Bumthang')),
       (CHUKHA, ('Chukha')),
       (DAGANA, ('Dagana')),
       (GASA, ('Gasa')),
       (HAA , ('Haa')),
       (LHUNTSE, ('Lhuntse')),  
       (MONGAR, ('Mongar')),
       (PARO , ('Paro')),
       (PAMAGATSHEL, ('Pemagatshel')),
       (PUNAKHA, ('Punakha')),
       (SAMDRUP_JONGKHAR, ('Samdrup Jongkhar ')),
       (SAMTSE, ('Samtse')),
       (SARPANG, ('Sarpang')),
       (THIMPHU, ('Thimphu')),
       (TRASHIGANG, ('Trashigang')),
       (TRASHIYANGTSE, ('Trashiyangtse')),
       (TRONGSA, ('Trongsa')),
       (TSIRANG, ('Tsirang')),
       (WANGDUE, ('Wangdue Phodrang')),
       (ZHEMGANG, ('Zhemgang')),
       
       
   ]
# marital status
   SELECT = 'select'
   SINGLE = 'Single'
   MARRIED = 'Married'
   
   
   STATUS3 = [
       (SELECT, ('---select maritals---')),
       (SINGLE, ('Single')),
       (MARRIED, ('Married')),
       
   ]
#  Employment  
   SELECT = 'select'
   EMPLOYED = 'Employed'
   UNEMPLOYED = 'Unemployed'
   STUDENT = 'Student'
   BUSINESS = 'Business'
   
   
   STATUS4 = [
       (SELECT, ('---select employment---')),
       (EMPLOYED, ('Employed')),
       (UNEMPLOYED, ('Unemployed')),
       (STUDENT, ('Student')),
       (BUSINESS, ('Business')),
       
   ]
#    skills
   SELECT = 'select'
   ARTIST ='artist'
   
   
   STATUS5 = [
       (SELECT, ('---select skills---')),
       (ARTIST,('artist'))
       
        
   ]
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   owner= models.IntegerField(blank=False, default=1)
   cell_number = models.IntegerField( unique= True)
   date_joined = models.DateTimeField(('date_joined'), auto_now_add=True, blank=True)
   country = models.CharField( max_length=32, choices=STATUS, default=SELECT,)
   Dzongkhag = models.CharField( max_length=32, choices=STATUS2, default=SELECT,)
   marital_status = models.CharField( max_length=32, choices=STATUS3, default=SELECT,)
   employment_status = models.CharField( max_length=32, choices=STATUS4, default=SELECT,)
   skills = models.CharField( max_length=32, choices=STATUS5, default=SELECT, blank=True)
   document = models.FileField(upload_to='documents/', null=True,)
   remarks = models.TextField(max_length=300, blank=True)
   is_staff = models.BooleanField(('staff'), default=False)


class pubemail(models.Model):
    
    mail = models.EmailField(max_length= 100, unique=True)
    is_show_mail = models.BooleanField(('show'), default=True)
    # is_hide_mail = models.BooleanField(('hide'), default=False)
    
    class Meta:
        abstract = True

class pubphone(models.Model):
   
   phone = models.CharField( unique=True, max_length=8, null=True, blank=True,)
   is_show = models.BooleanField(('show'), default=True)
#    is_hide = models.BooleanField(('hide'), default=False)
   class Meta:
        abstract = True

class artist_profile(pubemail, pubphone):
   SELECT = 'select'
   BHUTAN = 'Bhutan'
   INDIA = 'India'
   USA = 'USA'
   
   STATUS1 = [
       (SELECT, ('---select Countries---')),
       (BHUTAN, ('Bhutan')),
       (INDIA, ('India')),
       (USA, ('USA')),
       
   ]
#    dzongkha

   SELECT = 'select'
   BUMTHANG='Bumthang'
   CHUKHA='Chukha'
   DAGANA='Dagana'
   GASA='Gasa'
   HAA = 'Haa'
   LHUNTSE='Lhuntse'
   MONGAR='Mongar'
   PARO = 'Paro'
   PAMAGATSHEL='Pemagatshel'
   PUNAKHA='Punakha'
   SAMDRUP_JONGKHAR='Samdrup Jongkhar '
   SAMTSE='Samtse'
   SARPANG='Sarpang'
   THIMPHU = 'Thimphu'
   TRASHIGANG = 'Trashigang'
   TRASHIYANGTSE='Trashiyangtse'
   TRONGSA='Trongsa'
   TSIRANG='Tsirang'
   WANGDUE='Wangdue Phodrang'
   ZHEMGANG='Zhemgang'
   
   
   STATUS3 = [
       (SELECT, ('---select Dzongkhag---')),
       (BUMTHANG,('Bumthang')),
       (CHUKHA, ('Chukha')),
       (DAGANA, ('Dagana')),
       (GASA, ('Gasa')),
       (HAA , ('Haa')),
       (LHUNTSE, ('Lhuntse')),
       (MONGAR, ('Mongar')),
       (PARO , ('Paro')),
       (PAMAGATSHEL, ('Pemagatshel')),
       (PUNAKHA, ('Punakha')),
       (SAMDRUP_JONGKHAR, ('Samdrup Jongkhar ')),
       (SAMTSE, ('Samtse')),
       (SARPANG, ('Sarpang')),
       (THIMPHU, ('Thimphu')),
       (TRASHIGANG, ('Trashigang')),
       (TRASHIYANGTSE, ('Trashiyangtse')),
       (TRONGSA, ('Trongsa')),
       (TSIRANG, ('Tsirang')),
       (WANGDUE, ('Wangdue Phodrang')),
       (ZHEMGANG, ('Zhemgang')),
       
       
   ]
# marital status
   SELECT = 'select'
   SINGLE = 'Single'
   MARRIED = 'Married'
   
   
   STATUS4 = [
       (SELECT, ('---select maritals---')),
       (SINGLE, ('Single')),
       (MARRIED, ('Married')),
       
   ]
#  Employment  
   SELECT = 'select'
   EMPLOYED = 'Employed'
   UNEMPLOYED = 'Unemployed'
   STUDENT = 'Student'
   BUSINESS = 'Business'
   
   
   STATUS5 = [
       (SELECT, ('---select employment---')),
       (EMPLOYED, ('Employed')),
       (UNEMPLOYED, ('Unemployed')),
       (STUDENT, ('Student')),
       (BUSINESS, ('Business')),
       
   ]
#    skills
   SELECT = 'select'
   ARTIST ='Artist'
   
   
   STATUS6 = [
       (SELECT, ('---select skills---')),
       (ARTIST,('Artist'))
           
   ]
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   name = models.CharField(max_length=100, blank=False)
   pubprofile = models.ImageField(upload_to='avatars/', null=True, blank=True)
   pubcountry = models.CharField( max_length=32, choices=STATUS1, default=SELECT,)
   pudDzongkhag = models.CharField( max_length=32, choices=STATUS3, default=SELECT,)
   pubmarital_status = models.CharField( max_length=32, choices=STATUS4, default=SELECT,)
   pubemployment_status = models.CharField( max_length=32, choices=STATUS5, default=SELECT,)
   pubskills = models.CharField( max_length=32, choices=STATUS6, default=SELECT, blank=True)
   pubdocument = models.FileField(upload_to='documents/', null=True, )
   date_joined = models.DateTimeField(('date_joined'), auto_now_add=True, blank=True)
   
   def __str__(self):
       return self.name

