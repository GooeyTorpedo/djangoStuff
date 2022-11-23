from socket import fromshare
from django import forms
from blog.models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author', 'title', 'text') #connect field we want to edit

        widget = {
            # 'fieldName': forms.TypeOfWidget(attrs = ....)
            'title': forms.TextInput(attrs={'class': 'textinputclass'}), #textinputclass is a CSS styling
            'text': forms.Textarea(attrs={'class':'editables medium-editor-textarea postcontent'})
        }
    
class CommentForm(forms.ModelForm):
    
    class Meta():
        model = Comment
        fields= ('author', 'text')