from django.db import models


class DataFrame(models.Model):
    ai_id = models.AutoField(primary_key=True)
    id = models.IntegerField()
    temp = models.FloatField()
    humidity = models.IntegerField()
    pressure = models.IntegerField()
    co2 = models.IntegerField()
    co = models.IntegerField()
    time = models.TimeField()
    charge = models.IntegerField()

    def __str__(self):
        return "ai_id:{}; id:{}; temp:{}; hum:{}; prs:{}; co2:{}; co:{}; charge:{}". \
            format(self.ai_id, self.id, self.temp, self.humidity, self.pressure, self.co2, self.co, self.charge)

    class Meta:
        ordering = ["id", "temp", "humidity", "pressure", "co2", "co", "charge", "ai_id"]


class ActionFrame(models.Model):
    ai_id = models.AutoField(primary_key=True)
    id = models.IntegerField()
    action = models.CharField(max_length=255)
