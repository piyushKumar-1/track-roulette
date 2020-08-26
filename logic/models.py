from django.db import models



class EntriesModel(models.Model):
    number =  models.IntegerField()
    clr = models.CharField(max_length=20)
    gametype = models.CharField(max_length=50, default="color-based")
    playedTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.number)+self.clr
# Create your models here.

class SaveRecords(models.Model):
	number =  models.IntegerField()
	clr = models.CharField(max_length=20)
	gametype = models.CharField(max_length=50, default="color-based")
	playedTime = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return str(self.number)+self.clr