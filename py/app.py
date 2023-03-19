from flask import Flask, jsonify, render_template, request
from model import TranslatorModel
import os

class PrasvulsianTranslator:
    def __init__(self):
        current_dir = os.getcwd()

        self.app = Flask(__name__, template_folder=f'{current_dir}\html', static_folder='static')
        @self.app.route("/")
        def index():
            return render_template("welcome.html")

        @self.app.route("/send_message", methods=["POST"])
        def on_message_send():
            print("Message sent!")
            message = request.json["message"]
            if message != None:
                response = TranslatorModel.send_response(message)
                return jsonify({"user_message": message, "bot_response": response})



        @self.app.route('/settings', methods=['GET', 'POST'])
        def settings():
            if request.method == 'POST':
                image = request.files['image']
                if image:
                    filename = 'background.jpg'
                    image.save(filename)
            return render_template('index.html')
if __name__ == "__main__":
    translator = PrasvulsianTranslator()
    translator.app.run(debug=True)
