from django.contrib import admin

# Register your models here.

from .models import GSI, Lab, Section, Student, Part



class PartInline(admin.StackedInline):
    model = Part
    extra = 1

class StudentInline(admin.StackedInline):
    model = Student
    extra = 1

class SectionInline(admin.StackedInline):
    model = Section
    extra = 1


class LabAdmin(admin.ModelAdmin):
    inlines = [PartInline]


class SectionAdmin(admin.ModelAdmin):
    inlines = [StudentInline]


class GSIAdmin(admin.ModelAdmin):
    inlines = [SectionInline]

admin.site.register(Lab, LabAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(GSI, GSIAdmin)
admin.site.register(Student)