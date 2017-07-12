from django.db import models
from django.contrib.postgres.fields import ArrayField

class Delta(models.Model):
    lattice = ArrayField(
        ArrayField(
            models.FloatField(),
            size=40,
        ),
        size=60,
    )
    ts = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = (('-ts'),)

    # def notify(self):
    #     print('Feedback.notify')
    #     if not Notifier.objects.exists():
    #         return
    #
    #     notifier = Notifier.objects.first()
    #     notifier.notify(self)

    def __str__(self):
        return "{}".format(self.ts)
