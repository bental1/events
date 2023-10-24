# events project
event repository for alphabet interview

## API
- GET /events - get all scheduled events
- GET /events/filter - filter events by Query params (e.g GET localhost:5000/events/filter?name=meeting_name)
- GET /events/sort/:attribute - sort event table by attribute (e.g GET localhost:5000/events/sort/id)
- GET /events/:id - get event by event id

- POST /events - create new event by Query params

- DELETE /events/:id - delete event by event id

- PUT /event/:id - configure an existing event by Query params (e.g PUT localhost:5000/events/1?name=meeting_name)

## Implementation
- DB - MySQL - columns: id, name, participants, location, date (Not a good choice because there are no arrays in this type of DB)
- DB integeration with code - sqlalchemy package (Saved me some SQL queries)
- Python backend framework - Flask

## Before you run the code
- Connect to a MySql DB and create a db named "alchemy"
- If you wish to get reminders of your events run client.py
- Use Postman for sending queries

## Modules
- utils package - convertion from SqlAlchemy objects to json
- client.py - client code for contacting by SocketIO
- db_manipulations.py - abstract functions for manipulating the DB in all the ways required
- event_api.py - common /event request handle
- event_routes.py - all the other routes required
- events_db.py - DB class and table creation logic
- main.py - run Flask app

## Further work required
- could be a good idea to change the db
- finish tests
- requirements.txt
- setup.py
- run with docker
- add information to "30 minutes to meeting" message
