import dataclasses
import os
import pathlib

from functional import seq


@dataclasses.dataclass
class FilesAndDirectories:
    files: list[pathlib.Path]
    directories: list[pathlib.Path]


def set_working_directory(working_directory: pathlib.Path) -> pathlib.Path:
    """
    Sets the working directory.

    :param working_directory: The directory to set as the working directory.
    :return: Returns the working directory.
    """

    if not working_directory.exists():
        raise NotADirectoryError(working_directory)
    if not working_directory.is_dir():
        raise NotADirectoryError(working_directory)

    oldWorkingDirectory = pathlib.Path(os.getcwd())

    if oldWorkingDirectory == working_directory:
        # Trivial path.
        return working_directory

    os.chdir(working_directory)

    return pathlib.Path(os.getcwd())


def get_files_and_directories(path: pathlib.Path) -> FilesAndDirectories:
    """
    Gets the files and subdirectories of a path.

    :param path: The path to the directory to get all files and subdirectories.
    :return: The files and subdirectories of the path.
    """
    # Error cases.
    if not path.exists():
        raise NotADirectoryError(path)
    if not path.is_dir():
        raise NotADirectoryError(path)

    filesAndDirectories = FilesAndDirectories([], [])
    for (dirpath, dirnames, filenames) in os.walk(path):
        filesAndDirectories.files.extend(
            seq(filenames)
            .map(pathlib.Path)
            .map(lambda x: x.absolute())
            .to_list()
        )

        filesAndDirectories.directories.extend(
            seq(dirnames)
            .map(pathlib.Path)
            .map(lambda x: x.absolute())
            .to_list()
        )

    return filesAndDirectories
