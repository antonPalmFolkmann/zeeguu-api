#!/bin/env python
import sys
import logging

# this is needed since when run as wsgi this script
# can't access the systems' env vars. so we load them
# in another local configuration file.
try:
    import env_var_defs

except:
    print("didn't find env_var_defs. hopefully there's envvars defined")

from zeeguu.api.app import app as application

application.logger.debug(application.instance_path)

logging.getLogger("elasticsearch").setLevel(logging.CRITICAL)


if len(sys.argv) > 1 and sys.argv[1] == "run":
    # Make sure to keep this in sync with zeeguu_api_dev.wsgi
    application.run(
        host=application.config.get("HOST", "localhost"),
        port=application.config.get("PORT", 9001),
        debug=True,
    )
