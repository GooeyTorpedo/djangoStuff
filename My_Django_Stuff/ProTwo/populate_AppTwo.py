import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()

import random
from AppTwo.models import Users
from faker import Faker


# FAKE POP SCRIPT

fakegen = Faker()

# populate 
def populate(N=5):
    for entry in range(N):
        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_email = fakegen.email()
        
        usr = Users.objects.get_or_create(fname=fake_first_name, lname = fake_last_name, email=fake_email)[0]


        # # create the fake data for that entry
        # fake_first_name = fakegen.first_name()
        # fake_last_name = fakegen.last_name()
        # fake_email = fakegen.free_email()

        # # create new webpage entry
        # usr = Users.objects.get_or_create(
        #     fname=fake_first_name, lname = fake_last_name, email=fake_email)[0]


if __name__ == '__main__':
    print('populating script!')
    populate(20)
    print('Populating complete!')
