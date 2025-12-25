from django.db import models

class Bank(models.Model):
    bank_id = models.IntegerField(primary_key=True)  # CSV/user ka ID
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Branch(models.Model):
    bank = models.ForeignKey(
        Bank,
        on_delete=models.CASCADE,
        related_name="branches"
    )
    ifsc = models.CharField(max_length=20, unique=True)
    branch = models.CharField(max_length=255)
    address = models.TextField()
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return self.ifsc
