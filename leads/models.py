from django.db.models import Model, CharField, IntegerField, BooleanField, ImageField, FileField


class Lead(Model):
    SOURCE_CHOICES = (
        ('Youtube', 'Youtube'),
        ('Google', 'Google'),
        ('Newsletter', 'Newsletter')
    )

    first_name = CharField(max_length=20)
    last_name = CharField(max_length=20)
    age = IntegerField(default=0)

    phoned = BooleanField(default=False)
    source = CharField(choices=SOURCE_CHOICES, max_length=100)

    profile_picture = ImageField(blank=True, null=True)
    special_files = FileField(blank=True, null=True)




