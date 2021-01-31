chrome.browserAction.onClicked.addListener(function(tab){
  chrome.tabs.query({active: true, lastFocusedWindow: true}, tabs => {
    let url = tabs[0].url;
    window.alert("The URL is " + url);
    });
});