# import the main window object (mw) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showText
# import all of the Qt GUI library
from aqt.qt import *


def showDeckJson():
    import json
    jsonStr = mw.col.db.scalar(
            f"""
        SELECT decks FROM col LIMIT 1"""
        )
    prettyJson = json.dumps(json.loads(jsonStr), indent=4)
    showText(prettyJson, title="Deck JSON", minWidth=600, minHeight=600)


action = QAction("Show Deck JSON", mw)
action.triggered.connect(showDeckJson)
mw.form.menuTools.addAction(action)