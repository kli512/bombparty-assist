var injections = document.getElementsByClassName('injection');

for (var i = injections.length - 1; i >= 0; --i) {
  injections[i].remove();
}

if (smartWords.length > 0) {
  // could put sort in the python and just have it insert all three lines for words
  var ascendingWords = smartWords.slice().sort((a, b) => a.length - b.length);
  var descendingWords = smartWords.slice().sort((a, b) => b.length - a.length);


  function generateWordBankDiv(words, id, hidden=true) {
    wordBankDiv = document.createElement('div');
    wordBankDiv.hidden = hidden;
    wordBankDiv.id = id;
    wordBankDiv.className = 'chat pane injection'

    innerChat = document.createElement('div');
    innerChat.className = 'log darkScrollbar';

    words.forEach(e => {
      chatMessage = document.createElement('div');
      chatMessage.className = 'system';

      line = document.createElement('span');
      line.className = 'text';
      line.innerText = e;

      chatMessage.appendChild(line);
      innerChat.appendChild(chatMessage);

    });

    wordBankDiv.appendChild(innerChat);

    return wordBankDiv
  }

  // Generate control bar
  function generateButtonCode(showId, allIds) {
    let str = 'javascript:';
    for (const id of allIds) {
      str += 'document.getElementById("' + id + '").hidden = true;';
    }
    str += 'document.getElementById("' + showId + '").hidden = false;';

    return str;
  }

  controlBar = document.createElement('div');
  controlBar.className = 'tabs injection';
  banks = ['SmartBank', 'AscendingBank', 'DescendingBank'];
  symbols = ['🧠', '⬆️', '⬇️']

  for (var i = 0; i < banks.length; i++) {
    button = document.createElement('a');
    button.title = banks[i].slice(0, -4) + ' sort';
    button.innerText = symbols[i];
    button.href = generateButtonCode(banks[i], banks);
    controlBar.appendChild(button);
  }

  // Append control bar and word banks to sidebar
  sidebarElem = document.getElementsByClassName('sidebar')[0];

  sidebarElem.appendChild(controlBar);

  sidebarElem.appendChild(generateWordBankDiv(smartWords, 'SmartBank', false));
  sidebarElem.appendChild(generateWordBankDiv(ascendingWords, 'AscendingBank'));
  sidebarElem.appendChild(generateWordBankDiv(descendingWords, 'DescendingBank'));
}
