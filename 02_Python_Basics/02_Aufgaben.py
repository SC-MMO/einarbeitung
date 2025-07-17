from typing import List
import json

class member:
    def __init__(self, *, id:int, name: str, age: int, secretIdentity: str, powers: List[str]):
        self.id = id
        self.name = name
        self.age = age
        self.secretIdentity = secretIdentity
        self.powers = powers

    def __repr__(self):
        result = []
        for k, v in self.__dict__.items():
            result.append(f"{k}: {v}")

        return "\n" + ', '.join(result)

class squad:
    def __init__(self, *, squadName:str, homeTown: str, formed: int, status: str, active: bool, members:List[member]):
        self.squadName = squadName
        self.homeTown = homeTown
        self.formed = formed
        self.status = status
        self.active = active
        self.members = members
    
    def __str__(self):
        result = ""
        for k, v in self.__dict__.items():
            result += f"{k}: {v}\n"
        return result
    
    def add_new_member(self, **kwargs):
        self.members.append(member(**kwargs))

    def del_member(self, *,  id: int) -> bool:
        for idx, member in enumerate(self.members):
            if member.id == id:
                del self.members[idx]
                return True
        return False



with open("../base.json", "r") as my_file:
    content = json.load(my_file)

groups = []
for group in content:
    ids = iter(range(1 + len(group.get('members', []))))
    obj = squad(
        squadName=group.get('squadName', 'N/A'),
        homeTown=group.get('homeTown', 'N/A'),
        formed=group.get('formed', 'N/A'),
        status=group.get('status', 'N/A'),
        active=group.get('active', False),
        members= [
            member(
                id=next(ids),
                name=a_member.get('name', 'N/A'), 
                age=a_member.get('age', 'N/A'),
                secretIdentity=a_member.get('secretIdentity', 'N/A'),
                powers=a_member.get('powers', 'N/A')
                ) for a_member in group.get('members', [])]
        )
    groups.append(obj)

#Testing
for group in groups:
    print(group, "\n")

a_squad = squad(squadName="testname", homeTown="testtown", formed=1000, status="idk", active=True, members=[])
print(a_squad, "\n")

a_squad.add_new_member(id=1, name="test", age=4, secretIdentity="Batman", powers=[])
a_squad.add_new_member(id=2, name="test2", age=43, secretIdentity="Batgirl", powers=[])
print(a_squad)

a_squad.del_member(id=1)
print(a_squad)