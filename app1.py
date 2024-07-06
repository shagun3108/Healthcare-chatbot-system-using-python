import mysql.connector
from flask import Flask, request, jsonify

app = Flask(__name__)

# Create a database connection
connection = mysql.connector.connect(
    host="your_host",
    user="your_username",
    password="your_password",
    database="your_database"
)
cursor = connection.cursor()

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get("message")

    # Execute a query to fetch a response and precaution based on the message
    query = "SELECT response, precaution FROM chatbot_data WHERE pattern LIKE %s"
    cursor.execute(query, (f'%{message}%',))
    result = cursor.fetchone()

    if result:
        response, precaution = result
        return jsonify({"response": response, "precaution": precaution})
    else:
        return jsonify({"response": "I'm sorry, I couldn't find a matching response."})

if __name__ == '__main__':
    app.run(debug=True)
