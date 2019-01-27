from google.cloud import translate, texttospeech
import sys
import csv
import random
import re

# Instantiates clients
translate_client = translate.Client()
speech_client = texttospeech.TextToSpeechClient()

# global inputs to to_speech
voice_ = texttospeech.types.VoiceSelectionParams(language_code='fr-CA', ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)
audio_config_ = texttospeech.types.AudioConfig(audio_encoding=texttospeech.enums.AudioEncoding.MP3)

word_dict = {}
with open('./word/french-word-list-total.csv', 'r') as word_list:
    csv_reader = csv.reader(word_list, delimiter=',')
    n = 0
    for row in csv_reader:
        col_list = row[0].split(';')
        try:
            word_n = int(col_list[0])
        except ValueError:
            continue
        else:
            word = col_list[1]
            freq = col_list[2]
            word_dict[word_n] = [word, freq]

for i in list(word_dict):
    word = word_dict.get(i)[0]
    if(re.search('\W', word)):
        word_dict.pop(i)

def get_word():
    word_num = random.choice(list(word_dict.keys()))
    return word_dict.get(word_num)

def translation(word,  tgt_lang='en', src_lang='fr'):
    return translate_client.translate(word, target_language=tgt_lang, source_language=src_lang)

def to_speech(word, save_to='', filename='output'):
    input_ = texttospeech.types.SynthesisInput(text=word)
    response = speech_client.synthesize_speech(input_, voice_, audio_config_)

    output = filename + '.mp3'
    with open(save_to + output, 'wb') as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file %s' % output)