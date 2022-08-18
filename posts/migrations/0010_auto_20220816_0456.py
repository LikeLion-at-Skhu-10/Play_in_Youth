# Generated by Django 3.2.6 on 2022-08-15 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_post_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cmt_postid', to='posts.post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.BigAutoField(help_text='post_id', primary_key=True, serialize=False),
        ),
    ]
