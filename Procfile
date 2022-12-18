web: gunicorn -w 4 -k uvicorn.workers.UvicornWorker app:app --reload
heroku ps:scale web=1
