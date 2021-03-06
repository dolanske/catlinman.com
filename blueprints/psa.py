
# Import Python modules.
import json

# Import SQLAlchemy random ordering.
from sqlalchemy import func

# Import and setup this blueprint.
from sanic import Blueprint, response

# Import the database connection.
import database

bp_psa = Blueprint("psa")


@bp_psa.route("/psa", methods=["GET", "POST"])
async def psa_json(request):
    # On GET requests return a random PSA.
    if request.method == "GET":
        # Query the database and get a random PSA.
        result = database.db_session.query(database.PSA).order_by(func.random()).first()

        # Handle the result if it was found.
        if result:
            # Return the JSON.
            return response.json({
                "id": result.id,
                "content": result.content,
                "author": result.author,
                "date": result.create_on.strftime("%Y-%m-%d %H:%M:%S")
            })

        else:
            return response.json(
                {"message": "PSA entry not found!"},
                status=404
            )


@bp_psa.route("/psa/<id>", methods=["GET", "POST"])
async def psa_id_json(request, id):
    # On GET requests return all PSAs.
    if request.method == "GET":
        # Query the database and get the PSA with the given id.
        result = database.db_session.query(database.PSA).get(id)

        # Handle the result if it was found.
        if result:
            # Return the JSON.
            return response.json({
                "id": result.id,
                "content": result.content,
                "author": result.author,
                "date": result.create_on.strftime("%Y-%m-%d %H:%M:%S")
            })

        else:
            return response.json(
                {"message": "PSA entry not found!"},
                status=404
            )


@bp_psa.route("/psa/all", methods=["GET"])
async def psa_all_json(request):
    # On GET requests return a all PSAs.
    if request.method == "GET":
        # Query the database and get all PSAs.
        result = database.db_session.query(database.PSA).all()

        # Handle the result if it was found.
        if result:
            # Convert the query result into a JSON compliant format.
            data = []

            for psa in result:
                data.append({
                    "id": psa.id,
                    "content": psa.content,
                    "author": psa.author,
                    "date": psa.create_on.strftime("%Y-%m-%d %H:%M:%S")
                })

            # Return the JSON.
            return response.json(data)

        else:
            return response.json(
                {"message": "PSA entry not found!"},
                status=404
            )
