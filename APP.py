from flask import Flask, jsonify, request, abort

app = Flask(__name__)

@app.route("/")
def home():
    return "Ça marche !"
  
# Données "Mocks" : Liste d'écritures bancaires
entries = [
    {"id": 1, "date": "2023-10-01", "texte": "Loyer Octobre", "montant": -850.0},
    {"id": 2, "date": "2023-10-05", "texte": "Salaire", "montant": 2500.0},
    {"id": 3, "date": "2023-10-06", "texte": "Courses Carrefour", "montant": -120.5}
]

# --- POINTS D'ENTRÉE (ENDPOINTS) ---

# 1. Afficher toutes les écritures (GET)
@app.route('/entries', methods=['GET'])
def get_entries():
    return jsonify(entries), 200

# 2. Afficher une écriture spécifique par ID (GET)
@app.route('/entries/<int:entry_id>', methods=['GET'])
def get_entry(entry_id):
    entry = next((e for e in entries if e['id'] == entry_id), None)
    if entry is None:
        abort(404, description="Écriture non trouvée")
    return jsonify(entry), 200

# 3. Ajouter une écriture (POST)
@app.route('/entries', methods=['POST'])
def add_entry():
    if not request.json or not 'texte' in request.json:
        abort(400, description="Données invalides")
    
    new_entry = {
        "id": entries[-1]['id'] + 1 if entries else 1,
        "date": request.json.get('date', ""),
        "texte": request.json['texte'],
        "montant": request.json.get('montant', 0.0)
    }
    entries.append(new_entry)
    return jsonify(new_entry), 201

# 4. Modifier une écriture (PUT)
@app.route('/entries/<int:entry_id>', methods=['PUT'])
def update_entry(entry_id):
    entry = next((e for e in entries if e['id'] == entry_id), None)
    if entry is None:
        abort(404, description="Écriture non trouvée")
    
    entry['date'] = request.json.get('date', entry['date'])
    entry['texte'] = request.json.get('texte', entry['texte'])
    entry['montant'] = request.json.get('montant', entry['montant'])
    
    return jsonify(entry), 200

# 5. Supprimer une écriture (DELETE)
@app.route('/entries/<int:entry_id>', methods=['DELETE'])
def delete_entry(entry_id):
    global entries
    entries = [e for e in entries if e['id'] != entry_id]
    return jsonify({"result": "Écriture supprimée"}), 200

if __name__ == '__main__':
    # Lancement du serveur sur le port 5000
    app.run(port=5050, debug=False)
