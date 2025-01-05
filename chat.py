from typing import List

class Database:
    chats: List['Chat']
    def __init__(self):
        self.chats = [Chat(["a", "b"]), Chat(["a", "b", "c"])]
        
    def get_chats(self, username: str):
        return [{"id": idx, "usernames": chat.usernames} for idx, chat in enumerate(self.chats) if username in chat.usernames]
    
    def get_chat(self, id: int):
        return {
            "id": id,
            "usernames": self.chats[id].usernames,
            "messages": [{"username": message.username, "content": message.content} for message in self.chats[id].messages]
        }
        
    def create_chat(self, usernames: List[str]):
        self.chats.append(Chat(usernames))

    def send_message(self, id: int, username: str, content: str):
        self.chats[id].messages.append(Message(username, content))
        
    
class Chat:
    usernames: List[str]
    messages: List['Message']
    def __init__(self, usernames):
        self.usernames = usernames
        self.messages = []
    
class Message:
    username: str
    content: str
    def __init__(self, username: str, content: str):
        self.username = username
        self.content = content