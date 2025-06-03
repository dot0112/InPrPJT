from app.models import singleton, PacketData
import pickle
import os


@singleton
class PngUtils:
    def __init__(self):
        self.filePath = "./app/static/logo.png"

    def setFilePath(self, path):
        if os.path.exists(path):
            self.filePath = path
            return path
        else:
            return None

    def writePNGData(self, obj):
        with open(self.filePath, "ab") as f:
            f.write(pickle.dumps(obj))

    def readPNGData(self):
        try:
            with open(self.filePath, "rb") as f:
                content = f.read()
            iend_signature = b"\x00\x00\x00\x00IEND\xaeB`\x82"
            end_index = content.find(iend_signature)
            if end_index == -1:
                raise ValueError("Not a valid PNG file")
            data_start = end_index + len(iend_signature)
            appended_data = content[data_start:]
            return pickle.loads(appended_data)
        except Exception as e:
            return PacketData()

    def cleanPNGData(self):
        with open(self.filePath, "rb") as f:
            content = f.read()

        iend_signature = b"\x00\x00\x00\x00IEND\xaeB`\x82"
        end_index = content.find(iend_signature)
        if end_index == -1:
            raise ValueError("Not a valid PNG file")

        clean_content = content[: end_index + len(iend_signature)]

        with open(self.filePath, "wb") as f:
            f.write(clean_content)

    def checkPNGData(self):
        with open(self.filePath, "rb") as f:
            content = f.read()

        iend_signature = b"\x00\x00\x00\x00IEND\xaeB`\x82"
        end_index = content.find(iend_signature)
        if end_index == -1:
            raise ValueError("Not a valid PNG file")

        data_start = end_index + len(iend_signature)
        appended_data = content[data_start:]

        return bool(appended_data)
