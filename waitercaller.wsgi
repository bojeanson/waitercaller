activate_this = '/home/bojeanson/venv_ANEO/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import sys
sys.path.insert(0, "/var/www/waitercaller")
from waitercaller import app as application