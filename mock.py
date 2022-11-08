from unittest.mock import Mock

 mock: Mock = Mock()

 import json
 data = json.dumps( {'a':1})
 json = mock
 print(dir(json))