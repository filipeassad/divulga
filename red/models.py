from django.db import models

class video_canal(models.Model):

    codigo = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=250)
    link = models.CharField(max_length=500)

    def __str__(self):
        return self.codigo.__str__() + " - " + self.titulo.encode('utf8')

    def publish(self):
        self.save()

class video_site(models.Model):

    codigo = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=250)
    link = models.CharField(max_length=500)
    link_gif = models.CharField(max_length=500)

    def __str__(self):
        return self.codigo.__str__() + " - " + self.titulo.encode('utf8')

    def publish(self):
        self.save()




