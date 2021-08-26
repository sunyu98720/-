import os


class PoBuilder():
    json = {
        "className": "builderDemo",
        "function": "demo",
        "codeBlack": "pass",
        "par": ["user_loc", "password_loc", "vscode"]
    }

    def __init__(self, filePath, fileName, fileType):
        self.path = filePath
        self.type = fileType
        self.name = fileName

    def file_write(self, msg):
        fullPath = self.path + "\\" + self.name + self.type
        file = open(fullPath, 'w')
        file.write(msg)

    def class_builder(self):
        py_content = \
            "class {}:\n \
                def {}(self):\n \
                    {}".format(self.json.get("className"),
                               self.json.get("function"),
                               self.json.get("codeBlack")
                               )
        self.file_write(py_content)


if __name__ == '__main__':
    a = PoBuilder(r"D:\Project_Save\Test_SCRM_Ul_Auto\venv\Include\Common", "demo", ".py")
    a.class_builder()
