import json
import requests
from flask import current_app
from flask_babel import _


def get_supported_languages(auth):
    r = requests.get('https://api.cognitive.microsofttranslator.com/languages?api-version=3.0',
            headers=auth)
    response = r.json()
    return list(response["translation"].keys())


def translate(text, source_language, dest_language):
    if 'MS_TRANSLATOR_KEY' not in current_app.config or \
            not current_app.config['MS_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')
    auth = {
        'Ocp-Apim-Subscription-Key': current_app.config['MS_TRANSLATOR_KEY']}

    supported_languages = get_supported_languages(auth)

    if source_language not in supported_languages:
        return _('The detected language is not handled yet')
    elif source_language not in supported_languages:
        return _('Your browser language is not handled yet')

    r = requests.get('https://api.microsofttranslator.com/v2/Ajax.svc'
                     '/Translate?text={}&from={}&to={}'.format(
                         text, source_language, dest_language),
                     headers=auth)
    if r.status_code != 200:
        return _('Error: the translation service failed.')
    return json.loads(r.content.decode('utf-8-sig'))
