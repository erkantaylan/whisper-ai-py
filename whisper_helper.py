import json

import whisper


class WhisperHelper:
    def __init__(self):
        self.model = whisper.load_model('large')

    def save_to_file(self, media_file, output):
        result = self.model.transcribe(media_file)
        file = open(output, 'a')
        file.write(json.dumps(result))
        file.close()

    def get_text(self, media_file):
        """
        :rtype: str
        """
        result = self.model.transcribe(media_file)
        return result
        # return result["text"]
