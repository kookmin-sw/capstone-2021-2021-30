## Need to install google cloud speech to text api
## sample from google cloud speech to text api

from google.cloud import speech

def transcribe_gcs(gcs_uri):
    from google.cloud import speech
    
    language_code='ko-KR'
    
    client = speech.SpeechClient()
    audio = speech.RecognitionAudio(uri=gcs_uri)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=48000, # flac file hertz
        audio_channel_count=2,
        language_code='ko-KR')

    operation = client.long_running_recognize(config=config, audio=audio)
    response = operation.result()

    return response

gcs_uri = "gs://speech_to_text_ex1/[출근길 날씨] 맑고 큰 일교차…수도권·충청 황사 영향 KBS 20210317.flac"
response = transcribe_gcs(gcs_uri)

with open('script_file.txt', "w") as script:
    for result in response.results:
        script.write(u'{}'.format(result.alternatives[0].transcript)+"\n")

print("completed")
    
    
