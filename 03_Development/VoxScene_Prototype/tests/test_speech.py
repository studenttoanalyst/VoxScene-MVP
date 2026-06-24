import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.speech import SpeechRecognizer


speech = SpeechRecognizer()


command = speech.listen()


print(command)