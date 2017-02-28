from django.core.exceptions import ValidationError
from functools import wraps


def if_new(error_message):
	def decorator(func):
		@wraps(func)
		def wrapper(self, *args, **kwargs):
			if not self.pk:
				return func(self, *args, **kwargs)
			else:
				raise ValidationError(error_message)
		return wrapper
	return decorator


def non_editable_fields(*args):
	field_list = list(args)

	def decorator(class_obj):

		old_init = class_obj.__init__
		old_clean = class_obj.clean

		@wraps(class_obj.__init__)
		def __init__(self, *args, **kwargs):
			old_init(self, *args, **kwargs)
			self._initial_data = {k: v for k, v in self.__dict__.items() if k in field_list and v}

		@wraps(class_obj.clean)
		def clean(self):
			errors = list()
			for field in self._initial_data.keys():
				try:
					if hasattr(self, field) and getattr(self, field) != self._initial_data[field]:
						raise ValidationError('Изменилось значение поля {0}'.format(field))
				except ValidationError as e:
					errors.append(e)
			if errors:
				raise ValidationError(errors)
			return old_clean(self)

		setattr(class_obj, '__init__', __init__)
		setattr(class_obj, 'clean', clean)
		return class_obj
	return decorator
