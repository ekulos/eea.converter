""" Converters
"""
import logging
import sys, os
from subprocess import Popen, PIPE, STDOUT
logger = logging.getLogger('eea.converter')

CLOSE_FDS = not sys.platform.startswith('win')

def can_convert_image():
    """ Check if ImageMagick is installed
    """
    # Test for ImageMagik
    process = Popen('convert --version', shell=True,
                    stdin=PIPE, stdout=PIPE, stderr=STDOUT,
                    close_fds=CLOSE_FDS)
    res = process.stdout.read()
    if 'imagemagick' not in res.lower():
        logger.warn(
            ("ImageMagick NOT FOUND: "
             "Automatic generation of report's cover image is not supported."))
        return False
    return True

WK_COMMAND = os.environ.get('WKHTMLTOPDF_PATH')
if WK_COMMAND:
    logger.info('wkhtmltopdf found at  %s: ', WK_COMMAND)
else:
    WK_COMMAND = 'wkhtmltopdf'
    logger.warn("wkhtmltopdf path unknown, hope it's in the path")

CAN_CONVERT_IMAGE = can_convert_image()
CAN_GENERATE_COVER_IMAGE = CAN_CONVERT_IMAGE
