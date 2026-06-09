from django.core.management.base import BaseCommand
from branches_app.models import Branch

class Command(BaseCommand):
    help = "Заповнити БД тестовими філіями"

    def handle(self, *args, **options):
        if Branch.objects.exists():
            self.stdout.write("Дані вже є, пропускаю.")
            return
        Branch.objects.bulk_create([
            Branch(name="Головна філія", address="Київ, Хрещатик 1", phone="+380441234567"),
            Branch(name="Львівська філія", address="Львів, Свободи 10", phone="+380322345678"),
            Branch(name="Одеська філія", address="Одеса, Дерибасівська 5", phone="+380487654321"),
        ])
        self.stdout.write(self.style.SUCCESS("Готово."))
