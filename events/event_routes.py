import datetime

from flask import request, Flask

from events_db import Events, engine
from db_manipulations import DBManipulations

from apscheduler.schedulers.background import BackgroundScheduler
from flask_socketio import SocketIO

TIMESTAMP = "%Y-%m-%d %H:%M:%S"
REMINDER_MESSAGE = "Your meeting time is coming..."


flask_app = Flask(__name__)
scheduler = BackgroundScheduler(daemon=True)
socketio = SocketIO(flask_app)


@flask_app.route("/events", methods=['GET'])
def get_all_events():
    db_manipulations = DBManipulations(Events, engine)

    return db_manipulations.get_all_rows()


@flask_app.route("/events", methods=['POST'])
def create_new_event():
    db_manipulations = DBManipulations(Events, engine)
    new_event = db_manipulations.add_row(**dict(request.values))

    _add_scheduled_reminder_event(new_event)

    return new_event


@flask_app.route("/events/<int:event_id>", methods=['PUT'])
def update_event_by_id(event_id):
    db_manipulations = DBManipulations(Events, engine)
    updated_row = db_manipulations.update_row_by_id(event_id, **dict(request.values))

    _add_scheduled_reminder_event(updated_row)

    return updated_row


@flask_app.route("/events/filter", methods=['GET'])
def get_events_by_filters():
    db_manipulations = DBManipulations(Events, engine)

    return db_manipulations.get_by_parameters(**dict(request.values))


@flask_app.route("/events/sort/<string:parameter>", methods=['GET'])
def sort_events_by_filter(parameter):
    db_manipulations = DBManipulations(Events, engine)

    if parameter == "participants":
        return db_manipulations.sort_by_json_length(parameter)

    return db_manipulations.sort_by_parameter(parameter)


def get_scheduled_date_of_event(event):
    return datetime.datetime.strptime(event["date"], TIMESTAMP)


def _add_scheduled_reminder_event(event):
    scheduled_date_of_event = get_scheduled_date_of_event(event)
    unique_job_id = str(hash(event["creation_time"]))

    if scheduled_date_of_event > datetime.datetime.now():
        if unique_job_id in [job.id for job in scheduler.get_jobs()]:
            scheduler.remove_job(unique_job_id)

        scheduler.add_job(send_reminder, "date", run_date=scheduled_date_of_event - datetime.timedelta(minutes=30),
                          id=unique_job_id)


def send_reminder():
    socketio.emit('message', {'reminder': REMINDER_MESSAGE})


scheduler.start()
