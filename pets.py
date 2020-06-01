# Fetched from the lastest constant.py from https://github.com/notnotmelon/skyblock-simplified
# Changelogs:
# Add comments about damage pet abilities
# Add pet ability functions accordingly
# Updated all pet stats
# TODO: Missing ghoul pet icon


# region Pet ability functions


def pigman(player, stats, pet):
    # Buffs the Pigman sword by (Pet lvl * 0.4) damage and (Pet lvl * 0.25) strength. (All)
    # Deal (Pet lvl * 0.2%) extra damage to monsters level 100 and up. (Legendary)
    if player.weapon == 'PIGMAN_SWORD':
        stats['weapon damage'] += int(pet.level * 0.4)
        stats['strength'] += int(pet.level * 0.25)


def sheep(player, stats, pet):
    # Increases your total  Mana by (Pet lvl * 0.25%) while in dungeons. (Legendary)
    pass


def witherskeleton(player, stats, pet):
    # Deal (Pet lvl * 0.5%) more damage against wither mobs. (All)
    # Upon hitting an enemy inflict the wither effect for (Pet lvl * 2%) damage over 3 seconds (No stack). (Legendary)
    pass


def horse(player, stats, pet):
    # While riding your horse, gain (Pet lvl * 0.25%) bow damage. (Legendary)
    pass


def lion(player, stats, pet):
    # Adds (Pet lvl * 0.03) damage to your weapons. (Common) (0.05 on Uncommon) (0.1 on Rare) (0.15 on Epic) (0.2 on Legendary)
    # Increases damage dealt by (Pet lvl * 0.3%) on your first hit on a mob. (Rare) (0.4% on Epic) (0.5% on Legendary)
    # Deal (Pet lvl * 0.3%) weapon damage against mobs below level 80. (Legendary)
    stats['weapon damage'] += pet.level * {'common': 0.03, 'uncommon': 0.05, 'rare': 0.1, 'epic': 0.15, 'legendary': 0.2}[pet.rarity]


def wolf(player, stats, pet):
    # Gain (Pet lvl * 0.1%) crit damage for every nearby wolf (max 10). (Rare) (0.15% for Epic, Legendary)
    pass


def enderdragon(player, stats, pet):
    # Deal (Pet lvl * 0.25%) more damage to end mobs. (All)
    # Buffs the Aspect of the Dragon sword by (Pet lvl * 0.5) damage and (Pet lvl * 0.3) strength. (All)
    # Increases all stats by (Pet lvl * 0.1%). (Legendary)
    if player.weapon == 'ASPECT_OF_THE_DRAGONS':
        stats['weapon damage'] += pet.level // 2
        stats['weapon strength'] += int(pet.level * 0.3)
    if pet.rarity == 'legendary':
        boost = int(1 + (pet.level * 0.001))
        stats = {name: stat * boost for name, stat in stats.items()}


def giraffe(player, stats, pet):
    # Grants (Pet lvl * 0.4) strength and (20 + (Pet lvl * 0.1)) crit damage when mid air. (Rare)
    # ((Pet lvl * 0.5) strength and (20 + (Pet lvl * 0.25)) crit damage on Epic)
    # ((Pet lvl * 0.5) strength and (20 + (Pet lvl * 0.4)) crit damage on Legendary)
    pass


def phoenix(player, stats, pet):
    # Before death, become immune and gain (10 + (Pet lvl * 0.1)) strength on (2 + (Pet lvl * 0.02)) seconds (3 minutes cooldown). (Epic) ((10 + (Pet lvl * 0.2) STR on (2 + (Pet lvl * 0.02)) seconds on Legendary)
    # On 4th melee strike, ignite mobs, dealing (1 + (Pet lvl * 0.14)) your crit damage each second for (2 + (Pet lvl/25)) seconds. (Epic, Legendary)
    pass


def bee(player, stats, pet):
    # Gain (1 + (Pet lvl * 0.02)) Intelligence and (1 + (Pet lvl * 0.02)) Strength for each nearby bee. (Max 15) (Common)
    # (1+ (Pet lvl * 0.09) INT and (1 + (Pet lvl * 0.07)) STR on Rare)
    # (1+ (Pet lvl * 0.14) INT and (1 + (Pet lvl * 0.11)) STR on Epic)
    # (1+ (Pet lvl * 0.19) INT and (1 + (Pet lvl * 0.14)) STR on Legendary)
    pass


def squid(player, stats, pet):
    # Buffs the Ink Wand by (Pet lvl * 0.3) damage and (Pet lvl * 0.1) strength. (Rare) (0.4 DMG and 0.2 STR on Epic, Legendary)
    pass


def parrot(player, stats, pet):
    # Gives (5 + (Pet lvl * 0.25)) strength to players within 20 Blocks (No stack). (Legendary)
    if pet.rarity == 'legendary':
        stats['strength'] += int((5 + (pet.level * 0.25)))


def tiger(player, stats, pet):
    # Attacks have a (Pet lvl * 0.05%) chance to strike twice. (Common) (0.1% on Uncommon, Rare) (0.2% on Epic, Legendary)
    # Deal (Pet lvl * 0.2%) more damage against targets with no other mobs within 15 blocks. (Legendary)
    pass

def blaze(player, stats, pet):
    # Upgrades Blaze Armor stats and ability by (Pet lvl * 0.4%). (All)
    # Double effects of Hot Potato Books. (Legendary)
    pass


def zombie(player, stats, pet):
    # Deal (Pet lvl * 0.2%) more damage to zombies. (Epic, Legendary)
    pass


def skeleton(player, stats, pet):
    # Increase arrow damage by (Pet lvl * 0.1%), which is tripled while in dungeons. (Common, Uncommon, Rare) (0.2% on Epic, Legendary)
    # Gain a combo stack for every bow hit granting +3 Strength. Max (Pet lvl * 0.1) stacks, stacks disappear after 8 seconds. (Rare) (0.2 on Epic, Legendary)
    if player.weapon.type == 'bow' and (pet.rarity == 'legendary' or pet.rarity == 'epic'):
        stats['multiplier']

        

def spider(player, stats, pet):
    # Gain (Pet lvl * 0.1) strength for every nearby spider (Max 10). (All)
    pass


def rock(player, stats, pet):
    # While sitting on your rock, gain (Pet lvl * 0.3%) more damage. (Legendary)
    pass


def golem(player, stats, pet):
    # While less than 15% HP, deal (Pet lvl * 0.3%) more damage. (All)
    pass


def flyingfish(player, stats, pet):
    # Gives (Pet lvl * 0.4) strength when near water. (Rare) (0.5 on Epic, Legendary)
    # Increases the stats of Diver's Armor by (Pet lvl * 0.3%). (Legendary)
    pass


def magmacube(player, stats, pet):
    # Deal (Pet lvl * 0.25%) more damage to slimes. (Rare, Epic, Legendary)
    # Buffs the stats of Ember Armor by (Pet lvl * 1%). (Legendary)
    pass

def jerry(player, stats, pet):
    if pet.rarity == 'legendary' and player.weapon == 'ASPECT_OF_THE_JERRY':
        stats['weapon damage'] += int(pet.level * 0.1)



# endregion


# region Pet dictionaries


pet_stats = {
    'SKELETON_HORSE': {
        'name': 'Skeleton Horse',
        'stats': {
            'intelligence': lambda lvl: lvl,
            'speed': lambda lvl: lvl // 2
        },
        'type': 'combat',
        'icon': '/head/47effce35132c86ff72bcae77dfbb1d22587e94df3cbc2570ed17cf8973a'
    },
    'SNOWMAN': {
        'name': 'Snowman',
        'stats': {
            'damage': lambda lvl: lvl // 4,
            'strength': lambda lvl: lvl // 4,
            'crit damage': lambda lvl: lvl // 4
        },
        'type': 'combat',
        'icon': '/head/11136616d8c4a87a54ce78a97b551610c2b2c8f6d410bc38b858f974b113b208'
    },
    'BAT': {
        'name': 'Bat',
        'stats': {
            'intelligence': lambda lvl: lvl,
            'speed': lambda lvl: lvl // 20
        },
        'type': 'mining',
        'icon': '/head/382fc3f71b41769376a9e92fe3adbaac3772b999b219c9d6b4680ba9983e527'
    },
    'SHEEP': {
        'name': 'Sheep',
        'stats': {
            'intelligence': lambda lvl: lvl,
            'ability damage': lambda lvl: lvl // 2,
        },
        # Increases your total  Mana by (Pet lvl * 0.25%) while in dungeons. (Legendary)
        'ability': sheep,
        'type': 'alchemy',
        'icon': '/head/64e22a46047d272e89a1cfa13e9734b7e12827e235c2012c1a95962874da0'
    },
    'CHICKEN': {
        'name': 'Chicken',
        'stats': {
            'health': lambda lvl: lvl * 2
        },
        'type': 'farming',
        'icon': '/head/7f37d524c3eed171ce149887ea1dee4ed399904727d521865688ece3bac75e'
    },
    'WITHER_SKELETON': {
        'name': 'Wither Skeleton',
        'stats': {
            'strength': lambda lvl: lvl // 4,
            'crit chance': lambda lvl: lvl // 20,
            'crit damage': lambda lvl: lvl // 4,
            'defense': lambda lvl: lvl // 4,
            'intelligence': lambda lvl: lvl // 4
        },
        # Deal (Pet lvl * 0.5%) more damage against wither mobs. (All)
        # Upon hitting an enemy inflict the wither effect for (Pet lvl * 2%) damage over 3 seconds (No stack). (Legendary)
        'ability': witherskeleton,
        'type': 'combat',
        'icon': '/head/f5ec964645a8efac76be2f160d7c9956362f32b6517390c59c3085034f050cff'
    },
    'SILVERFISH': {
        'name': 'Silverfish',
        'stats': {
            'defense': lambda lvl: lvl,
            'health': lambda lvl: lvl // 5,
        },
        'type': 'mining',
        'icon': '/head/da91dab8391af5fda54acd2c0b18fbd819b865e1a8f1d623813fa761e924540'
    },
    'RABBIT': {
        'name': 'Rabbit',
        'stats': {
            'health': lambda lvl: lvl,
            'speed': lambda lvl: lvl // 5
        },
        'type': 'farming',
        'icon': '/head/117bffc1972acd7f3b4a8f43b5b6c7534695b8fd62677e0306b2831574b'
    },
    'HORSE': {
        'name': 'Horse',
        'stats': {
            'intelligence': lambda lvl: lvl // 2,
            'speed': lambda lvl: lvl // 4
        },
        # While riding your horse, gain (Pet lvl * 0.25%) bow damage. (Legendary)
        'ability': horse,
        'type': 'combat',
        'icon': '/head/36fcd3ec3bc84bafb4123ea479471f9d2f42d8fb9c5f11cf5f4e0d93226'
    },
    'PIGMAN': {
        'name': 'Pigman',
        'stats': {
            'strength': lambda lvl: lvl // 2,
            'defense': lambda lvl: lvl // 2
        },
        # Buffs the Pigman sword by (Pet lvl * 0.4) damage and (Pet lvl * 0.25) strength. (All)
        # Deal (Pet lvl * 0.2%) extra damage to monsters level 100 and up. (Legendary)
        'ability': pigman,
        'type': 'combat',
        'icon': '/head/63d9cb6513f2072e5d4e426d70a5557bc398554c880d4e7b7ec8ef4945eb02f2'
    },
    'WOLF': {
        'name': 'Wolf',
        'stats': {
            'crit damage': lambda lvl: lvl // 10,
            'true defense': lambda lvl: lvl // 10,
            'speed': lambda lvl: lvl // 5,
            'health': lambda lvl: lvl // 2
        },
        # Gain (Pet lvl * 0.1%) crit damage for every nearby wolf (max 10). (Rare) (0.15% for Epic, Legendary)
        'ability': wolf,
        'type': 'combat',
        'icon': '/head/dc3dd984bb659849bd52994046964c22725f717e986b12d548fd169367d494'
    },
    'OCELOT': {
        'name': 'Ocelot',
        'stats': {
            'speed': lambda lvl: lvl // 2
        },
        'type': 'foraging',
        'icon': '/head/5657cd5c2989ff97570fec4ddcdc6926a68a3393250c1be1f0b114a1db1'
    },
    'LION': {
        'name': 'Lion',
        'stats': {
            'strength': lambda lvl: lvl // 2,
            'speed': lambda lvl: lvl // 4
        },
        # Adds (Pet lvl * 0.03) damage to your weapons. (Common) (0.05 on Uncommon) (0.1 on Rare) (0.15 on Epic) (0.2 on Legendary)
        # Increases damage dealt by (Pet lvl * 0.3%) on your first hit on a mob. (Rare) (0.4% on Epic) (0.5% on Legendary)
        # Deal (Pet lvl * 0.3%) weapon damage against mobs below level 80. (Legendary)
        'ability': lion,
        'type': 'foraging',
        'icon': '/head/38ff473bd52b4db2c06f1ac87fe1367bce7574fac330ffac7956229f82efba1'
    },
    'ENDER_DRAGON': {
        'name': 'Dragon',
        'stats': {
            'strength': lambda lvl: lvl // 2,
            'crit chance': lambda lvl: lvl // 10,
            'crit damage': lambda lvl: lvl // 2
        },
        # Deal (Pet lvl * 0.25%) more damage to end mobs. (All)
        # Buffs the Aspect of the Dragon sword by (Pet lvl * 0.5) damage and (Pet lvl * 0.3) strength. (All)
        # Increases all stats by (Pet lvl * 0.1%). (Legendary)
        'ability': enderdragon,
        'type': 'combat',
        'icon': '/head/aec3ff563290b13ff3bcc36898af7eaa988b6cc18dc254147f58374afe9b21b9'
    },
    'GUARDIAN': {
        'name': 'Guardian',
        'stats': {
            'intelligence': lambda lvl: lvl,
            'defense': lambda lvl: lvl // 2
        },
        'type': 'fishing',
        'icon': '/head/221025434045bda7025b3e514b316a4b770c6faa4ba9adb4be3809526db77f9d'
    },
    'ENDERMAN': {
        'name': 'Enderman',
        'stats': {
            'crit damage': lambda lvl: lvl * 0.75
        },
        'type': 'combat',
        'icon': '/head/6eab75eaa5c9f2c43a0d23cfdce35f4df632e9815001850377385f7b2f039ce1'
    },
    'BLUE_WHALE': {
        'name': 'Whale',
        'stats': {
            'health': lambda lvl: lvl * 2
        },
        'type': 'fishing',
        'icon': '/head/dab779bbccc849f88273d844e8ca2f3a67a1699cb216c0a11b44326ce2cc20'
    },
    'GIRAFFE': {
        'name': 'Giraffe',
        'stats': {
            'health': lambda lvl: lvl,
            'crit chance': lambda lvl: lvl // 20
        },
        # Grants (Pet lvl * 0.4) strength and (20 + (Pet lvl * 0.1)) crit damage when mid air. (Rare)
        # ((Pet lvl * 0.5) strength and (20 + (Pet lvl * 0.25)) crit damage on Epic)
        # ((Pet lvl * 0.5) strength and (20 + (Pet lvl * 0.4)) crit damage on Legendary)
        'ability': giraffe,
        'type': 'foraging',
        'icon': '/head/6eab75eaa5c9f2c43a0d23cfdce35f4df632e9815001850377385f7b2f039ce1'
    },
    'PHOENIX': {
        'name': 'Phoenix',
        'stats': {
            'strength': lambda lvl: (lvl // 2) + 10,
            'intelligence': lambda lvl: lvl + 50
        },
        # Before death, become immune and gain (10 + (Pet lvl * 0.1)) strength on (2 + (Pet lvl * 0.02)) seconds (3 minutes cooldown). (Epic)
        # ((10 + (Pet lvl * 0.2) STR on (2 + (Pet lvl * 0.02)) seconds on Legendary)
        # On 4th melee strike, ignite mobs, dealing (1 + (Pet lvl * 0.14)) your crit damage each second for (2 + (Pet lvl/25)) seconds. (Epic, Legendary)
        'ability': phoenix,
        'type': 'combat',
        'icon': '/head/23aaf7b1a778949696cb99d4f04ad1aa518ceee256c72e5ed65bfa5c2d88d9e'
    },
    'BEE': {
        'name': 'Bee',
        'stats': {
            'intelligence': lambda lvl: lvl // 2,
            'strength': lambda lvl: (lvl // 4) + 5,
            'speed': lambda lvl: lvl // 10,
        },
        # Gain (1 + (Pet lvl * 0.02)) Intelligence and (1 + (Pet lvl * 0.02)) Strength for each nearby bee. (Max 15) (Common)
        # (1+ (Pet lvl * 0.09) INT and (1 + (Pet lvl * 0.07)) STR on Rare)
        # (1+ (Pet lvl * 0.14) INT and (1 + (Pet lvl * 0.11)) STR on Epic)
        # (1+ (Pet lvl * 0.19) INT and (1 + (Pet lvl * 0.14)) STR on Legendary)
        'ability': bee,
        'type': 'farming',
        'icon': '/head/7e941987e825a24ea7baafab9819344b6c247c75c54a691987cd296bc163c263'
    },
    'MAGMA_CUBE': {
        'name': 'Magma Cube',
        'stats': {
            'strength': lambda lvl: lvl // 5,
            'defense': lambda lvl: lvl // 3,
            'health': lambda lvl: lvl // 2
        },
        # Deal (Pet lvl * 0.25%) more damage to slimes. (Rare, Epic, Legendary)
        # Buffs the stats of Ember Armor by (Pet lvl * 1%). (Legendary)
        'ability': magmacube,
        'type': 'combat',
        'icon': '/head/38957d5023c937c4c41aa2412d43410bda23cf79a9f6ab36b76fef2d7c429'
    },
    'FLYING_FISH': {
        'name': 'Flying Fish',
        'stats': {
            'strength': lambda lvl: lvl // 2,
            'defense': lambda lvl: lvl // 2
        },
        # Gives (Pet lvl * 0.4) strength when near water. (Rare) (0.5 on Epic, Legendary)
        # Increases the stats of Diver's Armor by (Pet lvl * 0.3%). (Legendary)
        'ability': flyingfish,
        'type': 'fishing',
        'icon': '/head/40cd71fbbbbb66c7baf7881f415c64fa84f6504958a57ccdb8589252647ea'
    },
    'SQUID': {
        'name': 'Squid',
        'stats': {
            'intelligence': lambda lvl: lvl // 2,
            'health': lambda lvl: lvl // 2
        },
        # Buffs the Ink Wand by (Pet lvl * 0.3) damage and (Pet lvl * 0.1) strength. (Rare) (0.4 DMG and 0.2 STR on Epic, Legendary)
        'ability': squid,
        'type': 'fishing',
        'icon': '/head/01433be242366af126da434b8735df1eb5b3cb2cede39145974e9c483607bac'
    },
    'PARROT': {
        'name': 'Parrot',
        'stats': {
            'crit damage': lambda lvl: lvl // 10,
            'intelligence': lambda lvl: lvl
        },
        # Gives (5 + (Pet lvl * 0.25)) strength to players within 20 Blocks (No stack). (Legendary)
        'ability': parrot,
        'type': 'alchemy',
        'icon': '/head/5df4b3401a4d06ad66ac8b5c4d189618ae617f9c143071c8ac39a563cf4e4208'
    },
    'TIGER': {
        'name': 'Tiger',
        'stats': {
            'strength': lambda lvl: (lvl // 10) + 5,
            'crit chance': lambda lvl: lvl // 20,
            'crit damage': lambda lvl: lvl // 2
        },
        # Attacks have a (Pet lvl * 0.05%) chance to strike twice. (Common) (0.1% on Uncommon, Rare) (0.2% on Epic, Legendary)
        # Deal (Pet lvl * 0.2%) more damage against targets with no other mobs within 15 blocks. (Legendary)
        'ability': tiger,
        'type': 'combat',
        'icon': '/head/fc42638744922b5fcf62cd9bf27eeab91b2e72d6c70e86cc5aa3883993e9d84'
    },
    'TURTLE': {
        'name': 'Turtle',
        'stats': {
            'health': lambda lvl: lvl // 2,
            'defense': lambda lvl: lvl
        },
        'type': 'combat',
        'icon': '/head/212b58c841b394863dbcc54de1c2ad2648af8f03e648988c1f9cef0bc20ee23c'
    },
    'BLAZE': {
        'name': 'Blaze',
        'stats': {
            'intelligence': lambda lvl: lvl,
            'defense': lambda lvl: (lvl // 5) + 10
        },
        # Upgrades Blaze Armor stats and ability by (Pet lvl * 0.4%). (All)
        # Double effects of Hot Potato Books. (Legendary)
        'ability': blaze,
        'type': 'combat',
        'icon': '/head/b78ef2e4cf2c41a2d14bfde9caff10219f5b1bf5b35a49eb51c6467882cb5f0'
    },
    'JERRY': {
        'name': 'Jerry',
        'stats': {
            'intelligence': lambda lvl: -lvl
        },
        'type': 'combat',
        'icon': '/head/822d8e751c8f2fd4c8942c44bdb2f5ca4d8ae8e575ed3eb34c18a86e93b'
    },
    'ZOMBIE': {
        'name': 'Zombie',
        'stats': {
            'crit damage': lambda lvl: lvl * 0.3,
            'health': lambda lvl: lvl
        },
        # Deal (Pet lvl * 0.2%) more damage to zombies. (Epic, Legendary)
        'ability': zombie,
        'type': 'combat',
        'icon': '/head/822d8e751c8f2fd4c8942c44bdb2f5ca4d8ae8e575ed3eb34c18a86e93b'
    },
    'DOLPHIN': {
        'name': 'Dolphin',
        'stats': {
            'intelligence': lambda lvl: lvl,
            'sea creature chance': lambda lvl: lvl // 20
        },
        'type': 'fishing',
        'icon': '/head/6271bda308834d738faf194677090bc3'
    },
    'JELLYFISH': {
        'name': 'Jellyfish',
        'stats': {
            'health': lambda lvl: lvl * 2
        },
        'type': 'alchemy',
        'icon': '/head/913f086ccb56323f238ba3489ff2a1a34c0fdceeafc483acff0e5488cfd6c2f1'
    },
    'ELEPHANT': {
        'name': 'Elephant',
        'stats': {
            'health': lambda lvl: lvl,
            'intelligence': lambda lvl: lvl * 0.75
        },
        'type': 'farming',
        'icon': '/head/7071a76f669db5ed6d32b48bb2dba55d5317d7f45225cb3267ec435cfa514'
    },
    'MONKEY': {
        'name': 'Monkey',
        'stats': {
            'speed': lambda lvl: lvl // 5,
            'intelligence': lambda lvl: lvl // 2
        },
        'type': 'foraging',
        'icon': '/head/57ba53654c79265623b0aac6d2c611fe861b7fa22b392ef43674c11d8c8214c'
    },
    'SKELETON': {
        'name': 'Skeleton',
        'stats': {
            'crit chance': lambda lvl: lvl * 0.15,
            'crit damage': lambda lvl: lvl * 0.3
        },
        # Increase arrow damage by (Pet lvl * 0.1%), which is tripled while in dungeons. (Common, Uncommon, Rare) (0.2% on Epic, Legendary)
        # Gain a combo stack for every bow hit granting +3 Strength. Max (Pet lvl * 0.1) stacks, stacks disappear after 8 seconds. (Rare) (0.2 on Epic, Legendary)
        'ability': skeleton,
        'type': 'combat',
        'icon': '/head/301268e9c492da1f0d88271cb492a4b302395f515a7bbf77f4a20b95fc02eb2'
    },
    'SPIDER': {
        'name': 'Spider',
        'stats': {
            'strength': lambda lvl: lvl // 10,
            'crit chance': lambda lvl: lvl // 10
        },
        # Gain (Pet lvl * 0.1) strength for every nearby spider (Max 10). (All)
        'ability': spider,
        'type': 'combat',
        'icon': '/head/cd541541daaff50896cd258bdbdd4cf80c3ba816735726078bfe393927e57f1'
    },
    'ENDERMITE': {
        'name': 'Endermite',
        'stats': {
            'intelligence': lambda lvl: lvl
        },
        'type': 'mining',
        'icon': '/head/5a1a0831aa03afb4212adcbb24e5dfaa7f476a1173fce259ef75a85855'
    },
    'PIG': {
        'name': 'Pig',
        'stats': {
            'speed': lambda lvl: lvl // 4
        },
        'type': 'farming',
        'icon': '/head/621668ef7cb79dd9c22ce3d1f3f4cb6e2559893b6df4a469514e667c16aa4'
    },
    'ROCK': {
        'name': 'Rock',
        'stats': {
            'defense': lambda lvl: lvl * 2,
            'true defense': lambda lvl: lvl // 10
        },
        # While sitting on your rock, gain (Pet lvl * 0.3%) more damage. (Legendary)
        'ability': rock,
        'type': 'mining',
        'icon': '/head/ca979f76633f5dda89496511716948e9d7b8592f6e1e480c5de1c83238d3e32'
    },
    'HOUND': {
        'name': 'Hound',
        'stats': {
            'strength': lambda lvl: lvl * 0.4
        },
        'type': 'combat',
        'icon': '/head/b7c8bef6beb77e29af8627ecdc38d86aa2fea7ccd163dc73c00f9f258f9a1457'
    },
    'GHOUL': {
        'name': 'Ghoul',
        'stats': {
            'health': lambda lvl: lvl,
            'intelligence': lambda lvl: lvl * 0.7
        },
        'type': 'combat',
        'icon': ''
    },
    'TARANTULA': {
        'name': 'Tarantula',
        'stats': {
            'strength': lambda lvl: lvl // 10,
            'crit chance': lambda lvl: lvl // 10,
            'crit damage': lambda lvl: lvl * 0.3
        },
        'type': 'combat',
        'icon': '/head/8300986ed0a04ea79904f6ae53f49ed3a0ff5b1df62bba622ecbd3777f156df8'
    },
    'GOLEM': {
        'name': 'Golem',
        'stats': {
            'strength': lambda lvl: lvl // 2,
            'health': lambda lvl: lvl * 1.5
        },
        # While less than 15% HP, deal (Pet lvl * 0.3%) more damage. (All)
        'ability': golem,
        'type': 'combat',
        'icon': '/head/89091d79ea0f59ef7ef94d7bba6e5f17f2f7d4572c44f90f76c4819a714'
    },
    'BLACK_CAT': {
        'name': 'Black Cat',
        'stats': {
            'intelligence': lambda lvl: lvl,
            'speed': lambda lvl: lvl // 4
        },
        'type': 'combat',
        'icon': '/head/e4b45cbaa19fe3d68c856cd3846c03b5f59de81a480eec921ab4fa3cd81317'
    }
}


# endregion
