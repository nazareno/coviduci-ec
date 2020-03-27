from absl import logging
import jwt


class TokenEncoder:
  KEY = 'id'

  def __init__(self, config):
    self.config = config

  def encode(self, value) -> str:
    return jwt.encode(
      {self.KEY: value}, self.config.JWT_SECRET, algorithm='HS256').decode()


  def decode(self, token: str):
    try:
      obj = jwt.decode(token, self.config.JWT_SECRET, algorithms=['HS256'])
    except Exception as e:
      logging.error(f"Cannot decode token `{token}`, {e}")
      return
    return obj.get(self.KEY, None)

  def encode_hospital(self, hospital: str) -> str:
    return self.encode({'hospital': hospital})
