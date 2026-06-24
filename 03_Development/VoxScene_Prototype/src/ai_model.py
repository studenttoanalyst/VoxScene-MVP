from ultralytics import YOLO
from src.config import MODEL_NAME, CONFIDENCE_THRESHOLD
from src.logger import get_logger

logger = get_logger()


class VisionModel:


    def __init__(self):
        self.model = YOLO(MODEL_NAME)


    def detect_objects(self, image_path):

        try:

            results = self.model(
                        image_path,
                    conf= CONFIDENCE_THRESHOLD
                                                )

            detected_objects = []


            for result in results:

                for box in result.boxes:


                    class_id = int(box.cls[0])


                    name = self.model.names[class_id]


                    if name not in detected_objects:

                        detected_objects.append(name)



            return detected_objects



        except Exception as e:

            logger.error(f"AI error: {e}")
            logger.info(
    f"Detected objects: {detected_objects}"
)
            return []