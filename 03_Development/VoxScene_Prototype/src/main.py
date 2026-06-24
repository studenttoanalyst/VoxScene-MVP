from .camera import Camera
from .ai_model import VisionModel
from .description import DescriptionGenerator
from .voice import VoiceAssistant
from .speech import SpeechRecognizer



def main():

    print("VoxScene Ready...")


    # Voice Input

    speech = SpeechRecognizer()

    command = speech.listen()


    if command and "front" in command:


        # Camera

        camera = Camera()

        image_path = camera.capture_image()



        # AI Vision

        vision = VisionModel()

        objects = vision.detect_objects(image_path)



        print("Detected:", objects)



        # Description

        generator = DescriptionGenerator()

        description = generator.generate(objects)



        print(description)



        # Voice Output

        voice = VoiceAssistant()

        voice.speak(description)



        camera.release()



    else:

        print("Command not recognized")



if __name__ == "__main__":

    main()