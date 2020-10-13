from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

class Upload(models.Model):
    quality=models.IntegerField(default=40,blank=True,help_text='Enter the number between 0 to 100, lower number=higher compression.')
    image =models.ImageField(upload_to = '',blank=False,null=True)
    def save(self, *args, **kwargs):
        if not self.id:
            self.image = self.compressImage(self.image,self.quality)
        super(Upload, self).save(*args, **kwargs)
    def compressImage(self,image,quality):
        imageTemproary = Image.open(image)
        imageTemproary=imageTemproary.convert('RGB')
        outputIoStream = BytesIO()
        imageTemproary.save(outputIoStream , format='JPEG', quality=quality)
        outputIoStream.seek(0)
        image = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" % image.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
        return image
    
    def delete(self, *args, **kwargs):
        self.image.delete()
        super(Upload, self).delete(*args, **kwargs)

