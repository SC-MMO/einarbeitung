from flask import Blueprint, render_template
from .db import exec_cmd, read_rows, read_columns

squad_bp = Blueprint('squads', __name__, url_prefix='/squads')

@squad_bp.route('/', methods=["GET", "POST"])
def show_squads():
    squads = exec_cmd(sql_str="""             
SELECT 
    squads.squadID,
    CONCAT('<a href="/squads/', squads.squadName, '">', squads.squadName, '</a>') AS squadName,
    squads.homeTown,
    squads.formed,
    squads.status,
    squads.secretBase,
    IF(squads.active, 'yea', 'ney'),
    GROUP_CONCAT(DISTINCT CONCAT('<a href="/members/', members.name, '">', members.name, '</a>') ORDER BY powers.power SEPARATOR ', ') AS members

FROM 
    squads
JOIN 
    members ON members.squadId = squads.squadId
LEFT JOIN 
    powers ON members.memberId = powers.memberId
GROUP BY 
    squads.squadID
ORDER BY 
    squads.squadID;

""")
    columns = ["ID", "Squad Name", "Home Town", "Formed", "Status", "Secret Base", "Active", "Members"]
    return render_template("row_table.html", title="Squads", columns=columns, rows=squads)

@squad_bp.route('/<squadName>', methods=["GET", "POST"])
def show_a_squad(squadName):
    columns = read_columns(table="squads", only_name=True)
    rows = read_rows(table="squads", limit=1, filter_args=[f"squads.squadName = '{squadName}'"])[0]
    res = dict(zip(columns, rows))
    return f"{res}"