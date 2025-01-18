from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=225, primary_key=True)
    person_name = models.CharField(max_length=225)
    email = models.EmailField(max_length=255, unique=True)
    mobile = models.CharField(max_length=255, unique=True)
    dob = models.DateField()
    password_hash = models.CharField(max_length=255)

    class Meta:
        db_table = "users"
        managed = False

    def set_password(self, raw_password):
        self.password_hash = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password_hash)

    def __str__(self):
        return self.username

class FAQs(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.TextField()
    answer = models.TextField()

    class Meta:
        db_table = "faqs"
        managed = False
    
    def __str__(self):
        return self.question

class Equipment(models.Model):
    equipment_name = models.CharField(max_length=255, primary_key=True)
    equipment_description = models.TextField()
    image_link = models.CharField(max_length=255)
    quantitiy = models.IntegerField()

    class Meta:
        db_table = "equipment"
        managed = False

    def __str__(self):
        return self.equipment_name