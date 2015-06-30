from django.contrib import admin
from filer.admin import FileAdmin
from filer_pdf.models import PDF

admin.site.register(PDF, FileAdmin)
