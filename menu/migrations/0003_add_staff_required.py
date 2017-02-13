from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='staff_required',
            field=models.BooleanField(default=False, help_text='Should this item only be shown to members of staff?', verbose_name='Staff required'),
        ),
    ]
