from django.db import models

# Create your models here.
class BukuTamu(models.Model):

    KEPERLUAN_CHOICES = (
        ('Kunjungan', 'Kunjungan'),
        ('Magang', 'Magang'),
        ('Permohonan Informasi', 'Permohonan Informasi'),
        ('Lainnya', 'Lainnya')
    )

    nama = models.CharField(max_length=100)
    alamat = models.CharField(max_length=100)
    telepon = models.CharField(null=True, max_length=100)
    email = models.EmailField(max_length=100)
    instansi = models.CharField(max_length=100)
    tanggal = models.DateField(null=True)
    keperluan = models.CharField(choices=KEPERLUAN_CHOICES, max_length=100)
    keperluan_lainnya = models.CharField(max_length=100, blank=True, default=" ")

