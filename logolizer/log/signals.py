from django.db.models.signals import post_save
from django.dispatch import receiver
from logolizer.log.tasks import parse
from logolizer.log.models import Log

@receiver(post_save, sender=Log)
def parse_log(sender, **kwargs):
  instance = kwargs['instance']
  parse.delay(instance.id)
