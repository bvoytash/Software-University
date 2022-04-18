from django import forms

from examWeb.web.models import Profile, Album


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Age'}),
        }


class CreateAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'album_name': forms.TextInput(attrs={'placeholder': 'Album Name'}),
            'artist': forms.TextInput(attrs={'placeholder': 'Artist'}),
            'description': forms.TextInput(attrs={'placeholder': 'Description'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Image URL'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Price'}),
        }


class EditAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'


class DeleteAlbumForm(CreateAlbumForm):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.disable_fields()

        def disable_fields(self):
            for _, field in self.fields.items():
                field.widget.attrs["disabled"] = True
                field.widget.attrs["readonly"] = True
