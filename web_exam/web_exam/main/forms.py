from django import forms

from web_exam.main.models import Profile, Game


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('email', 'age', 'password')
        widgets = {
            'password': forms.PasswordInput(),
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CreateGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'


class EditGameForm(CreateGameForm):
    pass


class DeleteGameForm(CreateGameForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.disable_fields()

    def disable_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs["disabled"] = True
            field.widget.attrs["readonly"] = True
