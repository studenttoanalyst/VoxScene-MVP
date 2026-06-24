import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.ai_model import VisionModel


vision = VisionModel()


image_path = r"C:\Users\DELL\Desktop\VoxScene-MVP\03_Development\VoxScene_Prototype\assets\captured_images\20260624_234153.jpg"

objects = vision.detect_objects(image_path)


print("Detected Objects:")

for obj in objects:
    print(obj)