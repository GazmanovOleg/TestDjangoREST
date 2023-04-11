from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
import uuid

def width_or_height_vaildator(value):
    if value <= 20 or value%2 != 0:
        raise ValidationError(f'Число {value} невалидно.')
class File(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False )
    filename = models.CharField(max_length=255)
    video = models.FileField(upload_to='videos_uploaded', null=True,
                             validators=[FileExtensionValidator( allowed_extensions=['mp4'])])
    processing = models.BooleanField()
    processingSuccess = models.BooleanField(null=True)
    width = models.IntegerField(validators=[width_or_height_vaildator])
    height = models.IntegerField(validators=[width_or_height_vaildator])

    def __str__(self):
        return self.filename
