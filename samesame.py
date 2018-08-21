import english_confusables

print(english_confusables.get_homograph("Malwrologist"))

print(english_confusables.convert_to_ascii("𝐈𝟎𝐈𝔅١𝔑S",ignore_case=True))

print(english_confusables.convert_to_ascii("𝐈𝟎𝐈𝔅١𝔑S",ignore_case=False))

print(english_confusables.convert_to_ascii("01234"))

print(english_confusables.convert_to_ascii("测试"))


