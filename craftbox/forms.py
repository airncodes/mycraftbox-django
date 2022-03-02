from django.forms import ModelForm, CheckboxSelectMultiple

from .models import Link


class CustomEditLinkForm(ModelForm):
    class Meta:
        model = Link
        fields = ("link_name", "link_path", "image", "notes", "tags")
        widgets = {
            "tags": CheckboxSelectMultiple(),
        }

