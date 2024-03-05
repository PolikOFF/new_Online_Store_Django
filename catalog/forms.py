from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):

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

