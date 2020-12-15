from flask import request, jsonify
from app import app, db
from models import Zoo, Animal, Species


# ------------------------------------------------
# ANIMAL ROUTES
# ------------------------------------------------

# GET /animals,
# POST /animals
@app.route('/animals', methods=['GET', 'POST'])
def get_all_animals():
    if request.method == 'POST':
        name = request.form["name"]
        new_animal = Animal(name=name)
        db.session.add(new_animal)
        db.session.commit()
        return jsonify(new_animal.serialize())
    else:
        data = Animal.query.all()
        all_animals = [item.serialize() for item in data]
        return jsonify(all_animals)


# GET /animals/{id},
# PUT /animals/{id},
# DELETE /animals/{id}
@app.route('/animals/<int:animal_id>', methods=['GET', 'PUT', 'DELETE'])
def get_one_animal(animal_id):
    data = Animal.query.get(animal_id)

    if request.method == 'PUT':
        name = request.form["name"]
        data.name = name
        db.session.commit()
        return "Edited"
    elif request.method == 'DELETE':
        db.session.delete(data)
        db.session.commit()
        return "Deleted"
    else:
        one_animal = data.serialize()
        return jsonify(one_animal)


# GET /animals/query?species={species}
@app.route('/animals/query')
def get_all_animals_of_query():
    species = request.args.get("species")
    species_id = Species.query.filter(Species.colloquial_name == species).first().id
    data = Animal.query.filter(Animal.species_id == species_id).all()
    all_animals_of_species = [item.serialize() for item in data]
    return jsonify(all_animals_of_species)


# ------------------------------------------------
# ANIMAL ROUTES
# ------------------------------------------------

# GET /zoos
@app.route('/zoos')
def get_all_zoos():
    data = Zoo.query.all()
    all_zoos = [d.serialize() for d in data]
    return jsonify(all_zoos)