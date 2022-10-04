class InvalidDataError(Exception):
    ...

class ContentSerializer:
    required_keys = {
        "title": str, 
        "module": str, 
        "description": str, 
        "students": int, 
        "is_active": bool
    }


    def __init__(self, *args, **kwargs):
        self.data = kwargs
        self.errors = {}


    def data_validation(self):
        self.ignore_extra_keys()

        try:
            self.validate_required_keys()
            self.expected_types()
            return True
        except InvalidDataError:
            return False
        

    def ignore_extra_keys(self):
        data_keys = set(self.data.keys())

        for key in data_keys:
            if key not in self.required_keys.keys():
                self.data.pop(key)
    
    def validate_required_keys(self):
        for key in self.required_keys.keys():
            if key not in self.data.keys():
                self.errors[key] = "missing key"

        if self.errors:
            raise InvalidDataError

    def expected_types(self):
        for key, value_type in self.required_keys.items():
            if type(self.data[key]) is not value_type:
                self.errors[key] = f'must be a {value_type.__name__}'

        if self.errors:
            raise InvalidDataError
