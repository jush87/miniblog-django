# Generated by Django 4.2.1 on 2023-05-22 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('text_comments', models.TextField(max_length=2000, verbose_name='Comments')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post', verbose_name='Record')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
    ]
