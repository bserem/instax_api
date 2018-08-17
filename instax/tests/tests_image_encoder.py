"""
Instax SP3 Test File.

@jpwsutton 2016/17
"""
import unittest
import instax


class ImageTests(unittest.TestCase):
    """Instax-SP3 Image Encoding / Decoding Test Class."""

    def test_encode_and_decode_image(self):
        """Test Decoding and then Encoding a premade instax image."""
        encodedImageFile = "instax/tests/testEncodedImage.instax"
        rawInstaxBytes = None
        with open(encodedImageFile, 'rb') as infile:
            rawBytes = infile.read()
            rawInstaxBytes = bytearray(rawBytes)
        self.assertEqual(len(rawInstaxBytes), 1920000)

        # Initialize The Instax Image
        instaxImage = instax.InstaxImage()

        # Decode the Image from the Instax Byte Array
        instaxImage.decodeImage(rawInstaxBytes)

        # Re-Encode the image

        encodedImage = instaxImage.encodeImage()
        self.assertEqual(len(encodedImage), 1920000)

        for x in range(1920000):
            if(rawInstaxBytes[x] != encodedImage[x]):
                message = ("Mismatch: Index: %s: %s != %s" %
                           (x, rawInstaxBytes[x], encodedImage[x]))
                self.fail(message, True)


if __name__ == '__main__':

    unittest.main()
