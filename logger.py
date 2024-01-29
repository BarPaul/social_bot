from logging import getLogger, basicConfig, DEBUG


logger = getLogger(__name__)
basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=DEBUG)
