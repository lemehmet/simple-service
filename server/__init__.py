import connexion
import logging
from connexion.resolver import RelativeResolver

from server.common.definitions import SERVICE_NAME
from server.common.util import get_spec_dir, get_spec_file


def init_app(test_config=None):
    logging.info("Starting service %s", SERVICE_NAME)
    spec_dir = get_spec_dir()
    logging.info("Spec path: %s", spec_dir)
    options = {"swagger_ui": True}
    app = connexion.FlaskApp(SERVICE_NAME, specification_dir=spec_dir, options=options)
    app.add_api(specification=get_spec_file(),
                resolver=RelativeResolver('server.api.handlers'), resolver_error=501,
                pythonic_params=True)
    return app
