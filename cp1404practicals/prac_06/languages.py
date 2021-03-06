"""
Prac_06 - Daniel Keppie
Languages
"""
from prac_06.programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(visual_basic.is_dynamic())

coding_languages = [ruby, python, visual_basic]
print("The dynamically typed languages are:")
for language in coding_languages:
    if language.is_dynamic():
        print(language.name)