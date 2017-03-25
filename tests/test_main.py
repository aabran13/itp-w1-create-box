import unittest

from create_box import create_box

first_box_expected = """
****
****
****
""".lstrip()

second_box_expected = """
@
""".lstrip()

third_box_expected = """
xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxx
""".lstrip()


class TestCreateBox(unittest.TestCase):
    def test_box(self):
        self.assertEqual(create_box(3, 4, '*'), first_box_expected)

    def test_small_box(self):
        self.assertEqual(create_box(1, 1, '@'), second_box_expected)

    def test_third_box(self):
        self.assertEqual(create_box(3, 24, 'x'), third_box_expected)
        
    # Add your own test using third_box_expected

from create_box import create_hollow_box

fourth_box_expected = """
*****
*   *
*   *
*****
""".lstrip()

fifth_box_expected = """
@@@@@@
@    @
@    @
@@@@@@
""".lstrip()

sixth_box_expected = """
xxxxxxxxxxxxxxxxxxxxxxxx
x                      x
xxxxxxxxxxxxxxxxxxxxxxxx
""".lstrip()


class TestCreateHollowBox(unittest.TestCase):
    def test_box(self):
        self.assertEqual(create_hollow_box(4, 5, '*'), fourth_box_expected)

    def test_small_box(self):
        self.assertEqual(create_hollow_box(4, 6, '@'), fifth_box_expected)

    def test_third_box(self):
        self.assertEqual(create_hollow_box(3, 24, 'x'), sixth_box_expected)
        
