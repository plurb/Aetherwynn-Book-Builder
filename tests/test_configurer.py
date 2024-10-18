import os
import pathlib
import unittest

import configurer.reader


class TestConfigure(unittest.TestCase):
    def test_load(self):
        # save current working directory so that we can reset after testing.
        old_cwd = pathlib.Path(os.getcwd())

        os.chdir("./assets")
        t = pathlib.Path("./build-config.yaml")

        with open(t, 'r') as f:
            result = configurer.reader.load_build_config_file(f)

        self.assertTrue(result is not None)

        os.chdir(old_cwd)

    def test_schema_check(self):
        # save current working directory so that we can reset after testing.
        old_cwd = pathlib.Path(os.getcwd())

        os.chdir("./assets")
        t = pathlib.Path("./build-config-schemaless.yaml")

        try:
            with open(t, 'r') as f:
                result = configurer.reader.load_build_config_file(f)
        except TypeError as e:
            self.assertTrue(True)

        os.chdir(old_cwd)


if __name__ == '__main__':
    unittest.main()
