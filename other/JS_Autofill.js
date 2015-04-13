/**
The Following are all one (1) line javascript scripts that are intended to be used as a shortcut in chrome.

To create a shortcut:
1. In Chrome go to your Bookmark Manager (option + Apple + B)
2. Right(two finger) click to add a new page ('Add Page...')
3. Enter a Name
4. Enter one of the lines below as the url, including the 'javascript:' in the beginning.
5. Go Try it out

Most of these are page dependant and will only do something when you are on the correct page.
**/

//When filling out a Bug in JIRA this will auto fill the description with things you don't want to forget and puts stuff in a nice format
javascript:(function(){document.getElementsByName('description')[0].value='This is a test \n\n\n\n did it work?';})();

//When on a PR Page in Stash this will open a prompt that will have the branch name in it so all you have to do is Copy (Apple + C) and hit enter (to make window go away).
javascript:(function(){window.prompt("Copy to clipboard: Ctrl+C, Enter", document.evaluate('//*[@id="aui-page-panel-content-body"]/div/section/header/div/div[1]/div[2]/span[1]/span/span[2]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.innerHTML);})();


