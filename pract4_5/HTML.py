class HTML:
    code = ""

    class body:
        def __enter__(self):
            HTML.code += "<body>\n"

        def __exit__(self, exc_type, exc_val, exc_tb):
            HTML.code += "</body>\n"

    class div:
        def __enter__(self):
            HTML.code += "<div>\n"

        def __exit__(self, exc_type, exc_val, exc_tb):
            HTML.code += "</div>\n"

    class p:
        def __init__(self, text):
            HTML.code += f"<p>{text}</p>\n"

    def get_code(self):
        return self.code
