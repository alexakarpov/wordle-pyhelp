import unittest
from wordle import split, exclude, pin, somewhere

class TestWorldleHelperMethods(unittest.TestCase):

  def test_split1(self):
    assert split("qwerty") == ['q','w','e','r','t','y']

  def test_split2(self):
    assert split("") == []

  def test_exclude(self):
    words = ["qwert", "tyuio","opasd","fghjk","lzxcv"]
    trimmed = exclude(words, 'eoj')
    assert len(trimmed) == 1
    assert trimmed[0] == "lzxcv"

  def test_exclude_all(self):
    words = ["qwert", "awsed","zxdfv","polkj","zxcrs"]
    trimmed = exclude(words, 'asqzj')
    assert len(trimmed) == 0

  def test_pin(self):
    words = ["baboq", "asdfg", "manoq", "bibop" "xxxxx", "alpla"]
    pinned = pin(words, "b.b..")
    assert len(pinned) == 2

  def test_pin2(self):
    words = ["babak", "asdfg", "manoq", "bibop", "xxxxx", "blpla"]
    pinned = pin(words, "b....")
    assert len(pinned) == 3
    assert "babak" in pinned and "blpla" in pinned and "bibop" in pinned

  def test_somewhere(self):
    words = ["seabx", "acsce", "aefgh", "oseqr", "ascvb", "xiopl", "laleg"]
    assert len(somewhere(words, "ase")) == 2

  def test_somewhere2(self):
    words = ["abcde", "abcdf", "abcdx", "oseqr", "ascvb", "xiopb", "laleg"]
    assert somewhere(words, "bed") == ['abcde']

  def test_somewhere3(self):
    words = ["aopde", "oioio", "abcdx", "oseqr", "ascvb", "xiopb", "laleg"]
    assert somewhere(words, "poi") == ['xiopb']


if __name__ == '__main__':
    unittest.main()
