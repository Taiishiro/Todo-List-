import sqlite3

def create_connection():
    conn = sqlite3.connect('taches.db')
    return conn

class Tache:
    @staticmethod
    def add_task(titre, description):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO Tache (titre, description, timestamp) VALUES (?, ?, CURRENT_TIMESTAMP)''', (titre, description))
        conn.commit()
        conn.close()

    @staticmethod
    def remove_task(task_id):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('''DELETE FROM Tache WHERE id = ?''', (task_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def complete_task(task_id):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('''UPDATE Tache SET complete = 1 WHERE id = ?''', (task_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def get_tasks():
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('''SELECT id, titre, description, timestamp FROM Tache ORDER BY timestamp DESC''')
        tasks = cursor.fetchall()
        conn.close()
        return tasks
