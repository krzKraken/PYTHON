# Genera ficheros de registro

import logging

# => El nivel desde que queremos reportar en consola
logging.basicConfig(level=logging.INFO)

logging.debug("Mensaje de debug")
logging.warning("Mensaje de advertencia")
logging.info("Mensaje de informacion")
logging.error("Mensaje de Error Critico")
logging.critical("Mensaje de Error Critico")
