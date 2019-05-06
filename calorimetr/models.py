from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from math import *
from django.contrib.auth.models import User


class UserProfile(models.Model):
    SEX_LIST = (
        ('W', 'Женский'),
        ('M', 'Мужской'),
    )
    ACTIVITY_LIST = (
        ('Min', 'Минимальная активность'),
        ('W', 'Слабая активность'),
        ('Med','Средняя активность'),
        ('H','Высокая активность'),
        ('E','Экстра-активность'),
    )
    DIET_LIST = (
        ('L', 'Потеря веса'),
        ('K', 'Поддержание веса'),
        ('I','Набор веса'),
    )
    user = models.OneToOneField(User)
    height = models.IntegerField(default = 0)
    wish_weight = models.IntegerField(default = 0)
    age = models.IntegerField(default = 10,
    validators=[
            MaxValueValidator(100),
            MinValueValidator(10)
        ])
    activity = models.CharField(max_length=3, choices=ACTIVITY_LIST)
    sex = models.CharField(max_length=1, choices=SEX_LIST)
    diet = models.CharField(max_length=1, choices=DIET_LIST)

    def get_rsk(self):
        A={
            'Min': 1.2,
            'W': 1.375,
            'Med':1.55,
            'H':1.725,
            'E':1.9,
        }
        S={
            'M': 5,
            'W': -161,
        }
        D={
            'L': 0.8,
            'K': 1,
            'I': 1.2,
        }

        return floor(( 10 * self.weight() + 6.25 * self.height - 5 * self.age + S[self.sex]) * A[self.activity] * D[self.diet])

    def weight(self):
        weight_list=list(self.userweight_set.all().order_by('-date'))
        if not weight_list:
            return 0
        return weight_list[0].weight

    def __str__(self):
        return self.user.username


class UserWeight(models.Model):
    weight = models.IntegerField(default = 0)
    date = models.DateField();
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.user.username

class Eating(models.Model):
    name = models.CharField(max_length = 50)
    date = models.DateTimeField();
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    #is_using_now= models.BooleanField(default=False)
    def get_calorie(self):
        sum=0
        for d in self.dish_set.all():
            sum += d.calorie*d.portion/100
        return floor(sum)
    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length = 20)
    portion = models.IntegerField(default = 0)
    calorie = models.IntegerField(default = 0)
    fat = models.IntegerField(default = 0)
    carbohydrates = models.IntegerField(default = 0)
    protein = models.IntegerField(default = 0)
    eating = models.ManyToManyField(Eating)
    def __str__(self):
        return self.name
    #eat = models.ForeignKey(Eat, on_delete=models.CASCADE)
