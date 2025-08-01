import os
from gtts import gTTS
import elevenlabs
from elevenlabs.client import ElevenLabs
from elevenlabs import save
import subprocess
import platform
import pygame
from playsound import playsound




# Generates voice file from text
def generate_voice_with_elevenlabs(text, output_filepath):
    client = ElevenLabs(api_key="sk_20f292f820252d16c2263b4767da05b139582d221ff09f44")
    audio = client.generate(
        text=text,
        voice="Aria",
        output_format="mp3_22050_32",
        model="eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)

# Plays the generated voice file
def playsound(filepath):
    
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(filepath)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


# generate_voice_with_elevenlabs("Hello, how can I help you today?", "final.mp3")
# play_voice("final.mp3")

