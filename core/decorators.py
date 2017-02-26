from django.core.exceptions import ValidationError
import types


def if_new(error_message):
	def decorator(func):
		def wrapper(self, *args, **kwargs):
			if not self.pk:
				return func(self, *args, **kwargs)
			else:
				raise ValidationError(error_message)
		wrapper.__name__ = func.__name__
		return wrapper
	return decorator


def non_editable_fields(*args):
	field_list = list(args)

	def decorator(class_obj):
		def new_init(self, *args, **kwargs):
			super(class_obj, self).__init__(*args, **kwargs)
			self._initial_data = dict([(k, v) for k, v in self.__dict__.items() if k in field_list and v])

		def new_clean(self):
			errors = list()
			for field in self._initial_data.keys():
				try:
					if hasattr(self, field) and getattr(self, field) != self._initial_data[field]:
						raise ValidationError('Изменилось значение поля {0}'.format(field))
				except ValidationError as e:
					errors.append(e)
			if errors:
				raise ValidationError(errors)

		class_obj.__init__ = new_init
		class_obj.clean = new_clean
		return class_obj
	return decorator
