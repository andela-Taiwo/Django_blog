from django import forms
from markdownx.fields import MarkdownxFormField

from .models import Comment


class CommentForm(forms.ModelForm):
    message = MarkdownxFormField()
    parent = forms.CharField(widget=forms.HiddenInput(
                                attrs={'class': 'parent'}), required=False)

    class Meta:
        model = Comment
        fields = ["message"]

    def clean_message(self):
        title = self.cleaned_data.get("message")
        return title
