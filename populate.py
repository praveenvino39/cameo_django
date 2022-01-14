import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cameoproject.settings')
django.setup()
from faker import Faker
from cameo.models import Cameo
from django.contrib.auth.hashers import make_password
from cameoproject import settings
import random
import requests
import urllib
import os

fake = Faker()

user_response = requests.get('https://randomuser.me/api/?results=50')
user_response = user_response.json()
print(type(user_response))
rating = [1.5,1.7,3.5,5.0,4.6,1.3]

for i in range(1, 50):
    full_name = fake.name()
    newcameo = Cameo.objects.create(username=full_name.replace(" ", "_"),
                                    password=make_password("Pv4you39"))
    newcameo.first_name = full_name.split(' ')[0]
    newcameo.last_name = full_name.split(' ')[1]
    newcameo.delivery_duration = random.randint(1, 24)
    newcameo.delivery_duration_unit = random.choice(
        Cameo.delivery_duration_unit_choice)[0]
    newcameo.paypal_email = fake.email()
    newcameo.is_celebrity = True
    newcameo.rating = round(random.uniform(0.0, 5.0),1)
    newcameo.category = Cameo.category_choice[2][0]
    file_name = random.randint(1, 999)
    image = urllib.request.urlretrieve(
        user_response["results"][i]["picture"]["large"],
        "{}/{}.jpg".format(os.path.join(os.curdir, "media/cameo"), file_name))
    newcameo.image = image[0]
    newcameo.image = 'cameo/{}.jpg'.format(file_name)
    newcameo.intro = user_response["results"][i]["location"]["city"]
    newcameo.bio = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Ex totam nulla, qui accusantium quibusdam alias natus aliquam doloremque voluptas autem!"
    newcameo.price = random.randint(1, 999)
    newcameo.currency_code = random.choice(Cameo.currency_code_symbols)[0]
    newcameo.fans = random.randint(1, 999)
    for i in range(1,random.randint(1, 100)):
        newcameo.reviews.append(    {
            "user": "Someone",
            "review": "Very nice and humble",
            "star": "4"
        })
    newcameo.save()
