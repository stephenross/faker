localized = True

from .. import BaseProvider


class Provider(BaseProvider):
    formats = ('###-###-###',)

    @classmethod
    def phone_number(cls, format=None):
        """
        Creates a random phone number from the current locale

        :param format: optional format string to force a specific output format
        :example '1-800-867-5309'
        :return str
        """
	if format is not None:
            return cls.numerify(format)
        return cls.numerify(cls.random_element(cls.formats))
