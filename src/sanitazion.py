# ? --------------------------------------------------------------
# ? This function is not used, but I have made it for future use -
# ? --------------------------------------------------------------

from functools import wraps, reduce
import bleach


# * ------------------ FUNCTION SANITIZER ---------------------- *

def sanitize_xss(input_string: str) -> str:
    return bleach.clean(input_string)


def sanitize_sql(input_string: str) -> str:
    banned_char = [
        "'", '"', "/", "--", "/*", "*/", ";",
    ]
    return reduce(lambda s, char: s.replace(char, ""), banned_char, input_string)


def general_sanitizer(input_string: str) -> str:
    banned_char = [
        "'", '"', "\\", "/", "=", "<", ">", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "{", "}", "[", "]",
        ";", ":", "|", "\\"
    ]
    return reduce(lambda s, char: s.replace(char, ""), banned_char, input_string).strip()


# * ------------------ DECORATOR ---------------------- *

def sanitize_input(*sanitizers):
    def decorator(function):
        @wraps(function)
        async def wrapper(*args, **kwargs):
            new_kwargs = {}
            for key, value in kwargs.items():
                if key in sanitizers[0]:
                    new_kwargs[key] = sanitizers[0][key](value)
                else:
                    new_kwargs[key] = value
            return await function(*args, **new_kwargs)

        return wrapper

    return decorator
