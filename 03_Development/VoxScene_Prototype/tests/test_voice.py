import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.voice import VoiceAssistant


voice = VoiceAssistant()


message = "There is a chair and laptop in the scene."


voice.speak(message)


print("Voice module working")