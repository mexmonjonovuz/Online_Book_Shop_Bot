import os

from dotenv import load_dotenv
from redis_dict import RedisDict

load_dotenv('.env')

ADMIN_LIST = [123456789]  # [os.getenv('ADMIN_LIST')]  # admin ID
TOKEN = os.getenv('TOKEN')  # TOKEN
SOCIAL_LINKS = ['https://t.me/ikar_factor', 'https://t.me/factor_books', 'https://t.me/factorbooks']
SOCIAL_TEXT_BUTTONS = ['IKAR | Factor Books', 'Factor Books', '\"Factor Books\" nashiryoti']

LINKS = {
    'IKAR | Factor Books': 'https://t.me/ikar_factor',
    'Factor Books': 'https://t.me/factor_books',
    '\"Factor Books\" nashiryoti': 'https://t.me/factorbooks'
}
db = RedisDict('all')
print(db)

# 5684649553
