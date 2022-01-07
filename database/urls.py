from django.urls import path
from . import views as databaseviews

urlpatterns = [
    path('home/', databaseviews.home_database, name = 'homedatabase'),
    path('blog/', databaseviews.blog_database, name = 'blogdatabase'),
    path('termscs/', databaseviews.terms, name="termscs")
]
