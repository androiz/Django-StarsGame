from django.contrib import admin
from models import Race, UserProfile, Unit, Building, GeneralTechnology, Thematic, Resource, RelationGeneralTechnologiesUsers, RelationUnitsUsers, \
    RelationResourcesUsers, RelationBuildingsUsers

# Register your models here.

class ThematicAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )

class RaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'thematic',)
    search_fields = ('name', )
    list_filter = ('thematic',)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'race', 'thematic',)
    search_fields = ('user', 'race', )
    list_filter = ('race', 'thematic')

class UnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'race', 'thematic',)
    search_fields = ('name', 'race', )
    list_filter = ('race', 'thematic')

class BuildingAdmin(admin.ModelAdmin):
    list_display = ('name', 'race', 'thematic',)
    search_fields = ('name', 'race', )
    list_filter = ('race', 'thematic')

class GeneralTechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'thematic',)
    search_fields = ('name', )
    list_filter = ('thematic',)

class ResourcesAdmin(admin.ModelAdmin):
    list_display = ('name', 'thematic',)
    search_fields = ('name', )
    list_filter = ('thematic',)

class ResourcesUsersAdmin(admin.ModelAdmin):
    list_display = ('user', 'resource',)
    search_fields = ('user', 'resource', )

class UnitsUsersAdmin(admin.ModelAdmin):
    list_display = ('user', 'unit',)
    search_fields = ('user', 'unit', )

class BuildingsUsersAdmin(admin.ModelAdmin):
    list_display = ('user', 'building',)
    search_fields = ('user', 'building', )

class GeneralTechnologiesUsersAdmin(admin.ModelAdmin):
    list_display = ('user', 'technology',)
    search_fields = ('user', 'technology', )

admin.site.register(Race, RaceAdmin)
admin.site.register(Resource, ResourcesAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Building, BuildingAdmin)
admin.site.register(GeneralTechnology, GeneralTechnologyAdmin)
admin.site.register(Thematic, ThematicAdmin)

admin.site.register(RelationResourcesUsers, ResourcesUsersAdmin)
admin.site.register(RelationUnitsUsers, UnitsUsersAdmin)
admin.site.register(RelationBuildingsUsers, BuildingsUsersAdmin)
admin.site.register(RelationGeneralTechnologiesUsers, GeneralTechnologiesUsersAdmin)