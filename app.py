from flask import Flask, jsonify, request
import mysql.connector

# Initialize the Flask application
app = Flask(__name__)

# Database configuration
db_config = {
    'user': 'root',
    'password': '190420',
    'host': 'localhost',
    'database': 'gym',
    'port': '3306'
}

# Establish a database connection
def get_db_connection():
    return mysql.connector.connect(**db_config)

# Endpoint to fetch all users
@app.route('/users', methods=['GET'])
def get_users():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    query = "SELECT * FROM User"
    cursor.execute(query)
    users = cursor.fetchall()
    
    cursor.close()
    connection.close()
    
    return jsonify(users)

# Endpoint to add a new user
@app.route('/users', methods=['POST'])
def add_user():
    user_data = request.json
    
    user_id = user_data['id']
    name = user_data['name']
    password = user_data['password']
    address_line1 = user_data.get('address_line1', '')
    phone = user_data.get('phone', '')
    weight = user_data.get('weight', 0)
    age = user_data.get('age', 0)
    created_at = user_data.get('created_at', '2024-01-01')
    
    connection = get_db_connection()
    cursor = connection.cursor()
    
    insert_query = """
    INSERT INTO User (id, name, password, address_line1, phone, weight, age, created_at)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(insert_query, (user_id, name, password, address_line1, phone, weight, age, created_at))
    
    connection.commit()
    cursor.close()
    connection.close()
    
    return jsonify({'message': 'User added successfully!'}), 201

# Endpoint to delete a user by ID
@app.route('/users/<string:user_id>', methods=['DELETE'])
def delete_user(user_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    # Delete the user from the database
    delete_query = "DELETE FROM User WHERE id = %s"
    cursor.execute(delete_query, (user_id,))
    
    # Check if the user was deleted
    if cursor.rowcount == 0:
        cursor.close()
        connection.close()
        return jsonify({'message': 'User not found!'}), 404
    
    connection.commit()
    cursor.close()
    connection.close()
    
    return jsonify({'message': 'User deleted successfully!'}), 200

if __name__ == '__main__':
    app.run(debug=True)
