from flask import Blueprint, render_template
from .db import exec_cmd, read_rows, read_columns

member_bp = Blueprint('members', __name__, url_prefix='/members')

@member_bp.route('/', methods=["GET", "POST"])
def show_members():
    members = exec_cmd(sql_str="""
SELECT 
    members.memberId,
    CONCAT('<a href="/members/', members.name, '">', members.name, '</a>') AS memberName,
    members.age,
    members.secretIdentity,
    CONCAT('<a href="/squads/', squads.squadName, '">', squads.squadName, '</a>') AS squadName,
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

    columns = ["ID", "Name", "Age", "Secret Identity", "Squad Name", "Powers"]
    return render_template("row_table.html", title="Members", columns=columns, rows=members)

@member_bp.route('/<memberName>', methods=["GET", "POST"])
def show_a_member(memberName):
    columns = read_columns(table="members", only_name=True)
    rows = read_rows(table="members", limit=1, filter_args=[f"members.name = '{memberName}'"])[0]
    res = dict(zip(columns, rows))
    return f"{res}"