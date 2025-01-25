from flask import (
    Flask,
    render_template,
    make_response,
    request,
    redirect,
    url_for,
    session,
    flash,
    send_file,
    Response
)

# Flask app configuration
app = Flask(__name__, template_folder="../frontend/templates", static_folder="../frontend/static")

# Route for the homepage (index.html)
@app.route('/')
def index():
    return render_template('index.html')

# Route for the About Us page (aboutus.html)
@app.route('/about')
def about():
    return render_template('aboutus.html')

# Route for the Bridal page (bridal.html)
@app.route('/bridal')
def bridal():
    return render_template('bridal.html')

@app.route('/repairs')
def repairs():
    return render_template('repairs.html')


# Route for the Gallery page (gallery.html)
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

# Route for the Alteration page (alteration.html)
@app.route('/alteration')
def alteration():
    return render_template('alteration.html')

# **New route for the Formal page (formal.html)**
@app.route('/formal')
def formal():
    return render_template('formal.html')

# Route for the Contact Us page (contact.html)
@app.route('/contact')
def contact():
    return render_template('contact.html')
