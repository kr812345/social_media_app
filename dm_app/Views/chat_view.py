from flask import jsonify
class Chatview:
    @staticmethod
    def render_chat(chat):
        return {
            "chat_id": chat.chat_id,
            "sender_name": chat.sender_name,
            "receiver_name": chat.receiver_name,
            "sent_at": chat.sent_at
        }

    @staticmethod
    def render_msg(message):
        return jsonify({
            "chat_id": message.chat_id,
            "sender_name": message.sender_name,
            "receiver_name": message.receiver_name,
            "content": message.content,
            "sent_at": message.sent_at
        })

    @staticmethod
    def render_msges(msges):
        return [Chatview.render_msg(message) for message in msges]

    @staticmethod
    def render_media(content):
        return {
            "chat_id": content.chat_id,
            "content_type": content.content_type,
            "content_url": content.content_url
        }
         
    @staticmethod
    def render_chats(chats):
        return jsonify([Chatview.render_chat(chat) for chat in chats])

    @staticmethod
    def render_error(message):
        return {"error": message}

    @staticmethod
    def render_success(message, chat_id=None):
        response = {"message": message}
        if chat_id:
            response["chat_id"] = chat_id
        return response