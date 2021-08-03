from typing import List


class Standardquestionnaire:
    class Questions(list):
        class Items:
            def __init__(self, values: dict = None):
                values = values if values is not None else {}
                self.type: str = values.get("type", None)
                self.code: float = values.get("code", None)
                self.scale: float = values.get("scale", None)
                self.text: str = values.get("text", None)

            def __repr__(self):
                return "Items[" + ", ".join((
                    f"type: {repr(self.type)}",
                    f"code: {repr(self.code)}",
                    f"scale: {repr(self.scale)}",
                    f"text: {repr(self.text)}",
                )) + "]"

        def __init__(self, values: list = None):
            super().__init__()
            values = values if values is not None else []
            self[:] = [self.Items(value) for value in values]

    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.questions: List[Items] = self.Questions(values=values.get("questions"))
        self.code: str = values.get("code", None)
        self.title: str = values.get("title", None)

    def __repr__(self):
        return "Standardquestionnaire[" + ", ".join((
            f"questions: {repr(self.questions)}",
            f"code: {repr(self.code)}",
            f"title: {repr(self.title)}",
        )) + "]"
