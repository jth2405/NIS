from django.contrib import admin
from .models import Boards

# Register your models here.
admin.site.register(Boards)
admin.site.register(BoardCategories)
admin.site.register(BoardReplies)
admin.site.register(BoardLikes)
admin.site.register(User)

class BoardsAdmin(admin.ModelAdmin):
    list_display=('id','title')
    fields=('title','content')

admin.site.register(Boards,BoardsAdmin)