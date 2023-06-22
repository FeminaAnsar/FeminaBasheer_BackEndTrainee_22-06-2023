from django.forms import ModelForm
from .models import Book,Author

class CreateBook(ModelForm):
    class Meta:
        model=Book
        fields='__all__'


class CreateAuthor(ModelForm):
    class Meta:
        model=Author
        fields='__all__'