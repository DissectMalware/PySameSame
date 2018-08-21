# Introduction to PySameSame
This is a python port of [samesame](https://github.com/TheTarquin/samesame) utility developed by @TheTarquin. It also offers a few more features that deemed to be useful.

By using PySameSame, you can:
1. replace ASCII characters with homograph (look-alike) characters in a given string
```
homoglyph = english_confusables.get_homograph("this is for test")

```

2. obtain all of the potential ASCII representations of a given Unicode homoglyph. 
```
ascii_reprs = english_confusables.convert_to_ascii("𝐈𝟎𝐈𝔅١𝔑S",ignore_case=True)

```

3. obtain an HTML table representing the internal mappings that is used by PySameSame
```
mappings = english_confusables.generate_table()
```

4. manually select a Unicode homoglyph for ASCII characters and use the mapping to transform a test using a [web interface](https://github.com/DissectMalware/PySameSame/blob/master/mappings.html). 



