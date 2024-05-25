from django.urls import path
from . import views

from .views import DetailPost
from .views import Modifierprofil,SupprimerProfil



urlpatterns = [

  
  path('',views.home, name="home"),
  path('/help',views.help, name="help"),
  path('delete/<int:pk>/', SupprimerProfil.as_view(), name='SupprimerProfil'),
  path('modifier/<int:pk>/', Modifierprofil.as_view(), name='Modifierprofil'),
  path('profil/',views.profil, name="profil"),
  path('about/',views.about, name="about"),
  path('Transports/',views.Transports, name="Transports"),
  path('newpost/',views.newpost, name="newpost"),
  path('TransportForme/', views.TransportForm, name='TransportForme'),
  path('Stage/',views.tage, name="Stage"),
  path('Logement/',views.logement, name="Logement"),
  path('Recommandation/',views.recommandation, name="Recommandation"),
  path('Evenement/',views.evenement, name="Evenement"),
  path('EvenClub/',views.evenClub, name="EvenClub"),
  path('EvenSocial/',views.evenSocial, name="EvenSocial"),
  path('filter_posts/<str:post_type>/', views.filter_posts, name='filter'),
  path('TransportForm/', views.TransportForm, name='TransportForm'),
  path('StageForm/', views.StageForm, name='StageForm'),
  path('LogementForm/', views.LogementForm, name='LogementForm'),
  path('EvenClubForm/', views.EvenClubForme, name='EvenClubForm'),
   path('EvenSocialForme/', views.EvenSocialForme, name='EvenSocialForme'),
    path('evenSocial/', views.evenSocial, name='evenSocial'),
  path('<int:pk>/comment/', views.comment_view, name='comment_view'),
  path('RecommandationForm/', views.RecommandationForm, name='RecommandationForm'),
 

   path('post/', views.post, name='post'),
  path('logout/', views.logoutview, name='logout'),
  path('login/', views.login, name='success'),
  path('signup/', views.signup, name='signup'),
  path('toggle-like/<int:pk>/', views.toggle_like, name='toggle_like'),
  path('notification/', views.notification, name='notification'),

  path('post/<int:pk>/', DetailPost, name='detail_post'),
] 