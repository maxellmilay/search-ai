# Generated by Django 4.2.6 on 2023-10-30 01:53

from django.db import migrations, models
import pgvector.django


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LangchainPgCollection',
            fields=[
                ('uuid', models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, null=True)),
                ('cmetadata', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'langchain_pg_collection',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LangchainPgEmbedding',
            fields=[
                ('uuid', models.UUIDField(primary_key=True, serialize=False)),
                ('embedding', pgvector.django.VectorField(dimensions=1536)),
                ('document', models.CharField(blank=True, null=True)),
                ('cmetadata', models.TextField(blank=True, null=True)),
                ('custom_id', models.CharField(blank=True, null=True)),
            ],
            options={
                'db_table': 'langchain_pg_embedding',
                'managed': False,
            },
        ),
    ]
