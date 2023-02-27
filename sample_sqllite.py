import sqlite3
import pickle

class ObjectState:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.name} is {self.age} years old"

    def save_state(self):
        # Connect to the database
        conn = sqlite3.connect('object_state.db')

        # Create a table to store the object state if it doesn't exist
        conn.execute('''CREATE TABLE IF NOT EXISTS object_state
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     object_name TEXT,
                     object_state BLOB)''')

        # Serialize the object state
        object_state_bytes = pickle.dumps(self)

        # Save the object state to the database
        conn.execute("INSERT INTO object_state (object_name, object_state) VALUES (?, ?)", (self.__class__.__name__, object_state_bytes))

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

    @staticmethod
    def get_saved_state(object_name):
        # Connect to the database
        conn = sqlite3.connect('object_state.db')

        # Get the last saved state of the object from the database
        cursor = conn.execute("SELECT object_state FROM object_state WHERE object_name = ? ORDER BY id DESC LIMIT 1", (object_name,))

        # Deserialize the object state
        object_state_bytes = cursor.fetchone()[0]
        object_state = pickle.loads(object_state_bytes)

        # Close the connection and return the object state
        conn.close()
        return object_state

if __name__ == '__main__':
    # Create a sample object
    obj = ObjectState('John', 30)

    # Save the state of the object to the database
    obj.save_state()

    # Update the object
    obj.age = 31

    # Get the last saved state of the object from the database and compare it with the current state
    saved_state = ObjectState.get_saved_state('ObjectState')
    print(f'Saved State: {saved_state}')
    print(f'Current State: {obj}')
    print(f'Difference: {vars(saved_state) != vars(obj)}')
