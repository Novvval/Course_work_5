from dataclasses import dataclass
from skills import Skill
from skills import FuryPunch
from skills import HardShot


@dataclass
class UnitClass:
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: Skill


WarriorClass = UnitClass(name="warrior", max_health=60.0, max_stamina=15.0, attack=10.0, stamina=10.0, armor=50.0, skill=FuryPunch()) # TODO Инициализируем экземпляр класса UnitClass и присваиваем ему необходимые значения аттрибуотов

ThiefClass = UnitClass(name="thief", max_health=50.0, max_stamina=25.0, attack=12.0, stamina=15.0, armor=35.0, skill=HardShot())

unit_classes = {
    ThiefClass.name: ThiefClass,
    WarriorClass.name: WarriorClass
}