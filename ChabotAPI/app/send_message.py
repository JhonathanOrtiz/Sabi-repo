import dialogflow_v2
import os
import base64
from uuid import uuid4


######################################################################################################
#############################CONFIGURATION FUNCTIONS##################################################
######################################################################################################


def _get_project_id(file):
    with open(file, 'r') as f:
        project_id = f.read()
    return project_id

def _from_audio(audio, client, session):
    
    audio = base64.b64decode(audio)

    audio_encoding = dialogflow_v2.enums.AudioEncoding.AUDIO_ENCODING_LINEAR_16
    sample_rate_hertz = 16000

    audio_config = dialogflow_v2.types.InputAudioConfig(audio_encoding=audio_encoding, 
                                                        language_code=LANGUAGE,
                                                        sample_rate_hertz=sample_rate_hertz)

    query_input = dialogflow_v2.types.QueryInput(audio_config=audio_config)

    response = client.detect_intent(
        session=session, 
        query_input=query_input,
        input_audio=audio)

    return response

def _from_text(text, client, session):

    text_input = dialogflow_v2.types.TextInput(text=text, language_code=LANGUAGE)
    query_input = dialogflow_v2.types.QueryInput(text=text_input)

    return client.detect_intent(session, query_input)

def _get_session(client, project_id, session_id):
    return client.session_path(project_id, session_id)

def _get_client():
    return dialogflow_v2.SessionsClient()


#############################################################################################################################
###################################################CONSTANT VALUES###########################################################
#############################################################################################################################


PROJECT_ID = _get_project_id('utils_files/project_id.txt')
LANGUAGE = 'es-VE'

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'utils_files/small-talk-wlef-a373fd31bab8.json'
os.environ['DIALOGFLOW_PROJECT_ID'] = PROJECT_ID

##############################################################################################################################
#########################################################GET RESPONSE FROM DIALOGFLOW#########################################
##############################################################################################################################


def get_response(text=None, audio=None, session_id=None):
    """
    This function get a response from bot given an string or Audio file
    text: (str) Text from user
    audio: (Binary file) Audio File from user

    Returns: An str with text response from bot and binry file with Audio response 
    'query_result' method gives a json file with parameters text input and text output
    'output_audio' method gives a binary file with outputfile

    """

    #Config
    if session_id == None:
        session_id = str(uuid4())
        
    client = _get_client()
    session = _get_session(client, PROJECT_ID, session_id)

    if text:
        response = _from_text(text, client, session)
        return response.query_result, session_id
        
    if audio:
        response =  _from_audio(audio, client, session)
        return response.query_result, session_id
        
