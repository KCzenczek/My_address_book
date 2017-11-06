# Create your models here.
from django.db import models
from django.urls import reverse


class Person(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    description = models.TextField(null=True)

    def __str__(self):
        return '{} {}'.format(self.name, self.surname)

    def get_absolute_url(self):
        return reverse('contact-detail', kwargs={'person_id': self.id})


class Address(models.Model):
    city = models.CharField(max_length=64)
    street = models.CharField(max_length=64)
    building_number = models.IntegerField(null=True)
    flat_number = models.IntegerField(null=True)
    person = models.ForeignKey(
        Person,
        related_name='address_person',
        on_delete=models.CASCADE
    )


class Telephone(models.Model):
    phone_number = models.IntegerField(null=True)
    phone_type = models.CharField(
        max_length=28,
        default='H',
        choices=[
            ('H', 'Home'),
            ('W', 'Work'),
            ('P', 'Private')
        ]
    )
    person = models.ForeignKey(
        Person,
        related_name='telephone_person',
        on_delete=models.CASCADE
    )


class Email(models.Model):
    email_address = models.CharField(max_length=64)
    email_type = models.EmailField(
        max_length=28,
        default='H',
        choices=[
            ('H', 'Home'),
            ('W', 'Work'),
            ('P', 'Private')
        ]
    )
    person = models.ForeignKey(
        Person,
        related_name='email_person',
        on_delete=models.CASCADE
    )


class Groups(models.Model):
    group_name = models.CharField(max_length=128)
    person = models.ManyToManyField(
        Person,
        related_name='groups_person',
    )


