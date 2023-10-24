from db_manipulations import DBManipulations
from unit_tests.mock_alchemy_encoder import MockAlchemyEncoder
from unit_tests.mock_events import MockEvents

import sqlalchemy.orm
import utils

from unit_tests.mock_session import MockSession

sqlalchemy.orm.sessionmaker = None

db_manipulations_instance = DBManipulations(MockEvents(), None)
db_manipulations_instance.session = MockSession()

def test_get_all_rows():
    utils.alchemy_to_json.AlchemyEncoder = MockAlchemyEncoder
    import pdb; pdb.set_trace()
    print(db_manipulations_instance.get_all_rows())
