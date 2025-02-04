import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models




class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('books', '0003_book_total_sales'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]
    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('sale_date', models.DateTimeField(auto_now_add=True)),
                ('book',
                models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales', to='books.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales',to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]