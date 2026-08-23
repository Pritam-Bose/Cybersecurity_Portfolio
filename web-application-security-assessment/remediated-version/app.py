from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

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
            "INSERT OR IGNORE INTO users (id, username, password) VALUES (?, ?, ?)",
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
    <a href="/profile?id=1">Profile 1</a><br>
    <a href="/profile?id=2">Profile 2</a><br>
    <a href="/profile?id=3">Profile 3</a>
    """


# INTENTIONALLY VULNERABLE TO SQL INJECTION
@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "")
    password = request.form.get("password", "")

    conn = get_db()

    query = f"""
        SELECT * FROM users
        WHERE username = ?
        AND password = ?
    """

    result = conn.execute(query,(username, password)).fetchone()
    conn.close()

    if result:
        return f"<h2>Login successful</h2><p>Welcome {result['username']}</p>"

    return "<h2>Login failed</h2>"


# INTENTIONALLY VULNERABLE TO XSS
@app.route("/search")
def search():
    q = request.args.get("q", "")

    return render_template_string("""
        <h2>Search Results</h2>
        <p>You searched for: {{ q }}</p>
    """, q=q)


# INTENTIONALLY VULNERABLE TO BROKEN ACCESS CONTROL
@app.route("/profile")
def profile():
    user_id = request.args.get("id", "")

    conn = get_db()
    user = conn.execute(
        "SELECT id, username FROM users WHERE id = ?",
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


if __name__ == "__main__":
    init_db()
    app.run(host="127.0.0.1", port=5000, debug=False)