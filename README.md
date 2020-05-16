# anki-dev-tools
Utilities to Anki facilitate addon development and debugging.


## Functions

### Show Deck JSON: 
Displays JSON representing deck state in the collection. That is, the result of "SELECT decks FROM col;"

### Show WebView HTML: 
The main window of Anki consists of a Qt Menu, and three QtWebViews stacked: a thin navigation menu (mw.toolbarWeb), the primary viewing area (mw.web), and the bottom buttons (mw.bottomWeb). This displays all three HTML pages of the current view.
