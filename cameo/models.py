from locale import currency
from operator import mod
from django.db import models
from django.contrib.auth.models import AbstractUser, User
from jsonfield import JSONField
from rest_framework.serializers import ModelSerializer
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.


class Cameo(AbstractUser):
    category_choice = [
        ('Actors', 'actors'),
        ('Activists', 'activist'),
        ("Artists", "artists"),
        ("Astrologers", "astrologers"),
        ("Astronauts", "astronauts"),
        ('Athletes', 'athletes'),
        ("Authors", "authors"),
        ("Cameo Team", "cameo_team"),
        ('Comedian', 'comedians'),
        ("Commentators", "commentators"),
        ('Creator', 'creator'),
        ("Dancers", "dancers"),
        ("En Español", "en_español"),
        ("Food", "food"),
        ("Furry", "furry"),
        ("High Fashion", "high_fashion"),
        ("Home and Design", "home_and_design"),
        ("Impressionists", "impressionists"),
        ("Magicians", "magicians"),
        ('Model', 'model'),
        ("Motivational Speakers", "motivational_speakers"),
        ('Musician', 'musician'),
        ("News", "news"),
        ("Pageants", "pageants"),
        ("Photographers", "photographers"),
        ("Podcast", "podcast"),
        ("Poker", "poker"),
        ("Politics", "politics"),
        ("Radio", "radio"),
        ('Reality TV', 'reality_tv'),
        ("Royals", "Royals"),
        ("Santas", "santas"),
        ('Sports Commentator', 'sports_Commentator'),
        ("Stylists", "stylists"),
        ("TV Hosts", "tv_hosts"),
        ("Tarot Card Reader", "tarot_card_reader"),
        ("Venture Capitalists", "venture_capitalists"),
        ("Viral", "viral"),
        ("Radio", "radio"),
        ("Writers", "writers"),
    ]
    delivery_duration_unit_choice = [
        ("Hr", 'hr'),
        ("Day", 'day'),
        ("Week", 'week'),
    ]
    currency_code_symbols = [('USD', "$"), ('INR', "₹"), ('GBP', "£"),
                             ('EUR', "€")]
    is_celebrity = models.BooleanField(default=False)
    category = models.CharField(choices=category_choice,
                                max_length=100,
                                null=True)
    delivery_duration = models.IntegerField(null=True)
    price = models.FloatField(null=True)
    currency_code = models.CharField(max_length=10,
                                     choices=currency_code_symbols,
                                     null=True)
    delivery_duration_unit = models.CharField(
        max_length=10, null=True, choices=delivery_duration_unit_choice)
    image = models.ImageField(upload_to='cameo')
    intro = models.CharField(max_length=500, null=True)
    bio = models.CharField(max_length=2000, null=True)
    paypal_email = models.EmailField(null=True)
    is_featured = models.BooleanField(null=True, blank=True, default=False)
    reviews = JSONField(default=[])
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)], blank=True, null=True)
    fans = models.IntegerField(default=0)


class CameoSerializer(ModelSerializer):
    class Meta:
        model = Cameo
        exclude = []


class Review(models.Model):
    cameo = models.ForeignKey(Cameo, related_name="user_review", on_delete=models.CASCADE)
    user = models.CharField(max_length=256)
    review = models.CharField(max_length=1000)