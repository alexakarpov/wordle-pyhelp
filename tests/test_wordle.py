from wordle.wordle import split, exclude, pin

def test_split1():
  assert split("qwerty") == ['q','w','e','r','t','y']

def test_split2():
  assert split("") == []

def test_exclude():
  words = ["qwert", "tyuio","opasd","fghjk","lzxcv"]
  trimmed = exclude(words, 'eoj')
  assert len(trimmed) == 1
  assert trimmed[0] == "lzxcv"

def test_exclude_all():
  words = ["qwert", "awsed","zxdfv","polkj","zxcrs"]
  trimmed = exclude(words, 'asqzj')
  assert len(trimmed) == 0

def test_pin():
  words = ["baboq", "asdfg", "manoq", "bibop" "xxxxx", "alpla"]
  pinned = pin(words, "b.b..")
  assert len(pinned) == 2

def test_pin2():
  words = ["babak", "asdfg", "manoq", "bibop", "xxxxx", "blpla"]
  pinned = pin(words, "b....")
  assert len(pinned) == 3
  assert "babak" in pinned and "blpla" in pinned and "bibop" in pinned

print("ok")
