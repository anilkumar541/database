from django.contrib import admin

# Register your models here.

from myapp.models import Student, Teacher

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display =["id", "name", "roll_no"]
    

@admin.register(Teacher)    
class TeacherAdmin(admin.ModelAdmin):
    list_display =["id", "name", "student"]

    # def get_student(self, obj):
    #     return "\n".join([str(p) for p in obj.student.all()])