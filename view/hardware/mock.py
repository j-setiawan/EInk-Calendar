from PIL import Image

from utils.config_generator import Configurations


class EPD:
    def __init__(self, config: Configurations):
        self.save_path = config.debug_save_path

    # Hardware reset
    def reset(self):
        pass

    def send_command(self, command):
        pass

    def send_data(self, data):
        pass

    def wait_until_idle(self):
        pass

    def init(self):
        pass

    def getbuffer(self, image: Image):
        return image

    def display(self, image_black: Image, image_yellow: Image):
        print(self.save_path)
        image_black.save(self.save_path)

    def clear(self):
        pass

    def sleep(self):
        pass
