from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=50)
    roll_no=models.IntegerField(null=False)

    class Meta:
        db_table = 'students'

    def __str__(self):
        return self.name    

class Teacher(models.Model):
    name = models.CharField(max_length=88)
    student=models.ForeignKey(Student, on_delete=models.CASCADE)

    class Meta:
        db_table = 'teachers'

    def __str__(self):
        return self.name  