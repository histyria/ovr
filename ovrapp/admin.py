from django.contrib import admin


from .models import section_list , Type_of_person_involved , Type_of_involved , Order

model = (  section_list , Type_of_person_involved , Type_of_involved , Order)

admin.site.register(model)