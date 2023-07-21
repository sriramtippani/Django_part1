import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_with_api.settings')
import django
django.setup()
from app1.models import *
from faker import Faker
from random import *
faker = Faker()
k = ['B.Tech', 'M.Tech', 'B.Sc', 'Diploma', '10th class']
def f1(n):
    for x in range(n):
        a = faker.date()
        b = faker.company()
        c = faker.name()
        d = choice(k)
        e = faker.address()
        f = faker.email()
        g = randint(7382209900, 9012824899)
        record = punejobs.objects.get_or_create(date=a, company=b, title=c, eligibility=d, address=e, email=f, phone_number=g)
f1(30)