if (document.contains(document.getElementById('answerBox'))) {
  document.getElementById('answerBox').remove();
}

answerDiv = document.createElement('div');
answerDiv.id = 'answerBox';
answerDiv.className = 'chat pane'

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

answerDiv.appendChild(innerChat);

sidebarElem = document.getElementsByClassName('sidebar')[0];
sidebarElem.appendChild(answerDiv);
