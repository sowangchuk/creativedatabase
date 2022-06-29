
from django.db import models
from account.models import User
from django.utils.timezone import now
from multiselectfield import MultiSelectField

from app.models import pubemail, pubphone

# from app.models import pubemail, pubphone

class addevent(pubphone, pubemail):
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
   MEDIUM=(
        ('Dzongkha','Dzongkha'),
        ('English','English'),
        ('Sharchop','Sharchop'),
        ('Nepali','Nepali'),
        ('Other','Other'),
    )
   user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   owner= models.IntegerField(blank=False, default=1)
   title= models.CharField(max_length=100, blank=False)
   Dzongkhag = models.CharField( max_length=32, choices=STATUS2, default=SELECT,)
   medium =MultiSelectField(max_length=100, max_choices=5, choices=MEDIUM, default='Dzongkha')
   image_event = models.ImageField(upload_to='event/')
   discription= models.TextField(max_length=300, blank=True)
   available=models.BooleanField()
   create_date = models.DateTimeField( auto_now_add=True, blank=True)
   is_approved = models.BooleanField(('show'), default=False)
    
   
   