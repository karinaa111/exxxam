from django.db import models

class Branch(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=50)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "address": self.address, "phone": self.phone}

    def __str__(self):
        return self.name
