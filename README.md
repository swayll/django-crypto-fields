# django-crypto-fields
Collection fo crypto fileds crypt and decrypt **on the fly** with [Fernet (symmetric encryption)](https://cryptography.io/en/latest/fernet/).

**Import** fields collection to your models
```python
from .fields import (
    CryptoDateField,
    CryptoPositiveSmallIntegerField,
    CryptoPositiveIntegerField,
    CryptoCharField,
    CryptoTextField
)
cryptodate = CryptoDateField()
cryptochar = CryptoCharField(max_length=125)
cryptotext = CryptoTextField(max_length=500)
cryptopossmallint = CryptoPositiveSmallIntegerField()
cryptoposint = CryptoPositiveIntegerField()
```
All fields support standard django's fields properties and attributes as `null`, `blank`, `verbose_name`, `help_text`, `error_messages` and etc...

Tested on django 4.1
