from django.contrib     import admin, messages
from django.shortcuts   import render, redirect
from django.urls        import path
from Api.models         import Variable, WorldData
from .forms             import ExcelForm
from .parser            import parse_excel

@admin.register(WorldData, Variable)
class WorldDataAdmin(admin.ModelAdmin):
    change_list_template = 'DataParser/changelist.html'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('import-excel/', self.import_excel),
        ]
        return  custom_urls + urls
    
    def import_excel(self, request):

        if request.method == 'POST':
            form = ExcelForm(request.POST, request.FILES)
            if form.is_valid():
                updated, errors = parse_excel(form.cleaned_data)
                self.message_user(request, f"Succesful import. Updated {updated} / {updated + errors} rows.", messages.SUCCESS)
                return redirect('..')
            else:
                self.message_user(request, "File type not supported.", messages.ERROR)
                return render(
                    request, 'DataParser/excel_form.html', {'form': form}
                )
        else:
            form = ExcelForm()
            return render(
                request, 'DataParser/excel_form.html', {'form': form}
            )