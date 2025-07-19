"""
Image metadata storage for the gallery application.
Contains detailed information about each image including title, type, text box content, artist, colors, and regions.
"""

# Token mapping - maps card filenames to their associated token files
TOKEN_MAPPING = {
    'Anivia Cryophoenix.png': ['Anivia_token.png'],
    'Annie Dark Child.png': ['Annie_token.png'],
    'Azir Emperor of Shurima.png': ['Azir_token.png', 'Azir_token2.png'],
    'Elise the Spider Queen.png': ['Elise_token.png'],
    'Gangplank Saltwater Scourge.png': ['Gangplank_barrel.png'],
    'Kayn Shadow Reaper.png': ['Kayn_token.png'],
    'Kled Cantankerous Cavalier.png': ['Kled_token.png'],
    'Shen Eye of Twilight.png': ['Shen_token.png'],
    'Viktor Herald of Arcane.png': ['Viktor_token.png'],
    'Zed Master of Shadows.png': ['Zed_token.png']
}

# Token metadata - detailed information about each token
TOKEN_METADATA = {
    'Anivia_token.png': {
        'title': 'Wall Token',
        'type': 'Token Creature - Wall',
        'text_box': 'Defender\n(This creature can\'t attack.)'
    },
    'Annie_token.png': {
        'title': 'Tibbers',
        'type': 'Legendary Token Creature - Demon Bear',
        'text_box': 'Haste\n(This creature can attack and tap as soon as it comes under your control.)'
    },
    'Azir_token.png': {
        'title': 'Sand Soldier Token',
        'type': 'Token Creature - Soldier',
        'text_box': 'Vigilance, Haste\nSand Soldier tokens you control get +1/+1 for each Desert you control.'
    },
    'Azir_token2.png': {
        'title': 'Disc of the Sun',
        'type': 'Legendary Token Artifact Creature',
        'text_box': 'Defender\nSand Soldier tokens you control get +1/+1 for each Desert you control.'
    },
    'Elise_token.png': {
        'title': 'Spider Token',
        'type': 'Token Creature - Spider',
        'text_box': 'Menace.'
    },
    'Gangplank_barrel.png': {
        'title': 'Barrel Token',
        'type': 'Token Artifact Creature - Barrel',
        'text_box': 'This creature can\'t attack or block.\nThis creature gets +1/+0 for each other Barrel you control.'
    },
    'Kayn_token.png': {
        'title': 'Rhaast',
        'type': 'Legendary Token Creature - Demon',
        'text_box': 'Lifelink, Menace\n(Damage dealt by this creature also causes you to gain that much life. This creature can\'t be blocked except by two or more creatures.)'
    },
    'Kled_token.png': {
        'title': 'Skaarl',
        'type': 'Legendary Token Creature - Lizard Mount',
        'text_box': """Haste
                \nSaddle 2
                \nWhenever this creature attacks, if it was saddled by Kled, you may have target creature block Skaarl this turn."""
    },
    'Shen_token.png': {
        'title': 'Spirit Blade',
        'type': 'Legendary Token Equipment Artifact',
        'text_box': 'Equipped creature gets +1/+2.\nEquip 2 (2: Attach to target creature you control. Equip only as a sorcery.)'
    },
    'Viktor_token.png': {
        'title': 'Construct Token',
        'type': 'Token Artifact Creature - Construct',
        'text_box': 'Artifact creature tokens you control get +1/+1 counters when Viktor\'s ability resolves.'
    },
    'Zed_token.png': {
        'title': 'Shadow Clone Token',
        'type': 'Token Creature - Human Ninja',
        'text_box': 'Haste\nExile this token at the end of combat.'
    }
}

IMAGE_METADATA = {
    'Aatrox Darkin Blade.png': {
        'title': 'Aatrox, Darkin Blade',
        'type': 'Legendary Creature - God Warrior',
        'text_box':"""Double strike
                \nWhenever Aatrox attacks, it deals damage equal to its power to any target.
                \nWorld Ender —  XBBRR: Aatrox gains +X/+X, lifelink and flying until end of turn. X can’t be zero.
                """,
        'artist': 'Rolando D Tate',
        'color': ['Red', 'Black'],
        'region': ['Runeterra']
    },
    'Ahri Nine-Tailed Fox.png': {
        'title': 'Ahri, Nine-Tailed Fox',
        'type': 'Legendary Creature - Human Fox Wizard',
        'text_box': """Prowess
                \nCharm — 2R: Goad target creature an opponent controls. 
                \nOrb of Deception — T: Ahri deals damage equal to its power to any target. If that target is goaded, it deals double damage instead.""",
        'artist': 'Oreki Genya',
        'color': ['Blue', 'White', 'Red'],
        'region': ['Ionia']
    },
    'Akali Rogue Assassin.png': {
        'title': 'Akali, Rogue Assassin',
        'type': 'Legendary Creature - Human Assassin',
        'text_box': """Deathtouch
                \nTwilight Shroud — Whenever Akali deals combat damage to a player, untap it, then it phases out until the beginning of your next combat phase.""",
        'artist': 'Sun Haiyang',
        'color': ['Black'],
        'region': ['Ionia']
    },
    'Akshan Rogue Sentinel.png': {
        'title': 'Akshan, Rogue Sentinel',
        'type': 'Legendary Creature - Human Rogue',
        'text_box': """Reach, vigilance
                \nWhenever a creature you control dies, put a Scoundrel counter on target creature an opponent controls.
                \nWhenever a creature with a Scoundrel counter on it dies, return target creature card from your graveyard to the battlefield tapped.""",
        'artist': 'Kudos Productions',
        'color': ['White', 'Black'],
        'region': ['Shurima']
    },
    'Alistar the Minotaur.png': {
        'title': 'Alistar, the Minotaur',
        'type': 'Legendary Creature - Minotaur Warrior',
        'text_box': """Headbutt — T: Alistar fights target creature an opponent controls.
                \nUnbreakable Will — 3RG: Remove all all damage from Alistar. Untap it. It gains +X/+X until end of turn, where X is the greatest power among creatures your opponents control.""",
        'artist': 'YY6242',
        'color': ['Green', 'Red'],
        'region': ['Runeterra']
    },
    'Ambessa Matriarch of War.png': {
        'title': 'Ambessa, Matriarch of War',
        'type': 'Legendary Creature - Human Warrior',
        'text_box': """At the beginning of each end step, if you didn’t lose life this turn, you get a legacy counter.
                \nCreatures you control get +1/+0 for each legacy counter you have.
                \nWhenever one or more creatures deal combat damage to you, remove all legacy counters.""",
        'artist': 'Latter-Sleep-7221',
        'color': ['Red', 'White', 'Black'],
        'region': ['Noxus']
    },
    'Amumu the Sad Mummy.png': {
        'title': 'Amumu, the Sad Mummy',
        'type': 'Legendary Creature - Spirit',
        'text_box': """Deathtouch
                \nAt the beginning of your upkeep, sacrifice either Amumu or each other creature you control.
                \nWhenever a creature dies, put a +1/+1 counter on Amumu.""",
        'artist': 'Pawl Marchwicki',
        'color': ['Black'],
        'region': ['Shurima']
    },
    'Anivia Cryophoenix.png': {
        'title': 'Anivia, Cryophoenix // Egg of Rebirth',
        'type': 'Legendary Creature - Bird Spirit',
        'text_box': """Flying
                \nWhenever you cast a noncreature spell with mana value 4 or greater, create a 0/5 blue Wall creature token with defender.
                \nWhen Anivia dies, exile it, then return it to the battlefield transformed under its owner’s control.""",
        'artist': 'SixMoreVodka',
        'color': ['Blue', 'White'],
        'region': ['The Freljord'],
        'flippable': True
    },
    'Annie Dark Child.png': {
        'title': 'Annie, Dark Child',
        'type': 'Legendary Creature - Human Warlock',
        'text_box': """Whenever you cast or copy an instant or sorcery spell, Annie deals 1 damage to any target. If this is the fourth time this ability has resolved this turn, put a stun counter on each creature target opponent controls and create Tibbers, a legendary 6/6 red Demon Bear creature token with haste.""",
        'artist': 'Arifwijaya',
        'color': ['Red', 'Black', 'Blue'],
        'region': ['Noxus']
    },
    'Aphelios Weapon of Faith.png': {
        'title': 'Aphelios, Weapon of Faith',
        'type': 'Legendary Creature - Human Ranger',
        'text_box': """At the beginning of your upkeep, choose two:
                \n• Aphelios gains reach until your next turn.
                \n• Aphelios gains lifelink until your next turn.
                \n• Put a stun counter on target creature.
                \n• Aphelios deals 1 damage to up to three targets.
                \n• Create a 1/1 colorless Turret artifact creature token.""",
        'artist': 'coax콕스',
        'color': ['White', 'Blue', 'Black'],
        'region': ['Targon']
    },
    'Ashe Frost Archer.png': {
        'title': 'Ashe, Frost Archer',
        'type': 'Legendary Creature - Human Archer',
        'text_box': """T: Ashe deals 1 damage to target creature. Tap that creature.
                \n1WU, T: Ashe deals 1 damage to up to 3 target creatures. Tap those creatures.
                \n4WU, T: Ashe deals 6 damage to target player. Put a stun counter on each creature that player controls.""",
        'artist': 'Kat Chan',
        'color': ['Blue', 'White'],
        'region': ['The Freljord']
    },
    'Aurelion Sol.png': {
        'title': 'Aurelion Sol',
        'type': 'Legendary Enchantment Creature - God',
        'text_box': """Flying, Ward 3
                \nAt the beginning of your end step, if Aurelion Sol is untapped, put a charge counter on it.
                \nWhenever Aurelion Sol attacks, it gets +X/+X and deals X damage to each opponent where X is twice the number of charge counters on it.""",
        'artist': 'AlpariArt',
        'color': ['Blue', 'Black', 'Red', 'White'],
        'region': ['Targon']
    },
    'Aurora Witch Between Worlds.png': {
        'title': 'Aurora, Witch Between Worlds',
        'type': 'Legendary Creature - Human Bunny Wizard',
        'text_box': """Whenever Aurora or another creature you control enters the battlefield from exile, draw a card.
                \nBetween Worlds — 4UU, T: Exile Aurora and target creature an opponent controls. Return Aurora to the battlefield at the beginning of your next end step.""",
        'artist': 'Dao Trong Le ',
        'color': ['Blue'],
        'region': ['The Freljord']
    },
    'Azir Emperor of Shurima.png': {
        'title': 'Azir, Emperor of Shurima',
        'type': 'Legendary Creature - Bird Wizard',
        'text_box': """Landfall — Whenever a land enters the battlefield under your control, create a 2/1 red and white Sand Soldier creature token with vigilance and haste.
                \n4RR, T: Create Disc of the Sun, a legendary 4/4 colorless artifact creature token with defender and “Sand Soldier tokens you control get +1/+1 for each Desert you control.”""",
        'artist': 'Ignatius Budi',
        'color': ['White', 'Green', 'Red'],
        'region': ['Shurima']
    },
    'Bard Wandering Caretaker.png': {
        'title': 'Bard, Wandering Caretaker',
        'type': 'Legendary Creature - Spirit God',
        'text_box': """At the beginning of each player’s upkeep, you may have that player gain 2 life.
                \nTempered Fate — WW, T: Target creature phases out. If its controller has gained life this turn, draw a card. (Treat it and anything attached to it as though they don’t exist until its controller’s next turn.)""",
        'artist': 'Ewlina Bielska',
        'color': ['White'],
        'region': ['Runeterra']
    },
    'BelVeth Void Empress.png': {
        'title': "Bel'Veth, Void Empress",
        'type': 'Legendary Creature - Alien Noble',
        'text_box': """""",
        'artist': 'L.K. Rico',
        'color': ['Black', 'Blue'],
        'region': ['The Void']
    },
    'Blitzcrank Steam Golem.png': {
        'title': 'Blitzcrank, Steam Golem',
        'type': 'Legendary Artifact Creature - Golem',
        'text_box': """""",
        'artist': 'Augie Pagan',
        'color': [],
        'region': ['Zaun']
    },
    'Brand Burning Vengeance.png': {
        'title': 'Brand, Burning Vengeance',
        'type': 'Legendary Creature - Human Wizard',
        'text_box': """""",
        'artist': 'Chobysan',
        'color': ['Red'],
        'region': ['Runeterra']
    },
    'Braum Heart of the Freljord.png': {
        'title': 'Braum, Heart of the Freljord',
        'type': 'Legendary Creature - Human Soldier',
        'text_box': """Defender""",
        'artist': 'Elizaveta Ermoshina',
        'color': ['Blue', 'White'],
        'region': ['The Freljord']
    },
    'Briar Restrained Hunger.png': {
        'title': 'Briar, Restrained Hunger',
        'type': 'Legendary Creature - Horror Berserker',
        'text_box': """Haste, double strike
                \nBlood Frenzy— As long as you don’t control a Blood token, Briar attacks or blocks each combat if able.
                \nSnack Attack — Whenever Briar deals combat damage to a player, create a Blood token.
                \nWhenever you sacrifice a Blood token, Briar gets +1/+1 until end of turn.""",
        'artist': 'Thai Thanh',
        'color': ['Black', 'Red'],
        'region': ['Noxus']
    },
    'Caitlyn Piltover Sheriff.png': {
        'title': 'Caitlyn, Piltover Sheriff',
        'type': 'Legendary Creature - Human Detective',
        'text_box': """""",
        'artist': 'SixMoreVodka',
        'color': ['White'],
        'region': ['Piltover']
    },
    'Camille Steel Shadow.png': {
        'title': 'Camille, Steel Shadow',
        'type': 'Legendary Artifact Creature - ',
        'text_box': """""",
        'artist': 'ArcNoir',
        'color': [],
        'region': ['Piltover']
    },
    'Cassiopeia Serpents Embrace.png': {
        'title': 'Cassiopeia, Serpent’s Embrace',
        'type': 'Legendary Creature - Gorgon Wizard',
        'text_box': """Infect
                \nPetrifying Gaze — When Cassiopeia enters, destroy each tapped creature your opponents control.
                \nTwin Fang — Whenever a creature an opponent controls becomes tapped, Cassiopeia deals 1 damage to up to two targets. This triggers only once each turn.""",
        'artist': 'Blake Byun',
        'color': ['Green', 'Black', 'White'],
        'region': ['Noxus']
    },
    'ChoGath Terror of the Void.png': {
        'title': 'Cho’Gath, Terror of the Void',
        'type': 'Legendary Creature - Beast Horror',
        'text_box': """""",
        'artist': 'Qiang Zhou',
        'color': ['Black', 'Red', 'Green'],
        'region': ['The Void']
    },
    'Corki Daring Bombardier.png': {
        'title': 'Corki, Daring Bombardier',
        'type': 'Legendary Creature - Yordle Pilot',
        'text_box': """""",
        'artist': 'Forrest Imel',
        'color': ['Red'],
        'region': ['Bandle City']
    },
    'Darius Hand of Noxus.png': {
        'title': 'Darius, Hand of Noxus',
        'type': 'Legendary Creature - Human Warrior',
        'text_box': """""",
        'artist': 'Darius, Hand of Noxus',
        'color': ['Red'],
        'region': ['Noxus']
    },
    'Diana Scorn of the Moon.png': {
        'title': 'Diana, Scorn of the Moon',
        'type': 'Legendary Creature - Human',
        'text_box': """""",
        'artist': 'Ben Shaw',
        'color': ['Black', 'White'],
        'region': ['Targon']
    },
    'Dr. Mundo.png': {
        'title': 'Dr. Mundo',
        'type': 'Legendary Creature - Mutant',
        'text_box': """""",
        'artist': '神说要有光_L',
        'color': ['Green', 'Black', 'Blue'],
        'region': ['Zaun']
    },
    'Draven Glorious Executioner.png': {
        'title': 'Draven, Glorious Executioner',
        'type': 'Legendary Creature - Human Ranger',
        'text_box': """""",
        'artist': 'ArcNoir',
        'color': ['Red'],
        'region': ['Noxus']
    },
    'Ekko Who Shattered Time.png': {
        'title': 'Ekko, Who Shattered Time',
        'type': 'Legendary Creature - Human Artificer',
        'text_box': """Flash
                \nChronobreak — When Ekko enters, your life total becomes equal to what it was at the beginning of the turn.
                \n3U, T: Return Ekko to its owner’s hand.""",
        'artist': 'Blake Byun',
        'color': ['Green', 'Blue'],
        'region': ['Zaun']
    },
    'Elise the Spider Queen.png': {
        'title': 'Elise, the Spider Queen // Elise, Spider Form',
        'type': 'Legendary Creature - Human Spider',
        'text_box': """Whenever you deal noncombat damage to an opponent, put a Spiderling counter on Elise. 
                \nSpider Form — 1BR: Transform Elise. Activate only as a sorcery.
                \n\nWhen this creature transforms into Elise, Spider Form, remove all Spiderling counters from it and create that many 1/1 black Spider creature tokens with menace.
                \nSpiders you control have haste.
                \nHuman Form — B: Transform Elise. Activate only as a sorcery.""",
        'artist': 'Qimang2 and SixMoreVodka',
        'color': ['Black'],
        'region': ['Noxus'],
        'flippable': True
    },
    'Evelynn Agonys Embrace.png': {
        'title': 'Evelynn, Agonys Embrace',
        'type': 'Legendary Creature - Demon Assassin',
        'text_box': """Shroud, deathtouch
                \nAllure — T: Choose target opponent. Until the end of your next turn, that player can’t gain life, and is Marked.
                \nLast Caress — Whenever Eveylnn deals combat damage to a Marked player, if that player has less than one quarter of their starting life total, their life total becomes 0. Then, Evelynn phases out.""",
        'artist': 'Guan Yu',
        'color': ['Black', 'Blue'],
        'region': ['Runeterra'],
    },
    'Ezreal Prodigal Explorer.png': {
        'title': 'Ezreal, Prodigal Explorer',
        'type': 'Legendary Creature - Human Artificer',
        'text_box': """""",
        'artist': '於菟 SpTASIL',
        'color': ['Blue'],
        'region': ['Piltover']
    },
    'Fiddlesticks Ancient Fear.png': {
        'title': 'Fiddlesticks, Ancient Fear',
        'type': 'Legendary Creature - Nightmare Horror',
        'text_box': """""",
        'artist': 'Will Gist',
        'color': ['Black'],
        'region': ['Runeterra']
    },
    'Fiora Grand Duelist.png': {
        'title': 'Fiora, Grand Duelist',
        'type': 'Legendary Creature - Human Noble',
        'text_box': """First strike
                \nMark Vitals — At the beginning of each opponent’s upkeep, choose a creature that player controls at random. Until end of turn, that creature’s base toughness becomes 1.
                \nRiposte — T: Until end of turn, creatures attacking you or planeswalkers you control don’t cause triggered abilities to trigger. Activate only during an opponent’s combat phase, before attackers are declared.""",
        'artist': 'Ilyas Bolatov',
        'color': ['White'],
        'region': ['Demacia'],
    },
    'Fizz the Tidal Trickster.png': {
        'title': 'Fizz, the Tidal Trickster',
        'type': 'Legendary Creature - Fish Assassin',
        'text_box': """""",
        'artist': 'SixMoreVodka',
        'color': ['Blue'],
        'region': ['Runeterra']
    },
    'Galio the Colossus.png': {
        'title': 'Galio the Colossus',
        'type': 'Legendary Artifact Creature - Golem',
        'text_box': """""",
        'artist': 'Will Gist',
        'color': ['White'],
        'region': ['Demacia']
    },
    'Gangplank Saltwater Scourge.png': {
        'title': 'Gangplank, Saltwater Scourge',
        'type': 'Legendary Creature - Human Pirate',
        'text_box': """Whenever you attack, create a 1/1 colorless Barrel artifact creature token with “This creature can’t attack or block” and “This creature gets +1/+0 for each other Barrel you control.”
                \nBARREL! — T: Sacrifice all Barrels you control. Gangplank deals X damage to each opponent, where X is the total power of the sacrificed creatures.""",
        'artist': 'SixMoreVodka',
        'color': ['Red', 'Black', 'White'],
        'region': ['Bilgewater']
    },
    'Garen Might of Demacia.png': {
        'title': 'Garen, Might of Demacia',
        'type': 'Legendary Creature - Human Soldier',
        'text_box': """""",
        'artist': 'SixMoreVodka',
        'color': ['White'],
        'region': ['Demacia']
    },
    'Gnar the Missing Link.png': {
        'title': 'Gnar, the Missing Link // Mega Gnar',
        'type': 'Legendary Creature - Yordle',
        'text_box': """""",
        'artist': 'SixMoreVodka',
        'color': ['Green'],
        'region': ['The Freljord'],
        'flippable': True
    },
    'Gwen Hallowed Seamstress.png': {
        'title': 'Gwen, Hallowed Seamstress',
        'type': 'Legendary Creature - Spirit Doll',
        'text_box': """""",
        'artist': 'Fei Ren',
        'color': ['Black', 'White', 'Blue'],
        'region': ['Shadow Isles']
    },
    'Hecarim Shadow of War.png': {
        'title': 'Hecarim, Shadow of War',
        'type': 'Legendary Creature - Spirit Centaur',
        'text_box': """""",
        'artist': 'CubicSpace',
        'color': ['Black'],
        'region': ['Shadow Isles']
    },
    'Illaoi Kraken Priestess.png': {
        'title': 'Illaoi, Kraken Priestess',
        'type': 'Legendary Creature - Human Juggernaut',
        'text_box': """""",
        'artist': 'Evan Monteiro',
        'color': ['Green'],
        'region': ['Bilgewater']
    },
    'Jhin the Virtuoso.png': {
        'title': 'Jhin, the Virtuoso',
        'type': 'Legendary Creature - Human Assassin',
        'text_box': """Curtain Call — 2BR, T: Jhin deals 1 damage to up to three targets. Then it gains deathtouch until end of turn and deals 1 damage to any target.
                \nWhenever a creature an opponent controls dies after being dealt damage by a creature you control with deathtouch this turn, draw a card.""",
        'artist': 'KLYN007',
        'color': ['Black', 'Red', 'Blue'],
        'region': ['Ionia']
    },
    'Jinx Loose Cannon.png': {
        'title': 'Jinx, Loose Cannon',
        'type': 'Legendary Creature - Human Villain',
        'text_box': """Flame Chompers! — T: Target opponent creates three colorless Chomper artifact tokens with “Creatures you control enter the battlefield tapped” and “T, Sacrifice this artifact: You lose 2 life. Activate this ability only at sorcery speed.”
                \nSuper Mega Death Rocket! — 2BR, T: Jinx deals X damage to target opponent, where X is twice the number of artifacts that player controls.""",
        'artist': 'Yuyu Wong',
        'color': ['Black', 'Red', 'Blue'],
        'region': ['Zaun']
    },
    'KaiSa Daughter of the Void.png': {
        'title': 'Kai\'Sa, Daughter of the Void',
        'type': 'Legendary Creature - Human Ranger',
        'text_box': """Whenever you draw your first card each turn, you may reveal it. If it’s an artifact card, put your choice of a flying counter, hexproof counter, or menace counter on Kai’Sa.""",
        'artist': 'Andi Han',
        'color': ['Blue', 'Black'],
        'region': ['The Void']
    },
    'Kalista Spear of Vengeance.png': {
        'title': 'Kalista, Spear of Vengeance',
        'type': 'Legendary Creature - Spirit Ranger',
        'text_box': """""",
        'artist': 'CubicSpace',
        'color': ['Black', 'White'],
        'region': ['Shadow Isles']
    },
    'Karthus the Deathsinger.png': {
        'title': 'Karthus the Deathsinger',
        'type': 'Legendary Creature - Spirit Wizard',
        'text_box': """""",
        'artist': 'DanRobArt',
        'color': ['Black'],
        'region': ['Shadow Isles']
    },
    'Kayle the Righteous.png': {
        'title': 'Kayle the Righteous',
        'type': 'Legendary Creature - Angel Warrior',
        'text_box': """Flying
                \nLevel up R/W (R/W: Put a level counter on this. Level up only as a sorcery.)
                \nLevel 6- 10 Flying, first strike, vigilance
                \nT: Target creature gains indestructible until end of turn.
                \nLevel 11+ Flying, double strike, vigilance
                \nCreatures you control have indestructible.""",
        'artist': '卡卡也有',
        'color': ['White', 'Red'],
        'region': ['Demacia'],
    },
    'Kayn Shadow Reaper.png': {
        'title': 'Kayn, Shadow Reaper // Kayn, Shadow Assassin',
        'type': 'Legendary Creature - Human Assassin',
        'text_box': """Whenever another creature dies, put a red counter on Kayn. If that creature had flying, put a blue counter on it instead.
                \nRemove four blue counters from Kayn: Transform Kayn.
                \nRemove four red counters from Kayn, Exile Kayn: Create Rhaast, a legendary 6/6 red and black Demon creature token with lifelink and menace.
                \nShadow (This creature can block or be blocked by only creatures with shadow.)
                \nWhenever Kayn deals combat damage to a player, draw a card.""",
        'artist': 'Zuoan',
        'color': ['Black'],
        'region': ['Ionia'],
        'flippable': True
    },
    'Kennen Heart of the Tempest.png': {
        'title': 'Kennen, Heart of the Tempest',
        'type': 'Legendary Creature - Yordle Ninja',
        'text_box': """Ninjutsu 1UR (1UR, Return an unblocked attacker you control to hand: Put this card onto the battlefield from your hand tapped and attacking.)
                \nSlicing Maelstrom — Whenever Kennen deals combat damage to a player, it deals 1 damage to each creature that player controls.""",
        'artist': 'Dhaniels Castillo',
        'color': ['Blue', 'Red'],
        'region': ['Ionia']
    },
    'Kled Cantankerous Cavalier.png': {
        'title': 'Kled, Cantankerous Cavalier',
        'type': 'Legendary Creature - Yorde Beserker',
        'text_box': """When Kled enters, create Skaarl, a legendary 3/4 red lizard mount creature token with haste, saddle 2, and “Whenever this creature attacks, if it was saddled by Kled, you may have target creature block Skaarl this turn.”
                \nCHAAAAAAARGE!!! — 1RR: Creatures you control gain haste and first strike until end of turn.""",
        'artist': 'Hozure',
        'color': ['Red'],
        'region': ['Noxus']
    },
    'Lee Sin Blind Monk.png': {
        'title': 'Lee Sin, Blind Monk',
        'type': 'Legendary Creature - Human Monk',
        'text_box': """Haste, first strike
                \nSonic Wave — At the beginning of combat on your turn, choose target creature an opponent controls. That creature becomes Sighted until end of turn.
                \nResonating Strike — T: Lee Sin fights target Sighted creature.""",
        'artist': 'Park Jun Seong',
        'color': ['Red', 'Green'],
        'region': ['Ionia']
    },
    'Maokai Twisted Treant.png': {
        'title': 'Maokai, Twisted Treant',
        'type': 'Legendary Creature - Treefolk',
        'text_box': """""",
        'artist': 'SixMoreVodka',
        'color': ['Green'],
        'region': ['Shadow Isles']
    },
    'Master Yi.png': {
        'title': 'Master Yi',
        'type': 'Legendary Creature - Human Samurai',
        'text_box': """Alpha Strike — Whenever Master Yi attacks, it deals X damage to up to three target creatures, where X is the amount of life you gained this turn.
                \nMeditate — 3GW: You gain life equal to Master Yi’s toughness. Activate this ability only once each turn.""",
        'artist': 'Jack Hsu',
        'color': ['White', 'Green'],
        'region': ['Ionia']
    },
    'Mordekaiser Iron Revenant.png': {
        'title': 'Mordekaiser, Iron Revenant',
        'type': 'Legendary Creature - Spirit Juggernaut',
        'text_box': """Trample
                \nRealm of Death — BB: Choose target creature an opponent controls. Until end of turn, that creature blocks Mordekaiser if able. If that creature would die this turn, exile it instead and put a +1/+1 counter on Mordekaiser. Activate this ability only once each turn.""",
        'artist': 'Fighting Kumar D',
        'color': ['Black'],
        'region': ['Noxus']
    },
    'Morgana the Fallen.png': {
        'title': 'Morgana the Fallen',
        'type': 'Legendary Creature - Angel Wizard',
        'text_box': """Soul Siphon — At the beginning of each opponent’s end step, for each tapped creature they control, that player loses 1 life and you gain 1 life.
                \nSoul Shackles — At the beginning of your end step, if Morgana attacked a player this turn, you may pay 2WB. When you do, tap all creatures that player controls. Those creatures don’t untap during that player’s next untap step.""",
        'artist': 'Juan Pablo',
        'color': ['White', 'Black'],
        'region': ['Demacia'],
    },
    'Nidalee Bestial Huntress.png': {
        'title': 'Nidalee, Bestial Huntress // Nidalee, Cat Form',
        'type': 'Legendary Creature - Human Scout',
        'text_box': """""",
        'artist': 'Big Q Dai and Lisha Du',
        'color': ['Green'],
        'region': ['Ixtal'],
        'flippable': True
    },
    'Renata Glasc Chem-Baroness.png': {
        'title': 'Renata Glasc, Chem-Baroness',
        'type': 'Legendary Creature - Human Scientist',
        'text_box': """Bailout — 3B, T: Until the end of your next turn, you can’t lose the game for having 0 or less life. Choose target opponent. At the beginning of your next end step, if that player is still in the game, you lose the game. Otherwise, your life total becomes 10. Exile Renata Glasc.""",
        'artist': 'Grafit',
        'color': ['Black'],
        'region': ['Zaun']
    },
    'Samira the Desert Rose.png': {
        'title': 'Samira, the Desert Rose',
        'type': 'Legendary Creature - Human Mercenary',
        'text_box': """Haste, first strike
                \nWhenever you attack, put a combo counter on Samira for each opponent you’re attacking.
                \nInferno Trigger — Remove five combo counters from Samira: Samira deals 5 damage to each creature your opponents control.""",
        'artist': 'Kan Liu',
        'color': ['Red', 'Black'],
        'region': ['Noxus']
    },
    'Senna the Redeemer.png': {
        'title': 'Senna the Redeemer',
        'type': 'Legendary Creature - Human Ranger',
        'text_box': """""",
        'artist': 'Alsoing',
        'color': ['Black', 'White'],
        'region': ['Shadow Isles']
    },
    'Shen Eye of Twilight.png': {
        'title': 'Shen, Eye of Twilight',
        'type': 'Legendary Creature - Human Ninja',
        'text_box': """When Shen enters, create Spirit Blade, a legendary white Equipment artifact token with “Equipped creature gets +1/+2” and equip 2.
                \nStand United — 2W, T: Attach an equipment named Spirit Blade you control to another creature you control. That creature gains indestructible until end of turn. """,
        'artist': 'Jun Seong Park',
        'color': ['White'],
        'region': ['Ionia']
    },
    'Shyvana the Half-Dragon.png': {
        'title': 'Shyvana, the Half-Dragon // Shyvana, Dragon Form',
        'type': 'Legendary Creature - Human Dragon',
        'text_box': """Twin Bite — T: Copy target instant or sorcery spell you control. You may choose new targets for the copy.
                \nDragon’s Descent — 5RR: This ability costs 1 less to activate for each instant or sorcery spell you’ve cast or copied this turn. Transform Shyvana.
                \n\nFlying
                \nWhen this creature transforms into Shyvana, Dragon Form, untap it. It gets +1/+1 until end of turn for each instant or sorcery spell you’ve cast or copied this turn.
                \nAt the beginning of your end step, transform Shyvana.""",
        'artist': 'Monika Palosz',
        'color': ['Red', 'Blue'],
        'region': ['Demacia'],
        'flippable': True
    },
    'Singed Mad Chemist.png': {
        'title': 'Singed, Mad Chemist',
        'type': 'Legendary Creature - Human Scientist',
        'text_box': """Menace
                \nPoison Trail — Whenever Singed attacks, until your next turn, creatures defending player controls that attack you cause their controller to gain a poison counter.""",
        'artist': 'Amanda Jeffrey',
        'color': ['Black'],
        'region': ['Zaun']
    },
    'Sion Undead Juggernaut.png': {
        'title': 'Sion, Undead Juggernaut',
        'type': 'Legendary Creature - Zombie Juggernaut',
        'text_box': """Trample, menace
                \nGlory in Death — When Sion dies, if it is your first combat phase, return Sion from the graveyard to the battlefield. It gains haste and double strike until end of turn. After this phase, there is an additional combat phase. Sacrifice Sion at the beginning of your next end step.""",
        'artist': 'Xiaofeng',
        'color': ['Black', 'Red'],
        'region': ['Noxus']
    },
    'Smolder Fiery Fledgling.png': {
        'title': 'Smolder, Fiery Fledgling',
        'type': 'Legendary Creature - Dragon Wizard',
        'text_box': """Flying
                \nWhenever Smolder deals combat damage, put that many Practice counters on it.
                \nMMOOOMMMM! — Remove ten Practice counters from Smolder: Put target Dragon creature card from your hand onto the battlefield tapped. It deals damage equal to its power to each creature your opponents control.""",
        'artist': 'Pablo Gutiérrez',
        'color': ['Red'],
        'region': ['Noxus']
    },
    'Sona Maven of the Strings.png': {
        'title': 'Sona, Maven of the Strings',
        'type': 'Legendary Creature - Human Performer',
        'text_box': """At the beginning of your upkeep, choose target Aura you control that’s attached to a creature. For each other creature you control that the Aura could enchant, create a token that’s a copy of that Aura and attach it to that creature. Sacrifice those tokens at the beginning of the next end step.""",
        'artist': 'Amelia Rose',
        'color': ['Blue'],
        'region': ['Demacia'],
    },
    'Swain Grand General.png': {
        'title': 'Swain, Grand General',
        'type': 'Legendary Creature - Human Warlock',
        'text_box': """Menace
                \nVision of Empire — Whenever Swain deals combat damage to a player, you may look at that player’s hand. You may choose a nonland card from it. If you do, that player discards that card and you create a 1/1 black Bird creature token with flying.
                \nWhenever a token you control dies, target opponent loses 1 life and you gain 1 life.""",
        'artist': 'Exia',
        'color': ['Black', 'Red'],
        'region': ['Noxus']
    },
    'Sylas the Unshackled.png': {
        'title': 'Sylas the Unshackled',
        'type': 'Legendary Creature - Human Criminal',
        'text_box': """Suspend 3 1UU 
                \nFlash
                \nWhenever Sylas becomes suspended, counter target instant or sorcery spell. If that spell is countered this way, exile it with a Hijack counter on it.
                \nWhenever Sylas attacks, you may copy a card in exile with a Hijack counter on it. You may cast the copy without paying its mana cost.""",
        'artist': 'Minwoo Cho',
        'color': ['Blue'],
        'region': ['Demacia']
    },
    'Taliyah Stoneweaver.png': {
        'title': 'Taliyah, Stoneweaver',
        'type': 'Legendary Creature - Human Wizard',
        'text_box': """Landfall — Whenever a land enters the battlefield under your control, you may have it become a 0/4 red Wall creature with defender and haste in addition to its other types. 
                \nAs long as it’s your turn, Walls you control assign combat damage equal to their toughness rather than its power and can attack as though it didn’t have defender.""",
        'artist': 'Qi Mang',
        'color': ['Red', 'Green', 'White', 'Blue'],
        'region': ['Shurima']
    },
    'Thresh Chain Warden.png': {
        'title': 'Thresh, Chain Warden',
        'type': 'Legendary Creature - Spirit',
        'text_box': """""",
        'artist': 'Michal Ivan',
        'color': ['Black'],
        'region': ['Shadow Isles']
    },
    'Urgot the Dreadnought.png': {
        'title': 'Urgot, the Dreadnought',
        'type': 'Legendary Artifact Creature - Human Crab',
        'text_box': """Infect
                \nPurge — Whenever Urgot attacks and isn’t blocked, instead of dealing combat damage, Urgot deals 1 damage to up to X targets, where X is Urgot’s power.
                \nDisdain — 3BB, Pay 2 life: Urgot can’t be blocked this turn.""",
        'artist': 'Gi Taek Seo',
        'color': ['Black'],
        'region': ['Zaun']
    },
    'Varus Darkin Arrow.png': {
        'title': 'Varus, Darkin Arrow',
        'type': 'Legendary Creature - Demon Archer',
        'text_box': """Reach
                \nLiving Vengeance — Whenever another creature dies, Varus gets +1/+0 until end of turn.
                \nUnconquered Souls — Whenever one or more creature cards are exiled from anywhere, put a +1/+1 counter on Varus.""",
        'artist': 'Kan Liu',
        'color': ['Black', 'Blue'],
        'region': ['Ionia']
    },
    'Vayne Night Hunter.png': {
        'title': 'Vayne, Night Hunter',
        'type': 'Legendary Creature - Human Ranger',
        'text_box': """""",
        'artist': 'SixMoreVodka',
        'color': ['White'],
        'region': ['Shadow Isles']
    },
    'Vex the Gloomist.png': {
        'title': 'Vex the Gloomist',
        'type': 'Legendary Creature - Yordle Wizard',
        'text_box': """""",
        'artist': 'Horace Hsu',
        'color': ['Black', 'Blue'],
        'region': ['Shadow Isles']
    },
    'Viego Ruined King.png': {
        'title': 'Viego, Ruined King',
        'type': 'Legendary Creature - Noble Shapeshifter',
        'text_box': """Harrowed Path — When Viego enters, target land you control gains “1, T: Target creature you control gains Shadow until end of turn” for as long as you control Viego. 
                \nSovereign’s Domination — Whenever another creature dies, you may pay 2U. If you do, until your next end step, Viego becomes a copy of that creature, except it’s a 5/4 and it has this ability.""",
        'artist': 'Fighting Kumar D',
        'color': ['Black', 'Green', 'Blue'],
        'region': ['Shadow Isles']
    },
    'Viktor Herald of Arcane.png': {
        'title': 'Viktor, Herald of Arcane',
        'type': 'Legendary Creature - Human Artificer',
        'text_box': """Glorious Evolution — At the beginning of your end step, you may exile a Human you control. If you do, create a 3/3 colorless artifact Construct creature token, then choose one —
                \n• Put a +1/+1 counter on each artifact creature you control.
                \n• Draw a card, then lose 1 life.
                \n• Return target artifact card from your graveyard to you hand.""",
        'artist': 'Claudiu-Antoniu Magherusan',
        'color': ['Black', 'White', 'Blue'],
        'region': ['Zaun']
    },
    'Vladimir Crimson Reaper.png': {
        'title': 'Vladimir, Crimson Reaper',
        'type': 'Legendary Creature - Vampire Wizard',
        'text_box': """Lifelink
                \nCrimson Pact — Vladimir gets +1/+1 for each life you have above your starting life total.
                \nSanguine Pool — Pay 5 life, T: Vladimir gains hexproof and indestructible until end of turn.""",
        'artist': 'SixMoreVodka',
        'color': ['Red', 'Black', 'White'],
        'region': ['Noxus']
    },
    'Warwick Wrath of Zaun.png': {
        'title': 'Warwick, Wrath of Zaun',
        'type': 'Legendary Creature - Wolf Berserker',
        'text_box': """Eternal Hunger — As long as an opponent has 10 or less life, Warwick has haste.
                \nBlood Hunt — Whenever Warwick attacks, if defending play took damage this turn, Warwick gains double strike and lifelink until end of turn.""",
        'artist': 'Jun Seong Park',
        'color': ['Green', 'Red'],
        'region': ['Zaun']
    },
    'Yasuo the Unforgiven.png': {
        'title': 'Yasuo the Unforgiven',
        'type': 'Legendary Creature - Human Samurai',
        'text_box': """Vigilance
                Windwall — During your turn, prevent all noncombat damage to creatures you control.
                Whenever Yasuo attacks, target creature an opponent controls gains flying until the end of combat.
                Last Breath — T: Destroy target creature with flying.""",
        'artist': 'Rosolino',
        'color': ['Blue', 'White'],
        'region': ['Ionia'],
    },
    'Yone the Unforgotten.png': {
        'title': 'Yone the Unforgotten',
        'type': 'Legendary Creature - Spirit Samurai',
        'text_box': """Soul Unbound — 2UB, T: Target opponent creates a token copy of Yone, except it loses all abilities and gains “This creature can’t attack or block” and “At the beginning of each combat, sacrifice another creature.” 
                \nReturn — UT: Activate only if an opponent controls a token named Yone.
                \nWhenever Yone untaps, destroy all tokens named Yone.""",
        'artist': 'Kim Nha',
        'color': ['Blue', 'Black'],
        'region': ['Ionia']
    },
    'Yorick Shepherd of Souls.png': {
        'title': 'Yorick, Shepherd of Souls',
        'type': 'Legendary Creature - ',
        'text_box': """""",
        'artist': 'Vo Minh Tuan',
        'color': ['Black', 'Green', 'White'],
        'region': ['Shadow Isles']
    },
    'Zed Master of Shadows.png': {
        'title': 'Zed, Master of Shadows',
        'type': 'Legendary Creature - Human Ninja',
        'text_box': """Living Shadow — At the beginning of combat on your turn, for each opponent, create a 3/1 black and red Shadow Clone creature token with haste. Exile those tokens at the end of combat.
                \nSwap — Whenever a Shadow Clone token you control attacks and isn’t blocked, you may exile that token and Zed. If you do, return Zed to the battlefield tapped and attacking the player that token was attacking.""",
        'artist': 'Noah Thatcher',
        'color': ['Black', 'Red'],
        'region': ['Ionia']
    },
    'Zyra Rise of the Thorns.png': {
        'title': 'Zyra, Rise of the Thorns',
        'type': 'Legendary Creature - Human Plant',
        'text_box': """Garden of Thorns — At the beginning of your upkeep, create a 0/1 green Saproling creature token.
                \nWhenever you cast a noncreature spell, put a +1/+1 counter on each Saproling you control.""",
        'artist': 'Foritis Wang',
        'color': ['Green', 'Red', 'Black'],
        'region': ['Ixtal']
    }
}
