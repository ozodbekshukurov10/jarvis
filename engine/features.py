import playsound as playsound
import eel



#play assistant sound

@eel.expose

def playAssistantSound():
    music_dir = "www\\assets\\audio\\www_assets_audio_start_sound.mp3"
    playsound.playsound(music_dir)