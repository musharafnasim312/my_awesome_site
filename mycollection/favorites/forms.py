from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import FavoriteThing

class FavoriteThingForm(forms.ModelForm):
    class Meta:
        model = FavoriteThing
        fields = ['name', 'category', 'why_awesome', 'image', 'rating']
        widgets = {
            'rating': forms.RadioSelect(choices=FavoriteThing.RATINGS),
        }

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100, required=False)
    category = forms.ChoiceField(
        label='Category',
        choices=[('', 'All')] + FavoriteThing.CATEGORIES,
        required=False
    )
    min_rating = forms.ChoiceField(
        label='Minimum Rating',
        choices=[('', 'Any')] + [(i, '⭐' * i) for i in range(1, 6)],
        required=False
    )

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email address is already in use.')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not match.')
        return password2