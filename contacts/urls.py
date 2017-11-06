from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^welcome$',
        views.WelcomeView.as_view(), name="welcome-view"),
    url(r'^login/',
        views.LoginView.as_view(), name="login"),
    url(r'^logout/',
        views.LogoutView.as_view(), name="logout"),
    url(r'^list_contacts/$',
        views.PersonListView.as_view(), name="contact-list"),
    url(r'^contact/(?P<person_id>(\d)+)$',
        views.PersonDetailView.as_view(), name="contact-detail"),
    url(r'^new_contact/$',
        views.PersonCreateView.as_view(), name="contact-create"),
    url(r'^edit_contact/(?P<person_id>(\d)+)/$',
        views.PersonUpdateView.as_view(), name="contact-update"),
    url(r'^delete_contact/(?P<person_id>(\d)+)$',
        views.PersonDeleteView.as_view(), name="contact-delete"),

]
