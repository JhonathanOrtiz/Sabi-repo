from google.cloud import speech_v1p1beta1
from google.cloud.speech_v1p1beta1 import enums
import os
from app.storage_management import upload_and_get_uri, delete_blob
from io import BytesIO
import wave
import requests
from time import gmtime, strftime
import random

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "app/All-project-services-05f5490b9fae.json"
language_code = "es-VE"
client = speech_v1p1beta1.SpeechClient()
BUCKET_NAME = "categories_products"


def _get_config(language, sample_rate, encoding, n_channels):   
    return {
        'language_code': language,
        'sample_rate_hertz': sample_rate,
        'encoding': encoding,
        'audio_channel_count': n_channels
    }

def _get_audio(storage_uri):
    return {
        'uri': storage_uri
    }

def _get_audio_params(content):
    wav = wave.open(BytesIO(content))
    return wav.getparams()

def _get_file_name():
    return strftime("%Y-%m-%d_%H:%M:%S", gmtime())+'-'+str(random.random())[2:6]+'.'+'wav'

def sample_recognize_job(wav_bytes, delete=False):
    """
    Performs synchronous speech recognition on an audio file
    """

    filename = _get_file_name()
    storage_uri = upload_and_get_uri(wav_bytes, BUCKET_NAME, filename)
    encoding = enums.RecognitionConfig.AudioEncoding.LINEAR16
    params = _get_audio_params(wav_bytes)

    config = _get_config(language_code, params.framerate, encoding, params.nchannels)
    audio = _get_audio(storage_uri)
    
    response = client.recognize(config, audio)

    import pdb; pdb.set_trace()
    for result in response.results:
        alternative = result.alternatives[0]
        
    if delete:
      delete_blob(BUCKET_NAME, filename)
    
    return alternative.transcript