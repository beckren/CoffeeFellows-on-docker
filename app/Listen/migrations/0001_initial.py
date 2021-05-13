# Generated by Django 3.1.7 on 2021-03-20 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ListenEinheit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('einheit_bezeichnung', models.TextField()),
            ],
            options={
                'db_table': 'Listen_einheit',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ListenProdukt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produkt_bezeichnung', models.TextField()),
            ],
            options={
                'db_table': 'Listen_produkt',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Einheit',
            fields=[
                ('einheit_id_pkey', models.AutoField(primary_key=True, serialize=False)),
                ('einheit_bezeichnung', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'tbl_einheit',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Mitarbeiter',
            fields=[
                ('mitarbeiter_id_pkey', models.AutoField(primary_key=True, serialize=False)),
                ('mitarbeiter_vorname', models.CharField(blank=True, max_length=100, null=True)),
                ('mitarbeiter_nachname', models.CharField(blank=True, max_length=100, null=True)),
                ('mitarbeiter_bezeichnung', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'tbl_mitarbeiter',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Standorte',
            fields=[
                ('standort_id_pkey', models.AutoField(primary_key=True, serialize=False)),
                ('standorte_bezeichnung', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'tbl_standorte',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Produkt',
            fields=[
                ('produkt_id_pkey', models.AutoField(primary_key=True, serialize=False)),
                ('produkt_bezeichnung', models.CharField(blank=True, max_length=100, null=True)),
                ('produkt_einheit_id_fkey', models.ForeignKey(db_column='produkt_einheit_id_fkey', on_delete=django.db.models.deletion.DO_NOTHING, to='Listen.einheit')),
            ],
            options={
                'db_table': 'tbl_produktion',
                'managed': True,
            },
        ),
    ]
