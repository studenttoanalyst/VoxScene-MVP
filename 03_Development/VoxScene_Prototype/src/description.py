class DescriptionGenerator:


    def detect_scene(self, objects):

        if "bed" in objects:

            return "This looks like a bedroom."


        if "laptop" in objects and "chair" in objects:

            return "This looks like a workspace."


        if "cup" in objects and "bottle" in objects:

            return "This may be a dining or kitchen area."


        return None



    def generate(self, objects):

        if not objects:

            return "I could not detect anything."


        objects = list(set(objects))


        scene = self.detect_scene(objects)


        if len(objects) == 1:

            description = f"I can see a {objects[0]}."


        else:

            description = (
                "I can see "
                + ", ".join(objects)
                + " around you."
            )


        if scene:

            return scene + " " + description


        return description