import sqlite3

def create_table():
    """데이터베이스 테이블 생성"""
    with sqlite3.connect("pharmacy.db") as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS medicines (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                unique_code TEXT UNIQUE NOT NULL,
                name TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                price REAL NOT NULL,
                location TEXT NOT NULL,
                expiry_date TEXT NOT NULL
            )
        ''')
        print("Table created successfully.")

def add_medicine(unique_code, name, quantity, price, location, expiry_date):
    """약 추가"""
    with sqlite3.connect("pharmacy.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO medicines (unique_code, name, quantity, price, location, expiry_date) VALUES (?, ?, ?, ?, ?, ?)", (unique_code, name, quantity, price, location, expiry_date))
        conn.commit()
        print(f"Medicine '{name}' added successfully.")

def view_medicines():
    """모든 약 조회"""
    with sqlite3.connect("pharmacy.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM medicines")
        rows = cursor.fetchall()
        print("Medicines:")
        for row in rows:
            print(row)

def view_medicine_by_code_or_name(unique_code=None, name=None):
    """고유번호 또는 이름으로 약 조회"""
    with sqlite3.connect("pharmacy.db") as conn:
        cursor = conn.cursor()
        if unique_code:
            cursor.execute("SELECT * FROM medicines WHERE unique_code = ?", (unique_code,))
        elif name:
            cursor.execute("SELECT * FROM medicines WHERE name = ?", (name,))
        else:
            print("Please provide either a unique_code or a name.")
            return
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print("No matching medicine found.")

def update_medicine(medicine_id, unique_code=None, name=None, quantity=None, price=None, location=None, expiry_date=None):
    """약 정보 업데이트"""
    with sqlite3.connect("pharmacy.db") as conn:
        cursor = conn.cursor()
        if unique_code:
            cursor.execute("UPDATE medicines SET unique_code = ? WHERE id = ?", (unique_code, medicine_id))
        if name:
            cursor.execute("UPDATE medicines SET name = ? WHERE id = ?", (name, medicine_id))
        if quantity:
            cursor.execute("UPDATE medicines SET quantity = ? WHERE id = ?", (quantity, medicine_id))
        if price:
            cursor.execute("UPDATE medicines SET price = ? WHERE id = ?", (price, medicine_id))
        if location:
            cursor.execute("UPDATE medicines SET location = ? WHERE id = ?", (location, medicine_id))
        if expiry_date:
            cursor.execute("UPDATE medicines SET expiry_date = ? WHERE id = ?", (expiry_date, medicine_id))
        conn.commit()
        print(f"Medicine with ID {medicine_id} updated successfully.")

def delete_medicine(medicine_id):
    """약 삭제"""
    with sqlite3.connect("pharmacy.db") as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM medicines WHERE id = ?", (medicine_id,))
        conn.commit()
        print(f"Medicine with ID {medicine_id} deleted successfully.")

if __name__ == "__main__":
    create_table()

    # 약 추가
    add_medicine("M001", "Paracetamol", 100, 500.0, "Shelf A1", "2024-12-31")
    add_medicine("M002", "Ibuprofen", 50, 700.0, "Shelf B2", "2025-06-30")

    # 약 조회
    view_medicines()

    # 고유번호 또는 이름으로 약 조회
    print("\nQuery by unique_code:")
    view_medicine_by_code_or_name(unique_code="M001")

    print("\nQuery by name:")
    view_medicine_by_code_or_name(name="Ibuprofen")

    # 약 업데이트
    update_medicine(1, quantity=120, price=550.0)

    # 약 조회
    view_medicines()

    # 약 삭제
    delete_medicine(2)

    # 약 조회
    view_medicines()
