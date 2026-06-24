import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.camera import Camera


camera = Camera()


image = camera.capture_image()


if image:
    print("Camera module working")


camera.release()