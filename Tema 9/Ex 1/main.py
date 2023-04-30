from abc import ABC, abstractmethod
import subprocess


class Handler(ABC):
    @abstractmethod
    def handle(self, file_path):
        pass


class KotlinHandler(Handler):

    def __init__(self, next_handler, command):
        self.next = None
        self.command = command
        self.set_next(next_handler)

    def set_next(self, next_handler):
        self.next = next_handler

    def handle(self, file_path):
        f = open(file_path, 'r')
        content = f.read()

        if 'fun main(args: Array<String>)' in content:
            self.command.handle_command(file_path, "kotlin")
        else:
            self.next.handle(file_path)


class PythonHandler(Handler):

    def __init__(self, next_handler, command):
        self.next = None
        self.command = command
        self.set_next(next_handler)

    def set_next(self, next_handler):
        self.next = next_handler

    def handle(self, file_path):
        f = open(file_path, 'r')
        content = f.read()

        if "if __name__ == '__main__':" in content:
            self.command.handle_command(file_path, "python")
        else:
            self.next.handle(file_path)


class JavaHandler(Handler):

    def __init__(self, next_handler, command):
        self.next = None
        self.command = command
        self.set_next(next_handler)

    def set_next(self, next_handler):
        self.next = next_handler

    def handle(self, file_path):
        f = open(file_path, 'r')
        content = f.read()

        if 'public static void main(String args[])' in content:
            self.command.handle_command(file_path, "java")
        else:
            self.next.handle(file_path)


class BashHandler(Handler):

    def __init__(self, command):
        self.command = command

    def handle(self, file_path):
        f = open(file_path, 'r')
        content = f.read()

        if '#!/bin/bash' in content:
            self.command.handle_command(file_path, "bash")
        else:
            print("Fisierul nu respecta formatele suportate")


class Command:
    def handle_command(self, file_path, file_type):
        if file_type == "kotlin":
            subprocess.run(file_path)
        elif file_type == "python":
            subprocess.run(file_path)
        elif file_type == "java":
            subprocess.run(file_path)
        elif file_type == "bash":
            subprocess.run(file_path)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    filepath = input("file_path=")
    command1 = Command()

    bash_handler = BashHandler(command1)
    java_handler = JavaHandler(bash_handler, command1)
    python_handler = PythonHandler(java_handler, command1)
    kotlin_handler = KotlinHandler(python_handler, command1)

    kotlin_handler.handle(filepath)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
