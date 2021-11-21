# Generated by Django 3.1.8 on 2021-11-20 23:21

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_user_pronouns'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpreferences',
            name='cc_add_subscriptions',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('email', 'Email'), ('slack', 'Slack Notification')], default='email', max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='userpreferences',
            name='cc_needed_subscriptions',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('email', 'Email'), ('slack', 'Slack Notification')], default=['email', 'slack'], max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='userpreferences',
            name='cc_report_reminders',
            field=models.CharField(choices=[('email', 'Email'), ('slack', 'Slack Notification'), ('all', 'Both')], default='email', max_length=12),
        ),
        migrations.AddField(
            model_name='userpreferences',
            name='event_edited_field_subscriptions',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('event_name', 'Event name'), ('description', 'Description'), ('location', 'Location'), ('contact', 'Contact'), ('billing_org', 'Billing org'), ('datetime_setup_complete', 'Datetime setup complete'), ('datetime_start', 'Datetime start'), ('datetime_end', 'Datetime end'), ('internal_notes', 'Internal notes'), ('billed_in_bulk', 'Billed in bulk'), ('org', 'Client')], default=['location', 'datetime_setup_complete', 'datetime_start', 'datetime_end'], max_length=137),
        ),
        migrations.AddField(
            model_name='userpreferences',
            name='event_edited_notification_methods',
            field=models.CharField(choices=[('email', 'Email'), ('slack', 'Slack Notification'), ('all', 'Both')], default='email', max_length=12),
        ),
        migrations.AddField(
            model_name='userpreferences',
            name='ignore_user_action',
            field=models.BooleanField(default=False, help_text='Uncheck this to ignore notifications for actions triggered by the user'),
        ),
    ]
