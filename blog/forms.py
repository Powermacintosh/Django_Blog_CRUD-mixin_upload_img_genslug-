from django import forms
from .models import Post, Tag
from django.core.exceptions import ValidationError
 
class PostForm(forms.ModelForm):
 
    class Meta:
        model = Post
        fields = ['title', 'body', 'tags', 'image']
        
        widgets = {
        	'title': forms.TextInput(attrs={'class': 'form-control'}),
        	'body': forms.Textarea(attrs={'class': 'form-control'}),
        	'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        	'image': forms.ClearableFileInput(attrs={'multiple': True}),
        	}

    def clean_slug(self):
    	new_slug = self.cleaned_data['slug'].lower()
    	if new_slug == 'create':
    		raise ValidationError('Slug may not be "Create"')
    	return new_slug


class TagForm(forms.ModelForm):
	class Meta:
		model = Tag
		fields = ['title']

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
		}

	def clean_slug(self):
		new_slug = self.cleaned_data['slug'].lower()

		if new_slug == 'create':
			raise ValidationError('Slug may not be "Create"')
		if Tag.objects.filter(slug__iexact=new_slug).count():
			raise ValidationError('Slug must be unique. We have "{}" slug already'.format(new_slug))
		return new_slug