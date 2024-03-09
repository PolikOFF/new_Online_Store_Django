from django import forms

from catalog.models import Product, Version


class StyleForMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleForMixin, forms.ModelForm):
    banned_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at',)

    def clean_name(self):
        """
        Метод для проверки валидации поля 'name',
        при появлении слова из списка исключений banned_words.
        """
        cleaned_name = self.cleaned_data['name']
        if cleaned_name.lower() in self.banned_words:
            raise forms.ValidationError(f'Недопустимое значение.\nСписок недопустимых слов: {self.banned_words}.')

        return cleaned_name

    def clean_description(self):
        """
        Метод для проверки валидации поля 'description',
        при появлении слова из списка исключений banned_words.
        """
        cleaned_data = self.cleaned_data['description']
        if cleaned_data in self.banned_words:
            raise forms.ValidationError(f'Недопустимое значение.\nСписок недопустимых слов: {self.banned_words}.')

        return cleaned_data


class VersionForm(StyleForMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
