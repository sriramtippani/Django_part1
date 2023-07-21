import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'custom_authentication2.settings')
import django
django.setup()
from app1.models import *
from faker import Faker
from random import *
faker = Faker()
def f1(n):
    for x in range(n):
        a = randint(1001, 9999)
        b = faker.name()
        c = randint(1000, 2000)
        d = faker.city()
        record = Employee.objects.get_or_create(eno=a, ename=b, esal=c, eaddr=d)
f1(100)