# Stubs for _locale (Python 3.4)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Iterable

ABDAY_1 = ...  # type: int
ABDAY_2 = ...  # type: int
ABDAY_3 = ...  # type: int
ABDAY_4 = ...  # type: int
ABDAY_5 = ...  # type: int
ABDAY_6 = ...  # type: int
ABDAY_7 = ...  # type: int
ABMON_1 = ...  # type: int
ABMON_10 = ...  # type: int
ABMON_11 = ...  # type: int
ABMON_12 = ...  # type: int
ABMON_2 = ...  # type: int
ABMON_3 = ...  # type: int
ABMON_4 = ...  # type: int
ABMON_5 = ...  # type: int
ABMON_6 = ...  # type: int
ABMON_7 = ...  # type: int
ABMON_8 = ...  # type: int
ABMON_9 = ...  # type: int
ALT_DIGITS = ...  # type: int
AM_STR = ...  # type: int
CHAR_MAX = ...  # type: int
CODESET = ...  # type: int
CRNCYSTR = ...  # type: int
DAY_1 = ...  # type: int
DAY_2 = ...  # type: int
DAY_3 = ...  # type: int
DAY_4 = ...  # type: int
DAY_5 = ...  # type: int
DAY_6 = ...  # type: int
DAY_7 = ...  # type: int
D_FMT = ...  # type: int
D_T_FMT = ...  # type: int
ERA = ...  # type: int
ERA_D_FMT = ...  # type: int
ERA_D_T_FMT = ...  # type: int
ERA_T_FMT = ...  # type: int
LC_ALL = ...  # type: int
LC_COLLATE = ...  # type: int
LC_CTYPE = ...  # type: int
LC_MESSAGES = ...  # type: int
LC_MONETARY = ...  # type: int
LC_NUMERIC = ...  # type: int
LC_TIME = ...  # type: int
MON_1 = ...  # type: int
MON_10 = ...  # type: int
MON_11 = ...  # type: int
MON_12 = ...  # type: int
MON_2 = ...  # type: int
MON_3 = ...  # type: int
MON_4 = ...  # type: int
MON_5 = ...  # type: int
MON_6 = ...  # type: int
MON_7 = ...  # type: int
MON_8 = ...  # type: int
MON_9 = ...  # type: int
NOEXPR = ...  # type: int
PM_STR = ...  # type: int
RADIXCHAR = ...  # type: int
THOUSEP = ...  # type: int
T_FMT = ...  # type: int
T_FMT_AMPM = ...  # type: int
YESEXPR = ...  # type: int
_DATE_FMT = ...  # type: int

def bind_textdomain_codeset(domain, codeset): ...
def bindtextdomain(domain, dir): ...
def dcgettext(domain, msg, category): ...
def dgettext(domain, msg): ...
def gettext(msg): ...
def localeconv(): ...
def nl_langinfo(key): ...
def setlocale(category: int, locale: Iterable[str] = ...) -> str: ...
def strcoll(string1, string2) -> int: ...
def strxfrm(string): ...
def textdomain(domain): ...

class Error(Exception): ...
