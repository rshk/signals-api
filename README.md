# Signals API

Hosted at: https://signals-api.herokuapp.com


## Nautical flags API

``/flags/:text``

![](https://signals-api.herokuapp.com/flags/hello%20world)


Customize background: ``?background=:color``

![](https://signals-api.herokuapp.com/flags/hello?background=00ff00)


Customize row size: ``?row_size=20``

![](https://signals-api.herokuapp.com/flags/hello%20world?row_size=20)


### All the flags on display

Letters:

![](https://signals-api.herokuapp.com/flags/ABCDEFGHIJKLMNOPQRSTUVWXYZ?background=ddd&row_size=13)

Digits:

![](https://signals-api.herokuapp.com/flags/0123456789?background=ddd&row_size=5)

Repeater flags: ``!@#$`` (keep in mind that ``#`` needs to be specified as ``%23`` in URLs)

![](https://signals-api.herokuapp.com/flags/!@%23$?background=ddd)


### License

Flag images are coming from Wikimedia Commons, and are in Public Domain.

They're beautifully listed here: https://en.wikipedia.org/wiki/International_maritime_signal_flags
