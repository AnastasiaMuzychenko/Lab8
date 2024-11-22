from django.db import models


class Error(models.Model):
    LEVEL_CHOICES = [
        ("Критична", "Критична"),
        ("Важлива", "Важлива"),
        ("Незначна", "Незначна"),
    ]

    CATEGORY_CHOICES = [
        ("Інтерфейс", "Інтерфейс"),
        ("Дані", "Дані"),
        ("Розрахунковий алгоритм", "Розрахунковий алгоритм"),
        ("Інше", "Інше"),
        ("Невідома категорія", "Невідома категорія"),
    ]

    SOURCE_CHOICES = [
        ("Користувач", "Користувач"),
        ("Тестувальник", "Тестувальник"),
    ]

    description = models.TextField()
    received_date = models.DateField()
    error_level = models.CharField(max_length=10, choices=LEVEL_CHOICES)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    source = models.CharField(max_length=15, choices=SOURCE_CHOICES)

    def __str__(self):
        return f"Error {self.id}: {self.description[:50]}"


class Programmer(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Fix(models.Model):
    error = models.ForeignKey(Error, on_delete=models.CASCADE)
    start_date = models.DateField()
    duration = models.IntegerField()
    programmer = models.ForeignKey(Programmer, on_delete=models.CASCADE)
    daily_rate = models.DecimalField(max_digits=10, decimal_places=2)

    def total_cost(self):
        return self.duration * self.daily_rate

    def __str__(self):
        return f"Fix {self.id} for Error {self.error.id}"
