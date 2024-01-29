from logging import getLogger, basicConfig, DEBUG


logger = getLogger(__name__)
basicConfig(format='%(asctime)s %(levelname)s %(message)s', datefmt="%d-%m-%Y %H:%M:%S" level=DEBUG)
