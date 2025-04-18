# Copyright (C) 2020 King-Konsto
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import gzip
import json
import os

from lib.cuckoo.common.constants import CUCKOO_ROOT
from lib.cuckoo.common.path_utils import path_exists


def get_dga_lookup_dict():
    """
    Retrieves the DGA (Domain Generation Algorithm) lookup dictionary from a gzipped JSON file.

    The function constructs the file path to the DGA lookup dictionary, checks if the file exists,
    and if it does, reads and decompresses the file, then loads its contents as a JSON object.
    If the file does not exist, it returns an empty dictionary.

    Returns:
        dict: The DGA lookup dictionary if the file exists, otherwise an empty dictionary.
    """
    dga_lookup_path = os.path.join(CUCKOO_ROOT, "data", "dga_lookup_dict.json.gz")
    if path_exists(dga_lookup_path):
        with gzip.GzipFile(dga_lookup_path, "r") as fin:
            return json.loads(fin.read().decode())

    return {}
