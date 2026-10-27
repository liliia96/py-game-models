import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for nickname, player in players_data.items():
        race_dict = player["race"]
        race_obj, _ = Race.objects.get_or_create(
            name=race_dict["name"],
            defaults={"description": race_dict["description"]}
        )

        for skill_dict in race_dict["skills"]:
            Skill.objects.get_or_create(
                name=skill_dict["name"],
                defaults={
                    "bonus": skill_dict["bonus"],
                    "race": race_obj
                }
            )

        guild_dict = player["guild"]

        if guild_dict:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_dict["name"],
                defaults={"description": guild_dict["description"]}
            )
        else:
            guild_obj = None

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player["email"],
                "bio": player["bio"],
                "race": race_obj,
                "guild": guild_obj,
            }
        )


if __name__ == "__main__":
    main()
