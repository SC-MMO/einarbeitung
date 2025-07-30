from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from .db import exec_cmd, read_rows, read_columns, add_row, delete_row, edit_row
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField

squad_bp = Blueprint('squads', __name__, url_prefix='/squads')

class SquadForm(FlaskForm):
    squadId = HiddenField('squadId')
    squadName = StringField('squadName')
    homeTown = StringField('homeTown')
    formed = StringField('formed')
    status = StringField('status')
    secretBase = StringField('secretBase')
    active = StringField('active')
    submitField = SubmitField("Submit")

@squad_bp.route('/', methods=["GET", "POST"])
def show_squads():
    squads = exec_cmd(sql_str="""
SELECT 
    CONCAT('<a href="/squads/', squads.squadId, '">', squads.squadName, '</a>') AS squadName,
    squads.formed,
    squads.homeTown,
    squads.status,
    squads.secretBase,
    squads.active,
    GROUP_CONCAT(DISTINCT CONCAT('<a href="/members/', members.memberId, '">', members.name, '</a>') SEPARATOR ', ') AS members,
    CONCAT(
        '<a href="/squads/', squads.squadId, '/delete"><i class="fa-solid fa-trash"></i></a>', 
        ' - ',
        '<a href="/squads/', squads.squadId, '/edit"><i class="fa-solid fa-pen-to-square"></i></a>'
    )
FROM 
    squads
LEFT JOIN 
    members ON members.squadId = squads.squadId
GROUP BY 
    squads.squadId
ORDER BY 
    squads.squadId;


""")
    columns = ["Squad Name", "Formed", "Home Town", "Status", "Secret Base", "Active", "Members", "Actions"]
    return render_template("row_table.html", type="squad", columns=columns, rows=squads)

@squad_bp.route('/<squadId>', methods=["GET", "POST"])
def show_a_squad(squadId):
    columns = read_columns(table="squads", only_name=True)
    rows = read_rows(table="squads", limit=1, filter_args=[f"squads.squadId = \"{squadId}\""])[0]
    res = dict(zip(columns, rows))

    members = read_rows(table="members", columns=['memberId', 'name'], filter_args=[f"members.squadId = \"{squadId}\""])
    
    res['members'] = members
    return render_template("squad.html", res=res)

@squad_bp.route('/test', methods=["GET"])
def test():
    squads = exec_cmd(sql_str="""
SELECT 
    CONCAT('<a href="/squads/', squads.squadId, '">', squads.squadName, '</a>') AS squadName,
    squads.formed,
    squads.homeTown,
    squads.status,
    squads.secretBase,
    squads.active,
    GROUP_CONCAT(DISTINCT CONCAT('<a href="/members/', members.memberId, '">', members.name, '</a>') SEPARATOR ', ') AS members,
    CONCAT(
        '<a href="/squads/', squads.squadId, '/delete"><i class="fa-solid fa-trash"></i></a>', 
        ' - ',
        '<a href="/squads/', squads.squadId, '/edit"><i class="fa-solid fa-pen-to-square"></i></a>'
    )
FROM 
    squads
LEFT JOIN 
    members ON members.squadId = squads.squadId
GROUP BY 
    squads.squadId
ORDER BY 
    squads.squadId;
""")
    columns = ["Squad Name", "Formed", "Home Town", "Status", "Secret Base", "Active", "Members", "Actions"]
    return jsonify([columns, squads])

@squad_bp.route('/create', methods=["GET", "POST"])
def create_a_squad():
    form = SquadForm(request.form)
    form.submitField.label.text = 'Create'
    if request.method == "POST" and form.validate():
        args=[
            form.squadName.data, 
            form.homeTown.data, 
            form.formed.data, 
            form.status.data, 
            form.secretBase.data, 
            form.active.data
        ]
        add_row(table="squads", args=args)
        return redirect(url_for("squads.show_squads"))
    return render_template("edit_squad.html", form=form, intent='create', table='squads')


@squad_bp.route('/<squadId>/edit', methods=["GET", "POST"])
def edit_a_squad(squadId):
    squad_data = read_rows(table="squads", columns=["squadName", 'homeTown', 'formed', 'status', 'secretBase', "active" ], limit=1, filter_args=[f"squads.squadId = '{squadId}'"])[0]
    form = SquadForm(request.form)

    if request.method == "POST" and form.validate():
        row_changes = [
            f"squadName = '{form.squadName.data}'",
            f"homeTown = '{form.homeTown.data}'",
            f"formed = '{form.formed.data}'",
            f"status = '{form.status.data}'",
            f"secretBase = '{form.secretBase.data}'",
            f"active = '{form.active.data}'",
        ]
        edit_row(table='squads', row_changes=row_changes, filter_args=[f'squadId = {squadId}'])
        return redirect(url_for("squads.edit_a_squad", squadId=squadId))

    form.squadId.data = squadId
    form.squadName.data = squad_data[0]
    form.homeTown.data = squad_data[1]
    form.formed.data = squad_data[2]
    form.status.data = squad_data[3]
    form.secretBase.data = squad_data[4]
    form.active.data = squad_data[5]
    form.submitField.label.text = 'Apply Changes'
    return render_template("edit_squad.html", form=form, intent='Edit', table='squad')

@squad_bp.route('/<squadId>/delete', methods=["GET", "POST"])
def delete_a_squad(squadId):
    delete_row(table="squads", filter=f"squads.squadId = '{squadId}'")
    return redirect(url_for("squads.show_squads"))