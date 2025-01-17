from django.db import models

# Create your models here.
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