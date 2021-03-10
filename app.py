from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('mykeYUP2XfAW03inmjuu/IUYTa6fh0dEsY9dn7XsvqYTb1SN4zWA943sq+k0YTc7ySuimL5GvbWCJb8UmqgNGGcMQkgq1Eb6ClaQDdrGgqqL16u8AgNxZ8I1yZ6koSVhaHq2m2wmMfgBN1gD+6BR/QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('42e13f3aa7fa7f202fe2256b24c0be25')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = '窩看不懂 請輸入 hi 或 哈囉'

    if msg in ['hi', 'Hi']:
        r = 'hi'
    elif msg == '哈囉':
        r = '哈囉 需要幫忙嗎?'
    elif '訂位' in msg:
        r = '你想訂位，是嘛?'

    line_bot_api.reply_message(
        event.reply_token,
        StickerSendMessage(
            package_id='1',
            sticker_id='1'
    ))


if __name__ == "__main__":
    app.run()