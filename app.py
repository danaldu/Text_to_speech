from flask import Flask, request, send_file, render_template
from gtts import gTTS
import io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def text_to_speech():
    if request.method == 'POST':
        text = request.form['text']
        language = request.form['language']
        
      
        speech = gTTS(text=text, lang=language, slow=False)
        
       
        fp = io.BytesIO()
        speech.write_to_fp(fp)
        fp.seek(0)
        
        
        return send_file(fp, mimetype='audio/mp3')
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)