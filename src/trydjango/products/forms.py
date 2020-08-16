from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title         = forms.CharField(label='', widget=forms.TextInput(attrs={
                                                    "placeholder":"Your Title"
    }))
    description   = forms.CharField(required=False, widget=forms.Textarea(
                                                        attrs={
                                                            "class":"1 2",
                                                            "id"   : "desc-form",
                                                            "rows" : 10,
                                                            "cols" : 30,
    }
    )
    )
    price         = forms.DecimalField(initial=199.99)
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self, *args, **kwargs):
        title  =  self.cleaned_data.get("title")
        if 'CFE' in title:
            return title
        else:
            raise forms.ValidationError("This is not a valid title")

class RawProductForm(forms.Form):
    title         = forms.CharField(label='', widget=forms.TextInput(attrs={
                                                    "placeholder":"Your Title"
    }))
    description   = forms.CharField(required=False, widget=forms.Textarea(
                                                        attrs={
                                                            "class":"1 2",
                                                            "id"   : "desc-form",
                                                            "rows" : 10,
                                                            "cols" : 10,
    }
    )
    )
    price         = forms.DecimalField(initial=199.99)
    