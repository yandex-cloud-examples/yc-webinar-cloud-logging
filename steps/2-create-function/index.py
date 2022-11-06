import logging
from pythonjsonlogger import jsonlogger

class YcLoggingFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(YcLoggingFormatter, self).add_fields(log_record, record, message_dict)
        log_record['logger'] = record.name
        log_record['level'] = str.replace(str.replace(record.levelname, "WARNING", "WARN"), "CRITICAL", "FATAL")


logHandler = logging.StreamHandler()
logHandler.setFormatter(YcLoggingFormatter('%(message)s %(level)s %(logger)s'))

logger = logging.getLogger()
logger.addHandler(logHandler)
logger.setLevel(logging.DEBUG)

def handler(event, context):
    logger.setLevel(logging.DEBUG)
    logger.info("My log message info", extra={"the-key-fom-info": "the-value-from-info"})
    logger.error("My log message error", extra={"the-key-fom-error": "the-value-from-error"})
    logger.debug("My log message debug", extra={"the-key-fom-debug": "the-value-from-debug"})

    return {
        'statusCode': 200,
        'body': 'Hello World!',
    }