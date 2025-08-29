from django.db import models

class Bill(models.Model):
    image = models.ImageField(upload_to='bills/')
    raw_text = models.TextField(blank=True, null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Bill {self.id} @ {self.created_at}"
