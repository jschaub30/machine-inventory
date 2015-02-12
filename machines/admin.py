from django.contrib import admin
from machines.models import Rack, RackPosition, NetworkSpeed, NetworkSwitch, Machine

admin.site.register(Rack)
admin.site.register(RackPosition)
admin.site.register(NetworkSpeed)
admin.site.register(NetworkSwitch)
admin.site.register(Machine)
