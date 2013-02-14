from django.db import models

# Create your models here.

class Type(models.Model):
    name=models.CharField(max_length=20)
    ext=models.CharField(max_length=5)
    
    def __unicode__(self):
        return self.name
    
class File(models.Model):
    
    def get_upload_dir(instance, filename):                             #@NoSelf
        name='.'.join(filename.split('.')[:-1])
        ext=filename.split('.')[-1]
        #generate random filename
        import uuid
        return '%s.%s.%s' % (name, uuid.uuid4(), ext)
    
    name=models.FileField(upload_to=get_upload_dir )
    size=models.DecimalField(max_digits=10, decimal_places=2, null=True)
    type=models.ForeignKey(Type, null=True)
    date=models.DateField("Uploaded On", auto_now_add=True)

    def __unicode__(self):
        return ' / '.join(str(self.name).split('/')[-3:])