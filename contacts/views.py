from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.views import View
from django.views.generic import (
    CreateView,
    DeleteView,
    FormView,
    ListView,
    UpdateView,
)

from contacts.forms import (
    LoginForm,
)

from .models import (
    Address,
    Email,
    Person,
    Telephone,
)


class WelcomeView(View):
    def get(self, request):
        return TemplateResponse(request, 'contacts/welcoming_page.html', {
            'welcome': 'Welcome you',
        })


class LoginView(View):
    template_name = 'contacts/login.html'
    form_class = LoginForm

    def get(self, request):
        form = self.form_class
        return TemplateResponse(request, self.template_name, {
            'form': form,
        })

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            login(request, form.user)
            return redirect('/contacts/list_contacts/')
        else:
            return TemplateResponse(request, self.template_name, {
                'form': form,
            })


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/contacts/welcome')


class ContactListView(ListView):
    model = Person
    template_name = 'contacts/person_list.html'


class ContactDetailView(View):

    def get(self, request, person_id):
        person = Person.objects.get(id=person_id)
        addresses = Address.objects.filter(person_id=person_id)
        telephones = Telephone.objects.filter(person_id=person_id)
        emails = Email.objects.filter(person_id=person_id)
        return TemplateResponse(request, "contacts/contact_detail.html", {
            "person": person,
            "addresses": addresses,
            "telephones": telephones,
            "emails": emails,
        })


class ContactCreateView(CreateView):
    pass


class ContactUpdateView(UpdateView):
    pass


class ContactSearchView(FormView):
    pass


class ContactDeleteView(DeleteView):
    pass


class UserCreateView(View):
    pass


class UserList(View):
    pass


class PasswordResetView(View):
    pass
