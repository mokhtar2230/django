from django.contrib import admin
from .models import User,Poste,Stage,Logement,Transport,Evenement,Recommandation,EvenClub,EvenSocial
from .models import Like,Comment
# Register your models here.
admin.site.register(User)
admin.site.register(Poste)
admin.site.register(Stage)
admin.site.register(Logement)
admin.site.register(Transport)
admin.site.register(Evenement)
admin.site.register(Recommandation)
admin.site.register(EvenClub)
admin.site.register(EvenSocial)
admin.site.register(Like)
admin.site.register(Comment)
