import logging

logging.basicConfig(
    filename = 'game.log',
    filemode = 'a',
    level = logging.DEBUG,
    format = '%(name)s - %(level)s - %(message)s'
)
