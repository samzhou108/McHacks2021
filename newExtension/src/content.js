/* File: content.js
 * ---------------
 * Hello! You'll be making most of your changes
 * in this file. At a high level, this code replaces
 * the substring "cal" with the string "butt" on web pages.
 *
 * This file contains javascript code that is executed
 * everytime a webpage loads over HTTP or HTTPS.
 */

/*function clean (text) {
    var dictionary = { bad: 'good', worse: 'better', awful: 'wonderful'},
        regexp = RegExp ('\\b(' + Object.keys (dictionary).join ('|') + ')\\b', 'ig');

    return text.replace (regexp, function (_, word) { 
      _ = dictionary[word.toLowerCase ()];
      if (/^[A-Z][a-z]/.test (word)) // initial caps
        _ = _.slice (0,1).toUpperCase () + _.slice (1);
      else if (/^[A-Z][A-Z]/.test (word)) // all caps
        _ = _.toUpperCase ();
      return _;
    });
  }*/

var dictionary = { 'bad': 'good', 
                   'worse': 'better', 
                   'awful': 'wonderful',
                   'worst': 'best',
                   'loss': 'win',
                   'threats': 'gifts',
                   'terrible': 'amazing',
                   'tragedy': 'fortune',
                   'death': 'life',
                   'dead': 'alive',
                   'fire': 'water fight',
                   'injured': 'healthy'
                },
  regexp = RegExp ('\\b(' + Object.keys (dictionary).join ('|') + ')\\b', 'ig');

var elements = document.getElementsByTagName('*');

for (var i = 0; i < elements.length; i++) {
    var element = elements[i];

    for (var j = 0; j < element.childNodes.length; j++) {
        var node = element.childNodes[j];

        if (node.nodeType === 3) {
            var text = node.nodeValue;
            var replacedText = text.replace(/cal/gi, "cal"); // replaces "cal," "Cal", etc. with "butt"
            //replacedText = replacedText.replace(/tree/gi, "awesome");
            //xkcd stuff
            replacedText = replacedText.replace(/space/gi, "spaaaace"); 
            replacedText = replacedText.replace(/witnesses/gi, "these dudes I know");
            replacedText = replacedText.replace(/alledgedly/gi, "kinda probably");
            replacedText = replacedText.replace(/rebuild/gi, "avenge");
            //covid stuff
            replacedText = replacedText.replace(/coronavirus|COVID|COVID-19/gi, "Awesome Life");
            replacedText = replacedText.replace(/fuck|shit/gi, "owo");


            replacedText = replacedText.replace (regexp, function (_, word) { return dictionary[word.toLowerCase()]; });

            if (replacedText !== text) {
                element.replaceChild(document.createTextNode(replacedText), node);
              }
        }
    }
}
