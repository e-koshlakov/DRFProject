from django.db import models
from users.models import NULLABLE


class Section(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
        ordering = ['id']


class SectionContent(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='section_content',
                                verbose_name='Раздел')
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Контент', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Контент раздела'
        verbose_name_plural = 'Контент разделов'
        ordering = ['id']


class Tests(models.Model):
    test_section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name="Тест разделов")
    description = models.TextField(verbose_name='Test description', **NULLABLE)
    question = models.TextField(verbose_name='Question', **NULLABLE)
    answer = models.CharField(max_length=40, verbose_name='Answer', **NULLABLE)

    def __str__(self):
        return f"Тест {self.test_section.title}"

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'
        ordering = ['test_section']
