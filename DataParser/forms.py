from django                 import forms
from django.core.exceptions import ValidationError
from pandas                 import read_excel

class ExcelForm(forms.Form):
    excel_file = forms.FileField()
    def clean(self):
        cd = self.cleaned_data
        try:
            df = read_excel(cd['excel_file'], sheet_name=None, engine=None)
        except:
            raise ValidationError("Invalid file.", code='Invalid')
        return df
        