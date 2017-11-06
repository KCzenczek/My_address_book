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
    PersonForm, PersonUpdateForm)

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


class PersonListView(ListView):
    model = Person
    template_name = 'contacts/person_list.html'


class PersonDetailView(View):

    def get(self, request, person_id):
        person = Person.objects.get(id=person_id)
        addresses = Address.objects.filter(person_id=person_id)
        telephones = Telephone.objects.filter(person_id=person_id)
        emails = Email.objects.filter(person_id=person_id)
        return TemplateResponse(request, "contacts/person_detail.html", {
            "person": person,
            "addresses": addresses,
            "telephones": telephones,
            "emails": emails,
        })


class PersonCreateView(CreateView):
    template_name = 'contacts/person_form.html'
    form_class = PersonForm
    model = Person
    success_url = '/contacts/list_contacts'


class PersonUpdateView(UpdateView):
    template_name = 'contacts/person_update_form.html'
    form_class = PersonUpdateForm
    model = Person
    pk_url_kwarg = 'person_id'

    def get_success_url(self):
        return self.object.get_absolute_url()


class PersonSearchView(FormView):
    pass


class PersonDeleteView(DeleteView):
    pass


class UserCreateView(View):
    pass


class UserList(View):
    pass


class PasswordResetView(View):
    pass
