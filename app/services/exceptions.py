class Invalid_uuid_error(Exception):
    def __init__(self):
        self.message = (
            'O id do resíduo passado por parâmetro deve ser do formato uuid v4'
        )
        super().__init__(self.message)


class Not_found_item_error(Exception):
    def __init__(self, msg):
        self.message = msg
        super().__init__(self.message)


class Unauthorized_erro(Exception):
    def __init__(self, msg):
        self.message = msg
        super().__init__(self.message)
