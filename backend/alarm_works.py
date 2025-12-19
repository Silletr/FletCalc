import sqlite3

with sqlite3.connect("database/alarm_info.db", timeout=5) as db:
    cursor = db.cursor()

    # --- CREATE TABLE ---
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alarm (
        alarm_name TEXT PRIMARY KEY,
        alarm_description TEXT,
        alarm_category TEXT,
        alarm_time TEXT,
        alarm_day TEXT
    )
    """)

    # --- INSERT EXAMPLE ---
    cursor.execute("""
INSERT OR IGNORE INTO alarm VALUES
("Wake up", "u gotta go, now", "routine", "9:00", "everyday")
""")
    db.commit()

    # --- SELECT ---
    cursor.execute("SELECT * FROM alarm")
    print(cursor.fetchall())


def main():
    pass


if __name__ == "__main__":
    main()
