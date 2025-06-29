API_AUTH_ENDPOINT = 'https://ngw.devices.sberbank.ru:9443/api/v2/oauth'
API_TTS_ENDPOINT = 'https://smartspeech.sber.ru/rest/v1/text:synthesize'
DOMAIN = 'sbertts'

SUPPORT_LANGUAGES = [
    'ru-RU',
    'en-US'
]

SUPPORT_VOICES = {
    'Nec': 'Наталья',
    'Bys': 'Борис',
    'May': 'Марфа',
    'Tur': 'Тарас',
    'Ost': 'Александра',
    'Pon': 'Сергей',
    'Kin': 'EN Kira',
}

MAP_VOICES = {
    'ru-RU': {
        'Nec': 'Наталья',
        'Bys': 'Борис',
        'May': 'Марфа',
        'Tur': 'Тарас',
        'Ost': 'Александра',
        'Pon': 'Сергей',
    },
    'en-US': {
        'Kin': 'Kira',
    }
}


SUPPORT_RATE = [
    '24000',
    '8000',
]

CODEC_FORMAT = {
    'wav16': 'wav',
    'pcm16': 'wav',
    'alaw': 'wav',
    'opus': 'ogg',
}

CONF_VOICE = 'voice'
CONF_RATE = 'rate'
CONF_FLOW_RESTRICTION = 'flow_restriction'

DEFAULT_RATE = '24000'
DEFAULT_VOICE = 'Nec'
DEFAULT_LANG = 'ru-RU'
DEFAULT_FLOW_RESTRICTION = 3

SUPPORT_OPTIONS = [CONF_VOICE, CONF_RATE]
