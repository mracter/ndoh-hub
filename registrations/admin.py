from django.contrib import admin
from .models import Source, Registration, SubscriptionRequest


class RegistrationAdmin(admin.ModelAdmin):
    list_display = [
        "id", "reg_type", "validated", "registrant_id", "source",
        "created_at", "updated_at", "created_by", "updated_by"]
    list_filter = ["source", "validated", "created_at"]
    search_fields = ["registrant_id", "to_addr"]


class SubscriptionRequestAdmin(admin.ModelAdmin):
    list_display = [
        "id", "identity", "messageset", "next_sequence_number", "lang",
        "schedule", "created_at", "updated_at"]
    list_filter = ["messageset", "created_at"]
    search_fields = ["identity"]


admin.site.register(Source)
admin.site.register(Registration, RegistrationAdmin)
admin.site.register(SubscriptionRequest, SubscriptionRequestAdmin)
