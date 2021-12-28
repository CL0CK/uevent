from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', EventHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addevent/', AddEvent.as_view(), name='add_event'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('event/<slug:event_slug>/', ShowEvent.as_view(), name='event'),
    path('category/<slug:cat_slug>/', EventCategory.as_view(), name='category'),
    # path('cats/<int:catid>/', categories),
    # re_path(r'^archive/(?P<year>[0-9]{4})/', archive, name='archive'),
]
