import psycopg2
from psycopg2 import OperationalError


def create_connection():
    try:
        conn = psycopg2.connect(
            host="localhost",      
            dbname="financas",  
            user="postgres",    
            password="postgres"   
        )
        print("Conexão realizada com sucesso!")
        return conn
    except OperationalError as e:
        print(f"Erro ao conectar no banco: {e}")
        return None


if __name__ == "__main__":
    conn = create_connection()
    if conn:
        conn.close()
        print("Conexão encerrada.")

