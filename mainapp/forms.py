from django import forms

class LocationsForm(forms.Form):
        photo = forms.ImageField(label='Фото', required=False)
        title = forms.CharField(label='Назва', max_length=50)
        typeplace = forms.CharField(label='Тип місця')
        location = forms.CharField(label='Локація', required=True)
        rating = forms.IntegerField(label='Рейтинг', min_value=1, max_value=5)
        date = forms.DateField(label='Дата створення відгуку', widget=forms.DateInput(attrs={'type': 'date'}))
        text = forms.CharField(label='Опис', widget=forms.Textarea)

