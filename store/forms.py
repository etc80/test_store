import django.forms as forms
from django.contrib.auth.models import User
from store.models import Product
# from blog.models import Article


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
        "productname",
        "desc",
        "price",
        "producer",
        "category" ,
        "subcategory",
        "available",
        "image"
        )

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=20)
#     desc = forms.CharField(widget=forms.Textarea)
#     author_id = forms.IntegerField()


# class ArticleForm(forms.ModelForm):
#     class Meta:
#         model = Article
#         fields = ('title', 'desc', 'author_id')
#         # fields = '__all__'
