from dataclasses import dataclass
from pathlib import Path


@dataclass
class ProjectVariable:
    script_path: Path()
    open_source_path: Path()
    common_path: Path()
    build_path: Path()

    def __init__(self):
        print("Setted")
        self.script_path = Path('.')
        self.open_source_path = Path.joinpath(
            self.script_path, '..', 'Common', 'OpenSource')
        self.common_path = Path.joinpath(self.script_path, '..', 'Common')
        self.build_path = Path.joinpath(self.script_path, '..', 'Build')


class Singleton():
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        """ Virtually private constructor. """
        print(Singleton.__instance)
        print('Constructor')
        self.variables = ProjectVariable()
        if Singleton.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self


if __name__ == "__main__":
    variables = ProjectVariable()
    single_variable = Singleton.getInstance()
    print(single_variable)
    single_variable1 = Singleton.getInstance()
    print(single_variable1)
    single_variable2 = Singleton.getInstance()
    print(single_variable2)
