from flask import Flask, request, render_template_string, session, jsonify
import sqlite3

app = Flask(__name__)

# Used for the local lab session.
app.secret_key = "lab-secret-key-change-this"


def get_db():
    conn = sqlite3.connect("lab.db")
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT
        )
    """)

    users = [
        (1, "admin", "admin123"),
        (2, "pritam", "test123"),
        (3, "user2", "hello123")
    ]

    for user in users:
        conn.execute(
            """
            INSERT OR IGNORE INTO users
            (id, username, password)
            VALUES (?, ?, ?)
            """,
            user
        )

    conn.commit()
    conn.close()



@app.route("/")
def home():
    return """
    <h1>Security Assessment Lab</h1>

    <h2>Login Test</h2>
    <form action="/login" method="POST">
        <input name="username" placeholder="Username">
        <input name="password" placeholder="Password">
        <button type="submit">Login</button>
    </form>

    <h2>Search Test</h2>
    <form action="/search">
        <input name="q" placeholder="Search">
        <button type="submit">Search</button>
    </form>

    <h2>User Profile</h2>
    <a href="/profile">My Profile</a>
    """



@app.route("/login", methods=["POST"])
def login():

    username = request.form.get("username", "")
    password = request.form.get("password", "")

    conn = get_db()

    result = conn.execute(
        """
        SELECT * FROM users
        WHERE username = ?
        AND password = ?
        """,
        (username, password)
    ).fetchone()

    conn.close()

    if result:

        # Store authenticated user's ID in the server-side session.
        session["user_id"] = result["id"]

        return f"""
        <h2>Login successful</h2>
        <p>Welcome {result['username']}</p>
        <a href="/profile">View Profile</a>
        """

    return "<h2>Login failed</h2>"



@app.route("/search")
def search():

    q = request.args.get("q", "")

    return render_template_string("""
        <h2>Search Results</h2>
        <p>You searched for: {{ q }}</p>
    """, q=q)



@app.route("/profile")
def profile():

    # Get identity from authenticated session,
    # not from a user-controlled URL parameter.
    user_id = session.get("user_id")

    if not user_id:
        return "Unauthorized", 401

    conn = get_db()

    user = conn.execute(
        """
        SELECT id, username
        FROM users
        WHERE id = ?
        """,
        (user_id,)
    ).fetchone()

    conn.close()

    if not user:
        return "User not found", 404

    return f"""
        <h2>User Profile</h2>
        <p>User ID: {user['id']}</p>
        <p>Username: {user['username']}</p>
    """



@app.route("/api/profile", methods=["GET"])
def api_profile():

    user_id = session.get("user_id")

    if not user_id:
        return jsonify({
            "error": "Unauthorized"
        }), 401

    conn = get_db()

    user = conn.execute(
        """
        SELECT id, username
        FROM users
        WHERE id = ?
        """,
        (user_id,)
    ).fetchone()

    conn.close()

    if not user:
        return jsonify({
            "error": "User not found"
        }), 404

    return jsonify({
        "id": user["id"],
        "username": user["username"]
    })



@app.route("/logout")
def logout():

    session.clear()

    return """
    <h2>Logged out</h2>
    <a href="/">Return to Home</a>
    """



if __name__ == "__main__":

    init_db()

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )