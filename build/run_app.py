"""
Wrapper file for app.py. This script sets the config options and runs the streamlit application module.
Used by PyInstaller as a base script in creating a single executable.
"""

import os
import streamlit.web.bootstrap

if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))

    flag_options = {
        "server.port": 8501,
        "global.developmentMode": False,
    }

    streamlit.web.bootstrap.load_config_options(flag_options=flag_options)
    flag_options["_is_running_with_streamlit"] = True
    streamlit.web.bootstrap.run(
        "./app.py",
        "streamlit run",
        [],
        flag_options,
    )
    