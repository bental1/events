from sqlalchemy.orm import sessionmaker

from utils.alchemy_to_json import AlchemyEncoder


class DBManipulations(object):
    def __init__(self, db, engine):
        self.session = sessionmaker(bind=engine)()
        self.db = db

    def add_row(self, **row_data):
        new_row = self.db(**row_data)


        self.session.add(new_row)
        self.session.commit()

        return row_data

    def get_all_rows(self):
        all_rows = self.session.query(self.db).all()

        return {row.id: AlchemyEncoder().alchemy_to_json(row) for row in all_rows}

    def get_row_by_id(self, row_id):
        row = self.session.query(self.db).filter(self.db.id == row_id)[0]

        return AlchemyEncoder().alchemy_to_json(row)

    def delete_row_by_id(self, row_id):
        row_to_delete = self.session.query(self.db).filter(self.db.id == row_id)
        row_data = AlchemyEncoder().alchemy_to_json(row_to_delete[0])

        row_to_delete.delete()

        self.session.commit()

        return row_data

    def update_row_by_id(self, row_id, **row_data):
        row = self.session.query(self.db).filter(self.db.id == row_id)

        row.update(row_data)
        self.session.commit()

        return AlchemyEncoder().alchemy_to_json(row.all()[0])

    def get_by_parameters(self, **parameters):
        filtered_rows = self.session.query(self.db).filter_by(**parameters).all()

        return {row.id: AlchemyEncoder().alchemy_to_json(row) for row in filtered_rows}

    def sort_by_parameter(self, parameter):
        sorted_rows = self.session.query(self.db).order_by(parameter)

        return {str(row.id): AlchemyEncoder().alchemy_to_json(row) for row in sorted_rows}

    def sort_by_json_length(self, parameter):
        import pdb; pdb.set_trace()
        sorted_rows = self.session.query(self.db).order_by(len(self.db.participants))

        return {str(row.id): AlchemyEncoder().alchemy_to_json(row) for row in sorted_rows}

