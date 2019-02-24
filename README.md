# cardsforhumanity
baby nobly struggles through chrome extension architecture


READING THUS FAR 📖📖📖📖

-Boilerplate set up https://extensionizr.com/!#{"modules":["browser-mode","with-bg","with-persistent-bg","with-custom-options","no-override"],"boolean_perms":[],"match_ptrns":[]}

-High level overview: https://coderwall.com/p/hkmedw/understanding-chrome-extensions

-Reference on pushing to Heroku https://pusher.com/tutorials/chrome-extension-cryptocurrency-part-1

-All of the app samples https://github.com/GoogleChrome/chrome-app-samples/

-background html vs background js -- feelin' so seeeeen I was so confused https://stackoverflow.com/questions/24978473/background-html-vs-background-js-chrome-extension

-URL permissions: https://stackoverflow.com/questions/42601383/chrome-extension-what-is-the-point-of-url-permissions

-user interfaces https://developer.chrome.com/extensions/user_interface

-manage events w background scripts https://developer.chrome.com/extensions/background_pages

-my boilerplate https://extensionizr.com/!#{"modules":["page-mode","with-js-bg","with-persistent-bg","with-custom-options","no-override","inject-css","inject-js","omnibox","jquerymin","angular"],"boolean_perms":["bookmarks","chrome://favicon/","clipboardRead","clipboardWrite","contentSettings","contextMenus","cookies","tts","ttsEngine","history","idle","notifications","tabs","geolocation"],"match_ptrns":["https://twitter.com/*","https://facebook.com/*"]}

-alas we cannot have both browser and page actions https://stackoverflow.com/questions/26249783/why-a-chrome-extension-could-not-have-both-browser-action-and-page-action

-browser action https://developer.chrome.com/extensions/browserAction#method-setBadgeBackgroundColor

-page action (which we're using) https://developer.chrome.com/extensions/pageAction

-how do chrome extensions modify content scripts: https://medium.com/front-end-weekly/how-do-chrome-extensions-modify-webpages-using-content-scripts-9ae278e2bdf8