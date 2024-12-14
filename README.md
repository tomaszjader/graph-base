# Graph base
Funkcja load_data_to_neo4j:

Tworzy węzły typu User w Neo4j na podstawie danych z pliku users.json, zawierających informacje takie jak id, username, access_level, is_active i lastlog.

Funkcja create_relationships:

Tworzy dwukierunkowe relacje CONNECTED między użytkownikami na podstawie par user1_id i user2_id w pliku relations.json.
