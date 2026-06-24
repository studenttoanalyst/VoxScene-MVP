import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.description import DescriptionGenerator


generator = DescriptionGenerator()


objects = [
    "book",
    "person",
    "cup"
]


description = generator.generate(objects)


print(description)