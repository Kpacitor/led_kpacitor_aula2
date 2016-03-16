
import sys
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/led_kpacitor_aula2/")

activate_this = '/var/www/led_kpacitor_aula2/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

from led_kpacitor import app as application
application.secret_key = 'Add your secret key'