from django.forms import Form, CharField, FileField


class UploadFileForm(Form):
    name = CharField(max_length=100)
    file = FileField()
