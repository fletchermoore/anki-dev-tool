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


class DebugHtml:
    def __init__(self):
        self.clear()

    def clear(self):
        self.webHtml = None
        self.toolbarHtml = None
        self.bottomHtml = None

    def requestHtml(self):
        mw.web._page.toHtml(self.webCb)
        mw.toolbarWeb._page.toHtml(self.toolbarCb)
        mw.bottomWeb._page.toHtml(self.bottomCb)

    def webCb(self, html):
        self.webHtml = html
        self.onHtml()

    def toolbarCb(self, html):
        self.toolbarHtml = html
        self.onHtml()

    def bottomCb(self, html):
        self.bottomHtml = html
        self.onHtml()

    def onHtml(self):
        if self.webHtml != None and self.toolbarHtml != None and self.bottomHtml != None:
            html = self.toolbarHtml + "\n" + self.webHtml + "\n" + self.bottomHtml
            showText(html, title="WebView HTML", minWidth=600, minHeight=600)
            self.clear()


mw.debugHtml = DebugHtml()

debugMenu = mw.menuBar().addMenu("Debug")

action = QAction("Show Deck JSON", mw)
action.triggered.connect(showDeckJson)
#mw.form.menuTools.addAction(action)
debugMenu.addAction(action)

action2 = QAction("Show WebView HTML", mw)
action2.triggered.connect(mw.debugHtml.requestHtml)
#mw.form.menuTools.addAction(action2)
debugMenu.addAction(action2)