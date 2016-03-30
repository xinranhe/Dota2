import ast

heroes = ast.literal_eval(
'''
{
    "result": {
        "heroes": [
            {
                "name": "npc_dota_hero_antimage",
                "id": 1,
                "localized_name": "Anti-Mage"
            },
            {
                "name": "npc_dota_hero_axe",
                "id": 2,
                "localized_name": "Axe"
            },
            {
                "name": "npc_dota_hero_bane",
                "id": 3,
                "localized_name": "Bane"
            },
            {
                "name": "npc_dota_hero_bloodseeker",
                "id": 4,
                "localized_name": "Bloodseeker"
            },
            {
                "name": "npc_dota_hero_crystal_maiden",
                "id": 5,
                "localized_name": "Crystal Maiden"
            },
            {
                "name": "npc_dota_hero_drow_ranger",
                "id": 6,
                "localized_name": "Drow Ranger"
            },
            {
                "name": "npc_dota_hero_earthshaker",
                "id": 7,
                "localized_name": "Earthshaker"
            },
            {
                "name": "npc_dota_hero_juggernaut",
                "id": 8,
                "localized_name": "Juggernaut"
            },
            {
                "name": "npc_dota_hero_mirana",
                "id": 9,
                "localized_name": "Mirana"
            },
            {
                "name": "npc_dota_hero_nevermore",
                "id": 11,
                "localized_name": "Shadow Fiend"
            },
            {
                "name": "npc_dota_hero_morphling",
                "id": 10,
                "localized_name": "Morphling"
            },
            {
                "name": "npc_dota_hero_phantom_lancer",
                "id": 12,
                "localized_name": "Phantom Lancer"
            },
            {
                "name": "npc_dota_hero_puck",
                "id": 13,
                "localized_name": "Puck"
            },
            {
                "name": "npc_dota_hero_pudge",
                "id": 14,
                "localized_name": "Pudge"
            },
            {
                "name": "npc_dota_hero_razor",
                "id": 15,
                "localized_name": "Razor"
            },
            {
                "name": "npc_dota_hero_sand_king",
                "id": 16,
                "localized_name": "Sand King"
            },
            {
                "name": "npc_dota_hero_storm_spirit",
                "id": 17,
                "localized_name": "Storm Spirit"
            },
            {
                "name": "npc_dota_hero_sven",
                "id": 18,
                "localized_name": "Sven"
            },
            {
                "name": "npc_dota_hero_tiny",
                "id": 19,
                "localized_name": "Tiny"
            },
            {
                "name": "npc_dota_hero_vengefulspirit",
                "id": 20,
                "localized_name": "Vengeful Spirit"
            },
            {
                "name": "npc_dota_hero_windrunner",
                "id": 21,
                "localized_name": "Windranger"
            },
            {
                "name": "npc_dota_hero_zuus",
                "id": 22,
                "localized_name": "Zeus"
            },
            {
                "name": "npc_dota_hero_kunkka",
                "id": 23,
                "localized_name": "Kunkka"
            },
            {
                "name": "npc_dota_hero_lina",
                "id": 25,
                "localized_name": "Lina"
            },
            {
                "name": "npc_dota_hero_lich",
                "id": 31,
                "localized_name": "Lich"
            },
            {
                "name": "npc_dota_hero_lion",
                "id": 26,
                "localized_name": "Lion"
            },
            {
                "name": "npc_dota_hero_shadow_shaman",
                "id": 27,
                "localized_name": "Shadow Shaman"
            },
            {
                "name": "npc_dota_hero_slardar",
                "id": 28,
                "localized_name": "Slardar"
            },
            {
                "name": "npc_dota_hero_tidehunter",
                "id": 29,
                "localized_name": "Tidehunter"
            },
            {
                "name": "npc_dota_hero_witch_doctor",
                "id": 30,
                "localized_name": "Witch Doctor"
            },
            {
                "name": "npc_dota_hero_riki",
                "id": 32,
                "localized_name": "Riki"
            },
            {
                "name": "npc_dota_hero_enigma",
                "id": 33,
                "localized_name": "Enigma"
            },
            {
                "name": "npc_dota_hero_tinker",
                "id": 34,
                "localized_name": "Tinker"
            },
            {
                "name": "npc_dota_hero_sniper",
                "id": 35,
                "localized_name": "Sniper"
            },
            {
                "name": "npc_dota_hero_necrolyte",
                "id": 36,
                "localized_name": "Necrophos"
            },
            {
                "name": "npc_dota_hero_warlock",
                "id": 37,
                "localized_name": "Warlock"
            },
            {
                "name": "npc_dota_hero_beastmaster",
                "id": 38,
                "localized_name": "Beastmaster"
            },
            {
                "name": "npc_dota_hero_queenofpain",
                "id": 39,
                "localized_name": "Queen of Pain"
            },
            {
                "name": "npc_dota_hero_venomancer",
                "id": 40,
                "localized_name": "Venomancer"
            },
            {
                "name": "npc_dota_hero_faceless_void",
                "id": 41,
                "localized_name": "Faceless Void"
            },
            {
                "name": "npc_dota_hero_skeleton_king",
                "id": 42,
                "localized_name": "Wraith King"
            },
            {
                "name": "npc_dota_hero_death_prophet",
                "id": 43,
                "localized_name": "Death Prophet"
            },
            {
                "name": "npc_dota_hero_phantom_assassin",
                "id": 44,
                "localized_name": "Phantom Assassin"
            },
            {
                "name": "npc_dota_hero_pugna",
                "id": 45,
                "localized_name": "Pugna"
            },
            {
                "name": "npc_dota_hero_templar_assassin",
                "id": 46,
                "localized_name": "Templar Assassin"
            },
            {
                "name": "npc_dota_hero_viper",
                "id": 47,
                "localized_name": "Viper"
            },
            {
                "name": "npc_dota_hero_luna",
                "id": 48,
                "localized_name": "Luna"
            },
            {
                "name": "npc_dota_hero_dragon_knight",
                "id": 49,
                "localized_name": "Dragon Knight"
            },
            {
                "name": "npc_dota_hero_dazzle",
                "id": 50,
                "localized_name": "Dazzle"
            },
            {
                "name": "npc_dota_hero_rattletrap",
                "id": 51,
                "localized_name": "Clockwerk"
            },
            {
                "name": "npc_dota_hero_leshrac",
                "id": 52,
                "localized_name": "Leshrac"
            },
            {
                "name": "npc_dota_hero_furion",
                "id": 53,
                "localized_name": "Nature's Prophet"
            },
            {
                "name": "npc_dota_hero_life_stealer",
                "id": 54,
                "localized_name": "Lifestealer"
            },
            {
                "name": "npc_dota_hero_dark_seer",
                "id": 55,
                "localized_name": "Dark Seer"
            },
            {
                "name": "npc_dota_hero_clinkz",
                "id": 56,
                "localized_name": "Clinkz"
            },
            {
                "name": "npc_dota_hero_omniknight",
                "id": 57,
                "localized_name": "Omniknight"
            },
            {
                "name": "npc_dota_hero_enchantress",
                "id": 58,
                "localized_name": "Enchantress"
            },
            {
                "name": "npc_dota_hero_huskar",
                "id": 59,
                "localized_name": "Huskar"
            },
            {
                "name": "npc_dota_hero_night_stalker",
                "id": 60,
                "localized_name": "Night Stalker"
            },
            {
                "name": "npc_dota_hero_broodmother",
                "id": 61,
                "localized_name": "Broodmother"
            },
            {
                "name": "npc_dota_hero_bounty_hunter",
                "id": 62,
                "localized_name": "Bounty Hunter"
            },
            {
                "name": "npc_dota_hero_weaver",
                "id": 63,
                "localized_name": "Weaver"
            },
            {
                "name": "npc_dota_hero_jakiro",
                "id": 64,
                "localized_name": "Jakiro"
            },
            {
                "name": "npc_dota_hero_batrider",
                "id": 65,
                "localized_name": "Batrider"
            },
            {
                "name": "npc_dota_hero_chen",
                "id": 66,
                "localized_name": "Chen"
            },
            {
                "name": "npc_dota_hero_spectre",
                "id": 67,
                "localized_name": "Spectre"
            },
            {
                "name": "npc_dota_hero_doom_bringer",
                "id": 69,
                "localized_name": "Doom"
            },
            {
                "name": "npc_dota_hero_ancient_apparition",
                "id": 68,
                "localized_name": "Ancient Apparition"
            },
            {
                "name": "npc_dota_hero_ursa",
                "id": 70,
                "localized_name": "Ursa"
            },
            {
                "name": "npc_dota_hero_spirit_breaker",
                "id": 71,
                "localized_name": "Spirit Breaker"
            },
            {
                "name": "npc_dota_hero_gyrocopter",
                "id": 72,
                "localized_name": "Gyrocopter"
            },
            {
                "name": "npc_dota_hero_alchemist",
                "id": 73,
                "localized_name": "Alchemist"
            },
            {
                "name": "npc_dota_hero_invoker",
                "id": 74,
                "localized_name": "Invoker"
            },
            {
                "name": "npc_dota_hero_silencer",
                "id": 75,
                "localized_name": "Silencer"
            },
            {
                "name": "npc_dota_hero_obsidian_destroyer",
                "id": 76,
                "localized_name": "Outworld Devourer"
            },
            {
                "name": "npc_dota_hero_lycan",
                "id": 77,
                "localized_name": "Lycan"
            },
            {
                "name": "npc_dota_hero_brewmaster",
                "id": 78,
                "localized_name": "Brewmaster"
            },
            {
                "name": "npc_dota_hero_shadow_demon",
                "id": 79,
                "localized_name": "Shadow Demon"
            },
            {
                "name": "npc_dota_hero_lone_druid",
                "id": 80,
                "localized_name": "Lone Druid"
            },
            {
                "name": "npc_dota_hero_chaos_knight",
                "id": 81,
                "localized_name": "Chaos Knight"
            },
            {
                "name": "npc_dota_hero_meepo",
                "id": 82,
                "localized_name": "Meepo"
            },
            {
                "name": "npc_dota_hero_treant",
                "id": 83,
                "localized_name": "Treant Protector"
            },
            {
                "name": "npc_dota_hero_ogre_magi",
                "id": 84,
                "localized_name": "Ogre Magi"
            },
            {
                "name": "npc_dota_hero_undying",
                "id": 85,
                "localized_name": "Undying"
            },
            {
                "name": "npc_dota_hero_rubick",
                "id": 86,
                "localized_name": "Rubick"
            },
            {
                "name": "npc_dota_hero_disruptor",
                "id": 87,
                "localized_name": "Disruptor"
            },
            {
                "name": "npc_dota_hero_nyx_assassin",
                "id": 88,
                "localized_name": "Nyx Assassin"
            },
            {
                "name": "npc_dota_hero_naga_siren",
                "id": 89,
                "localized_name": "Naga Siren"
            },
            {
                "name": "npc_dota_hero_keeper_of_the_light",
                "id": 90,
                "localized_name": "Keeper of the Light"
            },
            {
                "name": "npc_dota_hero_wisp",
                "id": 91,
                "localized_name": "Io"
            },
            {
                "name": "npc_dota_hero_visage",
                "id": 92,
                "localized_name": "Visage"
            },
            {
                "name": "npc_dota_hero_slark",
                "id": 93,
                "localized_name": "Slark"
            },
            {
                "name": "npc_dota_hero_medusa",
                "id": 94,
                "localized_name": "Medusa"
            },
            {
                "name": "npc_dota_hero_troll_warlord",
                "id": 95,
                "localized_name": "Troll Warlord"
            },
            {
                "name": "npc_dota_hero_centaur",
                "id": 96,
                "localized_name": "Centaur Warrunner"
            },
            {
                "name": "npc_dota_hero_magnataur",
                "id": 97,
                "localized_name": "Magnus"
            },
            {
                "name": "npc_dota_hero_shredder",
                "id": 98,
                "localized_name": "Timbersaw"
            },
            {
                "name": "npc_dota_hero_bristleback",
                "id": 99,
                "localized_name": "Bristleback"
            },
            {
                "name": "npc_dota_hero_tusk",
                "id": 100,
                "localized_name": "Tusk"
            },
            {
                "name": "npc_dota_hero_skywrath_mage",
                "id": 101,
                "localized_name": "Skywrath Mage"
            },
            {
                "name": "npc_dota_hero_abaddon",
                "id": 102,
                "localized_name": "Abaddon"
            },
            {
                "name": "npc_dota_hero_elder_titan",
                "id": 103,
                "localized_name": "Elder Titan"
            },
            {
                "name": "npc_dota_hero_legion_commander",
                "id": 104,
                "localized_name": "Legion Commander"
            },
            {
                "name": "npc_dota_hero_ember_spirit",
                "id": 106,
                "localized_name": "Ember Spirit"
            },
            {
                "name": "npc_dota_hero_earth_spirit",
                "id": 107,
                "localized_name": "Earth Spirit"
            },
            {
                "name": "npc_dota_hero_terrorblade",
                "id": 109,
                "localized_name": "Terrorblade"
            },
            {
                "name": "npc_dota_hero_phoenix",
                "id": 110,
                "localized_name": "Phoenix"
            },
            {
                "name": "npc_dota_hero_oracle",
                "id": 111,
                "localized_name": "Oracle"
            },
            {
                "name": "npc_dota_hero_techies",
                "id": 105,
                "localized_name": "Techies"
            },
            {
                "name": "npc_dota_hero_winter_wyvern",
                "id": 112,
                "localized_name": "Winter Wyvern"
            }
        ]
        ,
        "count": 112
    }
}
''')
# two hero missing: 24 and 108

hero_names_dict = {}
for hero in heroes['result']['heroes']:
	hero_names_dict[hero['id']] = hero['localized_name']


game_modes = ast.literal_eval(
'''
{
    "mods": [
        {
            "id" : 0,
            "name" : "Unknown"
        },
        {
            "id" : 1,
            "name" : "All Pick"
        },
        {
            "id" : 2,
            "name" : "Captains Mode"
        },
        {
            "id" : 3,
            "name" : "Random Draft"
        },
        {
            "id" : 4,
            "name" : "Single Draft"
        },
        {
            "id" : 5,
            "name" : "All Random"
        },
        {
            "id" : 6,
            "name" : "?? INTRO/DEATH ??"
        },
        {
            "id" : 7,
            "name" : "The Diretide"
        },
        {
            "id" : 8,
            "name" : "Reverse Captains Mode"
        },
        {
            "id" : 9,
            "name" : "Greeviling"
        },
        {
            "id" : 10,
            "name": "Tutorial"
        },
        {
            "id" : 11,
            "name" : "Mid Only"
        },
        {
            "id" : 12,
            "name" : "Least Played"
        },
        {
            "id" : 13,
            "name" : "New Player Pool"
        },
        {
            "id" : 14,
            "name" : "Compendium Matchmaking"
        },
        {
            "id": 15,
            "name": "Custom"
        },
        {
            "id": 16,
            "name": "Captains Draft"
        },
        {
            "id": 17,
            "name": "Balanced Draft"
        },
        {
            "id": 18,
            "name": "Ability Draft"
        },
        {
            "id": 19,
            "name": "?? Event ??"
        },
        {
            "id": 20,
            "name": "All Random Death Match"
        },
        {
            "id": 21,
            "name": "1vs1 Solo Mid"
        },
        {
            "id": 22,
            "name": "Ranked All Pick"
        }
    ]
}
''')

game_mode_dict = {}
for mode in game_modes['mods']:
    game_mode_dict[mode['id']] = mode['name']

items =  ast.literal_eval(
'''
{
  "items": [
    {
      "id": 0,
      "name": "empty"
    },
    {
      "id": 1,
      "name": "blink"
    },
    {
      "id": 2,
      "name": "blades_of_attack"
    },
    {
      "id": 3,
      "name": "broadsword"
    },
    {
      "id": 4,
      "name": "chainmail"
    },
    {
      "id": 5,
      "name": "claymore"
    },
    {
      "id": 6,
      "name": "helm_of_iron_will"
    },
    {
      "id": 7,
      "name": "javelin"
    },
    {
      "id": 8,
      "name": "mithril_hammer"
    },
    {
      "id": 9,
      "name": "platemail"
    },
    {
      "id": 10,
      "name": "quarterstaff"
    },
    {
      "id": 11,
      "name": "quelling_blade"
    },
    {
      "id": 12,
      "name": "ring_of_protection"
    },
    {
      "id": 182,
      "name": "stout_shield"
    },
    {
      "id": 13,
      "name": "gauntlets"
    },
    {
      "id": 14,
      "name": "slippers"
    },
    {
      "id": 15,
      "name": "mantle"
    },
    {
      "id": 16,
      "name": "branches"
    },
    {
      "id": 17,
      "name": "belt_of_strength"
    },
    {
      "id": 18,
      "name": "boots_of_elves"
    },
    {
      "id": 19,
      "name": "robe"
    },
    {
      "id": 20,
      "name": "circlet"
    },
    {
      "id": 21,
      "name": "ogre_axe"
    },
    {
      "id": 22,
      "name": "blade_of_alacrity"
    },
    {
      "id": 23,
      "name": "staff_of_wizardry"
    },
    {
      "id": 24,
      "name": "ultimate_orb"
    },
    {
      "id": 25,
      "name": "gloves"
    },
    {
      "id": 26,
      "name": "lifesteal"
    },
    {
      "id": 27,
      "name": "ring_of_regen"
    },
    {
      "id": 28,
      "name": "sobi_mask"
    },
    {
      "id": 29,
      "name": "boots"
    },
    {
      "id": 30,
      "name": "gem"
    },
    {
      "id": 31,
      "name": "cloak"
    },
    {
      "id": 32,
      "name": "talisman_of_evasion"
    },
    {
      "id": 33,
      "name": "cheese"
    },
    {
      "id": 34,
      "name": "magic_stick"
    },
    {
      "id": 35,
      "name": "recipe_magic_wand"
    },
    {
      "id": 36,
      "name": "magic_wand"
    },
    {
      "id": 37,
      "name": "ghost"
    },
    {
      "id": 38,
      "name": "clarity"
    },
    {
      "id": 39,
      "name": "flask"
    },
    {
      "id": 40,
      "name": "dust"
    },
    {
      "id": 41,
      "name": "bottle"
    },
    {
      "id": 42,
      "name": "ward_observer"
    },
    {
      "id": 43,
      "name": "ward_sentry"
    },
    {
      "id": 44,
      "name": "tango"
    },
    {
      "id": 45,
      "name": "courier"
    },
    {
      "id": 46,
      "name": "tpscroll"
    },
    {
      "id": 47,
      "name": "recipe_travel_boots"
    },
    {
      "id": 48,
      "name": "travel_boots"
    },
    {
      "id": 49,
      "name": "recipe_phase_boots"
    },
    {
      "id": 50,
      "name": "phase_boots"
    },
    {
      "id": 51,
      "name": "demon_edge"
    },
    {
      "id": 52,
      "name": "eagle"
    },
    {
      "id": 53,
      "name": "reaver"
    },
    {
      "id": 54,
      "name": "relic"
    },
    {
      "id": 55,
      "name": "hyperstone"
    },
    {
      "id": 56,
      "name": "ring_of_health"
    },
    {
      "id": 57,
      "name": "void_stone"
    },
    {
      "id": 58,
      "name": "mystic_staff"
    },
    {
      "id": 59,
      "name": "energy_booster"
    },
    {
      "id": 60,
      "name": "point_booster"
    },
    {
      "id": 61,
      "name": "vitality_booster"
    },
    {
      "id": 62,
      "name": "recipe_power_treads"
    },
    {
      "id": 63,
      "name": "power_treads"
    },
    {
      "id": 64,
      "name": "recipe_hand_of_midas"
    },
    {
      "id": 65,
      "name": "hand_of_midas"
    },
    {
      "id": 66,
      "name": "recipe_oblivion_staff"
    },
    {
      "id": 67,
      "name": "oblivion_staff"
    },
    {
      "id": 68,
      "name": "recipe_pers"
    },
    {
      "id": 69,
      "name": "pers"
    },
    {
      "id": 70,
      "name": "recipe_poor_mans_shield"
    },
    {
      "id": 71,
      "name": "poor_mans_shield"
    },
    {
      "id": 72,
      "name": "recipe_bracer"
    },
    {
      "id": 73,
      "name": "bracer"
    },
    {
      "id": 74,
      "name": "recipe_wraith_band"
    },
    {
      "id": 75,
      "name": "wraith_band"
    },
    {
      "id": 76,
      "name": "recipe_null_talisman"
    },
    {
      "id": 77,
      "name": "null_talisman"
    },
    {
      "id": 78,
      "name": "recipe_mekansm"
    },
    {
      "id": 79,
      "name": "mekansm"
    },
    {
      "id": 80,
      "name": "recipe_vladmir"
    },
    {
      "id": 81,
      "name": "vladmir"
    },
    {
      "id": 84,
      "name": "flying_courier"
    },
    {
      "id": 85,
      "name": "recipe_buckler"
    },
    {
      "id": 86,
      "name": "buckler"
    },
    {
      "id": 87,
      "name": "recipe_ring_of_basilius"
    },
    {
      "id": 88,
      "name": "ring_of_basilius"
    },
    {
      "id": 89,
      "name": "recipe_pipe"
    },
    {
      "id": 90,
      "name": "pipe"
    },
    {
      "id": 91,
      "name": "recipe_urn_of_shadows"
    },
    {
      "id": 92,
      "name": "urn_of_shadows"
    },
    {
      "id": 93,
      "name": "recipe_headdress"
    },
    {
      "id": 94,
      "name": "headdress"
    },
    {
      "id": 95,
      "name": "recipe_sheepstick"
    },
    {
      "id": 96,
      "name": "sheepstick"
    },
    {
      "id": 97,
      "name": "recipe_orchid"
    },
    {
      "id": 98,
      "name": "orchid"
    },
    {
      "id": 99,
      "name": "recipe_cyclone"
    },
    {
      "id": 100,
      "name": "cyclone"
    },
    {
      "id": 101,
      "name": "recipe_force_staff"
    },
    {
      "id": 102,
      "name": "force_staff"
    },
    {
      "id": 103,
      "name": "recipe_dagon"
    },
    {
      "id": 197,
      "name": "recipe_dagon_2"
    },
    {
      "id": 198,
      "name": "recipe_dagon_3"
    },
    {
      "id": 199,
      "name": "recipe_dagon_4"
    },
    {
      "id": 200,
      "name": "recipe_dagon_5"
    },
    {
      "id": 104,
      "name": "dagon"
    },
    {
      "id": 201,
      "name": "dagon_2"
    },
    {
      "id": 202,
      "name": "dagon_3"
    },
    {
      "id": 203,
      "name": "dagon_4"
    },
    {
      "id": 204,
      "name": "dagon_5"
    },
    {
      "id": 105,
      "name": "recipe_necronomicon"
    },
    {
      "id": 191,
      "name": "recipe_necronomicon_2"
    },
    {
      "id": 192,
      "name": "recipe_necronomicon_3"
    },
    {
      "id": 106,
      "name": "necronomicon"
    },
    {
      "id": 193,
      "name": "necronomicon_2"
    },
    {
      "id": 194,
      "name": "necronomicon_3"
    },
    {
      "id": 107,
      "name": "recipe_ultimate_scepter"
    },
    {
      "id": 108,
      "name": "ultimate_scepter"
    },
    {
      "id": 109,
      "name": "recipe_refresher"
    },
    {
      "id": 110,
      "name": "refresher"
    },
    {
      "id": 111,
      "name": "recipe_assault"
    },
    {
      "id": 112,
      "name": "assault"
    },
    {
      "id": 113,
      "name": "recipe_heart"
    },
    {
      "id": 114,
      "name": "heart"
    },
    {
      "id": 115,
      "name": "recipe_black_king_bar"
    },
    {
      "id": 116,
      "name": "black_king_bar"
    },
    {
      "id": 117,
      "name": "aegis"
    },
    {
      "id": 118,
      "name": "recipe_shivas_guard"
    },
    {
      "id": 119,
      "name": "shivas_guard"
    },
    {
      "id": 120,
      "name": "recipe_bloodstone"
    },
    {
      "id": 121,
      "name": "bloodstone"
    },
    {
      "id": 122,
      "name": "recipe_sphere"
    },
    {
      "id": 123,
      "name": "sphere"
    },
    {
      "id": 124,
      "name": "recipe_vanguard"
    },
    {
      "id": 125,
      "name": "vanguard"
    },
    {
      "id": 126,
      "name": "recipe_blade_mail"
    },
    {
      "id": 127,
      "name": "blade_mail"
    },
    {
      "id": 128,
      "name": "recipe_soul_booster"
    },
    {
      "id": 129,
      "name": "soul_booster"
    },
    {
      "id": 130,
      "name": "recipe_hood_of_defiance"
    },
    {
      "id": 131,
      "name": "hood_of_defiance"
    },
    {
      "id": 132,
      "name": "recipe_rapier"
    },
    {
      "id": 133,
      "name": "rapier"
    },
    {
      "id": 134,
      "name": "recipe_monkey_king_bar"
    },
    {
      "id": 135,
      "name": "monkey_king_bar"
    },
    {
      "id": 136,
      "name": "recipe_radiance"
    },
    {
      "id": 137,
      "name": "radiance"
    },
    {
      "id": 138,
      "name": "recipe_butterfly"
    },
    {
      "id": 139,
      "name": "butterfly"
    },
    {
      "id": 140,
      "name": "recipe_greater_crit"
    },
    {
      "id": 141,
      "name": "greater_crit"
    },
    {
      "id": 142,
      "name": "recipe_basher"
    },
    {
      "id": 143,
      "name": "basher"
    },
    {
      "id": 144,
      "name": "recipe_bfury"
    },
    {
      "id": 145,
      "name": "bfury"
    },
    {
      "id": 146,
      "name": "recipe_manta"
    },
    {
      "id": 147,
      "name": "manta"
    },
    {
      "id": 148,
      "name": "recipe_lesser_crit"
    },
    {
      "id": 149,
      "name": "lesser_crit"
    },
    {
      "id": 150,
      "name": "recipe_armlet"
    },
    {
      "id": 151,
      "name": "armlet"
    },
    {
      "id": 183,
      "name": "recipe_invis_sword"
    },
    {
      "id": 152,
      "name": "invis_sword"
    },
    {
      "id": 153,
      "name": "recipe_sange_and_yasha"
    },
    {
      "id": 154,
      "name": "sange_and_yasha"
    },
    {
      "id": 155,
      "name": "recipe_satanic"
    },
    {
      "id": 156,
      "name": "satanic"
    },
    {
      "id": 157,
      "name": "recipe_mjollnir"
    },
    {
      "id": 158,
      "name": "mjollnir"
    },
    {
      "id": 159,
      "name": "recipe_skadi"
    },
    {
      "id": 160,
      "name": "skadi"
    },
    {
      "id": 161,
      "name": "recipe_sange"
    },
    {
      "id": 162,
      "name": "sange"
    },
    {
      "id": 163,
      "name": "recipe_helm_of_the_dominator"
    },
    {
      "id": 164,
      "name": "helm_of_the_dominator"
    },
    {
      "id": 165,
      "name": "recipe_maelstrom"
    },
    {
      "id": 166,
      "name": "maelstrom"
    },
    {
      "id": 167,
      "name": "recipe_desolator"
    },
    {
      "id": 168,
      "name": "desolator"
    },
    {
      "id": 169,
      "name": "recipe_yasha"
    },
    {
      "id": 170,
      "name": "yasha"
    },
    {
      "id": 171,
      "name": "recipe_mask_of_madness"
    },
    {
      "id": 172,
      "name": "mask_of_madness"
    },
    {
      "id": 173,
      "name": "recipe_diffusal_blade"
    },
    {
      "id": 195,
      "name": "recipe_diffusal_blade_2"
    },
    {
      "id": 174,
      "name": "diffusal_blade"
    },
    {
      "id": 196,
      "name": "diffusal_blade_2"
    },
    {
      "id": 175,
      "name": "recipe_ethereal_blade"
    },
    {
      "id": 176,
      "name": "ethereal_blade"
    },
    {
      "id": 177,
      "name": "recipe_soul_ring"
    },
    {
      "id": 178,
      "name": "soul_ring"
    },
    {
      "id": 179,
      "name": "recipe_arcane_boots"
    },
    {
      "id": 180,
      "name": "arcane_boots"
    },
    {
      "id": 181,
      "name": "orb_of_venom"
    },
    {
      "id": 184,
      "name": "recipe_ancient_janggo"
    },
    {
      "id": 185,
      "name": "ancient_janggo"
    },
    {
      "id": 186,
      "name": "recipe_medallion_of_courage"
    },
    {
      "id": 187,
      "name": "medallion_of_courage"
    },
    {
      "id": 188,
      "name": "smoke_of_deceit"
    },
    {
      "id": 189,
      "name": "recipe_veil_of_discord"
    },
    {
      "id": 190,
      "name": "veil_of_discord"
    },
    {
      "id": 205,
      "name": "recipe_rod_of_atos"
    },
    {
      "id": 206,
      "name": "rod_of_atos"
    },
    {
      "id": 207,
      "name": "recipe_abyssal_blade"
    },
    {
      "id": 208,
      "name": "abyssal_blade"
    },
    {
      "id": 209,
      "name": "recipe_heavens_halberd"
    },
    {
      "id": 210,
      "name": "heavens_halberd"
    },
    {
      "id": 211,
      "name": "recipe_ring_of_aquila"
    },
    {
      "id": 212,
      "name": "ring_of_aquila"
    },
    {
      "id": 213,
      "name": "recipe_tranquil_boots"
    },
    {
      "id": 214,
      "name": "tranquil_boots"
    },
    {
      "id": 215,
      "name": "shadow_amulet"
    },
    {
      "id": 216,
      "name": "enchanted_mango"
    },
    {
      "id": 218,
      "name": "ward_dispenser"
    },
    {
      "id": 220,
      "name": "travel_boots_2"
    },
    {
      "id": 226,
      "name": "lotus_orb"
    },
    {
      "id": 229,
      "name": "solar_crest"
    },
    {
      "id": 231,
      "name": "guardian_greaves"
    },
    {
      "id": 235,
      "name": "octarine_core"
    },
    {
      "id": 247,
      "name": "moon_shard"
    },
    {
      "id": 249,
      "name": "silver_edge"
    },
    {
      "id": 254,
      "name": "glimmer_cape"
    },
    {
      "id": 1000,
      "name": "halloween_candy_corn"
    },
    {
      "id": 1001,
      "name": "mystery_hook"
    },
    {
      "id": 1002,
      "name": "mystery_arrow"
    },
    {
      "id": 1003,
      "name": "mystery_missile"
    },
    {
      "id": 1004,
      "name": "mystery_toss"
    },
    {
      "id": 1005,
      "name": "mystery_vacuum"
    },
    {
      "id": 1006,
      "name": "halloween_rapier"
    },
    {
      "id": 1007,
      "name": "greevil_whistle"
    },
    {
      "id": 1008,
      "name": "greevil_whistle_toggle"
    },
    {
      "id": 1009,
      "name": "present"
    },
    {
      "id": 1010,
      "name": "winter_stocking"
    },
    {
      "id": 1011,
      "name": "winter_skates"
    },
    {
      "id": 1012,
      "name": "winter_cake"
    },
    {
      "id": 1013,
      "name": "winter_cookie"
    },
    {
      "id": 1014,
      "name": "winter_coco"
    },
    {
      "id": 1015,
      "name": "winter_ham"
    },
    {
      "id": 1016,
      "name": "winter_kringle"
    },
    {
      "id": 1017,
      "name": "winter_mushroom"
    },
    {
      "id": 1018,
      "name": "winter_greevil_treat"
    },
    {
      "id": 1019,
      "name": "winter_greevil_garbage"
    },
    {
      "id": 1020,
      "name": "winter_greevil_chewy"
    },
    {
      "id": 241,
      "name": "tango_single"
    },
    {
      "id": 242,
      "name": "crimson_guard"
    }
  ]
}
''')
item_dict = {}
for item in items['items']:
    item_dict[item['id']] = item['name']