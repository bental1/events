from flask_restful import Resource, Api

from events_db import Events, engine
from db_manipulations import DBManipulations


class EventAPI(Resource):
    db_manipulations = DBManipulations(Events, engine)

    def get(self, event_id):
        return self.db_manipulations.get_row_by_id(event_id)

    def delete(self, event_id):
        return self.db_manipulations.delete_row_by_id(event_id)
