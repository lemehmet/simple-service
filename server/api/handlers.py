import connexion
import logging
import server.app

from flask import send_file

from server.common.util import append_headers, get_spec_path


def getHealth():
    return server.app.getHealth()


def getSpec():
    spec_path = get_spec_path()
    logging.info("Returning spec: %s", spec_path)
    return send_file(path_or_file=spec_path, mimetype='application/x-yaml')


def getServiceDescription():
    return server.app.getServiceDescription()


def postCalculate():
    return server.app.postCalculate(connexion.request.json)
