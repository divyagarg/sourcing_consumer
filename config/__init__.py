import os

env = os.environ.get('HOSTENV') or 'default'

if env in ['default', 'development']:
    from config.development_config import *

elif env == 'staging':
    from config.staging_config import *

elif env == 'production':
    from config.production_config import *

else:
    from .development_config import *
