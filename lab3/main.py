import json

from flask import Flask, jsonify, request, Response

app = Flask(__name__)
movies = []
crt_id = 1


# GET /movies - în format JSON, o listă cu toate filmele din sistem
@app.route('/movies', methods=['GET'])
def get_movies():
    result = movies
    return Response(status=200, response=json.dumps(movies))


# POST /movies - payload nume și adaugă respectivul film în listă
@app.route('/movies', methods=['POST'])
def post_movie():
    global crt_id
    body = request.json
    key = 'nume'
    if body and key in body and body[key] != '':
        movies.append({'id': crt_id, 'nume': body[key]})
        crt_id += 1
        return Response(response=json.dumps(movies[-1]), status=201)
    else:
        return Response(status=400)


# PUT /movie/{id}
@app.route('/movie/<id>', methods=['PUT'])
def put_movie(id):
    body = request.json
    key = 'nume'

    if key not in body:
        return Response(status=400)

    for m in movies:
        if m['id'] == int(id):
            m[key] = body[key]
            return Response(status=200)
    return Response(status=404)


# GET /movie/{id}
@app.route('/movie/<id>', methods=['GET'])
def get_movie(id):
    key = 'id'

    for m in movies:
        if m[key] == int(id):
            return Response(status=200, response=json.dumps(m))

    return Response(status=404)


# DELETE /movie/{id}
@app.route('/movie/<id>', methods=['DELETE'])
def del_movie(id):
    key = 'id'
    i = -1

    for m in movies:
        i += 1
        if m[key] == int(id):
            del movies[i]
            return Response(status=200)

    return Response(status=404)


# - DELETE /reset
@app.route('/reset', methods=['DELETE'])
def reset_movie():
    movies.clear()
    crt_id = 1

    return Response(status=200)


if __name__ == '__main__':
    app.run()
