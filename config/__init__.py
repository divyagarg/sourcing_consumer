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


class KafkaMessageTypes:
    BUYER_ORDER_MESSAGE = 'create_order'
    SELLER_ORDER_MESSAGE = 'create_seller_order'
    BUYER_PAYMENT_STATUS = 'update_payment'
    SELLER_PAYEMNT_STATUS = 'seller_payment_update'

