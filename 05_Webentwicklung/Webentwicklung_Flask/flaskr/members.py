from flask import Blueprint, render_template, request, redirect, url_for
from .db import exec_cmd, read_rows, read_columns
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

member_bp = Blueprint('members', __name__, url_prefix='/members')

class MemberForm(FlaskForm):
    name = StringField('name')
    squadName = StringField('squadName')
    age = StringField('age')
    secretIdentity = StringField('secretIdentity')
    submitField = SubmitField("Submit")

@member_bp.route('/', methods=["GET", "POST"])
def show_members():
    members = exec_cmd(sql_str="""
SELECT 
    CONCAT('<a href="/members/', members.name, '">', members.name, '</a>') AS memberName,
    members.age,
    members.secretIdentity,
    squads.status,
    CONCAT('<a href="/squads/', squads.squadName, '">', squads.squadName, '</a>') AS squadName,
    IF(squads.active, 'yea', 'ney'),
    GROUP_CONCAT(powers.power ORDER BY powers.power SEPARATOR ', ') AS powers
    
FROM 
    members
JOIN 
    squads ON members.squadId = squads.squadId
LEFT JOIN 
    powers ON members.memberId = powers.memberId
GROUP BY 
    members.memberID
ORDER BY members.memberID;
""")

    columns = ["Name", "Age", "Secret Identity", "Status", "Squad Name", "Active", "Powers"]
    return render_template("row_table.html", title="Members", columns=columns, rows=members)

@member_bp.route('/<memberName>', methods=["GET", "POST"])
def show_a_member(memberName):
    columns = read_columns(table="members", only_name=True)
    rows = read_rows(table="members", limit=1, filter_args=[f"members.name = '{memberName}'"])[0]
    res = dict(zip(columns, rows))
    
    squadName = read_rows(table="squads", columns=["squadName", "status", "active"], limit=1, filter_args=[f"squadId = \"{res.get('squadId')}\""])[0]
    res["squadName"] = squadName[0]
    res["status"] = squadName[1]
    res["active"] = squadName[2]
    
    powers = read_rows(table="powers", columns=["power"], filter_args=[f"memberId = \"{res.get('memberId')}\""])
    powers = [powers[0] for powers in powers]
    res["powers"] = powers

    return render_template("member.html", res=res)


@member_bp.route('/create', methods=["GET", "POST"])
def create_a_member():
    form = MemberForm(request.form)
    if request.method == "POST" and form.validate():
        
        return redirect(url_for('index'))
    return render_template("edit_member.html", form=form, intent='create', table='members')


@member_bp.route('/<memberName>/edit', methods=["GET", "POST"])
def edit_a_member(memberName):
    member_data = read_rows(table="members", columns=['squadId', 'age', 'secretIdentity'], limit=1, filter_args=[f"members.name = '{memberName}'"])[0]
    squad_name = read_rows(table="squads", columns=['squadName'], limit=1, filter_args=[f"squads.squadId = '{member_data[0]}'"])[0][0]

    form = MemberForm(request.form)
    form.name.data = memberName
    form.squadName.data = squad_name
    form.age.data = member_data[1]
    form.secretIdentity.data = member_data[2]

    if request.method == "POST" and form.validate():
        
        return redirect(url_for('index'))
    return render_template("edit_member.html", form=form, intent='Edit', table='member')