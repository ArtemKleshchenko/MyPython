class GroupLimitError(Exception):
    def __init__(self, message='Досягнуто ліміту студентів у групі (максимум 10)'):
        super().__init__(message)