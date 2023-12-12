from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from config import Config


app = Flask(__name__)
app.config.from_object(Config)

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'saini',
    'password': 'absaini',
    'database': 'recipesdatabase'
}

# Function to establish database connection
def connect_db():
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as e:
        print(f"Database connection error: {e}")
        return None

# Route to display overview of relevant data
@app.route('/')
def overview():
    try:
        # Fetch relevant data from the database
        conn = connect_db()

        if conn:
            cursor = conn.cursor(dictionary=True)

            # Fetch data from tables (excluding autonumber keys)
            cursor.execute("SELECT recipe_id, name, instructions FROM recipes")
            recipes_data = cursor.fetchall()

            cursor.execute("SELECT ingredient_id, name, nutritional_info FROM ingredients")
            ingredients_data = cursor.fetchall()

            cursor.execute("SELECT category_id, name, description FROM categories")
            categories_data = cursor.fetchall()

            conn.close()

            # Render template with relevant data
            return render_template('overview.html', recipes=recipes_data, ingredients=ingredients_data, categories=categories_data)
        else:
            return "Database connection error", 500  # Return a 500 error response

    except Exception as e:
        print(f"Error: {str(e)}")
        return "An error occurred", 500  # Return a 500 error response

    # Add the following lines for debugging template rendering
    except TemplateNotFound as e:
        print(f"Template not found: {str(e)}")
        return "Template not found", 500  # Return a 500 error response
    except TemplateError as e:
        print(f"Template rendering error: {str(e)}")
        return "Template rendering error", 500  # Return a 500 error response





# Route to add a new recipe
@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        name = request.form['name']
        instructions = request.form['instructions']

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO recipes (name, instructions) VALUES (%s, %s)", (name, instructions))

        conn.commit()
        conn.close()

        return redirect(url_for('overview'))

    return render_template('add_recipe.html')

# Route to update an existing recipe
@app.route('/update_recipe/<int:recipe_id>', methods=['GET', 'POST'])
def update_recipe(recipe_id):
    if request.method == 'POST':
        name = request.form['name']
        instructions = request.form['instructions']

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("UPDATE recipes SET name = %s, instructions = %s WHERE recipe_id = %s",
                       (name, instructions, recipe_id))

        conn.commit()
        conn.close()

        return redirect(url_for('overview'))

    conn = connect_db()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT recipe_id, name, instructions FROM recipes WHERE recipe_id = %s", (recipe_id,))
    recipe = cursor.fetchone()

    conn.close()

    return render_template('update_recipe.html', recipe=recipe)

# Route to delete a recipe
@app.route('/delete_recipe/<int:recipe_id>', methods=['POST'])
def delete_recipe(recipe_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM recipes WHERE recipe_id = %s", (recipe_id,))

    conn.commit()
    conn.close()

    return redirect(url_for('overview'))


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
