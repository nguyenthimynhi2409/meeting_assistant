const sendBtn = document.getElementById('sendBtn');
const userInput = document.getElementById('userInput');
const chatMessages = document.getElementById('chatMessages');

const uploadBtn = document.getElementById('uploadBtn');
const memoInput = document.getElementById('memoInput');

const meetingsUl = document.getElementById('meetingsUl');

// ------------------- Chat -------------------
function addMessage(text, sender) {
  const msgDiv = document.createElement('div');
  msgDiv.classList.add('message', sender);
  msgDiv.textContent = text;
  chatMessages.appendChild(msgDiv);
  chatMessages.scrollTop = chatMessages.scrollHeight;
}

async function sendMessage() {
  const message = userInput.value.trim();
  if (!message) return;
  addMessage(message, 'user');
  userInput.value = '';

  try {
    const res = await fetch('/ask_question', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ question: message })
    });
    const data = await res.json();
    addMessage(data.answer || 'No response', 'bot');
  } catch (err) {
    addMessage('Error contacting server', 'bot');
    console.error(err);
  }
}

sendBtn.addEventListener('click', sendMessage);
userInput.addEventListener('keypress', e => {
  if (e.key === 'Enter') sendMessage();
});

// ------------------- Upload Memo -------------------
async function uploadMemo() {
  const memo = memoInput.value.trim();
  if (!memo) return;

  try {
    const res = await fetch('/upload_memo', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ memo })
    });
    const data = await res.json();
    addMessage(`Memo uploaded! Summary: ${data.summary}`, 'bot');
    memoInput.value = '';
    fetchMeetings();
  } catch (err) {
    addMessage('Error uploading memo', 'bot');
    console.error(err);
  }
}

uploadBtn.addEventListener('click', uploadMemo);

// ------------------- Fetch Meetings -------------------
async function fetchMeetings() {
  try {
    const res = await fetch('/meetings');
    const data = await res.json();
    meetingsUl.innerHTML = '';
    data.meetings.forEach(m => {
      const li = document.createElement('li');
      li.textContent = `[${m.id}] ${m.summary}`;
      meetingsUl.appendChild(li);
    });
  } catch (err) {
    console.error(err);
  }
}

// Load meetings on page load
fetchMeetings();
