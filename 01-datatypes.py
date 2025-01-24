from typing import Final

s='single quote string'
s1="double quote string"
s2='''"Triple" quoted string'''
print(f"Type of '{s}' : ",type(s))
print(s1)
print(s2)
number: int=10
print(f"Type of {number}={type(number)}")
decimal: float=86.9
print(f"Type of {decimal}={type(decimal)}")
is_online: bool=True
print(f"Type of {is_online}={type(is_online)}")
#Constants
LANGUAGE: Final[str]="Python"
print(f"language first value = {LANGUAGE}")
#LANGUAGE="Java"#IS A WARNING/suggestion by the IDE.Final constants are not supposed to be RE-ASSIGNMENT after INITIALIZATION in python.
print(f"language value(re-assigned) = {LANGUAGE}")
LANGUAGE_VERSION: float=float(input("Enter your version number for example : 3.13"))
print(f"Type of {LANGUAGE}={type(LANGUAGE)}")
print(f"Type of {LANGUAGE_VERSION}={type(LANGUAGE_VERSION)}")