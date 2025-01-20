from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.conf import settings

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

class MySessions(models.Model):
    session_id = models.AutoField(primary_key=True)
    username = models.ForeignKey(Users,on_delete=models.CASCADE,db_column='username')
    date_of_session = models.DateField()
    pre_made = models.IntegerField()
    check_in_time = models.DateTimeField()
    check_out_time = models.DateTimeField()

    class Meta:
        db_table = "my_sessions"
        managed = False

    def __str__(self):
        return str(self.session_id)

class ExerciseTypes(models.Model):
    type_name = models.CharField(primary_key=True,max_length=255)

    class Meta:
        db_table = "exercise_types"
        managed = False

    def __str__(self):
        return self.type_name

class Exercises(models.Model):
    exercise_name = models.CharField(primary_key=True, max_length=255)
    type_name = models.ForeignKey(ExerciseTypes,on_delete=models.CASCADE,db_column="type_name")
    description = models.TextField()

    class Meta:
        db_table = "exercises"
        managed = False

    def __str__(self):
        return self.exercise_name

class SessionExercises(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.ForeignKey(Users,on_delete=models.CASCADE,db_column='username')
    session_id = models.ForeignKey(MySessions,on_delete=models.CASCADE,db_column='session_id')
    exercise_name = models.ForeignKey(Exercises,on_delete=models.CASCADE,db_column='exercise_name')
    set_number = models.IntegerField()
    reps = models.IntegerField()
    weight = models.IntegerField()
    unit = models.CharField(max_length=255)

    class Meta:
        db_table = "session_exercises"
        managed = False

    def __str__(self):
        return str(self.id) 