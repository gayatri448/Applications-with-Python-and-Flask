# a. Import the relevant libraries and functions
from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

# b. Initiate the Flask app
app = Flask("Sentiment Analyzer")

# c. Define the function to handle sentiment analysis
@app.route("/sentimentAnalyzer")
def sent_analyzer():
    # Get text from the GET request
    text_to_analyze = request.args.get('textToAnalyze')
    
    # If no text is provided, return an error message
    if not text_to_analyze:
        return "No text provided for analysis."
    
    # Get sentiment analysis result
    response = sentiment_analyzer(text_to_analyze)
    
    # Extract values
    label = response['label']
    score = response['score']
    
    # Format the output
    return f"The given text has been identified as {label.split('_')[1]} with a score of {score}."

# d. Define route to render the HTML page
@app.route("/")
def render_index_page():
    return render_template('index.html')

# e. Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
