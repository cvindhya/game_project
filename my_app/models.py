from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.



class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth= models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save


class game(models.Model):
    game_id= models.AutoField(primary_key=True)
    game_name= models.CharField(max_length=255)

    def __str__(self):
        return self.game_name
    



    