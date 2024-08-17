TELEGRAM_ACCOUNTS = [
    dict(phone='+380982575987', proxy="http://144.76.120.202:3128"),
    dict(phone='+380974907186', proxy="http://185.233.37.108:3128"),
    dict(phone='+380982575986'),
    dict(phone='+380969528058'),
]

try:
    from accounts_local import *
except ImportError:
    pass
