from django import forms
from .models import Post
from django.contrib.auth.models import User
from django.utils.encoding import smart_text


class UserFullnameChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return smart_text(obj.get_full_name())


class PostForm(forms.ModelForm):
    author = UserFullnameChoiceField(queryset=User.objects.all())

    class Meta:
        model = Post
        fields = ['title', 'description', 'image_url', 'tags', 'posted_on']
