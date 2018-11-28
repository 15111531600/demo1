import datetime

from django.db import models


# Create your models here.
class User(models.Model):
    '''user data models'''

    SEX = (
        ('M', 'man'),
        ('F', 'woman'),
    )
    nickname = models.CharField(max_length=32, unique=True)
    phonenum = models.CharField(max_length=16, unique=True)
    sex = models.CharField(max_length=8, choices=SEX)
    birth_year = models.IntegerField()
    birth_month = models.IntegerField()
    birth_day = models.IntegerField()
    avatar = models.CharField(max_length=256)
    location = models.CharField(max_length=32)

    @property
    def age(self):
        now = datetime.date.today()
        birth_date = datetime.date(self.birth_year, self.birth_month, self.birth_day)
        return (now - birth_date).days // 365

    @property
    def profile(self):
        '''
        user config
        :return: connect User and Profile without foreignkey
        '''
        if not hasattr(self,'_profile'):
            # add if to make when 'get_or create' on just once
            self._profile, _ = Profile.objects.get_or_create(id=self.id)
        return self._profile
        


class Profile(models.Model):
    '''user config'''

    SEX = (
        ('M', 'man'),
        ('F', 'woman'),
    )

    location = models.CharField(default='M', max_length=32, verbose_name='your location')

    min_distance = models.IntegerField(default=1, verbose_name='min distance')
    max_distance = models.IntegerField(default=10, verbose_name='max distance')

    min_dating_age = models.IntegerField(default=18, verbose_name='min age')
    max_dating_age = models.IntegerField(default=45, verbose_name='max age')

    dating_sex = models.CharField(max_length=8, choices=SEX, verbose_name='target sex')
    vibration = models.BooleanField(default=True, verbose_name='is not take on vibration')
    only_matche = models.BooleanField(default=False, verbose_name='is not for other')
    auto_play = models.BooleanField(default=False, verbose_name='is not auto play video')
