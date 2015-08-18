#!/usr/bin/python
import logging
from subprocess import Popen, PIPE

# print a log message to the console.
logging.warning('This is a warning!')

# logging.basicConfig( filename = 'program.log', level = logging.DEBUG)
logging.warning('An example message.')
logging.warning('Another message')

logging.basicConfig( format = '%(asctime)s %(message)s', level = logging.DEBUG)
logging.info('Logging app started')
logging.warning('An example logging message.')


process = Popen(['ls', '-l'], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()
print(stdout)
