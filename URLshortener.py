from flask import Flask, render_template, request, redirect
import shortuuid

app = Flask(__name__)

# Dictionary to store mappings between short and original URLs
url_mapping = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    original_url = request.form['url']
    short_code = shortuuid.uuid()[:6]  # Generating a short code using shortuuid

    url_mapping[short_code] = original_url

    short_url = f'http://yourdomain/{short_code}'  # Replace 'yourdomain' with your actual domain

    return render_template('index.html', short_url=short_url)

@app.route('/<short_code>')
def redirect_to_original(short_code):
    original_url = url_mapping.get(short_code)

    if original_url:
        return redirect(original_url)
    else:
        return 'URL not found'

if __name__ == '__main__':
    app.run(debug=True)
