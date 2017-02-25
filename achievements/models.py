from django.db import models
from core.models import Authored, Titled

friendship = {
	1: 'Первый друг',
	10: 'Дружелюбный',
	50: 'Братишка',
	100: 'Филантроп',
	500: 'Другоман',
	1000: 'Другофил',
}

likes = {
	1: 'Первый лайк',
	10: 'Интересный пост!',
	50: 'Популярный',
	100: 'Соточка',
	500: 'Создатель мемов',
	1000: 'Лайкодрочер',
}

comments = {
	1: 'Первый коммент',
	10: 'Интересный пост!',
	50: 'Интересное обсуждение!',
	100: 'Срач',
	500: 'Мегасрач',
	1000: 'Разжигатель',
}


class Achievement(Authored, Titled):
	content = models.TextField(verbose_name='Содержание')

	class Meta:
		verbose_name = 'Достижение'
		verbose_name_plural = 'Достижения'
		unique_together = (('author', 'title'), )



