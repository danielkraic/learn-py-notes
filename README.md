# learn-py-notes
notes from learning python

## bytes vs str vs unicode

```python
# python3
bytes # raw 8bit values
str # unicode characters

def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        return bytes_or_str.decode('utf-8')
    return bytes_or_str

def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        return bytes_or_str.encode('utf-8')
    return bytes_or_str
```

```python
# python2
str # raw 8-bit chars
unicode # unicode characters

def to_unicode(unicode_or_str):
    if isinstance(unicode_or_str, str):
        return unicode_or_str.decode('utf-8')
    return unicode_or_str

def to_str(unicode_or_str):
    if isinstance(unicode_or_str, unicode):
        return unicode_or_str.encode('utf-8')
    return unicode_or_str
```
