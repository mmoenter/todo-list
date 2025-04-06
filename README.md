# 📝 Todolistenverwaltung (Flask + OpenAPI)

Ein einfaches REST-API-Projekt zur Verwaltung von To-Do-Listen und Einträgen. Implementiert mit Python, Flask und dokumentiert mit einer OpenAPI-Spezifikation.

---

## 🚀 Features

- Erstellen, Abrufen und Löschen von To-Do-Listen
- Hinzufügen, Bearbeiten und Entfernen von Einträgen innerhalb einer Liste
- REST-konformes API-Design
- UUIDs als eindeutige Identifikatoren
- OpenAPI 3.0 Spezifikation (YAML)

---

## 📦 Setup

### Voraussetzungen

- Python 3.9 oder höher
- Flask
- `curl` oder Postman zum Testen

### Installation

```bash
git https://github.com/mmoenter/todo-list.git
cd todo-list
```

---

## ▶️ Starten des Servers

```bash
python webserver.py
```

Der Server läuft standardmäßig unter:  
**http://localhost:3000**

---

## 📚 API-Dokumentation

Die API ist beschrieben in [`Todolistenverwaltung.yaml`](./Todolistenverwaltung.yaml) (OpenAPI 3.0).

---

## 📬 Beispielanfragen (per curl)

### Neue Liste erstellen
```bash
curl -X POST http://localhost:3000/todo-list \
  -H "Content-Type: application/json" \
  -d '{"name": "Meine neue Liste"}'
```

### Alle Listen abrufen
```bash
curl http://localhost:3000/todo-lists
```

### Eintrag zur Liste hinzufügen
```bash
curl -X POST http://localhost:3000/todo-list/<list_id>/entry \
  -H "Content-Type: application/json" \
  -d '{"name": "Milch kaufen", "description": "1L", "user_id": "123e4567-e89b-12d3-a456-426614174000"}'
```

---

## 🧪 Testdaten

Beim Start werden drei Test-Listen mit Test-Entries automatisch generiert.
Sie können über GET-Requests ausgelesen werden.

---

## ✨ Autor

Erstellt von [Manuel Mönter](https://github.com/mmoenter)
