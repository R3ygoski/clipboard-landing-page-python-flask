from flask import Flask, render_template
from flask_frozen import Freezer
app = Flask(__name__)
freezer = Freezer(app)

@app.route("/")
def home():
    features_1 = [
        {
            'title': 'Quick Search',
            'text': 'Easily search your snippets by content, category, web address, application, and more.'
        },
        {
            'title': 'iCloud Sync',
            'text': 'Instantly saves and syncs snippets across all your devices.'
        },
        {
            'title': 'Complete History',
            'text': 'Retrieve any snippets from the first moment you started using the app.'
        },
    ]
    features_2 = [
        {
            'image': 'icon-blacklist.svg',
            'title': 'Create blacklists',
            'text': 'Ensure sensitive information never makes its way to your clipboard by excluding certain sources.'
        },
        {
            'image': 'icon-text.svg',
            'title': 'Plain text snippets',
            'text': 'Remove unwanted formatting from copied text for a consistent look.'
        },
        {
            'image': 'icon-preview.svg',
            'title': 'Sneak preview',
            'text': 'Quick preview of all snippets on your Clipboard for easy access.'
        }
    ]
    brands = [
        {
            'brand':'logo-google.png',
            'alt': 'Logo of Google'
        },
        {
            'brand':'logo-ibm.png',
            'alt': 'Logo of IBM'
        },
        {
            'brand':'logo-microsoft.png',
            'alt': 'Logo of Microsoft'
        },
        {
            'brand':'logo-hp.png',
            'alt': 'logo of Hewlett Packard'
        },
        {
            'brand':'logo-vector-graphics.png',
            'alt': 'Logo of Vector Graphics'
        },
    ]
    return render_template(
        "index.html", 
        features_1=features_1, 
        features_2=features_2,
        brands=brands)

if __name__ == "__main__":
    # app.run(debug=True)
    freezer.freeze()