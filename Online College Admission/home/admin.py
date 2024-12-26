from django.contrib import admin

# Register your models here.

#dummy
#from home.models import Post

#admin.site.register(Post)

#dummy1
from home.models import Contact, Destination

admin.site.register(Contact)
admin.site.register(Destination)