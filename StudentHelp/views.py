from django.shortcuts import render
from .models import User,Comment,Like,Poste,Transport,Stage,Logement,Recommandation,Evenement,EvenClub,EvenSocial
from .forms import  userfrom,PosteForm
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.views.generic import DetailView,DeleteView
from django.views.generic.edit import UpdateView
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages


class SupprimerProfil(DeleteView):
    model = Poste
    template_name = 'blog/supprimer_poste.html'
    success_url = reverse_lazy('profil')

class Modifierprofil(UpdateView):
    model = User
    template_name = 'blog/modifier_user.html'
    form_class = userfrom
    success_url = reverse_lazy('profil')

def comment_view(request, pk):
    if request.method == 'POST':
        user = User.objects.get(email=request.session.get('user'))
        
        comment_text = request.POST.get('comment')
        
  
        reaction_obj = get_object_or_404(Poste, pk=pk)
        
      
        reaction = Comment(user=user, com=comment_text, poste=reaction_obj)
        reaction.save()
     
        return redirect('home')
        

def toggle_like(request, pk):
    poste = get_object_or_404(Poste, pk=pk)

    user = User.objects.get(email=request.session.get('user'))

    try:
        like = Like.objects.get(poste=poste, user=user)
        like.delete()
          # If like exists, delete it (toggle off)
    except Like.DoesNotExist:
        Like.objects.create(poste=poste, user=user, li=True) 
    return redirect('home')

def home(request):
    if 'user' in request.session:
        current_user = request.session['user']
        param = {'current_user': current_user}
        context = {
            'poste': Poste.objects.order_by('-date'), 
            'comments': Comment.objects.all(),
            'likes': Like.objects.all(),
            'users': User.objects.all(),
        }
        return render(request, 'blog/home.html', context)
    else:
        context = {
            'poste': Poste.objects.order_by('-date')[:5], 
         
        }
        return render(request, 'blog/home.html', context)


  
        
def help(request):
     return render(request, 'blog/help.html')
 



def filter_posts(request, post_type):
    if post_type == 'offre':
        posts = Poste.objects.filter(type=0)  
    elif post_type == 'demande':
        posts = Poste.objects.filter(type=1)  
    else:
        posts = None  
    
    return render(request, 'blog/home.html', {'poste': posts})






def about(request):
    return render(request, 'blog/about.html', {'title': "About"})

def Transports(request):
    context = {
        'poste': Poste.objects.all(),
 
        'transports': Transport.objects.all(),

    }
    return render(request, 'blog/Transports.html', context)

def newpost(request):
    return render(request, 'blog/newpost.html')

def TransportForm(request):
    if request.method == 'POST':
        user = User.objects.get(email=request.session['user'])
        post_type = request.POST.get('type')  # Assurez-vous que 'type' correspond au champ dans votre modèle Poste
        date = request.POST.get('date')
        image = request.FILES.get('image')
        depart = request.POST.get('depart') 
        destination = request.POST.get('destination') 
        heuredep = request.POST.get('heuredep') 
        nbreSiege = request.POST.get('nbreSiege') 
        contactInfo = request.POST.get('contactInfo') 

        # Création d'une instance de Poste avec les données reçues
        post = Transport(
            user=user,
            type=post_type,
            date=date,
            image=image,
            depart=depart,
            destination=destination,
            heuredep=heuredep,
            nbreSiege=nbreSiege,
            contactInfo=contactInfo
        )

        # Enregistrement de l'objet dans la base de données
        post.save()

        return redirect('home')
    else:
        return render(request, 'blog/from/TransportForm.html')
  
def StageForm(request):
    if request.method == 'POST':
        user = User.objects.get(email=request.session['user'])
        post_type = request.POST.get('type')  # Ensure that 'type' matches the field in your Post model
        date = request.POST.get('date')
        image = request.FILES.get('image')
        typeStg = request.POST.get('typeStg') 
        societe = request.POST.get('societe') 
        duree = request.POST.get('duree') 
        sujet = request.POST.get('sujet')   
        contactinfo = request.POST.get('contactinfo')  # Corrected the variable name
        specialite = request.POST.get('specialite') 

        post = Stage(
            user=user,
            type=post_type,
            date=date,
            image=image,
            typeStg=typeStg,
            societe=societe,
            duree=duree,
            sujet=sujet,
            contactinfo=contactinfo,  # Corrected the variable name
            specialite=specialite,
        )

        post.save()

        return redirect('home')
    else:
        return render(request, 'blog/from/StageForm.html')  





def LogementForm(request):
    if request.method == 'POST':
        if 'user' in request.session:
            user = get_object_or_404(User, email=request.session['user'])
            post_type = request.POST.get('type')
            date = request.POST.get('date')
            image = request.FILES.get('image')
            localisation = request.POST.get('localisation')
            description = request.POST.get('description')
            contact_info = request.POST.get('contactInfo')

            post = Logement(
                user=user,
                type=post_type,
                date=date,
                image=image,
                localisation=localisation,
                description=description,
                contactInfo=contact_info,  # Corrected the variable name
            )

            post.save()

            return redirect('home')

    else:
         return render(request, 'blog/from/LogementForm.html')  




def RecommandationForm(request):
    if request.method == 'POST':
        if 'user' in request.session:
            user = get_object_or_404(User, email=request.session['user'])
            post_type = request.POST.get('type')
            date = request.POST.get('date')
            image = request.FILES.get('image')
            texte = request.POST.get('texte')
         
            post = Recommandation(
                user=user,
                type=post_type,
                date=date,
                image=image,
                texte=texte,
                  # Corrected the variable name
            )

            post.save()

            return redirect('home')

    else:
         return render(request, 'blog/from/RecommandationForm.html')  
    



def EvenClubForme(request):
    if request.method == 'POST':
        if 'user' in request.session:
            user = get_object_or_404(User, email=request.session['user'])
            post_type = request.POST.get('type')
            date = request.POST.get('date')
            image = request.FILES.get('image')
            intitule = request.POST.get('intitule')
            description = request.POST.get('description')
            lieu = request.POST.get('lieu')
            contact_info = request.POST.get('contactInfo')

            post = EvenClub(
                user=user,
                type=post_type,
                date=date,
                image=image,
                intitule=intitule,
                description=description,
                lieu=lieu,
                contactInfo=contact_info  # Added comma and corrected variable name
            )

            post.save()

            return redirect('home')
       
    else:
         return render(request, 'blog/from/EvenClubForm.html')  




     
def EvenSocialForme(request):
    if request.method == 'POST':
        if 'user' in request.session:
            user = get_object_or_404(User, email=request.session['user'])
            post_type = request.POST.get('type')
            date = request.POST.get('date')
            image = request.FILES.get('image')
            intitule = request.POST.get('intitule')
            description = request.POST.get('description')
            lieu = request.POST.get('lieu')
            contact_info = request.POST.get('contactInfo')
            prix = request.POST.get('prix')

            post = EvenSocial(
                user=user,
                type=post_type,
                date=date,
                image=image,
                intitule=intitule,
                description=description,
                lieu=lieu,
                contactInfo=contact_info,
                prix=prix   # Added comma and corrected variable name
            )

            post.save()

            return redirect('home')
       
    else:
         return render(request, 'blog/from/EvenSocialForme.html')  
   
  
def tage(request):
    context = {
        'poste': Poste.objects.all(),
       
        'Stage': Stage.objects.all(),

    }
    return render(request, 'blog/Stage.html', context)

def logement(request):
    context = {
        'poste': Poste.objects.all(),

        'Logement': Logement.objects.all(),

    }
    return render(request, 'blog/Logement.html', context)

def recommandation(request):
    context = {
        'poste': Poste.objects.all(),
    
        'Recommandation': Recommandation.objects.all(),

    }
    return render(request, 'blog/Recommandation.html', context)

def evenement(request):
    context = {
        'poste': Poste.objects.all(),
  
        'Evenement': Evenement.objects.all(),

    }
    return render(request, 'blog/Evenement.html', context)
  
def evenClub(request):
    context = {
        'poste': Poste.objects.all(),
   
        'EvenClub': EvenClub.objects.all(),

    }
    return render(request, 'blog/EvenClub.html', context)

def evenSocial(request):
    context = {
        'poste': Poste.objects.all(),
     
        'EvenSocial': EvenSocial.objects.all(),

    }
    return render(request, 'blog/EvenSocial.html', context)

    
from django.shortcuts import render
from .models import User, Poste

def profil(request):
    # Retrieve the user object using the email stored in the session
    user_email = request.session.get('user')
    user = User.objects.get(email=user_email)

    # Retrieve all posts associated with the user
    poste = Poste.objects.filter(user=user)

    context = {
        'poste': poste,
        'user': user
    }
    return render(request, 'blog/profil.html', context)



  
def logoutview(request):
    logout(request)  
    context = {
        'poste': Poste.objects.all(),
    
        
    }
    return render(request, 'blog/home.html', context)




def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)

            
            if user.check_password(password):
                request.session['user'] = email
                request.session['user_image_url'] = user.image.url if user.image else '/path/to/default/image.jpg'

                # Authentification réussie, rediriger l'utilisateur vers une page de succès
                return redirect('home')
            else:
                # Authentification échouée, afficher un message d'erreur
                error_message = "Email ou mot de passe incorrect"
                return render(request, 'registration/login.html', {'error_message': error_message})
        except User.DoesNotExist:
            # L'utilisateur n'existe pas, afficher un message d'erreur
            error_message = "utilisateur n'existe pas "
            return render(request, 'registration/login.html', {'error_message': error_message})
    else:
        # Afficher le formulaire de connexion
        return render(request, 'registration/login.html')
    

def signup(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        telephone = request.POST.get('telephone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        image = request.FILES.get('image')
        user = User(nom=nom, prenom=prenom, telephone=telephone, email=email, password=password, image=image)
        user.save()

        request.session['user'] = email
        request.session['user_image_url'] = user.image.url if user.image else '/path/to/default/image.jpg'
        return redirect('home')  
    else:
        return render(request, 'registration/signup.html')

def post(request):
    if request.method == 'POST':
        form = PosteForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = User.objects.get(email=request.session['user'])
            post.save()
            messages.success(request, 'Post created successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the errors below.')
            return render(request, 'blog/post.html', {'form': form})
    else:
        form = PosteForm()
        return render(request, 'blog/post.html', {'form': form})    

def notification(request):
    context = {
        'comments': Comment.objects.order_by('-date'),
        'likes': Like.objects.order_by('-date'),
    }
    return render(request, 'notification.html', context)


class DetailPost(DetailView):
    model = Poste
    template_name = 'blog/detail_post.html'
    context_object_name = 'posts'




        

def DetailPost(request, pk):
    post_obj = get_object_or_404(Poste, pk=pk)
    comments = Comment.objects.filter(poste=post_obj)
    likes = Like.objects.filter(poste=post_obj)

    context = {
        'post_obj': post_obj,
        'comments': comments,
        'likes': likes,
    }

    return render(request, 'blog/detail_post.html', context)

    













