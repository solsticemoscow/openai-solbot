import os


PHOTO = None

MSGS = []
anthropic_api = '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'

OPENAI_API = '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'

TAVILY_API = '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'

SINGLESTORE_API = '6186ed59a92aebde9ff7dc3aa1fac27048beff0b5ca5719c2337f8523bf74ec8'

ASSISTANT_ID = 'asst_N2sqrhkjhg36qStwqhoRoOmC'
VECTOR_STORE = 'vs_QLZj9px4OjtHDv8gGCYEM3pi'
THREAD_ID = 'thread_ygB2S4eqM7CgtaPRimnVADEy'
SOLBOT_TOKEN = '6644138303:AAH0Ft4e8U0ALQ0X-NKQqIQv6Nd7ZuWYQm4'

TG_SOLSTICE = 239203155
KSY = 1314883291
TEST_GROUP = -1002187434036
ADMINS = [TG_SOLSTICE, KSY]

ROOT_DIR: str = os.path.dirname((__file__))

WEBAPPURL = 'https://7d89-185-18-5-193.ngrok-free.app'


MODEL_35 = "gpt-3.5-turbo-0125"
MODEL4o = "gpt-4o"
MODEL_VOICE = "whisper-1"
VECTARA = 'zut_UA2fb_L2lS-AWy5ASi5ofaLyteQIotogjhfFsg'
VECTOR = 'vs_QLZj9px4OjtHDv8gGCYEM3pi'

PROMT2 = 'Подробно расскажи, что изображено на изображении. Если есть текст - пришли весь текст курсивом.'
MSG_SOLBOT = '✨ SolBot:\n\n'

REG_USER: str = 'u1488792_mk'
REG_PASS: str = 'iN4wD1xI4iaX0vC6'
REG_DB: str = 'u1488792_mkdb'
REG_IP: str = '37.140.192.84'
REG_PORT: int = 3306

DB_MYSQL: str = f'mysql+aiomysql://{REG_USER}:{REG_PASS}@{REG_IP}:{REG_PORT}/{REG_DB}'


