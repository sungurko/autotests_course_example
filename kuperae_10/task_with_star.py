# Есть маркер @pytest.mark.id_check(1, 2, 3), нужно вывести на печать, то что в него передано
#
# >>> 1, 2, 3

import pytest
import sys


@pytest.mark.id_check(1, 2, 3)
def test():
    print(pytest.mark.id_check().with_args)
