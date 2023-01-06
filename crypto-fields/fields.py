from django.db import models
from cryptography.fernet import Fernet
from django.utils.dateparse import parse_date
from django.utils.translation import gettext_lazy as _
from django.conf import settings

class CryptoDateField(models.DateField):

    description = _("Crypto date field")

    def value_from_object(self, obj):
        val = getattr(obj, self.attname)
        if val not in (None, "", b""):
            val = settings.CYPHER.decrypt(val).decode('utf-8')
            return parse_date(val).strftime("%d.%m.%Y")
        return ""

    def get_internal_type(self):
        return "BinaryField"

    def get_db_prep_value(self, value, connection, prepared=False):
        value = super().get_db_prep_value(value, connection, prepared)
        if value is not None:
            return connection.Database.Binary(settings.CYPHER.encrypt(str(value).encode('utf-8')))
        return value

class CryptoPositiveSmallIntegerField(models.PositiveSmallIntegerField):

    description = _("Crypto number field from 0 to 32767")

    def value_from_object(self, obj):
        val = getattr(obj, self.attname)
        if val not in (None, "", b""):
            val = int(settings.CYPHER.decrypt(val).decode('utf-8'))
        return val

    def get_internal_type(self):
        return "BinaryField"

    def get_db_prep_value(self, value, connection, prepared=False):
        value = super().get_db_prep_value(value, connection, prepared)
        if value is not None:
            return connection.Database.Binary(settings.CYPHER.encrypt(str(value).encode('utf-8')))
        return value

class CryptoPositiveIntegerField(models.PositiveIntegerField):

    description = _("Crypto number field from 0 to 2147483647")

    def value_from_object(self, obj):
        val = getattr(obj, self.attname)
        if val not in (None, "", b""):
            val = int(settings.CYPHER.decrypt(val).decode('utf-8'))
        return val

    def get_internal_type(self):
        return "BinaryField"

    def get_db_prep_value(self, value, connection, prepared=False):
        value = super().get_db_prep_value(value, connection, prepared)
        if value is not None:
            return connection.Database.Binary(settings.CYPHER.encrypt(str(value).encode('utf-8')))
        return value


class CryptoCharField(models.CharField):

    description = _("Crypto char field")

    def value_from_object(self, obj):
        val = getattr(obj, self.attname)
        if val not in (None, "", b""):
            val = settings.CYPHER.decrypt(val).decode('utf-8')
        return val

    def get_internal_type(self):
        return "BinaryField"

    def get_db_prep_value(self, value, connection, prepared=False):
        value = super().get_db_prep_value(value, connection, prepared)
        if value is not None:
            return connection.Database.Binary(settings.CYPHER.encrypt(str(value).encode('utf-8')))
        return value

class CryptoTextField(models.TextField):

    description = _("Crypto text field")

    def value_from_object(self, obj):
        val = getattr(obj, self.attname)
        if val not in (None, "", b""):
            val = settings.CYPHER.decrypt(val).decode('utf-8')
        return val

    def get_internal_type(self):
        return "BinaryField"

    def get_db_prep_value(self, value, connection, prepared=False):
        value = super().get_db_prep_value(value, connection, prepared)
        if value is not None:
            return connection.Database.Binary(settings.CYPHER.encrypt(str(value).encode('utf-8')))
        return value
