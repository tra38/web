# Generated by Django 2.0.4 on 2018-04-30 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0063_add_interest_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='bounty',
            name='token_value_in_usdt',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50, null=True),
        ),
        migrations.AddField(
            model_name='bounty',
            name='token_value_time_peg',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bounty',
            name='value_in_eth',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50, null=True),
        ),
        migrations.AddField(
            model_name='bounty',
            name='value_in_usdt',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50, null=True),
        ),
        migrations.AddField(
            model_name='bounty',
            name='value_in_usdt_now',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50, null=True),
        ),
        migrations.AddField(
            model_name='bounty',
            name='value_true',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50, null=True),
        ),
    ]
