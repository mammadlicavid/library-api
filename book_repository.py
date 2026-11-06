
import database as db


def get_all(available_only=False):
    conn = db.connect()
    if available_only:
        rows = conn.execute(
            "SELECT * FROM books WHERE available = 1"
        ).fetchall()
    else:
        rows = conn.execute("SELECT * FROM books").fetchall()
    conn.close()
    return rows


def get_by_id(book_id):
    conn = db.connect()
    row = conn.execute(
        "SELECT * FROM books WHERE id = ?", (book_id,)
    ).fetchone()
    conn.close()
    return row


def create(title, author, isbn):
    conn = db.connect()
    cur = conn.execute(
        "INSERT INTO books (title, author, isbn, available) VALUES (?, ?, ?, 1)",
        (title, author, isbn),
    )
    conn.commit()
    row = conn.execute(
        "SELECT * FROM books WHERE id = ?", (cur.lastrowid,)
    ).fetchone()
    conn.close()
    return row


def delete(book_id):
    conn = db.connect()
    conn.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()
    conn.close()
