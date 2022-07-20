from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . forms import CeremonyForm
from . models import UserProfile, Ceremonies, CEREMONY_TYPES
# Register your models here.

class UserAdminConfig(UserAdmin):
    model = UserProfile
    search_fields = ('email', 'user_name', 'first_name',)
    list_filter = ('email', 'user_name', 'first_name', 'is_active', 'is_staff',
                    'has_psm1', 'has_psm2',)
    ordering = ('-start_date',)
    list_display = ('email', 'user_name', 'first_name', 'start_date', 'date_extended','subs_end_date',
                    'is_active', 'is_staff',)
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name','start_date','date_extended','subs_end_date',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('image','has_psm1','has_psm2',)}),
    )
    # formfield_overrides = {
    #     UserProfile.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    # }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'password1', 'password2', 
            'is_active', 'is_staff')}
         ),
    )
# class CeremonyChoicesAdmin(admin.ModelAdmin):
#     model = CeremonyChoices

class CeremoniesAdmin(admin.ModelAdmin):
    form = CeremonyForm
    # model = Ceremonies
    # search_fields = ('cer_date', 'user',)
    # ordering = ('-cer_date',)
    list_display = ('cer_date', 'user','ceremonies')
    # formfield_overrides = {
    #     Ceremonies.ceremonies: {'widget': forms.CheckboxSelectMultiple(choices=CEREMONY_TYPES)},
    # }

#admin.site.register(CeremonyChoices, CeremonyChoicesAdmin)
admin.site.register(UserProfile, UserAdminConfig)
admin.site.register(Ceremonies, CeremoniesAdmin)