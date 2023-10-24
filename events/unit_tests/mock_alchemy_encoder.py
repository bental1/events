
class MockAlchemyEncoder(object):
    def alchemy_to_json(self, event):
        return event.__dict__
