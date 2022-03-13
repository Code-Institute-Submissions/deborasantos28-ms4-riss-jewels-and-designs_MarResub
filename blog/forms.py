from django import forms

# Imported from products app
from products.widgets import CustomClearableFileInput
from .models import Comment, BlogPost


class BlogPostForm(forms.ModelForm):
    '''A function allows the Blog form to be displayed'''
    class Meta:
        '''Meta class for BlogPosts'''
        model = BlogPost
        fields = (
            "title",
            "image",
            "content",
        )

    image = forms.ImageField(
        label="Image", required=True, widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        """
        Function sets placeholders, adds auto-focus to top field
        and assigns all fields a class
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            "title": "Title",
            "image": "Image",
            "content": "Blog Content",
        }

        self.fields["title"].widget.attrs["autofocus"] = True
        for field in self.fields:
            if field != "image":
                self.fields[field].widget.attrs["placeholder"] = placeholders[field]
            self.fields[field].widget.attrs["class"] = "blog-form-input"


class CommentForm(forms.ModelForm):
    '''A function for the Comment Forms.
    This function is used to display the forms
    parameters on the page'''
    class Meta:
        '''Meta class for the comment form'''
        model = Comment
        fields = ("body",)

    def __init__(self, *args, **kwargs):
        """
        Function sets placeholder, removes auto-generated input label
        and assigns a class
        """
        super().__init__(*args, **kwargs)
        self.fields["body"].widget.attrs[
            "placeholder"
        ] = "Write your comment here... (500 characters max)."
        self.fields["body"].label = False
        self.fields["body"].widget.attrs["class"] = "comment-form-input"
