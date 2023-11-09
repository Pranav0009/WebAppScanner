from flask import Flask, render_template, request
import WebScanner

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def index():
    if request.method == 'POST':
        url = request.form['url']
        UserAgent = WebScanner.UserAgent()
        
        # Call the scanning functions and collect results
        rce_results = WebScanner.rce_func(url, UserAgent)
        xss_results = WebScanner.xss_func(url, UserAgent)
        error_based_sqli_results = WebScanner.error_based_sqli_func(url, UserAgent)
        
        return render_template('results.html', rce_results=rce_results, xss_results=xss_results, error_based_sqli_results=error_based_sqli_results)
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    url = request.form['url']
    UserAgent = WebScanner.UserAgent()
    
    # Initialize result variables
    rce_results = ""
    xss_results = ""
    error_based_sqli_results = ""
    
    try:
        rce_results = WebScanner.rce_func(url, UserAgent)
    except Exception as e:
        rce_results = f"RCE scan error: {str(e)}"

    try:
        xss_results = WebScanner.xss_func(url, UserAgent)
    except Exception as e:
        xss_results = f"XSS scan error: {str(e)}"

    try:
        error_based_sqli_results = WebScanner.error_based_sqli_func(url, UserAgent)
    except Exception as e:
        error_based_sqli_results = f"Error-Based SQL Injection scan error: {str(e)}"
    
    return render_template('results.html', rce_results=rce_results, xss_results=xss_results, error_based_sqli_results=error_based_sqli_results)

if __name__ == '__main__':
    app.run(debug=True)
