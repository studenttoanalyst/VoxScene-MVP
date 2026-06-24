import cv2
import os
from datetime import datetime
from src.config import CAMERA_INDEX, IMAGE_FOLDER
from src.logger import get_logger

logger = get_logger()

class Camera:


    def __init__(self):

        self.camera = cv2.VideoCapture(CAMERA_INDEX)



    def capture_image(self):

        try:

            if not self.camera.isOpened():

                logger.error("Camera not available")

                return None



            ret, frame = self.camera.read()


            if not ret:

                print("Image capture failed")

                return None



            folder = IMAGE_FOLDER

            os.makedirs(folder, exist_ok=True)



            filename = datetime.now().strftime(
                "%Y%m%d_%H%M%S.jpg"
            )


            path = os.path.join(
                folder,
                filename
            )


            cv2.imwrite(path, frame)


            logger.info(f"Image saved: {path}")


            return path


        except Exception as e:

            print("Camera error:", e)

            return None



    def release(self):

        self.camera.release()

        cv2.destroyAllWindows()