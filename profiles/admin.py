from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    """ Class to allow admin to view orders """
    model = UserProfile
    readonly_fields = ('user',)

    fields = ('user', 'default_phone_number', 'default_street_address1', 'default_street_address2',
              'default_town_or_city', 'default_county', 'default_postcode',
              'default_country', 'dob', 'health_conditions',
              'active_class_package', 'class_package_type', 'class_tokens',
              'package_expiry',)

    list_display = ('user', 'dob', 'active_class_package',
                    'default_phone_number',)

    ordering = ('user',)

admin.site.register(UserProfile, UserProfileAdmin)
