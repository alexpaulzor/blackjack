def boolean_input(
    prompt="", errorMessage="Invalid input, please try again.",
        default=None):
    line = string_input(
        prompt, ["yes", "y", "no", "n"], errorMessage, default)
    return (line == "yes" or line == "y")


def integer_input(
        prompt="", errorMessage="Invalid input, please enter an integer.",
        default=None, minVal=None, maxVal=None):
    line = None
    while line is None:
        try:
            line = string_input(prompt, None, errorMessage, default)
            line = int(line)
            if (minVal is not None and line < minVal) or (maxVal is not None and line > maxVal):
                if minVal is not None and maxVal is not None:
                    validRange = f"between {minVal} and {maxVal}"
                elif minVal is not None:
                    validRange = f"at least {minVal}"
                else:
                    validRange = f"at most {maxVal}"
                print(f"Value must be {validRange}.")
                line = None
        except Exception as e:
            print(e)
            print(errorMessage)
            line = None
    return line


# Get a line of information from the user.    prompt is printed first.
# If options is not None, it is alist of allowed string responses.
def string_input(
        prompt="", options=None,
        errorMessage="Invalid input, please try again.", default=None):
    line = input(prompt).strip()
    while options is not None and line not in options and not (
            default is not None and line == ""):
        print(f"'{line}':" + errorMessage)
        if options is not None:
            print("[" + ", ".join(options) + "]")
        line = input(prompt).strip()

    if default is not None and line == "":
        return default

    return line
