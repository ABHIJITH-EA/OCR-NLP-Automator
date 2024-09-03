from enum import IntEnum

class FileStatus(IntEnum):
    IN_PROGRESS = 0
    COMPLETED = 1
    FAILED = 2


class FileActiveStatus(IntEnum):
    DELETED = 0
    ACTIVE = 1
