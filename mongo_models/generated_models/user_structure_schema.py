from typing import List


class Userstructure:
    class Surgeries:
        class Entries(list):
            class Items:
                class StandardResponses(list):
                    class Items:
                        def __init__(self, values: dict = None):
                            values = values if values is not None else {}
                            self.question_code: float = values.get("question_code", None)
                            self.response: str = values.get("response", None)

                        def __repr__(self):
                            return "Items[" + ", ".join((
                                f"question_code: {repr(self.question_code)}",
                                f"response: {repr(self.response)}",
                            )) + "]"

                    def __init__(self, values: list = None):
                        super().__init__()
                        values = values if values is not None else []
                        self[:] = [self.Items(value) for value in values]

                class DoctorResponses(list):
                    class Items:
                        def __init__(self, values: dict = None):
                            values = values if values is not None else {}
                            self.question: str = values.get("question", None)
                            self.response: str = values.get("response", None)

                        def __repr__(self):
                            return "Items[" + ", ".join((
                                f"question: {repr(self.question)}",
                                f"response: {repr(self.response)}",
                            )) + "]"

                    def __init__(self, values: list = None):
                        super().__init__()
                        values = values if values is not None else []
                        self[:] = [self.Items(value) for value in values]

                def __init__(self, values: dict = None):
                    values = values if values is not None else {}
                    self.date: float = values.get("date", None)
                    self.standard_responses: List[Items] = self.StandardResponses(values=values.get("standard_responses"))
                    self.doctor_responses: List[Items] = self.DoctorResponses(values=values.get("doctor_responses"))

                def __repr__(self):
                    return "Items[" + ", ".join((
                        f"date: {repr(self.date)}",
                        f"standard_responses: {repr(self.standard_responses)}",
                        f"doctor_responses: {repr(self.doctor_responses)}",
                    )) + "]"

            def __init__(self, values: list = None):
                super().__init__()
                values = values if values is not None else []
                self[:] = [self.Items(value) for value in values]

        def __init__(self, values: dict = None):
            values = values if values is not None else {}
            self.code: str = values.get("code", None)
            self.status: str = values.get("status", None)
            self.current_doctor_questionnaire: List[str] = values.get("current_doctor_questionnaire", None)
            self.entries: List[Items] = self.Entries(values=values.get("entries"))

        def __repr__(self):
            return "Surgeries[" + ", ".join((
                f"code: {repr(self.code)}",
                f"status: {repr(self.status)}",
                f"current_doctor_questionnaire: {repr(self.current_doctor_questionnaire)}",
                f"entries: {repr(self.entries)}",
            )) + "]"

    def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.user_id: str = values.get("user_id", None)
        self.surgeries = self.Surgeries(values=values.get("surgeries"))

    def __repr__(self):
        return "Userstructure[" + ", ".join((
            f"user_id: {repr(self.user_id)}",
            f"surgeries: {repr(self.surgeries)}",
        )) + "]"
