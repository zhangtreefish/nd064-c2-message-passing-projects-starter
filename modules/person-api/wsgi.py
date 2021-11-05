import os
import logging

from app import create_app

app = create_app(os.getenv("FLASK_ENV") or "test")
if __name__ == "__main__":
    logging.basicConfig(filename='app.log', level=logging.DEBUG, format=f'%(asctime)s  %(message)s')
    app.run(host='0.0.0.0', port=5002, debug=True)
