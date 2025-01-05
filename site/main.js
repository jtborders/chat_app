const searchParams = new URLSearchParams(window.location.search);

document.getElementById("createChat").addEventListener("submit", async function(event) {
  event.preventDefault();
  const input = document.getElementById("usernames").value.trim();
  const usernamesArray = input.split(",").map(username => username.trim()).filter(username => username.length > 0);
  await fetch(this.action, {
    method: this.method,
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(usernamesArray)
  });
  loadPage();
});

async function loadChats() {
  let response = await fetch(`/api/get_chats?username=${searchParams.get("username")}`);
  let chatInfos = await response.json();
  let chats = document.getElementById("chats");
  let createChat = document.getElementById("createChat");
  chats.innerHTML = "";
  chats.appendChild(createChat);
  for(let chatInfo of chatInfos) {
    let link = document.createElement("a");
    link.href = `/?username=${searchParams.get("username")}&chat=${chatInfo.id}`;
    link.innerHTML = chatInfo.usernames.join(", ");
    chats.insertBefore(link, document.getElementById("createChat"));
  }
}

async function loadMessages() {
  if(searchParams.has("chat")) {
    let response = await fetch(`/api/get_chat?id=${searchParams.get("chat")}`);
    let chatInfo = await response.json();
    let messages = document.getElementById("messages");
    messages.innerHTML = "";
    for(let messageInfo of chatInfo.messages) {
      let message = document.createElement("div");
      message.className = "message";
      message.innerHTML = `<div>${messageInfo.username}</div><div>${messageInfo.content}</div>`;
      messages.appendChild(message);
    }
  }
}

document.getElementById("textarea").addEventListener("keydown", async function(event) {
  if(searchParams.has("chat")) {
    if(event.key == "Enter"){
      await fetch("/api/send_message", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({id: parseInt(searchParams.get("chat")), username: searchParams.get("username"), text: event.target.value})
      });
      event.target.value = "";
      event.preventDefault();
      loadPage();
    }
  }
});

function loadPage() {
  loadChats();
  loadMessages();
}


setInterval(loadPage, 1000);