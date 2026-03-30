from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('skillsessions', '0003_sessionmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='sessionmessage',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
