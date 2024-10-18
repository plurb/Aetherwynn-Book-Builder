import os
import pathlib
import unittest

from crawler import load_dirs


class TestFileCrawler(unittest.TestCase):
    def test_set_working_directory(self):
        print("Testing set_working_directory...")

        # save current working directory so that we can reset after testing.
        old_cwd = pathlib.Path(os.getcwd())

        target = "./assets"
        expected = pathlib.Path(target).absolute()
        new_dir = load_dirs.set_working_directory(pathlib.Path(target))
        self.assertEqual(new_dir, expected)

        # reset after finishing test.
        os.chdir(old_cwd)

    def test_get_files_and_directories(self):
        print("Testing get_files_and_directories...")

        # save current working directory so that we can reset after testing.
        old_cwd = pathlib.Path(os.getcwd())

        os.chdir("./assets")
        target = pathlib.Path("./Barbarian")
        files_and_directories = load_dirs.get_files_and_directories(target)
        print(f"Files: {files_and_directories.files}")
        print(f"Directories: {files_and_directories.directories}")

        # reset after finishing test.
        os.chdir(old_cwd)


if __name__ == '__main__':
    unittest.main()
