from django.db import models
from django.contrib.auth.hashers import make_password, check_password


class User(models.Model):
    nom = models.CharField(max_length=100, verbose_name="Nom", blank=False)
    prenom = models.CharField(max_length=100, verbose_name="Prénom", blank=False)
    telephone = models.CharField(max_length=20, verbose_name="Téléphone", blank=False)
    email = models.EmailField(unique=True, verbose_name="Email", blank=False)
    image = models.ImageField(upload_to='post_images', null=True, default=None, blank=True)
    password = models.CharField(max_length=255, null=False, default=None)


    def __str__(self):
        return f"{self.nom} {self.prenom}"

    def save(self, *args, **kwargs):
        if not self.pk:
          
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def check_password(self, password):
        return check_password(password, self.password)

class Poste(models.Model):
    TYPE_CHOICES = [
        (0, 'offre'),
        (1, 'demande'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    type = models.IntegerField(choices=TYPE_CHOICES, default=0)
    date = models.DateField()
    image = models.ImageField(upload_to='post_images')  

    def affichertype(self):
        return 'offre' if self.type == 0 else 'demande'
    def count_likes(self):
        return self.likes.count()

    def count_comments(self):
        return self.comments.count()
class Meta:
     ordering = ['-date']




   
class Comment(models.Model):
    poste = models.ForeignKey(Poste, on_delete=models.CASCADE, related_name='comments', default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    com = models.CharField(max_length=100, null=True)

class Like(models.Model):
    poste = models.ForeignKey(Poste, on_delete=models.CASCADE, related_name='likes', default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    li = models.BooleanField(default=True, null=True)



class Stage(Poste):  # Définir la classe Stage en tant que modèle Django
    TYPE_CHOICES = [
        (1, 'ouvrier'),
        (2, 'technicien'),
        (3, 'PFE')
    ]
    
    typeStg = models.IntegerField(choices=TYPE_CHOICES, default=1)
    societe = models.CharField(max_length=100)
    duree = models.IntegerField(default=0)
    sujet = models.CharField(max_length=100)
    contactinfo = models.CharField(max_length=100)
    specialite = models.CharField(max_length=100)

    def __str__(self):
        return f"Stage at {self.societe}"
class Logement(Poste):
    localisation = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    contactInfo = models.CharField(max_length=255)

    def __str__(self):
        return f"{super().__str__()} - Location: {self.localisation}"

class Transport(Poste):
    depart=models.CharField(max_length=100)
    destination=models.CharField(max_length=100)
    heuredep =models.DateTimeField(auto_now_add=True)
    nbreSiege = models.IntegerField()
    contactInfo = models.CharField(max_length=100)

    def __str__(self):
        return f"{super().__str__()} - Departure: {self.depart}, Destination: {self.destination}"

class Evenement(Poste):
    intitule=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    lieu =models.CharField(max_length=100)
    contactInfo = models.CharField(max_length=100)

    def __str__(self):
        return f"{super().__str__()} - Event: {self.intitule}, Location: {self.lieu}"

class Recommandation(Poste):
    texte=models.CharField(max_length=100)

    def __str__(self):
        return f"{super().__str__()} - Recommendation: {self.texte}"

class EvenClub(Evenement):
    
    club=models.CharField(max_length=100)

    def __str__(self):
        return f"{super().__str__()} - Club Event: {self.club}"

class EvenSocial(Evenement):
    prix=models.FloatField()

    def __str__(self):
        return f"{super().__str__()} - Social Event: Price - {self.prix}"



