from django.contrib import admin
from one.models import *
# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    pass

class EmployeeAdmin(admin.ModelAdmin):
    pass

class AuthorAdmin(admin.ModelAdmin):
    pass

class PublisherAdmin(admin.ModelAdmin):
    pass

class BookAdmin(admin.ModelAdmin):
    pass

class StoreAdmin(admin.ModelAdmin):
    pass

admin.site.register(Author, AuthorAdmin)    
admin.site.register(Publisher, PublisherAdmin)

admin.site.register(Book, BookAdmin)    
admin.site.register(Store, StoreAdmin)

admin.site.register(Department, DepartmentAdmin)    
admin.site.register(Employee, EmployeeAdmin)