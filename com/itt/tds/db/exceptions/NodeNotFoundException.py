"""NodeNotFoundException Class"""

try:
    from com.itt.tds.db.exceptions.RecordNotFoundException import RecordNotFoundException

except ImportError as error:
    print(error.__str__())
    log = LogManager.get_logger()
    if log:
        log.log_warn(
            'NodeNotFoundException', 'Import Module', error.__str__(), str(error))


class NodeNotFoundException(RecordNotFoundException):

    """NodeNotFoundException Class"""

    def __init__(self, error_string, error_code=None):
        super().__init__(error_string, error_code)
