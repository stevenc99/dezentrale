# Generated by Django 2.0.8 on 2018-11-26 19:15

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatenschutzPage',
            fields=[
                ('page_ptr', models.OneToOneField(
                    auto_created=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    parent_link=True, primary_key=True, serialize=False,
                    to='wagtailcore.Page')),
                ('content',
                 wagtail.core.fields.StreamField(
                     (('Datenschutzerklaerung',
                       wagtail.core.blocks.RichTextBlock()),))),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
