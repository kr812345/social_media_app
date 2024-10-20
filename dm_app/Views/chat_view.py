class Chatview:
    @staticmethod
    def render_chat(chat):
        return {
            "sender_name": chat.sender_name,
            "receiver_name": chat.receiver_name,
            "content_type": chat.content_type,
            "content": chat.content
        }

    @staticmethod
    def render_chats(chats):
        return [Chatview.render_chat(chat) for chat in chats]

    @staticmethod
    def render_error(message):
        return {"error": message}

    @staticmethod
    def render_success(message, chat_id=None):
        response = {"message": message}
        if chat_id:
            response["chat_id"] = chat_id
        return response