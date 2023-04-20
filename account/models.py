from django.db import models
from django.contrib.auth.models import User
# Create your models here.
education = (
    ('NURSERY', 'NURSERY'), 
    ('PRIMARY', 'PRIMARY'), ('SECONDARY', 'SECONDARY'), ('DEGREE', 'DEGREE'), ('MASTERS', 'MASTERS'), ('PHD','PHD')
)
ids = (
    ('NATIONAL IDENTIFICATION CARD','NATIONAL IDENTIFICATION CARD'), ('VOTERS CARD','VOTERS CARD'),('DRIVERS LICENSE','DRIVERS LICENSE'),
('PASSPORT','PASSPORT')
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)    
    other_names = models.CharField(max_length=20, null=True)
    profile_pics = models.ImageField(default='', upload_to='pics', null=True)
    email = models.EmailField(default='', null=True)
    phone_number = models.IntegerField(null=True)
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(max_length=20, choices=(('MALE', 'Male'),('FEMALE', 'Female')
    ), null=True)
    state_of_origin = models.CharField(max_length=100, null=True)
    lga_origin = models.CharField(max_length=100, null=True)
    scheme_name = models.CharField(max_length=100, null=True)
    year_of_application = models.CharField(max_length=4, null=True)
    residential_address = models.CharField(max_length=100, null=True)
    state_of_residence = models.CharField(max_length=20, null=True)
    lga_residence = models.CharField(max_length=100, null=True)
    highest_level_of_education = models.CharField(max_length=50, choices=education, null=True)
    id_type = models.CharField(max_length=100, choices=ids, null=True)
    id_number = models.IntegerField(null=True)
    id_image = models.ImageField(upload_to='pics')
    bvn = models.IntegerField(null=True)
    bank_account_number = models.IntegerField(null=True)
    bank_name = models.CharField(max_length=50, null=True)
    account_name = models.CharField(max_length=50, null=True)

    def __str__(self) -> str:
        return f'{self.user}'

