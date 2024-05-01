from django.contrib import admin
from django.utils.html import mark_safe
from .models import Category, Course, Lesson, User, Tag, Comment, Like
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
import cloudinary


class MyCourseAdminSite(admin.AdminSite):
    site_header = 'eCourseOnline'


admin_site = MyCourseAdminSite(name='iCourse')

class CourseForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Course
        fields = '__all__'


class MyCourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_date', 'updated_date', 'active']
    search_fields = ['name', 'description']
    list_filter = ['id', 'created_date', 'name']
    readonly_fields = ['my_image']
    form = CourseForm

    def my_image(self, course):
        if course.image:
            if type(course.image) is cloudinary.CloudinaryResource:
                return mark_safe(f"<img width='300' src='{course.image.url}' />")
            return mark_safe(f"<img width='300' src='/static/{course.image.name}' />")

    class Media:
        css = {
            'all': ('/static/css/style.css',)
        }


admin_site.register(Category)
admin_site.register(Lesson)
admin_site.register(User)
admin_site.register(Tag)
admin_site.register(Course, MyCourseAdmin)
admin_site.register(Comment)
admin_site.register(Like)
