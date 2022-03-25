# ForexNewsProject

This project is to scrape articles from news websites and display them on UI.
These are my code base for the project.


reuters.py: 

Opens the Reuters news website and scrape the news title and 
its URL. Method newsReuters(url) receives string argument 
and returns two lists titleList and hrefList.
titleList has article title, hrefList has news URL.

tradingEconomics.py: 

Do similar thing to reuters.py, but created for trading
Economics website. It also receives the news page URL 
and returns titleList and hrefList.

main.py: 

It opens the GUI for users that allow them  to retrieve 
news title and article URL from 2 websites.
Used tkinter to create GUI,
used webbrowser to make the link clickable.
