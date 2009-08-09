#!/bin/bash

pyuic4 -o configForm_ui.py ../ui/configForm.ui

pyrcc4 -o images_rc.py images.qrc
