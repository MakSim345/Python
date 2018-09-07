class singleton(object):

  __instance = None

  def __new__(cls):
    if cls.__instance is None:
      cls.__instance = super(singleton, cls).__new__()
    return cls.__instance
  def __init__(self):
    assert self.__instance is None
	
class singleton(object):

  __instance = None

  def __init__(self):
    assert self.__instance is None

  @classmethod
  def getInstance(cls):
    if cls.__instance is None:
      cls.__instance = cls()
    return cls.__instance