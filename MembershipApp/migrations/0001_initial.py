# Generated by Django 3.2.7 on 2021-10-02 19:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('MemberId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('MemberFirstName', models.CharField(max_length=500)),
                ('MemberLastName', models.CharField(max_length=500)),
                ('MemberDateOfBirth', models.DateField()),
                ('MemberCountry', models.CharField(max_length=500)),
            ],
        ),
    ]
