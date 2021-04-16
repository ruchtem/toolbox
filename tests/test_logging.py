from unittest import TestCase

import logging
from rtb import log_first_n, setup_logger

class TestSetupLogger(TestCase):

    def test_setup(self):
        logger = setup_logger(output=None, name='test')
        logger.warning('setup1')
    

    def test_setup2(self):
        setup_logger(output=None, name='test2')

        logger = logging.getLogger('test2')
        logger.debug('got the right logger?')
        
    
    def test_log_first_n(self):
        setup_logger(output=None, name=__name__)
        for i in range(10):
            log_first_n(logging.DEBUG, f"log no {i}", n=5)
