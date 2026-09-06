from django import forms
from cities.models import City


class CityContactForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['phone', 'address', 'price_text']




class CityAdminForm(forms.ModelForm):

    copy_structure = forms.BooleanField(
        required=False,
        label='Скопировать структуру Москвы'
    )

    class Meta:
        model = City
        fields = '__all__'

    from django import forms
from cities.models import City


class CityContactForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['phone', 'address', 'price_text']




class CityAdminForm(forms.ModelForm):

    copy_structure = forms.BooleanField(
        required=False,
        label='Скопировать структуру Москвы'
    )

    class Meta:
        model = City
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Перебираем все поля формы и делаем короткие текстовые поля длинными
        for field_name, field in self.fields.items():
            # Проверяем, является ли виджет полем ввода (TextInput)
            if isinstance(field.widget, (forms.TextInput, forms.Textarea)):
                field.widget.attrs.update({
                    # Устанавливаем ширину на 100% контейнера с ограничением max-width,
                    # чтобы на широких экранах инпуты не растягивались до бесконечности
                    'style': 'width: 100%; min-width: 450px; max-width: 850px;',
                    'class': 'form-control' # Родной класс Bootstrap 4, который использует Jazzmin
                })

        


