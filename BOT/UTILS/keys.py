from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder


class MKeys:

    def in_yt(self):
        KEY = InlineKeyboardBuilder()
        KEY.button(text='Скачать видео', callback_data='yt_mp4')
        KEY.button(text='Скачать аудио', callback_data='yt_mp3')
        KEY.adjust(1)
        return KEY.as_markup()

    def in_file(self):
        KEY = InlineKeyboardBuilder()
        KEY.button(text='Скачать', callback_data='yt_download')
        KEY.button(text='Сохранить', callback_data='yt_s3')
        KEY.button(text='Удалить', callback_data='yt_delete')
        KEY.adjust(1)
        return KEY.as_markup()

    def in_search(self):
        KEY = InlineKeyboardBuilder()
        KEY.button(text='🌐 Поиск в интернете', callback_data='search_web')
        KEY.button(text='🔍 Поиск в Youtube', callback_data='search_yt')
        KEY.button(text='🔍 Поиск по ', callback_data='search_yt')
        KEY.adjust(1)
        return KEY.as_markup()

    def in_text(self):
        KEY = InlineKeyboardBuilder()
        KEY.button(text='📝 Заметка', callback_data='text_note')
        KEY.button(text='🔍 Поиск', callback_data='text_search')
        KEY.adjust(1)
        return KEY.as_markup()

    def in_ocr(self):
        KEY = InlineKeyboardBuilder()
        KEY.button(text='Распознать', callback_data='image_ocr')
        KEY.button(text='Сохранить', callback_data='image_s3')
        KEY.button(text='Удалить', callback_data='image_delete')
        KEY.adjust(1)
        return KEY.as_markup()


    def in_admin(self):
        KEY = InlineKeyboardBuilder()
        KEY.button(text='Ban | Unban', callback_data='admin_ban')
        KEY.button(text='FAQ', callback_data='admin_faq')
        KEY.button(text='Captcha', callback_data='admin_captcha')
        KEY.adjust(1)
        return KEY.as_markup()

MK = MKeys()