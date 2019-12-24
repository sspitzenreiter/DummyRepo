import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ujian_praktikum_1174035.settings')

import django

django.setup()

import random
from ujian_aplikasi_1174035.models import User
from faker import Faker

fakegen = Faker()
def po_1174035(N=10):
    for x in range(N):
        fake_first_name = fakegen.first_name_male()
        fake_last_name = fakegen.last_name()
        fake_email = fakegen.email()
        user = User.objects.get_or_create(first_name = fake_first_name, last_name = fake_last_name, email = fake_email)[0]
        user.save()

if __name__=='__main__':
    print("Inputing User Data")
    po_1174035(30)
    print("Populating Complete, 30 Data Inserted")