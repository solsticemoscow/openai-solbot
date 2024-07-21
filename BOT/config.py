import os


PHOTO = None

MSGS = []
anthropic_api = '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'

OPENAI_API = 'sk-proj-5fcyXQRd3YGvogyxy0RcT3BlbkFJmC9ipoyys5oRYe5msgNz'

TAVILY_API = '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'

SINGLESTORE_API = '6186ed59a92aebde9ff7dc3aa1fac27048beff0b5ca5719c2337f8523bf74ec8'


SOLBOT_TOKEN = '6644138303:AAH0Ft4e8U0ALQ0X-NKQqIQv6Nd7ZuWYQm4'

TG_SOLSTICE = 239203155
KSY = 1314883291
TEST_GROUP = -1002187434036
ADMINS = [TG_SOLSTICE, KSY]

ROOT_DIR: str = os.path.dirname((__file__))


MODEL_35 = "gpt-3.5-turbo-0125"
MODEL4o = "gpt-4o"
MODEL_VOICE = "whisper-1"
VECTARA = 'zut_UA2fb_L2lS-AWy5ASi5ofaLyteQIotogjhfFsg'
VECTOR = 'vs_QLZj9px4OjtHDv8gGCYEM3pi'

PROMT2 = 'Подробно расскажи, что изображено на изображении. Если есть текст - пришли весь текст курсивом.'
MSG_SOLBOT = '✨ SolBot:\n\n'