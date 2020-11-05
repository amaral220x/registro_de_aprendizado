from django.contrib import admin

# Importando os modelos
from learning_logs.models import Topic
from learning_logs.models import Entry

#Registrando os modelos
admin.site.register(Topic)
admin.site.register(Entry)