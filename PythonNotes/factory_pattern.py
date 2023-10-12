import pathlib
from abc import ABC, abstractclassmethod

class VideoExporter(ABC):
    """Basic representation of video exporting codec."""

    @abstractmethod
    del prepare_export(self, video_data):
        """Prepares video data for exporting"""

    @abstractmethod
    del do_export(self, folder: pathlib.Path):
        """Exports the video data to a folder"""


class LosslessVideoExporter(VideoExporter):
    def prepare_export(self, video_data):
        print("Preparing video data for lossless export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in lossless format to {folder}.")
