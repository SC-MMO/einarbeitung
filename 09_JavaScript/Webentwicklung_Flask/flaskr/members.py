from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from .db import exec_cmd, read_rows, read_columns, delete_row, edit_row, add_row
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField

member_bp = Blueprint('members', __name__, url_prefix='/members')

class MemberForm(FlaskForm):
    memberId = HiddenField('memberId')
    name = StringField('name')
    squadName = StringField('squadName')
    age = StringField('age')
    secretIdentity = StringField('secretIdentity')
    submitField = SubmitField("Submit")

@member_bp.route('/', methods=["GET", "POST"])
def show_members():
    return render_template("row_table.html", type="member")

@member_bp.route('/<memberId>', methods=["GET", "POST"])
def show_a_member(memberId):
    columns = read_columns(table="members", only_name=True)
    row = read_rows(table="members", limit=1, filter_args=[f"members.memberId = \"{memberId}\""])[0]
    res = dict(zip(columns, row))
    
    squadName = read_rows(table="squads", columns=["squadName", "status", "active"], limit=1, filter_args=[f"squadId = \"{res.get('squadId')}\""])[0]
    res["squadName"] = squadName[0]
    res["status"] = squadName[1]
    res["active"] = squadName[2]

    powers = read_rows(table="powers", columns=["power"], filter_args=[f"memberId = \"{res.get('memberId')}\""])
    res["powers"] = [p[0] for p in powers]

    return render_template("member.html", res=res)

@member_bp.route('/test', methods=["GET"])
def test():
    members = exec_cmd(sql_str="""
SELECT 
    CONCAT('<a href="/members/', members.memberId, '">', members.name, '</a>') AS memberName,
    members.age,
    members.secretIdentity,
    squads.status,
    CONCAT('<a href="/squads/', squads.squadId, '">', squads.squadName, '</a>') AS squadName,
    IF(squads.active, 'yea', 'ney'),
    GROUP_CONCAT(powers.power ORDER BY powers.power SEPARATOR ', ') AS powers,
    CONCAT(
        '<span style="display:inline-flex; gap: 10px;">',
            '<a href="/squads/', members.memberId, '/delete"><i class="fa-solid fa-trash" style="font-size: 30px;"></i></a>',
            '<a href="/squads/', members.memberId, '/edit"><i class="fa-solid fa-pen-to-square" style="font-size: 30px;"></i></a>',
        '</span>'
    )


FROM 
    members
JOIN 
    squads ON members.squadId = squads.squadId
LEFT JOIN 
    powers ON members.memberId = powers.memberId
GROUP BY 
    members.memberId
ORDER BY members.memberId;
""")
    columns = ["Name", "Age", "Secret Identity", "Status", "Squad Name", "Active", "Powers", "Actions"]
    return jsonify([columns, members])
    

@member_bp.route('/create', methods=["GET", "POST"])
def create_a_member():
    form = MemberForm(request.form)
    form.submitField.label.text = 'Create'
    if request.method == "POST" and form.validate():
        squadId = read_rows(table="squads", columns=["squadId"], limit=1, filter_args=[f"squads.squadName = '{form.squadName.data}'"])
        if not squadId:
            return "Error, that squad does not exist"
        squadId = squadId[0][0]
        add_row(table="members", args=[squadId, form.name.data, form.age.data, form.secretIdentity.data])
        return redirect(url_for("members.show_members"))
    return render_template("edit_member.html", form=form, intent='create', table='members')


@member_bp.route('/<memberId>/edit', methods=["GET", "POST"])
def edit_a_member(memberId):
    member_data = read_rows(table="members", columns=["memberId", 'squadId', 'name', 'age', 'secretIdentity'], limit=1, filter_args=[f"members.memberId = '{memberId}'"])[0]
    squad_name = read_rows(table="squads", columns=['squadName'], limit=1, filter_args=[f"squads.squadId = '{member_data[1]}'"])[0][0]

    form = MemberForm(request.form)
    
    if request.method == "POST" and form.validate():
        squadId = read_rows(table="squads", columns=['squadId'], limit=1, filter_args=[f"squads.squadName = '{form.squadName.data}'"])[0][0]
        row_changes = [
            f"name = '{form.name.data}'",
            f"squadId = '{squadId}'",
            f"age = '{form.age.data}'",
            f"secretIdentity = '{form.secretIdentity.data}'"
        ]
        edit_row(table='members', row_changes=row_changes, filter_args=[f'memberId = {member_data[0]}'])
        return redirect(url_for("members.edit_a_member", memberId=member_data[0]))

    form.memberId.data = member_data[0]
    form.name.data = member_data[2]
    form.squadName.data = squad_name
    form.age.data = member_data[3]
    form.secretIdentity.data = member_data[4]
    form.submitField.label.text = 'Apply Changes'

    return render_template("edit_member.html", form=form, intent='Edit', table='member')

@member_bp.route('/<memberId>/delete', methods=["GET", "POST"])
def delete_a_member(memberId):
    delete_row(table="members", filter=f"members.memberId = '{memberId}'")
    return redirect(url_for("members.show_members"))