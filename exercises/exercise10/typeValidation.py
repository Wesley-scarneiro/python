class TypeValidation:
    @staticmethod
    def validation(kind: str, data: int | float | complex | str | bool) -> bool:
        if kind == "int":
            if isinstance(data, bool):
                return False
            else:
                if isinstance(data, int):
                    return True
                else:
                    return False
        elif kind == "float":
            if isinstance(data, float):
                return True
            else:
                return False
        elif kind == "complex":
            if isinstance(data, complex):
                return True
            else:
                return False
        elif kind == "str":
            if isinstance(data, str):
                return True
            else:
                return False
        elif kind == "bool":
            if isinstance(data, bool):
                return True
            else:
                return False
        else:
            return False