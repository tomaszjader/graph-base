from neo4j import GraphDatabase
import json


NEO4J_URI = "bolt://localhost:7687"  # Adres Neo4j
NEO4J_USER = "neo4j"  # Użytkownik (domyślnie "neo4j")
NEO4J_PASSWORD = "password"  # Hasło


# Funkcja do załadowania danych z JSON do Neo4j
def load_data_to_neo4j(file_path):
    # Ładowanie danych JSON
    # Ładowanie danych JSON z wymuszonym kodowaniem UTF-8
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    # Połączenie z Neo4j
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

    with driver.session() as session:
        for user in data:
            session.run(
                """
                CREATE (u:User {
                    id: $id,
                    username: $username,
                    access_level: $access_level,
                    is_active: $is_active,
                    lastlog: $lastlog
                })
                """,
                id=user["id"],
                username=user["username"],
                access_level=user["access_level"],
                is_active=user["is_active"],
                lastlog=user["lastlog"]
            )
    driver.close()
    print("Dane zostały załadowane do Neo4j.")


def create_relationships(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)

    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

    with driver.session() as session:
        for relation in data:
            session.run(
                """
                MATCH (u1:User {id: $user1_id}), (u2:User {id: $user2_id})
                CREATE (u1)-[:CONNECTED]->(u2),
                       (u2)-[:CONNECTED]->(u1)
                """,
                user1_id=relation["user1_id"],
                user2_id=relation["user2_id"]
            )
    driver.close()
    print("Relacje zostały stworzone w Neo4j.")



file_path = "relations.json"
create_relationships(file_path)


# file_path = "users.json"
# load_data_to_neo4j(file_path)
