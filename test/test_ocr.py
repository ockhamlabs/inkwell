import logging
import os
import unittest

from inkwell.io import read_image
from inkwell.ocr import OCRFactory, OCRType

_logger = logging.getLogger(__name__)


class TestOCR(unittest.TestCase):

    def setUp(self):
        _logger.debug("Running test: %s", self._testMethodName)

    @staticmethod
    def _load_test_image():
        curr_path = os.path.dirname(__file__)
        image_path = os.path.join(curr_path, "./data/sample.png")
        image = read_image(image_path)
        return image

    def _test_results(self, text: str):
        assert isinstance(text, str), "Text should be a string"
        assert len(text) > 0, "Text should not be empty"
        assert "receipt" in text, "Text should contain 'receipt'"

    def test_tesseract_ocr(self):
        ocr = OCRFactory.get_ocr(OCRType.TESSERACT, lang="eng")

        image = self._load_test_image()

        text = ocr.process(image)
        self._test_results(text)
