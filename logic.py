import os
from random import randint


class Mixer:

    def shuffle(self, dir: str) -> int:
        """Adds a random number and underscore to the beginning of
        the file name and return 0. If path isn't correct then return 1."""
        status_code = 0

        try:
            for file in os.listdir(dir):
                old_path = self._get_path_to_file(dir, file)
                file = self._get_clean_filename(file)
                new_path = self._get_path_to_file(dir,
                                                  self._get_random_number() + '_' + file)
                self._rename_file(old_path, new_path)
        except FileNotFoundError:
            status_code = 1

        return status_code

    @staticmethod
    def _get_path_to_file(dir: str, file: str) -> str:
        return os.path.join(dir, file)

    @staticmethod
    def _get_clean_filename(file: str) -> str:
        """if the file already contains numbers at the beginning
        of the name, then cut them off."""
        return file.split('_', 1)[-1] if file[0].isdigit() else file

    @staticmethod
    def _rename_file(old_name, new_name):
        os.rename(old_name, new_name)

    @staticmethod
    def _get_random_number(start=1, stop=500) -> str:
        return str(randint(start, stop))
