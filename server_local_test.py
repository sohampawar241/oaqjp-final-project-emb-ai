"""
Local Test Server for Emotion Detection Web Application.
Use this script to run and test the Flask app locally without requiring
connection to the internal IBM Skills Network Watson NLP service.
"""
from flask import Flask, render_template, request

app = Flask("Emotion Detector Local Test", template_folder="templates", static_folder="static")

def mock_emotion_detector(text_to_analyze):
    """
    Local mock for emotion detection that simulates the Watson NLP responses
    for test statements and blank entries.
    """
    if not text_to_analyze or not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    text_lower = text_to_analyze.lower()

    if "having fun" in text_lower or "love" in text_lower or "happy" in text_lower or "glad" in text_lower:
        return {
            'anger': 0.006274985,
            'disgust': 0.0025598293,
            'fear': 0.009251528,
            'joy': 0.9680386,
            'sadness': 0.049744144,
            'dominant_emotion': 'joy'
        }
    elif "mad" in text_lower or "hate" in text_lower:
        return {
            'anger': 0.64999825,
            'disgust': 0.03349073,
            'fear': 0.05567236,
            'joy': 0.008661813,
            'sadness': 0.2829034,
            'dominant_emotion': 'anger'
        }
    elif "disgust" in text_lower:
        return {
            'anger': 0.012,
            'disgust': 0.854,
            'fear': 0.005,
            'joy': 0.001,
            'sadness': 0.045,
            'dominant_emotion': 'disgust'
        }
    elif "sad" in text_lower:
        return {
            'anger': 0.021,
            'disgust': 0.003,
            'fear': 0.014,
            'joy': 0.002,
            'sadness': 0.925,
            'dominant_emotion': 'sadness'
        }
    elif "afraid" in text_lower or "fear" in text_lower:
        return {
            'anger': 0.015,
            'disgust': 0.004,
            'fear': 0.892,
            'joy': 0.003,
            'sadness': 0.032,
            'dominant_emotion': 'fear'
        }
    else:
        return {
            'anger': 0.05,
            'disgust': 0.02,
            'fear': 0.03,
            'joy': 0.85,
            'sadness': 0.05,
            'dominant_emotion': 'joy'
        }

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyzes the text passed via GET parameter 'textToAnalyze'.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = mock_emotion_detector(text_to_analyze)

    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Renders the index.html page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    print("Starting local test server at http://127.0.0.1:5000 ...")
    app.run(host="0.0.0.0", port=5000, debug=False)
