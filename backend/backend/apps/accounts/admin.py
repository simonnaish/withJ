from django.contrib import admin
from backend.apps.courses.models import Instructor, CourseType, Specialization, Client, ClientCourses

class ClientAdmin(admin.ModelAdmin):
    list_display = ("user",)

class ClientCoursesAdmin(admin.ModelAdmin):
    list_display = ("",)

class InstructorAdmin(admin.ModelAdmin):
    list_display = ("user",)

class CourseTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)

class SpecializationAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(Client, ClientAdmin)

admin.site.register(Instructor, InstructorAdmin)
# admin.site.register(ClientCourses, ClientCoursesAdmin)
admin.site.register(CourseType, CourseTypeAdmin)
admin.site.register(Specialization, SpecializationAdmin)