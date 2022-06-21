# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define cur_version = "0.4.0"

define persistent.auth_code = ""
define persistent.uname = ""
define persistent.pledgecent = 0
define persistent.uimg = ""
define persistent.tier = ""
define persistent.follower = False
define persistent.patron_status = ""
define persistent.pledge_cadence = 0
define persistent.top_donators = ""

define persistent.king_place = None
define persistent.your_npc = None

define persistent.server = "https://lustmadness.me"
# define persistent.next_label = ""
define chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

define check_errors = False

default dev_enable_grid = False
default dev_unlockall_door = False
#+++++++++++++++Characters+++++++
define quest_giver = im.Scale("/gui/map/TheGaffer_idle.png",316,722)  
define mirana_elf_bar = im.Scale("/gui/map/MiranaElf_idle.png",364,595)  
define quest_giver_hover = im.Scale("/gui/map/TheGaffer_hover.png",316,722)  
define mirana_elf_bar_hover = im.Scale("/gui/map/MiranaElf_hover.png",364,595)  

#+0.3.9
define npc_tavern_haircutter_idle_img = im.Scale("/gui/map/TheHaircutter_idle.png",207,483) 
define npc_tavern_haircutter_hover_img = im.Scale("/gui/map/TheHaircutter_hover.png",207,483) 
#-0.3.9

image player_female_idle = im.Scale("/360/body/player_female_idle.png",540,800)
image player_male_idle = im.Scale("/360/body/player_male_idle.png",540,800)
image player_futa_idle = im.Scale("/360/body/player_futa_idle.png",540,800)
image player_female_hover = im.Scale("/360/body/player_female_hover.png",540,800)
image player_male_hover = im.Scale("/360/body/player_male_hover.png",540,800)
image player_futa_hover = im.Scale("/360/body/player_futa_hover.png",540,800)

default _vnumlist = []

define santa_enemy_desc = None
define santa_helper_enemy_desc1 = None
define santa_helper_enemy_desc2 = None
define mirana_enemy_desc = None

define worldmap = WorldLocationMap()

image alpha_bg:
    "/images/alpha_bg.png"



image quest_giver_img:
    "/gui/map/TheGaffer_idle.png"
    size(316,722) 
image mirana_elf_bar_img:
    "/gui/map/MiranaElf_idle.png"
    size(364,595) 
image quest_giver_img_hover:
    "/gui/map/TheGaffer_hover.png"
    size(316,722) 
image mirana_elf_bar_img_hover:
    "/gui/map/MiranaElf_hover.png"
    size(364,595) 

image quest_giver_say_img:
    "/images/Characters/TheGaffer_say.png"
    size(1080,1600)

image nunchurch_say_img:
    "/images/Characters/church_nun_say.png"
    size(1080,1600)

image herbalica_new_say_img:
    "/images/Characters/TheHerbalicaNew_say.png"
    size(1080,1600)
image herbalica_old_say_img:
    "/images/Characters/TheHerbalicaOld_say.png"
    size(1080,1600)
image seller_shop_say_img:
    "/images/Characters/TheShoperClothing_say.png"
    size(1080,1600)
image seller_shop_new_say_img:
    "/images/Characters/TheShoperClothingNew_say.png"
    size(1080,1600)
image rathaircutter_say_img:
    "/images/Characters/HairCutterRat_say_img.png"
    size(1080,1600)
    
image seller_shop_img:
    "/gui/map/TheSeller_idle.png"
    size(279,870) 
image seller_shop_img_hover:
    "/gui/map/TheSeller_hover.png"
    size(279,870) 
image seller_shop_img2:
    "/gui/map/TheSellerNew_idle.png"
    size(304,870) 
image seller_shop_img2_hover:
    "/gui/map/TheSellerNew_hover.png"
    size(304,870) 
image herbalist_shop_img:
    "/gui/map/TheHerbalist_idle.png"
    size(560,863) 
image herbalist_shop_img_hover:
    "/gui/map/TheHerbalist_hover.png"
    size(560,863)    
image herbalist_shop_img2:
    "/gui/map/TheHerbalist2_idle.png"
    size(892,820) 
image herbalist_shop_img2_hover:
    "/gui/map/TheHerbalist2_hover.png"
    size(892,820)   
    
#++++Characters++++
define e = Character("[ee]", color='#957d54')
define g = Character("[gg]", color='#ffffff')

default GafferChoo = NpcChar("Gaffer Choo","male","80")
default HerbalicaFlower = NpcChar("Herbalica Flower","female","20")
default GloomyJack = NpcChar("Gloomy Jack","male","36")
default NunChurch = NpcChar("Nun","female","21")
default MysteriousFarmer = NpcChar("Mysterious Farmer","male","33")
default CunninGrawl = NpcChar("Cunnin Grawl","male","35")
default WagonKront = NpcChar("Wagon Kront","male","25")

default npc_Freya = NpcChar("Freya","female","30", im.Scale("/images/NPC/Freya/Freya_idle_img.png", 1080, 1600))#0.0.8
default npc_Richman = NpcChar("Richman","male","50", im.Scale("/images/NPC/Richman/richman_idle_img.png", 3200, 3200))#0.0.8

default MiranaElf = NpcChar("Mirana","female","150", im.Scale("/images/NPC/MiranaElf/MiranaElf_say_img.png", 1080, 1600))

default npc_CrookedPeasant = NpcChar("Crooked-toothed peasant","male","22", im.Scale("/images/NPC/Peasant/npc_peasant_crazy.png", 1080, 1600))
default npc_Santa = NpcChar("Santa","male","76", im.Scale("/images/NPC/Santa/npc_santa_idle.png", 1080, 1600))#0.1.0

default npc_Rascal = NpcChar("Rascal","male","150", im.Scale("/images/NPC/Rascal/Rascal_npc_say.png", 1080, 1600)) #0.1.8

default npc_SlutStatue = NpcChar("Slut Statue","female","150", im.Scale("/images/NPC/SlutStatue/slutstatue_npc_say.png", 1080, 1600)) #0.2.6
default npc_SlutsWall = NpcChar("Sluts wall","female","150", im.Scale("/images/NPC/SlutsWall/slutswall_npc_say.jpg", 1080, 1600)) #0.2.6

default npc_LumberJack = NpcChar("Lumberjack","male","150", im.Scale("/images/NPC/LumberJack/lumberjack_m_npc_say.png", 1080, 1600)) #0.3.1

default npc_TheHairCutterRat = NpcChar("Rat Haircutter","female","150", im.Scale("/images/NPC/HairCutterRat/HairCutterRat_say_img.png", 1080, 1600))

image npcFreya_naked_img:
    "/images/NPC/Freya/Freya_naked_view.png"
    xzoom 1
    yzoom 1

default get_church_reward = False
default _countitem = 1
default _page = 0 
default selected_num_clothe_page = 0
default selected_page = 0
default selected_num = 0

default card_sort_by_active = False
default card_sort_by_rare = False
default card_sort_by_type = False
default card_sort_deactivate_all = False

default _all_coins = 0
default _all_points = 0

image CunninGrawl_anim:
    "images/NPC/squeeze_boobs_anim0.jpg"
    0.2
    "images/NPC/squeeze_boobs_anim1.jpg"
    0.2
    "images/NPC/squeeze_boobs_anim2.jpg"
    0.2
    "images/NPC/squeeze_boobs_anim3.jpg"
    0.2
    "images/NPC/squeeze_boobs_anim4.jpg"
    0.2
    "images/NPC/squeeze_boobs_anim5.jpg"
    0.2
    "images/NPC/squeeze_boobs_anim4.jpg"
    0.2
    "images/NPC/squeeze_boobs_anim3.jpg"
    0.2
    "images/NPC/squeeze_boobs_anim4.jpg"
    0.2
    "images/NPC/squeeze_boobs_anim5.jpg"
    0.2
    "images/NPC/squeeze_boobs_anim4.jpg"
    0.2
    "images/NPC/squeeze_boobs_anim3.jpg"
    0.2
    "images/NPC/squeeze_boobs_anim4.jpg"
    0.2
    "images/NPC/squeeze_boobs_anim5.jpg"
    0.2
    "images/NPC/squeeze_boobs_anim4.jpg"
    0.2
    "images/NPC/squeeze_boobs_anim3.jpg"
    0.2
    "images/NPC/squeeze_boobs_anim2.jpg"
    0.2
    "images/NPC/squeeze_boobs_anim1.jpg"
    0.2
    repeat
#----Characters----
#---------------Characters-------

#body++++++++++++++
define body_female = im.Scale("/body/female_base.png",540,800)
image body_female_abdomen:
    "/body/female_base_abdomen.png"
    size(540,800)
    
image breast_size0:
    "/body/breasts/breast_size0.png"
    size(540,800)    
image breast_size1:
    "/body/breasts/breast_size1.png"
    size(540,800)
image breast_size2:
    "/body/breasts/breast_size2.png"
    size(540,800)
    
#hair_style
image hair_style1_black:
    "/body/hairs/hair_style1_black.png"
    size(540,800)
image hair_style1_blonde:
    "/body/hairs/hair_style1_blonde.png"
    size(540,800)
#--------------------

#eye_style
image eye_color1:
    "/body/eye/base_face_eye1.png"
    size(540,800)
image eye_color2:
    "/body/eye/base_face_eye2.png"
    size(540,800)
image eye_color3:
    "/body/eye/base_face_eye3.png"
    size(540,800)
#--------------------

#lips_style
image lips_color1:
    "/body/lips/base_face_lips1.png"
    size(540,800)
image lips_color2:
    "/body/lips/base_face_lips2.png"
    size(540,800)
image lips_color3:
    "/body/eye/base_face_eye3.png"
    size(540,800)
#--------------------
    


default cur_loc = None
default cur_quest = None

image img_forest_return_to_camp = "images/Locations/Forest/return_to_camp.png"
image img_village_wall_return_to_camp = "images/Locations/Village wall/return_to_camp.png"
# default gender = ["Male", "Female", "Neutral (It)", "Neutral (They)"]   
# default body_color = ["pale"] #black, yellow
# default body_typeArr = {"pale":body_female}
# default breast_sizeArr = {"pale":{"size0":"breast_size0","size1":"breast_size1","size2":"breast_size2"}}
# default hair_typeArr = {"hair_style1":{"black":"hair_style1_black","blonde":"hair_style1_blonde"}}


default inventory = []
default inventory_private = []

default selected_item = None
default private_selected_item = None

default body_parts = ["head", "neck", "chest","bra","arm","belt","hips","panties","legs","foot"]

default selected_window = None
default selected_card = None
default selected_card_upgrade = None
default selected_enemy_sex = None
default selected_enemy_stat = None

#++++++++++++++++++++++skills list+++++++++++++++++++++++

#++++++++++Items+++++++++++++++++
#name, icon, gain = [], desc = "", stack_count)
default items_list = []
default item_lustherb = Unconsumable("Lust Herb", im.Scale("/Items/lustherb.png",64,64),"Bright red plant, not usable without preparation",15)#im.Scale("/Items/lustherb.png",64,64))

default item_lewdpotion = Unconsumable("Lewdpotion", im.Scale("/Items/lewdpotion.png",64,64),"A very unstable drink that causes lust", 5)

default item_herb = Consumable("Herb", im.Scale("/Items/herb.png",64,64), [{"target":"hp", "count":10}], "A plant that restores a slight amount of Health.",20)
default item_ivy = Unconsumable("Ivy", im.Scale("/Items/ivy.png",64,64),"A lightweight and extremely strong plant",99)
default item_supply_potion = Consumable("Potion (supply)", im.Scale("/Items/potion.png",64,64), [{"target":"hp", "count":30}], "Restores a small amount of health.",10)
default item_potion = Consumable("Potion", im.Scale("/Items/potion.png",64,64), [{"target":"hp", "count":30}], "Restores a small amount of health.",10)
default item_megapotion = Consumable("Mega potion", im.Scale("/Items/potion.png",64,64), [{"target":"hp", "count":50}], "Restores a moderate amount of health.",10)
default item_smallstick = Unconsumable("Small stick", im.Scale("/Items/smallstick.png",64,64),"Small twig of shrub",99)
default item_cloth_piece = Unconsumable("Piece of cloth", im.Scale("/Items/cloth_piece.png",64,64),"The basis for creating clothes",50)
default item_leather_piece = Unconsumable("Piece of leather", im.Scale("/Items/leather_piece.png",64,64),"The basis for creating leather clothes",50)
default item_latex_piece = Unconsumable("Piece of latex", im.Scale("/Items/latex_piece.png",64,64),"The basis for creating latex clothes",50)
default item_book = Unconsumable("Book", im.Scale("/Items/book.png",64,64),"Book is the basis of knowledge",20)
default item_sap_plant = Unconsumable("Sap plant", im.Scale("/Items/sap_plant.png",64,64), "A plant with leaves coated in sticky sap. Difficult to remove once attached.",99) #0.1.3
default item_sleep_herb = Unconsumable("Sleep herb", im.Scale("/Items/sleep_herb.png",64,64), "Plant with sleep-inducing qualities.",50) #0.1.3

default item_bone = Unconsumable("Bone", im.Scale("/Items/bone.png",64,64),"Just a bone. So worn and weathered, it's unidentifiable",99)
default item_stone = Unconsumable("Stone", im.Scale("/Items/stone.png",64,64),"A small rock",99)
default item_blue_mushroom = Unconsumable("Blue mushroom", im.Scale("/Items/blue_mushroom.png",64,64),"Ordinary mushroom with a power-enhancing effect",99)
default item_powershroom = Unconsumable("Powershroom", im.Scale("/Items/powershroom.png",64,64),"",99)
default item_exciteshroom = Unconsumable("Exciteshroom", im.Scale("/Items/exciteshroom.png",64,64),"",10)
default item_honey = Unconsumable("Honey", im.Scale("/Items/honey.png",64,64),"Normal honey. Highly nutritious",99)
default item_hairs = Unconsumable("Hairs", im.Scale("/Items/hairs.png",64,64),"Great hair. Almost like a thread",99)
default item_red_flower = Unconsumable("Red flower", im.Scale("/Items/red_flower.png",64,64),"",99)
default item_blue_flower = Unconsumable("Blue flower", im.Scale("/Items/blue_flower.png",64,64),"",99)
default item_yellow_flower = Unconsumable("Yellow flower", im.Scale("/Items/yellow_flower.png",64,64),"",99)

default item_mucus = Unconsumable("Mucus", im.Scale("/Items/mucus.png",64,64),"Very sticky thing",99)
default item_worm = Unconsumable("Worm", im.Scale("/Items/worm.png",64,64),"A fat nightcrawler that works well as bait for fishing.",99)
default item_net = Unconsumable("Net", im.Scale("/Items/net.png",64,64),"Powerful net able to withstand a certain amount of weight.",99)
default item_pollen = Unconsumable("Pollen", im.Scale("/Items/pollen.png",64,64),"Particles from flowers. Can be found on the fairy's wings",99)
default item_oil = Unconsumable("Oil", im.Scale("/Items/oil.png",64,64),"Very slippery liquid",99)
default item_water = Unconsumable("Water", im.Scale("/Items/water.png",64,64),"Just a water",99)

default item_return_pass = Unconsumable("Return pass", im.Scale("/Items/return_pass.png",64,64),"This allows you to finishing the quest", 1)

default item_satyr_horn = Unconsumable("Satyr's horn", im.Scale("/Items/satyr_horn.png",64,64),"Satyr horn. It's not easy to get it",10)
default item_satyr_fur = Unconsumable("Satyr's fur", im.Scale("/Items/satyr_fur.png",64,64),"Just a fur",50)
default item_satyr_cum = Consumable("Satyr cum", im.Scale("/Items/sperm.png",64,64), [{"target":"swallowed_cum", "count":5}, {"target":"temp_max_hp", "count":5}], "Satyr cum in flask.",5)
default item_flydick_cum = Consumable("Flydick cum", im.Scale("/Items/sperm.png",64,64), [{"target":"swallowed_cum", "count":3}], "Flydick cum in flask.",5)

default item_testosterone = Consumable("Testesterone", im.Scale("/Items/testosterone.png",64,64), [{"target":"temp_max_st", "count":50}], "Pure testosterone.",10) #0.0.5

default item_locket = Unconsumable("The locket", im.Scale("/Items/locket.png",64,64),"Father Troy's old locket",1)

default item_pumpkin = Unconsumable("Pumpkin", im.Scale("/Items/pumpkin.png",64,64),"Large ripe pumpkin",5) #0.0.6

default item_red_ink = Unconsumable("Red ink", im.Scale("/Items/red_ink.png",64,64),"Red ink",99) #0.0.6
default item_white_ink = Unconsumable("White ink", im.Scale("/Items/white_ink.png",64,64),"White ink",99) #0.0.6
default item_pink_ink = Unconsumable("Pink ink", im.Scale("/Items/pink_ink.png",64,64),"Pink ink",99) #0.0.6

default item_orc_skin = Unconsumable("Green Orc's skin", im.Scale("/Items/orc_skin.png",64,64),"Special green skin for creating clothes.",10)#0.1.1
default item_orc_fang = Unconsumable("Orc's fang", im.Scale("/Items/orc_fang.png",64,64),"Orc's sharp fang.",10)#0.1.1

default item_cave_key_part1 = Unconsumable("Part of key for hidden cave (1)", im.Scale("/Items/cave_key_part1.png",64,64), "Metal plate with bulges.",1) #0.1.8
default item_cave_key_part2 = Unconsumable("Part of key for hidden cave (2)", im.Scale("/Items/cave_key_part2.png",64,64), "Metal plate with bulges.",1) #0.1.8
default item_cave_key = Unconsumable("Key for hidden cave", im.Scale("/Items/cave_key.png",64,64), "Metal plate with bulges.",1) #0.1.8

default item_glassful = Unconsumable("Glassful", im.Scale("/Items/glassful.png",64,64), "Glassful for deception.",3) #0.1.8

default item_trap_tool = Unconsumable("Trap tools", im.Scale("/Items/trap_tool.png",64,64),"A must-have item for putting together bear traps and other kinds of traps.", 4) #0.1.9
default item_bear_trap = Consumable("Bear trap", im.Scale("/Items/bear_trap.png",64,64), [{"target":"building", "count":1}], "Mechanism for capturing monsters. It's almost impossible to escape from it.", 20) #0.1.9



default item_catalist = Unconsumable("Catalist", im.Scale("/Items/catalist.png",64,64),"Mixes with other materials to improve their effect. Cannot be used by itself.", 50) #0.2.1
default item_potion_stamina = Consumable("Stamina juice", im.Scale("/Items/stamina_juice.png",64,64), [{"target":"st", "count":2}], "Adds 2 stamina.",3,True) #0.2.1
default item_potion_gain_armor = Consumable("Armor juice", im.Scale("/Items/armor_juice.png",64,64), [{"target":"armor", "count":12}], "Adds 15 block.",3,True) #0.2.1
default item_potion_draw_card = Consumable("Drawcard juice", im.Scale("/Items/drawcard_juice.png",64,64), [{"target":"drawcard", "count":1}], "Draw 1 card from draw deck.",3,True) #0.2.1


default item_poisonshroom = Consumable("Poisonshrooms", im.Scale("/Items/poisonshroom.png",64,64), [{"target":"hp", "count":-15}], "A small poisonous mushrooms that is best not to eat.",20)
default item_amanita = Unconsumable("Amanita", im.Scale("/Items/amanita.png",64,64),"Red mushroom with white splashes on the cap. Suitable for some potions.",20)
default item_mushroom_slime = Unconsumable("Mushroom slime", im.Scale("/Items/mushroom_slime.png",64,64),"This substance is very difficult to obtain.",10)


default item_red_dildo = Unconsumable("Red dildo", im.Scale("/Items/item_red_dildo.png",64,64), "Red dildo for slut statue.",1) #0.2.6
default item_blue_dildo = Unconsumable("Blue buttplug", im.Scale("/Items/item_blue_dildo.png",64,64), "Blue buttplug for slut statue.",1) #0.2.6
default item_yellow_dildo = Unconsumable("Yellow dildo", im.Scale("/Items/item_yellow_dildo.png",64,64), "Yellow dildo for slut statue.",1) #0.2.6

default item_piece_scroll = Unconsumable("Piece of scrolls", im.Scale("/Items/piece_of_scroll.png",64,64), "Part of an old scrolls.",4) #0.2.6

default item_cavemaze_key = Unconsumable("Cavemaze Key", im.Scale("/Items/cavemaze_key.png",64,64), "Cave maze exit key.",1) #0.2.6
default item_cavemaze_key_part1 = Unconsumable("Cavemaze Key (part 1)", im.Scale("/Items/cavemaze_key_part1.png",64,64), "Part of an unknown key.",1) #0.2.6
default item_cavemaze_key_part2 = Unconsumable("Cavemaze Key (part 2)", im.Scale("/Items/cavemaze_key_part2.png",64,64), "Part of an unknown key.",1) #0.2.6

default item_red_mushroom = Consumable("Red mushrooms", im.Scale("/Items/red_mushroom.png",64,64), [{"target":"hp", "count":-20}], "This mushroom emits warmth. Don't eat!",20)#0.2.6
default item_hot_drink = Consumable("Hot drink", im.Scale("/Items/hot_drink.png",64,64), [{"target":"temperature", "count":200}], "This drink will keep you warm.",20)#0.2.6

default item_amber_ore = Unconsumable("Ambre ore", im.Scale("/Items/amber_ore.png",64,64), "PBright yellow and orange stones with a perfectly round shape.",99) #0.2.6

default item_slime_part = Unconsumable("Slime part", im.Scale("/Items/slime_part.png",64,64),"A very wet piece that slips out of your hands.",20)#0.2.9
default item_slime_stone = Unconsumable("Slime stone", im.Scale("/Items/slime_stone.png",64,64),"Solid particles of slime.",20)#0.2.9
default item_slime_fluid = Consumable("Slime fluid", im.Scale("/Items/slime_fluid.png",64,64), [{"target":"hp", "count":-50}], "Very viscous liquid.",20)#0.2.9

default item_cave_herb = Unconsumable("Cave herb", im.Scale("/Items/cave_herb.png",64,64),"This plant doesn't need sunlight.",99)
default item_snake_herb = Unconsumable("Snake herb", im.Scale("/Items/snake_herb.png",64,64),"This plant looks like a snake.",99)

default item_ax = Unconsumable("Lumberjack's ax", im.Scale("/Items/ax.png",64,64), "Lumberjack's ax. Heavy and sharp.",1) #0.3.1

default item_max_potion = Consumable("Max potion", im.Scale("/Items/max_potion.png",64,64), [{"target":"hp", "count":9999999}], "Fully restores health.",5)#0.3.2
default item_rare_cloth = Unconsumable("Rare cloth", im.Scale("/Items/rare_cloth.png",64,64), "Very dense fabric that is difficult to find.",99) #0.3.2

default item_snowball_small = Consumable("Snowball (small)", im.Scale("/Items/snowball_small.png",64,64), [{"target":"enemy_lust", "count":1}], "It's just a little snowball. Deal {color=#fff}{size=22}1{/size}{/color} damage in a battle",99,True) #0.3.7
default item_snowball = Consumable("Snowball", im.Scale("/Items/snowball.png",64,64), [{"target":"enemy_lust", "count":3}], "It's just a snowball. . Deal {color=#fff}{size=22}3{/size}{/color} damage in a battle",49,True) #0.3.7
default item_snowman_item = Consumable("Snowman", im.Scale("/Items/snowman_item.png",64,64), [{"target":"building", "count":1}], "This snowman made of snow seems to be alive. Put it somewhere.", 1) #0.3.7
default item_snowflake = Unconsumable("Snowflake", im.Scale("/Items/snowflake.png",64,64), "It's ordinary snowflake.",99) #0.3.7
default item_ice_crystal = Unconsumable("Ice crystal", im.Scale("/Items/ice_crystal.png",64,64), "Willn't thaw at room temperature. Confirmed to increase ore density.",99) #0.3.7
default item_ice = Unconsumable("Ice", im.Scale("/Items/ice.png",64,64), "Frozen water.",99) #0.3.7
default item_pine_cone = Unconsumable("Pine cone", im.Scale("/Items/pine_cone.png",64,64), "The pinecone is ordinary. Don't try to put it in your ass.",99) #0.3.7

default item_recipes_scroll_001 = Consumable("Recipies scroll (Lewdpotion)", im.Scale("/Items/recipes_scroll.png",64,64), [{"target":"unlock_combo", "item1":item_megapotion, "item2":item_lustherb, "item_result":item_lewdpotion}], "Unlock the recipe in combo list.",1)#0.3.8
default item_recipes_scroll_002 = Consumable("Recipies scroll (Mega potion)", im.Scale("/Items/recipes_scroll.png",64,64), [{"target":"unlock_combo", "item1":item_potion, "item2":item_honey, "item_result":item_megapotion}], "Unlock the recipe in combo list.",1)#0.3.8
default item_recipes_scroll_003 = Consumable("Recipies scroll (Net)", im.Scale("/Items/recipes_scroll.png",64,64), [{"target":"unlock_combo", "item1":item_ivy, "item2":item_hairs, "item_result":item_net}], "Unlock the recipe in combo list.",1)#0.3.8
default item_recipes_scroll_004 = Consumable("Recipies scroll (Oil)", im.Scale("/Items/recipes_scroll.png",64,64), [{"target":"unlock_combo", "item1":item_mucus, "item2":item_water, "item_result":item_oil}], "Unlock the recipe in combo list.",1)#0.3.8
default item_recipes_scroll_005 = Consumable("Recipies scroll (Piece of latex)", im.Scale("/Items/recipes_scroll.png",64,64), [{"target":"unlock_combo", "item1":item_leather_piece, "item2":item_oil, "item_result":item_latex_piece}], "Unlock the recipe in combo list.",1)#0.3.8
default item_recipes_scroll_006 = Consumable("Recipies scroll (Red ink)", im.Scale("/Items/recipes_scroll.png",64,64), [{"target":"unlock_combo", "item1":item_red_flower, "item2":item_oil, "item_result":item_red_ink}], "Unlock the recipe in combo list.",1)#0.3.8
default item_recipes_scroll_007 = Consumable("Recipies scroll (Pink ink)", im.Scale("/Items/recipes_scroll.png",64,64), [{"target":"unlock_combo", "item1":item_white_ink, "item2":item_red_ink, "item_result":item_pink_ink}], "Unlock the recipe in combo list.",1)#0.3.8
default item_recipes_scroll_009 = Consumable("Recipies scroll (Key for hidden cave)", im.Scale("/Items/recipes_scroll.png",64,64), [{"target":"unlock_combo", "item1":item_cave_key_part1, "item2":item_cave_key_part2, "item_result":item_cave_key}], "Unlock the recipe in combo list.",1)#0.3.8
default item_recipes_scroll_010 = Consumable("Recipies scroll (Bear trap)", im.Scale("/Items/recipes_scroll.png",64,64), [{"target":"unlock_combo", "item1":item_trap_tool, "item2":item_satyr_horn, "item_result":item_bear_trap}], "Unlock the recipe in combo list.",1)#0.3.8
default item_recipes_scroll_011 = Consumable("Recipies scroll (Catalist)", im.Scale("/Items/recipes_scroll.png",64,64), [{"target":"unlock_combo", "item1":item_honey, "item2":item_powershroom, "item_result":item_catalist}], "Unlock the recipe in combo list.",1)#0.3.8
default item_recipes_scroll_012 = Consumable("Recipies scroll (Stamina juice)", im.Scale("/Items/recipes_scroll.png",64,64), [{"target":"unlock_combo", "item1":item_catalist, "item2":item_testosterone, "item_result":item_potion_stamina}], "Unlock the recipe in combo list.",1)#0.3.8
default item_recipes_scroll_013 = Consumable("Recipies scroll (Armor juice)", im.Scale("/Items/recipes_scroll.png",64,64), [{"target":"unlock_combo", "item1":item_catalist, "item2":item_blue_flower, "item_result":item_potion_gain_armor}], "Unlock the recipe in combo list.",1)#0.3.8
default item_recipes_scroll_014 = Consumable("Recipies scroll (Cavemaze Key)", im.Scale("/Items/recipes_scroll.png",64,64), [{"target":"unlock_combo", "item1":item_cavemaze_key_part1, "item2":item_cavemaze_key_part2, "item_result":item_cavemaze_key}], "Unlock the recipe in combo list.",1)#0.3.8
default item_recipes_scroll_015 = Consumable("Recipies scroll (Snowball (small))", im.Scale("/Items/recipes_scroll.png",64,64), [{"target":"unlock_combo", "item1":item_snowball_small, "item2":item_snowball_small, "item_result":item_snowball}], "Unlock the recipe in combo list.",1)#0.3.8
default item_recipes_scroll_016 = Consumable("Recipies scroll (Snowball)", im.Scale("/Items/recipes_scroll.png",64,64), [{"target":"unlock_combo", "item1":item_snowball_small, "item2":item_snowball, "item_result":item_snowman_item}], "Unlock the recipe in combo list.",1)#0.3.8

default item_soup = Consumable("Just a soup", im.Scale("/Items/soap.png",64,64), [{"target":"hp", "count":9999999}], "Fully restores health.",3)#0.4.0
#----------Items-----------------
    
    
default pathfound = None
# The game starts here.

default pathkeys = ["-1"]#[(255,255,255,255)]#"0","q","d","e","m"]

default who_turn = None
default battle_timer = 0

default Player = None
default current_quest = None
default current_event = None #0.0.8
default current_battle = None #0.0.9
default cur_return_chest = None
default quest_list = []
default comboBook = None
default monster_list = [] #0.0.5

default _player_rot = None

#++++++++++++++++Battle system+++++++++++
default your_turn = True
default your_wait = False
default battle_is_start = False
default _time = 0

default attack_sequence = []
default attack_sequence_enemy = []
default _startAttack = False
default _prepareAttack = False
default _restoreStamina = False
#----------------Battle system----------


# #++++++++++++++++Locations++++++++++++++++
# default standart_forest_map = LocationMap("Forest and hills", None, "return_to_camp_bg")
# default standart_library_map = LocationMap("Library", None, None)
# #----------------Locations----------------

#Fade(out_time, hold_time, in_time, color="#000")
define fade = Fade(0.3, 0.3, 0.3)
define fade_half_long = Fade(0.7, 1.5, 0.7)
define fade_long = Fade(0.7, 3.0, 0.7)
define dissolve_half = Dissolve(0.1)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
init python:
    show_player = False

    screens = []
    gamemenu = config.game_menu_action
    
    # music_channels = ["music_tavern","music_village","music_battle"]
    renpy.music.register_channel("music_all", mixer="music", loop=True)
    renpy.music.register_channel("music_all2", mixer="music", loop=True)
    # renpy.music.set_volume(0.7, delay=0, channel="music_all2")
    renpy.music.register_channel("sound0", mixer="sound", loop=False)
    renpy.music.register_channel("sound1", mixer="sound", loop=False)
    renpy.music.register_channel("sound2", mixer="sound", loop=False)
    renpy.music.register_channel("sound3", mixer="sound", loop=False)
    renpy.music.register_channel("sound4", mixer="sound", loop=False)
    renpy.music.register_channel("sound5", mixer="sound", loop=False)
    renpy.music.register_channel("sound6", mixer="sound", loop=False)
    renpy.music.register_channel("sound7", mixer="sound", loop=False)
    renpy.music.register_channel("sound8", mixer="sound", loop=False)
    renpy.music.register_channel("sound9", mixer="sound", loop=False)
    renpy.music.register_channel("sound10", mixer="sound", loop=False)
    renpy.music.register_channel("sound11", mixer="sound", loop=False)
    renpy.music.register_channel("sound12", mixer="sound", loop=False)
    renpy.music.register_channel("sound13", mixer="sound", loop=False)
    renpy.music.register_channel("sound14", mixer="sound", loop=False)
    renpy.music.register_channel("sound15", mixer="sound", loop=False)
    renpy.music.register_channel("sound16", mixer="sound", loop=False)
    renpy.music.register_channel("sound17", mixer="sound", loop=False)
    renpy.music.register_channel("sound18", mixer="sound", loop=False)
    renpy.music.register_channel("sound19", mixer="sound", loop=False)
    renpy.music.register_channel("sound20", mixer="sound", loop=False)
    renpy.music.register_channel("sound21", mixer="sound", loop=False)
    renpy.music.register_channel("sound22", mixer="sound", loop=False)
    renpy.music.register_channel("sound23", mixer="sound", loop=False)
    renpy.music.register_channel("sound24", mixer="sound", loop=False)
    renpy.music.register_channel("sound25", mixer="sound", loop=False)
    renpy.music.register_channel("sound26", mixer="sound", loop=False)
    renpy.music.register_channel("sound27", mixer="sound", loop=False)
    renpy.music.register_channel("sound28", mixer="sound", loop=False)
    renpy.music.register_channel("sound29", mixer="sound", loop=False)
    # renpy.music.register_channel("music_tavern", mixer="music", loop=True)
    # renpy.music.register_channel("music_village", mixer="music", loop=True)
    # renpy.music.register_channel("music_battle", mixer="music", loop=True)

    # def MusicManager_play(_music, _channel):
        # renpy.music.set_pause(False, channel="music_tavern")
transform openworldalert:
    xzoom 1.0 yzoom 1.0
    easein 1.2 xzoom 1.1 yzoom 1.1
    easeout 1.2 xzoom 1.0 yzoom 1.0
    repeat

transform tf_check_flash:
    alpha 0.3
    linear 1.0 alpha 0.0
    linear 1.0 alpha 0.3
    repeat

screen world_map():
    $selected_item = None
    add "MainMenuMap"
    use player_ui_bars()
    if "home_wardrobe" in Player.check_info or "home_attacks" in Player.check_info or "home_sexskills" in Player.check_info:
        image "/gui/map/map_home_check.png" xpos 0 ypos 380 at tf_check_flash
    imagebutton auto "/gui/map/map_home_%s.png" xpos 0 ypos 380 action [Return("house"),With(fade)]
    if "village_tavern_GafferChoo" in Player.check_info or "village_tavern_Mirana" in Player.check_info or GetQuestsIsNewExists(GafferChoo):
        image "/gui/map/map_bar_check.png" xpos 1100 ypos 220 at tf_check_flash
    imagebutton auto "/gui/map/map_bar_%s.png" xpos 1100 ypos 220 action [Return("world_bar"),With(fade)]
    imagebutton auto "/gui/map/map_shop_%s.png" xpos 500 ypos 320 action [Return("shop"),With(fade)]
    imagebutton auto "/gui/map/map_church_%s.png" xpos 1520 ypos 320 action [Return("church"),With(fade)]
    imagebutton auto "/gui/map/map_oldfarm_%s.png" xpos 1350 ypos 0 action [Return("oldfarm"),With(fade)]
    imagebutton auto "/gui/map/map_town_square_%s.png" xpos 1080 ypos 590 action [Return("townsquare"),With(fade)]
    if Player.hr >= 3:
        imagebutton auto "/gui/map/map_prison_%s.png" xpos 831 ypos 670 action [Return("prison"),With(fade)]#0.2.0
    else:
        imagebutton auto "/gui/map/map_prison_%s.png" xpos 831 ypos 670 action [Return("prison_locked"),With(fade)]#0.2.0
    
    imagebutton auto "/gui/map/map_kingplace_%s.png" focus_mask True xpos 405 ypos -15 action [Return("kingplace"),With(fade)]
    
    if len(Player.quests) > 0:
        $_tf = openworldalert
    else:
        $_tf = None
    frame at _tf:
        xalign 1.0
        yalign 1.0
        background None
        imagebutton auto "/gui/ui/ui_gotoworldmap_%s.png" xalign 1.0 yalign 1.0 xoffset 70 yoffset 50 action Return("openworld")
    # textbutton "Go to open world" xalign 1.0 yalign 1.0 action Jump("SelectLocationToGo")#call QuestOpenMapLabel(_return["param"]) from _call_QuestOpenMapLabel
    # ui_gotoworldmap.png

label SelectLocationToGo:
    $renpy.block_rollback()
    scene MainMenuMap
    call screen gotol_locations_screen()
    if _return == "Cave maze" or _return == "Forest" or _return == "Village wall" or _return == "Mysterious cave" or _return == "Snow forest":
        if renpy.music.is_playing(channel="music_all") == False or renpy.music.get_playing(channel="music_all") != "/sound/%s.mp3"%(_return):
            $renpy.music.play("/sound/%s.mp3"%_return, channel="music_all")
    $renpy.block_rollback()
    if _return == "Snow forest":
        $worldmap.setCurLoc("NN00")
    if _return == "Mysterious cave":
        $worldmap.setCurLoc("CL03")
    if _return == "Cave maze":
        $worldmap.setCurLoc("JJ00")
    if _return == "Forest":
        $worldmap.setCurLoc("FL01")
    if _return == "Village wall":
        $worldmap.setCurLoc("AA00")
    if _return == "Return to village":
        jump world_map_label 
    if _return == "Cancel":
        jump world_map_label 
    if _return == "unlock_all_location":
        $RefreshPatronInfo()
        if IsHunter3OrHigher():
            $worldmap.unlockAllLocations()
        else:
            call screen become_a_patron_screen("AllLocations","Only {color=#e67a2a}Hunter 3{/color} or higher {color=#f96854}patrons{/color} tier have access to unlock all locations. Become a {color=#f96854}patron{/color} and get more options!") 
            $renpy.block_rollback()
        jump world_map_label 
    # menu:
        # "Select destination location:"
        # "Cave maze" if "Cave maze" in worldmap.unlocked_location:
            # $worldmap.setCurLoc("JJ00")
        # "Forest" if "Forest" in worldmap.unlocked_location:
            # $worldmap.setCurLoc("FL01")
        # "Village wall" if "Village wall" in worldmap.unlocked_location:
            # $worldmap.setCurLoc("AA00")
        # "Return":
            # jump world_map_label
    show blackscreen with fade
    jump OpenWorldMapLabel
            

image splash_label:
    "images/LustHunter/lusthunter.png"
 
label splashscreen:
    $renpy.block_rollback()
    scene blackscreen
    with Pause(1)
    
    scene lusthunter_lmp with dissolve
    with Pause(2)
    
    scene blackscreen with dissolve
    with Pause(1)
    
    show lusthunter_t with dissolve
    with Pause(0.7)
    
    show lusthunter_moles with dissolve
    with Pause(0.7)
    
    show lusthunter_huner with dissolve
    # show lusthunter_er with dissolve
    with Pause(1.5)
    
    scene lusthunter_bg with dissolve
    # show lusthunter
    # show lusthunter_er with dissolve
    # with Pause(0.5)

    return
        
label start:
    $check_errors = True
    $selected_window = None
    $selected_card = None
    $selected_card_upgrade = None
    $selected_enemy_sex = None
    $selected_enemy_stat = None
    # $_game_menu_screen = "preferences"
    $_game_menu_screen = "history"
    $shake = SShake((0, 0, 0, 0), 0.7, dist=15)
    # scene black
    # call screen test_face2
    $show_player = False
    $ bv = 0
    $your_turn = False
    $_time = 0
    $pw = ""
    $cur_version = config.version
    
    
    #+0.1.8
    
    #$renpy.music.play("celebration_tavern.mp3", channel="music_tavern")
    # if renpy.music.is_playing(channel="bg_music") == False:
        # $renpy.music.play(filenames, channel="bg_music", loop=True, fadeout = None , synchro_start = False , fadein = 0 , tight = None , if_changed = True)
        # renpy.music.set_pause(value, channel=u'music')
    #-0.1.8
    jump init_plot




label login_patreon_label:
    $renpy.block_rollback()
    if persistent.auth_code == "":
        $persistent.auth_code = GenRandomAuthCode()
    $renpy.run(OpenURL("%s/loginrenpy?gencode=%s"%(persistent.server, persistent.auth_code)))
    scene allow_patreon
    menu:
        
        "Click allow in your web browser and then select this option":
            python:
                try:
                    userList = json.loads(urllib2.urlopen(urllib2.Request(url='%s/getinfotier?gencode=%s'%(persistent.server, persistent.auth_code)), context = ssl._create_unverified_context()).read())
                    ret_status = userList["result"] 
                except:
                    ret_status = "Failed"
                
            if ret_status == "Sucsess":
                $persistent.uname = userList["uname"]
                $persistent.pledgecent = int(userList["curamount"])/100
                $persistent.uimg = userList["uimg"]
                $persistent.tier = userList["tier"]
                $persistent.follower = userList["follower"]
                $persistent.patron_status = userList["patron_status"]
                $persistent.pledge_cadence = userList["pledge_cadence"]
                python:
                    openurl = urllib2.build_opener()
                    openurl.addheaders = [('User-agent', 'Mozilla/5.0')]
                    page1 = openurl.open(persistent.uimg)
                    pic = page1.read()
                    filename = os.path.join("%s/images/"%config.gamedir, ("profile_image.png"))    # Might as well just make sure you know the file extension.
                    fout = open(filename, "wb")
                    fout.write(pic)
                    fout.close()
                # $renpy.Jump(persistent.next_label)
                jump create_new_char
            else:
                "Authorization failed...are you sure you clicked Allow?"
                menu:
                    "Try again":
                        jump login_patreon_label
                    "Skip and login to patreon later":
                        jump create_new_char
        # "Cancel":
            # jump create_new_char# $renpy.Jump(persistent.next_label)# jump create_new_char
   
label create_new_char:   
    $renpy.music.stop(channel="music_all")
    $renpy.block_rollback()
    if persistent.auth_code == "" or persistent.uname == "":
        menu:
            "Login to Patreon":
                jump login_patreon_label
            "Continue without login (some options will be limited)":
                $persistent.auth_code = ""
    $age = ""
    $cur_gender = ""
    $renpy.transition(fade)
    call screen character_select_screen
    
    $renpy.block_rollback()
    $cur_gender = _return
    if cur_gender == "female" or cur_gender == "futa":
        $renpy.sound.play("/sound/moan_female.mp3")
    else:
        $renpy.sound.play("/sound/select_char.mp3")
    $penis = None
    scene blackscreen
    $cur_type = "female"
    $gender_like = []
    if cur_gender == "female":
        $cur_type = "female"
    if cur_gender == "futa":
        menu:
            "small penis":
                $penis = Clothing("Small futa penis", "futa_small", ("penis", ),["futa"],None, 0, 0, 1, None, "", 1,"body")
                $cur_type = "futa_small"
            "mid penis":
                $penis = Clothing("Medium futa penis", "futa_mid", ("penis", ),["futa"],None, 0, 0, 1, None, "", 1,"body")
                $cur_type = "futa_mid"
    if cur_gender == "male":
        # menu:
            # "muscular":
        $penis = Clothing("Male muscular penis", "male_muscular_penis", ("penis", ),["male"],None, 0, 0, 1, None, "", 1,"body")
        $cur_type = "male_muscular"
    
    $_return = None
    call screen choose_gender_screen(cur_gender) 
    if cur_gender == "female" or cur_gender == "futa":
        $renpy.sound.play("/sound/moan_female.mp3")
    else:
        $renpy.sound.play("/sound/select_char.mp3")
    $renpy.block_rollback()    
    $gender_like = _return["genders"]    
    
    # $age = renpy.input("", default='20', allow='0123456789', length=3)
    $age = 20
    # name, gender, age, type, hp, max_hp, st, max_st,lust,max_lust, defense,attack, hr
    $Player = PlayerChar("Lust Madness", cur_gender, age, cur_type, 80, 4, 0, 0, 5, 1)   
    $Player.gender_like = gender_like
    
    if cur_gender == "female" or cur_gender == "futa":
        $exp_base_female = ["exp_eyeclose0_female","exp_eyeclose1_female","exp_eyeclose2_female","exp_eyeclose3_female","exp_eyeclose4_female","exp_eyeclose5_female","exp_eyeclose6_female","exp_eyeclose7_female"]
        $Player.exp_img = {"base":exp_base_female, "pain":exp_pain_female, "wow":exp_wow_female, "tongue":exp_tongue_female} #0.0.8
        $Player.ChangeBody(body_base)
        if cur_gender == "futa":
            $Player.penis = penis
            $Player.penis.equip(Player)
        $Player.ChangeHair("hair_type", hair_cady) 
        # $hair_list = [hair_cady, hair_gili, hair_turbblonde,hair_turbopink,hair_calista,hair_carla,hair_pina, hair_bald_head,hair_katarina,hair_redhead,hair_tifa,hair_lara,male_beard1,wizard_beard_male,hair_roxana,beard_bald_head]
        $Player.return_to_camp = {"0":"return_to_camp_cart1", "1":"return_to_camp_cart2", "2":"return_to_camp_cart3", "3":"return_to_camp_cart4"}
    if cur_gender == "male":   
        if cur_type == "male_muscular":
            $exp_base_male_muscular = ["exp_eyeclose0_male_muscular","exp_eyeclose1_male_muscular","exp_eyeclose2_male_muscular","exp_eyeclose3_male_muscular","exp_eyeclose4_male_muscular","exp_eyeclose5_male_muscular","exp_eyeclose6_male_muscular","exp_eyeclose7_male_muscular"]
            $Player.ChangeBody(body_male_muscular)
            $Player.exp_img = {"base":exp_base_male_muscular, "pain":exp_pain_male_muscular}
            $Player.ChangeHair("hair_type", hair_bald_head) 
            # $hair_list = [hair_bald_head]
            $Player.penis = penis
            $Player.penis.equip(Player)
        $Player.return_to_camp = {"0":"return_to_camp_cart1_male", "1":"return_to_camp_cart2_male", "2":"return_to_camp_cart3_male", "3":"return_to_camp_cart4_male"}
    $Player.current_exp = "base"
    
    
    $Player.check_info.append("home_wardrobe")
    $Player.check_info.append("home_attacks")  
    $Player.check_info.append("home_sexskills")
    $Player.check_info.append("village_tavern_GafferChoo")
    $Player.check_info.append("village_tavern_Mirana")
     
    jump init_var

    return

screen character_select_screen():
    add "black"
    text "Choose a character:" xalign 0.5 yoffset 25
    hbox:
        yoffset 150
        frame:
            xminimum 640
            xmaximum 640
            background None
            imagebutton auto "player_female_%s" action Return("female") hover_sound "/sound/select_char_hover.mp3"
            image hair_cady.img[0] xzoom 0.5 yzoom 0.5
        frame:
            xminimum 640
            xmaximum 640
            background None
            imagebutton auto "player_futa_%s" action Return("futa") hover_sound "/sound/select_char_hover.mp3"
            image hair_cady.img[0] xzoom 0.5 yzoom 0.5
        frame:
            xminimum 640
            xmaximum 640
            background None
            imagebutton auto "player_male_%s" action Return("male") hover_sound "/sound/select_char_hover.mp3"

label world_map_label:
    if renpy.music.is_playing(channel="music_all") == False or renpy.music.get_playing(channel="music_all") != "/sound/village.mp3":
        $renpy.music.play("/sound/village.mp3", channel="music_all")
    # if renpy.music.is_playing(channel="music_village") == False:
        # $renpy.music.play("/sound/village.mp3", channel="music_village")
    # if renpy.music.get_pause(channel="music_village"):
        # $renpy.music.set_pause(False, channel="music_village")
    $renpy.block_rollback()
    $selected_item = None
    scene MainMenuMap with fade
    # hide screen player_for_dialoge
    call screen world_map
    $renpy.block_rollback()
    if _return == "house":
        jump world_map_label_house#call screen world_map_house
    elif _return == "world_bar":
        # $show_player = True
        # $renpy.music.set_pause(True, channel="music_village")
        jump world_map_label_bar#call screen world_map_bar
    # elif _return == "craft":
        # call screen world_map_craft
    elif _return == "shop":
        jump world_map_label_shop
    elif _return == "kingplace":
        jump world_map_label_kingplace
    elif _return == "church":
        # $renpy.show_screen("player_for_dialoge", char_appear_left_to_right, 1, 0.85)
        # show screen nunchurch_for_dialoge
        $ee = NunChurch.name
        # $RefreshPatronInfo() 
        scene MainMenuMap
        if IsTiers():
            jump world_map_patrons_church
        else:
            call screen become_a_patron_screen("Church","Only {color=#f96854}patrons{/color} have access to Patrons Church. Become a {color=#f96854}patron{/color} and get more options!")
            $renpy.block_rollback()
            jump world_map_label
        # hide screen player_for_dialoge
        # hide screen nunchurch_for_dialoge
    elif _return == "oldfarm":
        "Old farm in active development"
        # call screen world_map_shop
    elif _return == "townsquare":
        jump world_townsquare_label
        # menu:
        # "There is nothing in the town square now. Come back later."
            #"Town square will be available when I reach 50 patrons on my patreon page. (In the game version above 0.0.4)"
            # "Go to patreon.com/LustMadness":
                # $renpy.run(OpenURL("https://www.patreon.com/LustMadness?fan_landing=true"))
            # "Return":
                # jump world_map_label
    elif _return == "prison":
        jump world_prison_label
    elif _return == "prison_locked":
        "Your HR is too low. HR must be 3 or more. Complete the tavern quests!"
        jump world_map_label
    elif _return == "openworld":
        jump SelectLocationToGo
    jump world_map_label
     
# --------------------------------------------------------------------------------------------------
    
label init_var: 
    $renpy.block_rollback()
    $_page = 0 #0.0.5
    $get_church_reward = False
    # $gamemenu = renpy.config.game_menu_action
    $skills_effects_list = []
    $current_enemy = None
    $current_quest = None
    $current_battle = None #0.0.9
    $_notify = ""
    
    $char_visible = True
    #++++++++++++++++++++++enemy+++++++++++++++++++++++
    #(self, name, desc,img,img_stat, gender, size_min, size_max, hp, max_hp, st, max_st, defense,rank,is_dead):
    $monster_list = [] #0.0.5
    
    #Satyr male
    $enemy_satyr_tactics_m = EnemyTactics()
    $enemy_satyr_tactics_m.AddTactics({"phase":0, "type":"lust", "from_to":(0,100), "type_choice_attack":"row", "cards": ({"attack":card_skill_hoof, "from_to":(0,0)}, {"attack":card_attack_satyr, "from_to":(1,1)}, {"attack":card_attack_satyr2, "from_to":(2,2)})})
    $enemy_satyr_desc_m = EnemyDesc("Satyr","satyr","Lives in the forest. Aggressive. He has horns, fur and a large cock.", "satyr_m", "idle","male",30,({"from":11,"to":100,"item":item_cloth_piece,"condition":None},{"from":0,"to":5,"item":item_satyr_horn,"condition":None},{"from":6,"to":10,"item":item_satyr_fur,"condition":None},{"from":0,"to":100,"item":item_satyr_cum,"condition":"cum"}), {"first":"Are you lost? Give you directions to my dick?"},{"sex_type":"satyr_enemysex", "img":"satyr_m_enemysex_anim","max_lust":0,"lust":0,"cum":{"cum_type":"Cum", "img":"/Enemies/satyr_m/satyr_male_enemysex_cum.jpg","effect":"face_cum"}}, enemy_satyr_tactics_m, [], True, 0.6, (0,0), None, [card_attack_twinstrike, card_attack_boobsstrike])#, 1, 1, 40, 40, 15, 15,10,10, 5,7, 1, False)
    
    #Satyr female
    $enemy_satyr_tactics_f = EnemyTactics()
    $enemy_satyr_tactics_f.AddTactics({"phase":0, "type":"lust", "from_to":(0,100), "type_choice_attack":"row", "cards": ({"attack":card_attack_satyr, "from_to":(0,0)}, {"attack":card_skill_hoof, "from_to":(1,1)}, {"attack":card_skill_gotstrength, "from_to":(2,2)})})
    $enemy_satyr_desc_f = EnemyDesc("Satyr","satyr","Lives in the forest. Aggressive. She has horns, fur and a tight pussy.", "satyr_f", "idle","female",30,({"from":11,"to":100,"item":item_cloth_piece,"condition":None},{"from":0,"to":5,"item":item_satyr_horn,"condition":None},{"from":6,"to":10,"item":item_satyr_fur,"condition":None},{"from":0,"to":100,"item":item_satyr_cum,"condition":"cum"}), {"first":"Are you lost? Give you directions to my pussy?"},{"sex_type":"satyr_enemysex", "img":"satyr_m_enemysex_anim","max_lust":0,"lust":0,"cum":{"cum_type":"Cum", "img":"/Enemies/satyr_m/satyr_male_enemysex_cum.jpg","effect":"face_cum"}}, enemy_satyr_tactics_f, [], True, 0.6, (0,0), None, [card_attack_twinstrike, card_attack_boobsstrike])#, 1, 1, 40, 40, 15, 15,10,10, 5,7, 1, False)
    $enemy_satyr_desc_f.img["naked1"] = "/Enemies/satyr_f/satyr_f_naked.png"
    
    #Satyr futa #0.2.5
    $enemy_satyr_tactics_futa = EnemyTactics()
    $enemy_satyr_tactics_futa.AddTactics({"phase":0, "type":"lust", "from_to":(0,100), "type_choice_attack":"row", "cards": ({"attack":card_attack_satyr, "from_to":(0,0)}, {"attack":card_skill_hoof, "from_to":(1,1)}, {"attack":card_skill_gotstrength, "from_to":(2,2)})})
    $enemy_satyr_desc_futa = EnemyDesc("Satyr","satyr","Lives in the forest. Aggressive. She has horns, fur and a large cock.", "satyr_futa", "idle","futa",30,({"from":11,"to":100,"item":item_cloth_piece,"condition":None},{"from":0,"to":5,"item":item_satyr_horn,"condition":None},{"from":6,"to":10,"item":item_satyr_fur,"condition":None},{"from":0,"to":100,"item":item_satyr_cum,"condition":"cum"}), {"first":"Are you lost? Give you directions to my pussy?"},{"sex_type":"satyr_enemysex", "img":"satyr_m_enemysex_anim","max_lust":0,"lust":0,"cum":{"cum_type":"Cum", "img":"/Enemies/satyr_m/satyr_male_enemysex_cum.jpg","effect":"face_cum"}}, enemy_satyr_tactics_futa, [], True, 0.6, (0,0), None, [card_attack_twinstrike, card_attack_boobsstrike])#, 1, 1, 40, 40, 15, 15,10,10, 5,7, 1, False)
    $enemy_satyr_desc_futa.img["naked1"] = "/Enemies/satyr_futa/satyr_futa_naked.png"
    # $monster_list.append(enemy_satyr_desc_futa)
    
    #FlyDick 0.0.9    
    $enemy_flydick_tactics = EnemyTactics()
    $enemy_flydick_tactics.AddTactics({"phase":0, "type":"lust", "from_to":(0,100), "type_choice_attack":"row", "cards": ({"attack":card_attack_lickbetweenlegs, "from_to":(0,0)},{"attack":card_skill_gotstrength, "from_to":(1,1)})})
    $enemy_flydick_desc_m = EnemyDesc("Flying dick","flydick","It's a natural cock with wings. Lives in the caves. Aggressive. Live in flocks. With them you will love gangbang and bukake", "flydick", "idle","male",15,({"from":0,"to":70,"item":item_leather_piece,"condition":None},{"from":71,"to":100,"item":item_mucus,"condition":None},{"from":0,"to":100,"item":item_flydick_cum,"condition":"cum"}),{"first":"PhhaaaMWHAAaaaa Ktsccccccc TCHHHHH!"},{"sex_type":"flydick_enemysex", "img":"flydick_enemysex_anim","max_lust":0,"lust":0,"cum":None}, enemy_flydick_tactics, [], True, 0.5)#,{"sex_type":"threesome", "img":"","max_lust":40,"lust":0,"cum":None},{"sex_type":"bukake", "img":"","max_lust":80,"lust":0,"cum":None}
        
    #FlyDick Queen 0.1.7    
    $enemy_flydick_f_tactics = EnemyTactics()
    $enemy_flydick_f_tactics.AddTactics({"phase":0, "type":"lust", "from_to":(0,100), "type_choice_attack":"row", "cards": ({"attack":card_attack_lickbetweenlegs, "from_to":(0,0)},{"attack":card_skill_gotstrength, "from_to":(1,1)})})
    $enemy_flydick_desc_f = EnemyDesc("Flydick's Queen","flydickqueen","It's a natural snake with half-female. Without pussy. Lives in the caves. Aggressive. Live in flocks. With them you will love gangbang and bukake", "flydick_f", "idle","female",15,({"from":0,"to":70,"item":item_leather_piece,"condition":None},{"from":71,"to":100,"item":item_mucus,"condition":None},{"from":0,"to":100,"item":item_flydick_cum,"condition":"cum"}),{"first":"PhhaaaMWHAAaaaa Ktsccccccc TCHHHHH!"},{"sex_type":"flydick_enemysex", "img":"flydick_enemysex_anim","max_lust":0,"lust":0,"cum":None}, enemy_flydick_f_tactics, [], True, 0.5, (-70, -50+150))#,{"sex_type":"threesome", "img":"","max_lust":40,"lust":0,"cum":None},{"sex_type":"bukake", "img":"","max_lust":80,"lust":0,"cum":None}
    $enemy_flydick_desc_f.img["naked1"] = "/Enemies/flydick_f/flydick_f_naked1.png"
    $enemy_flydick_desc_f.img["naked2"] = "/Enemies/flydick_f/flydick_f_naked2.png"    
    
    #Flydick Queen futa #0.2.5
    $enemy_flydick_futa_tactics = EnemyTactics()
    $enemy_flydick_futa_tactics.AddTactics({"phase":0, "type":"lust", "from_to":(0,100), "type_choice_attack":"row", "cards": ({"attack":card_attack_lickbetweenlegs, "from_to":(0,0)},{"attack":card_skill_gotstrength, "from_to":(1,1)})})
    $enemy_flydick_desc_futa = EnemyDesc("Flydick's Queen futa","flydick","It's a natural snake without tail and with legs and huge cock. Lives in the caves. Aggressive. Live in flocks. With them you will love gangbang and bukake", "flydick_futa", "idle","futa",15,({"from":0,"to":70,"item":item_leather_piece,"condition":None},{"from":71,"to":100,"item":item_mucus,"condition":None},{"from":0,"to":100,"item":item_flydick_cum,"condition":"cum"}),{"first":"PhhaaaMWHAAaaaa Ktsccccccc TCHHHHH!"},{"sex_type":"flydick_enemysex", "img":"flydick_enemysex_anim","max_lust":0,"lust":0,"cum":None}, enemy_flydick_futa_tactics, [], True, 0.6, (-70, -40))#,{"sex_type":"threesome", "img":"","max_lust":40,"lust":0,"cum":None},{"sex_type":"bukake", "img":"","max_lust":80,"lust":0,"cum":None}
    $enemy_flydick_desc_futa.img["naked1"] = "/Enemies/flydick_futa/flydick_futa_naked1.png"
    $enemy_flydick_desc_futa.img["naked2"] = "/Enemies/flydick_futa/flydick_futa_naked2.png" 
    # $monster_list.append(enemy_flydick_desc_futa)
       
    #forest_fairy 0.0.9
    $enemy_forest_fairy_tactics = EnemyTactics()
    $enemy_forest_fairy_tactics.AddTactics({"phase":0, "type":"lust", "from_to":(0,100), "type_choice_attack":"row", "cards": ({"attack":card_attack_wings, "from_to":(0,0)},{"attack":card_skill_pollen, "from_to":(1,1)})})
    # $enemy_forest_fairy_desc_f = EnemyDesc("Forest fairy", "She is a playful forest girl with huge wings and boobs. She can heal herself in battle", "forest_fairy_f", "idle", "female", ({"from":51,"to":100,"item":item_cloth_piece,"condition":None},{"from":0,"to":50,"item":item_hairs,"condition":None}, {"from":0,"to":100,"item":item_pollen,"condition":"cum"}), {"first":"Hi, honey! You are so sweety!", "d1":"If you lose, you will lick my hairy pussy :3"}, {"sex_type":"forest_fairy_enemysex", "img":"forest_fairy_enemysex_anim","max_lust":0,"lust":0,"cum":None}, ({"sex_type":"scissors", "img":"forest_fairy_scissors_anim","need_max_lust":0,"max_lust":0,"lust":0,"cum":{"cum_type":"cum", "img":"/Enemies/forest_fairy_f/anim/forest_fairy_scissors_anim2_02.jpg","effect":None}},), {"sex_type":"forest_fairy_masturbated", "img":"forest_fairy_masturbated_anim","max_lust":0,"lust":0,"cum":{"cum_type":"Cum", "img":"/Enemies/forest_fairy_f/anim/forest_fairy_masturbated_anim05.jpg","effect":None}}, enemy_forest_fairy_tactics, [], True, 0.45)
    $enemy_forest_fairy_desc_f = EnemyDesc("Forest fairy","forest_fairy", "She is a playful forest girl with huge wings and boobs. She can heal herself in battle", "forest_fairy_f", "idle", "female",70, ({"from":51,"to":100,"item":item_cloth_piece,"condition":None},{"from":0,"to":50,"item":item_hairs,"condition":None}, {"from":0,"to":100,"item":item_pollen,"condition":"cum"}), {"first":"Hi, honey! You are so sweety!", "d1":"If you lose, you will lick my hairy pussy :3"}, {"sex_type":"forest_fairy_enemysex", "img":"forest_fairy_enemysex_anim","max_lust":0,"lust":0,"cum":None}, enemy_forest_fairy_tactics, [], True, 0.45)
    $enemy_forest_fairy_desc_f.img["naked1"] = "/Enemies/forest_fairy_f/forest_fairy_f_naked1.png"
    $enemy_forest_fairy_desc_f.img["naked2"] = "/Enemies/forest_fairy_f/forest_fairy_f_naked2.png"
    
    
    #Nymph 0.0.9
    $enemy_nymph_tactics = EnemyTactics()
    $enemy_nymph_tactics.AddTactics({"phase":0, "type":"lust", "from_to":(0,100), "type_choice_attack":"row", "cards": ({"attack":card_attack_lighthugs1, "from_to":(0,0)},{"attack":card_attack_lighthugs2, "from_to":(1,1)},{"attack":card_attack_lighthugs3, "from_to":(2,2)},{"attack":card_attack_lighthugs4, "from_to":(3,3)},{"attack":card_attack_lighthugs5, "from_to":(4,4)},{"attack":card_attack_lighthugs6, "from_to":(5,5)},{"attack":card_attack_lighthugs7, "from_to":(6,6)},{"attack":card_attack_lighthugs8, "from_to":(7,7)})})
    # $enemy_nymph_desc_f = EnemyDesc("Nymph", "She is a pretty girl with elf's ears. She is very friendly", "nymph", "idle", "female", ({"from":61,"to":100,"item":item_cloth_piece,"condition":None},{"from":10,"to":60,"item":item_hairs,"condition":None},{"from":0,"to":9,"item":item_ivy,"condition":None}), {"first":"Hiiiya!", "d1":"If you lose, I'll touch you by my wooden dildo"}, {"sex_type":"nymph_enemysex", "img":"nymph_enemysex_anim","max_lust":0,"lust":0,"cum":None}, ({"sex_type":"cunnilingus_dom", "img":"nymph_cunnilingus_anim","need_max_lust":50,"max_lust":50,"lust":0,"cum":None},), {"sex_type":"nymph_masturbated", "img":"nymph_masturbated_anim","max_lust":0,"lust":0,"cum":None}, enemy_nymph_tactics ,[], True, 0.5)
    $enemy_nymph_desc_f = EnemyDesc("Nymph","nymph", "She is a pretty girl with elf's ears. She is very friendly", "nymph", "idle", "female",60, ({"from":61,"to":100,"item":item_cloth_piece,"condition":None},{"from":10,"to":60,"item":item_hairs,"condition":None},{"from":0,"to":9,"item":item_ivy,"condition":None}), {"first":"Hiiiya!", "d1":"If you lose, I'll touch you by my wooden dildo"}, {"sex_type":"nymph_enemysex", "img":"nymph_enemysex_anim","max_lust":0,"lust":0,"cum":None}, enemy_nymph_tactics ,[], True, 0.5)
    $enemy_nymph_desc_f.img["naked1"] = "/Enemies/nymph/nymph_naked1.png"
    $enemy_nymph_desc_f.img["lust"] = "nymph_lust_anim"
    $enemy_nymph_desc_f.available_catch = True
    
    #Nymph futa 0.3.0
    $enemy_nymph_futa_tactics = EnemyTactics()
    $enemy_nymph_futa_tactics.AddTactics({"phase":0, "type":"lust", "from_to":(0,100), "type_choice_attack":"row", "cards": ({"attack":card_attack_lighthugs1, "from_to":(0,0)},{"attack":card_attack_lighthugs2, "from_to":(1,1)},{"attack":card_attack_lighthugs3, "from_to":(2,2)},{"attack":card_attack_lighthugs4, "from_to":(3,3)},{"attack":card_attack_lighthugs5, "from_to":(4,4)},{"attack":card_attack_lighthugs6, "from_to":(5,5)},{"attack":card_attack_lighthugs7, "from_to":(6,6)},{"attack":card_attack_lighthugs8, "from_to":(7,7)})})
    $enemy_nymph_futa_desc = EnemyDesc("Nymph","nymph", "She is a pretty girl with elf's ears. She is very friendly", "nymph_futa", "idle", "futa",60, ({"from":61,"to":100,"item":item_cloth_piece,"condition":None},{"from":10,"to":60,"item":item_hairs,"condition":None},{"from":0,"to":9,"item":item_ivy,"condition":None}), {"first":"Hiiiya!", "d1":"If you lose, I'll touch you by my wooden dildo"}, {"sex_type":"nymph_enemysex", "img":"nymph_enemysex_anim","max_lust":0,"lust":0,"cum":None}, enemy_nymph_futa_tactics ,[], True, 0.5)
    $enemy_nymph_futa_desc.img["naked1"] = "/Enemies/nymph_futa/nymph_futa_naked1.png"
    $enemy_nymph_futa_desc.img["lust"] = "nymph_futa_lust_anim"
    $enemy_nymph_futa_desc.available_catch = True
    
    
    #enemy_muscular 0.0.9
    $enemy_muscular_tactics = EnemyTactics()
    $enemy_muscular_tactics.AddTactics({"phase":0, "type":"lust", "from_to":(0,49), "type_choice_attack":"row", "cards": ({"attack":card_skill_getarmor10, "from_to":(0,0)},{"attack":card_attack_heavyslap, "from_to":(1,1)})})
    $enemy_muscular_tactics.AddTactics({"phase":1, "type":"lust", "from_to":(50,100), "type_choice_attack":"row", "cards": ({"attack":card_skill_getarmor10, "from_to":(0,0)},{"attack":card_attack_veryheavyslap, "from_to":(1,1)})})
    # $enemy_muscular_desc_f = EnemyDesc("Muscle female", "She is a very strong. She once lifted a cow and threw it on the roof of a barn. She loves to use a strapon. Your holes are in danger.", "muscular_f", "idle", "female", ({"from":5,"to":100,"item":item_testosterone,"condition":None},{"from":0,"to":4,"item":item_ivy,"condition":None}), {"first":"Stop!", "d1":"If you donâ€™t lick my pussy, Iâ€™ll crush your head like a pumpkin"}, {"sex_type":"muscular_female_enemysex", "img":"muscular_f_enemysex_anim","max_lust":0,"lust":0,"cum":None}, ({"sex_type":"vaginal_sex_sub", "img":"muscular_f_vaginal_anim","need_max_lust":50,"max_lust":50,"lust":0,"cum":None},), {"sex_type":"muscular_female_solo", "img":"muscular_f_solodildo_anim","max_lust":0,"lust":0,"cum":None},enemy_muscular_tactics ,[mod_barricade], True, 0.55)
    $enemy_muscular_desc_f = EnemyDesc("Muscle female","muscular", "She is a very strong. She once lifted a cow and threw it on the roof of a barn. She loves to use a strapon. Your holes are in danger.", "muscular_f", "idle", "female", 90, ({"from":5,"to":100,"item":item_testosterone,"condition":None},{"from":0,"to":4,"item":item_ivy,"condition":None}), {"first":"Stop!", "d1":"If you donâ€™t lick my pussy, Iâ€™ll crush your head like a pumpkin"}, {"sex_type":"muscular_female_enemysex", "img":"muscular_f_enemysex_anim","max_lust":0,"lust":0,"cum":None},enemy_muscular_tactics ,[mod_barricade], True, 0.55)
    $enemy_muscular_desc_f.img["naked1"] = "/Enemies/muscular_f/muscular_f_naked1.png"
    $enemy_muscular_desc_f.available_catch = True
    
    #skeleton 0.0.9
    $enemy_skeleton_tactics = EnemyTactics()
    $enemy_skeleton_tactics.AddTactics({"phase":0, "type":"hp", "from_to":(0,100), "type_choice_attack":"row", "cards": ({"attack":card_skill_getarmor10, "from_to":(0,0)},{"attack":card_skill_gotstrength, "from_to":(1,1)},{"attack":card_attack_skeleton3, "from_to":(2,2)})})
    $enemy_skeleton_desc = EnemyDesc("Skeleton","skeleton", "Lots of bones", "skeleton", "idle", "male", 30, ({"from":0,"to":100,"item":item_bone,"condition":None},), {"first":"I need flesh!"}, None, enemy_skeleton_tactics, [], True, 0.6)
    
    #giant orc 0.1.1
    $enemy_orc_tactics = EnemyTactics() 
    $enemy_orc_tactics.AddTactics({"phase":0, "type":"lust", "from_to":(0,35), "type_choice_attack":"row", "cards": ({"attack":card_skill_getarmor50, "from_to":(0,0)},{"attack":card_attack_orc1, "from_to":(1,1)},{"attack":card_skill_gotstrength5, "from_to":(2,2)},{"attack":card_attack_orc2, "from_to":(3,3)})})
    $enemy_orc_tactics.AddTactics({"phase":1, "type":"lust", "from_to":(36,100), "type_choice_attack":"row", "cards": [{"attack":card_skill_escape0, "from_to":(0,0)}]})
    $enemy_orc_tactics2 = EnemyTactics() 
    $enemy_orc_tactics2.AddTactics({"phase":0, "type":"lust", "from_to":(0,100), "type_choice_attack":"row", "cards": ({"attack":card_skill_getarmor50, "from_to":(0,0)},{"attack":card_attack_orc1, "from_to":(1,1)},{"attack":card_skill_gotstrength5, "from_to":(2,2)},{"attack":card_attack_orc2, "from_to":(3,3)})})
    $enemy_orc_desc = EnemyDesc("Giant orc","giantorc", "He is huge. He is green. And he's got a giant dick.", "orc_m", "idle", "male", 300,({"from":5,"to":100,"item":item_orc_skin,"condition":None},{"from":0,"to":4,"item":item_orc_fang,"condition":None}), {"first":"*GrrrrRRRRrrrrr!*", "d1":"*GRRrrrrr* ORC *grrrrrrrr* WANTS *grrrRRrrr* FUUUUCK"}, {"sex_type":"orc_male_enemysex", "img":"orc_male_enemysex_anim","max_lust":0,"lust":0,"cum":None},enemy_orc_tactics,[mod_barricade], True, 0.55, (-300,-650), "first_view_label_orc_m")
    
    #giant orc Female 0.1.7
    $enemy_orc_f_tactics = EnemyTactics() 
    $enemy_orc_f_tactics.AddTactics({"phase":0, "type":"lust", "from_to":(0,35), "type_choice_attack":"row", "cards": ({"attack":card_skill_getarmor50, "from_to":(0,0)},{"attack":card_attack_orc1, "from_to":(1,1)},{"attack":card_skill_gotstrength5, "from_to":(2,2)},{"attack":card_attack_orc2, "from_to":(3,3)})})
    $enemy_orc_f_tactics.AddTactics({"phase":1, "type":"lust", "from_to":(36,100), "type_choice_attack":"row", "cards": [{"attack":card_skill_escape0, "from_to":(0,0)}]})
    $enemy_orc_f_tactics2 = EnemyTactics() 
    $enemy_orc_f_tactics2.AddTactics({"phase":0, "type":"lust", "from_to":(0,100), "type_choice_attack":"row", "cards": ({"attack":card_skill_getarmor50, "from_to":(0,0)},{"attack":card_attack_orc1, "from_to":(1,1)},{"attack":card_skill_gotstrength5, "from_to":(2,2)},{"attack":card_attack_orc2, "from_to":(3,3)})})
    $enemy_orc_f_desc = EnemyDesc("Female orc","orc", "She is huge. She is green. And she's got a big tits.", "orc_f", "idle", "female", 300, ({"from":5,"to":100,"item":item_orc_skin,"condition":None},{"from":0,"to":4,"item":item_orc_fang,"condition":None}), {"first":"*GrrrrRRRRrrrrr!*", "d1":"*GRRrrrrr* ORC *grrrrrrrr* WANTS *grrrRRrrr* FUUUUCK"}, {"sex_type":"orc_male_enemysex", "img":"orc_male_enemysex_anim","max_lust":0,"lust":0,"cum":None},enemy_orc_f_tactics,[mod_barricade], True, 0.35, (-200, -200))
    $enemy_orc_f_desc.img["naked1"] = "/Enemies/orc_f/orc_f_naked1.png"
    
    #enemy_mushroomqueen_female 0.2.3
    $enemy_mushroomqueen_tactics = EnemyTactics()
    $enemy_mushroomqueen_tactics.AddTactics({"phase":0, "type":"lust", "from_to":(0,100), "type_choice_attack":"row", "cards": ({"attack":card_attack_heavyslap15, "from_to":(0,0)},{"attack":card_attack_heavyslap15, "from_to":(1,1)},{"attack":card_skill_gotstrength3, "from_to":(2,2)})})
    $enemy_mushroomqueen_desc_f = EnemyDesc("Mushrooms queen","mushroom_queen", "She has a huge hat on her head. She has huge tits and an ass. She always hides her face.", "mushroom_queen_f", "idle", "female", 80, ({"from":55,"to":100,"item":item_poisonshroom,"condition":None},{"from":10,"to":55,"item":item_amanita,"condition":None},{"from":0,"to":10,"item":item_mushroom_slime,"condition":None}), {"first":"Oooo don't come near me, I'm ashamed of you!"}, None,enemy_mushroomqueen_tactics,[mod_defencepoison], True, 0.50)
    $enemy_mushroomqueen_desc_f.img["naked1"] = "/Enemies/mushroom_queen_f/mushroom_queen_f_naked1.png"
    $enemy_mushroomqueen_desc_f.difficulty_hp = 15
    
    #enemy_mushroomqueen_futa 0.2.8
    $enemy_mushroomqueen_futa_tactics = EnemyTactics()
    $enemy_mushroomqueen_futa_tactics.AddTactics({"phase":0, "type":"lust", "from_to":(0,100), "type_choice_attack":"row", "cards": ({"attack":card_attack_heavyslap15, "from_to":(0,0)},{"attack":card_attack_heavyslap15, "from_to":(1,1)},{"attack":card_skill_gotstrength3, "from_to":(2,2)})})
    $enemy_mushroomqueen_desc_futa = EnemyDesc("Mushrooms queen","mushroom_queen", "She has a huge hat on her head. She has huge tits and an ass. She always hides her face.", "mushroom_queen_futa", "idle", "futa", 80, ({"from":55,"to":100,"item":item_poisonshroom,"condition":None},{"from":10,"to":55,"item":item_amanita,"condition":None},{"from":0,"to":10,"item":item_mushroom_slime,"condition":None}), {"first":"Oooo don't come near me, I'm ashamed of you!"}, None,enemy_mushroomqueen_tactics,[mod_defencepoison], True, 0.50)
    $enemy_mushroomqueen_desc_futa.img["naked1"] = "/Enemies/mushroom_queen_futa/mushroom_queen_futa_naked1.png"
    $enemy_mushroomqueen_desc_futa.difficulty_hp = 20
    
    #enemy_slime_female 0.2.9
    $enemy_slime_acid_tactics = EnemyTactics()
    $enemy_slime_acid_tactics.AddTactics({"phase":0, "type":"lust", "from_to":(0,100), "type_choice_attack":"row", "cards": ({"attack":card_attack_corrosive_spit, "from_to":(0,0)}, {"attack":card_attack_lick_weak, "from_to":(1,1)}, {"attack":card_attack_tackle, "from_to":(2,2)})})
    $enemy_slime_acid_desc = EnemyDesc("Acid slime", "acidslime", "acidslime", "acidslime", "idle", "male",15, None, None, None, enemy_slime_acid_tactics, [mod_servant, mod_defend_boss], False)
    $enemy_slime_acid_desc.img = {"hide":"/Enemies/slime_f/slime_servant.png","idle":"/Enemies/slime_f/slime_servant.png", "naked":"/Enemies/slime_f/slime_servant.png","lust":"/Enemies/slime_f/slime_servant.png"}
    $enemy_slime_acid_desc.icon = "/Enemies/slime_f/slime_f_icon.png"
    $enemy_slime_spike_tactics = EnemyTactics()
    $enemy_slime_spike_tactics.AddTactics({"phase":0, "type":"lust", "from_to":(0,100), "type_choice_attack":"row", "cards": ({"attack":card_attack_lick_frail, "from_to":(0,0)}, {"attack":card_attack_corrosive_spit, "from_to":(1,1)})})
    $enemy_slime_spike_desc = EnemyDesc("Spike slime", "spikeslime", "spikeslime", "spikeslime", "idle", "male",15, None, None, None, enemy_slime_spike_tactics, [mod_servant, mod_defend_boss], False)
    $enemy_slime_spike_desc.img = {"hide":"/Enemies/slime_f/slime_servant.png","idle":"/Enemies/slime_f/slime_servant.png", "naked":"/Enemies/slime_f/slime_servant.png","lust":"/Enemies/slime_f/slime_servant.png"}
    $enemy_slime_spike_desc.icon = "/Enemies/slime_f/slime_f_icon.png"
    
    $enemy_slime_f_tactics = EnemyTactics()
    $enemy_slime_f_tactics.boss = True
    $enemy_slime_f_tactics.servants = [enemy_slime_acid_desc, enemy_slime_spike_desc]
    $enemy_slime_f_tactics.AddTactics({"phase":0, "type":"lust", "from_to":(0,50), "type_choice_attack":"row", "cards": ({"attack":card_skill_slimed3, "from_to":(0,0)},{"attack":card_skill_prepared, "from_to":(1,1)},{"attack":card_attack_slam, "from_to":(2,2)})})
    $enemy_slime_f_tactics.AddTactics({"phase":1, "type":"lust", "from_to":(50,100), "type_choice_attack":"row", "cards": ({"attack":card_skill_gotstrength3_all, "from_to":(0,0)},{"attack":card_skill_prepared, "from_to":(1,1)})})
    $enemy_slime_desc_f = EnemyDesc("Slime girl","slime", "She is green and very slimy. She is a little transparent so objects are visible inside she. If she catches you, she won't let you go.", "slime_f", "idle", "female", 140, ({"from":0,"to":50,"item":item_slime_part,"condition":None},{"from":51,"to":90,"item":item_slime_fluid,"condition":None},{"from":91,"to":100,"item":item_slime_stone,"condition":None}), {"first":"Do you want to touch me?"}, None,enemy_slime_f_tactics,[], True, 0.50)
    $enemy_slime_desc_f.difficulty_hp = 20
    
    #enemy_domwidow_f 0.3.2
    $enemy_domwidow_f_tactics = EnemyTactics()
    $enemy_domwidow_f_tactics.AddTactics({"phase":0, "type":"img_stat", "from_to":["idle","naked1","naked2"], "type_choice_attack":"row", "cards": ({"attack":card_skill_naked, "from_to":(0,0)},{"attack":card_skill_gotstrength3, "from_to":(1,1)},{"attack":card_skill_gotstrength3, "from_to":(2,2)},{"attack":card_skill_gotstrength5, "from_to":(3,3)},{"attack":card_attack_lashblow, "from_to":(4,4)})})
    $enemy_domwidow_f_tactics.AddTactics({"phase":1, "type":"img_stat", "from_to":["naked3"], "type_choice_attack":"row", "cards": ({"attack":card_attack_widow, "from_to":(0,0)},{"attack":card_skill_gotstrength, "from_to":(1,1)},{"attack":card_skill_gotstrength3, "from_to":(2,2)},{"attack":card_skill_gotstrength5, "from_to":(3,3)},{"attack":card_attack_lashblow, "from_to":(4,4)})})
    $enemy_domwidow_f_tactics.AddTactics({"phase":2, "type":"img_stat", "from_to":["naked4","lust"], "type_choice_attack":"row", "cards": ({"attack":card_skill_gotstrength5, "from_to":(0,0)},{"attack":card_skill_gotstrength5, "from_to":(1,1)},{"attack":card_attack_lashblow_x5, "from_to":(2,2)})})
    $enemy_domwidow_desc_f = EnemyDesc("Dom widow","domwidow", "This lonely woman hasn't been with a man for a long time. Because of this, she is very wayward. She will try to dominate you.", "domwidow_f", "idle", "female", 300, ({"from":55,"to":100,"item":item_max_potion,"condition":None},{"from":10,"to":55,"item":item_max_potion,"condition":None},{"from":0,"to":10,"item":item_rare_cloth,"condition":None}), {"first":"I said take off your clothes!"}, None,enemy_domwidow_f_tactics,[mod_naked3_inv], True, 0.50)
    $enemy_domwidow_desc_f.img["naked"] = "/Enemies/domwidow_f/domwidow_f_naked1.png"
    $enemy_domwidow_desc_f.img["naked1"] = "/Enemies/domwidow_f/domwidow_f_naked1.png"
    $enemy_domwidow_desc_f.img["naked2"] = "/Enemies/domwidow_f/domwidow_f_naked2.png"
    $enemy_domwidow_desc_f.img["naked3"] = "/Enemies/domwidow_f/domwidow_f_naked3.png"
    $enemy_domwidow_desc_f.img["naked4"] = "/Enemies/domwidow_f/domwidow_f_naked4.png"
    $enemy_domwidow_desc_f.difficulty_hp = 20
    
    #enemy snowman_m 0.3.7
    $enemy_snowman_desc_m_tactics = EnemyTactics()
    $enemy_snowman_desc_m_tactics.AddTactics({"phase":0, "type":"lust", "from_to":(0,100), "type_choice_attack":"row", "cards": ({"attack":card_attack_snowballs_storm1, "from_to":(0,0)},{"attack":card_skill_getarmor10_all, "from_to":(1,1)},{"attack":card_attack_snowballs_storm2, "from_to":(2,2)},{"attack":card_skill_getarmor10_all, "from_to":(3,3)},{"attack":card_attack_snowballs_storm3, "from_to":(4,4)},{"attack":card_skill_gotstrength3, "from_to":(5,5)})})
    $enemy_snowman_desc_m = EnemyDesc("Snowman","snowman", "This is a revived snowman, which has a dildo-shaped icicle instead of a nose. And between his legs he has a second icicle, which increases in size. And it will also melt if it's not cold enough outside.", "snowman_m", "idle", "male", 250, ({"from":81,"to":100,"item":item_ice_crystal,"condition":None},{"from":0,"to":80,"item":item_snowflake,"condition":None}), {"first":"Sit on my nose!"}, None,enemy_snowman_desc_m_tactics,[], True, 0.50)
    $enemy_snowman_desc_m.img["naked1"] = "/Enemies/snowman_m/snowman_m_naked1.png"
    $enemy_snowman_desc_m.img["naked2"] = "/Enemies/snowman_m/snowman_m_naked2.png"
    $enemy_snowman_desc_m.difficulty_hp = 20
    
    $enemy_snowman_desc_f_tactics = EnemyTactics()
    $enemy_snowman_desc_f_tactics.AddTactics({"phase":0, "type":"lust", "from_to":(0,100), "type_choice_attack":"row", "cards": ({"attack":card_attack_snowballs_storm1, "from_to":(0,0)},{"attack":card_skill_getarmor10_all, "from_to":(1,1)},{"attack":card_attack_snowballs_storm2, "from_to":(2,2)},{"attack":card_skill_getarmor10_all, "from_to":(3,3)},{"attack":card_attack_snowballs_storm3, "from_to":(4,4)},{"attack":card_skill_gotstrength3, "from_to":(5,5)})})
    $enemy_snowman_desc_f = EnemyDesc("Snowman","snowman", "This is a revived snowman, which has a dildo-shaped icicle instead of a nose. And between his legs he has a second icicle, which increases in size. And it will also melt if it's not cold enough outside.", "snowman_f", "idle", "female", 250, ({"from":81,"to":100,"item":item_ice_crystal,"condition":None},{"from":0,"to":80,"item":item_snowflake,"condition":None}), {"first":"Sit on my nose!"}, None,enemy_snowman_desc_f_tactics,[], True, 0.50)
    $enemy_snowman_desc_f.img["naked1"] = "/Enemies/snowman_f/snowman_f_naked1.png"
    $enemy_snowman_desc_f.img["naked2"] = "/Enemies/snowman_f/snowman_f_naked2.png"
    $enemy_snowman_desc_f.difficulty_hp = 20
    
    
    
    $monster_list.append(enemy_satyr_desc_m) #0.0.5
    $monster_list.append(enemy_satyr_desc_f)
    $monster_list.append(enemy_satyr_desc_futa)
    $monster_list.append(enemy_flydick_desc_m)
    $monster_list.append(enemy_flydick_desc_f)
    $monster_list.append(enemy_flydick_desc_futa)
    $monster_list.append(enemy_forest_fairy_desc_f)
    $monster_list.append(enemy_nymph_desc_f)
    $monster_list.append(enemy_muscular_desc_f)
    $monster_list.append(enemy_skeleton_desc)
    $monster_list.append(enemy_orc_desc)#0.1.1
    #0.1.7
    $monster_list.append(enemy_orc_f_desc)
    #0.2.3
    $monster_list.append(enemy_mushroomqueen_desc_f)
    #0.2.8
    $monster_list.append(enemy_mushroomqueen_desc_futa)
    #0.2.9
    $monster_list.append(enemy_slime_desc_f)
    #0.3.0
    $monster_list.append(enemy_nymph_futa_desc)
    #0.3.2
    $monster_list.append(enemy_domwidow_desc_f)
    #0.3.7
    $monster_list.append(enemy_snowman_desc_m)
    $monster_list.append(enemy_snowman_desc_f)
    
    
    
    #npc enemy
    $mirana_enemy_tactics = EnemyTactics()
    $mirana_enemy_tactics.AddTactics({"phase":0, "type":"lust", "from_to":(0,100), "type_choice_attack":"row", "cards": ({"attack":card_skill_getarmor_hi, "from_to":(0,0)},{"attack":card_attack_heavyslap, "from_to":(1,1)})})
    $mirana_enemy_desc = EnemyDesc(MiranaElf.name, "miranaelf", "Warrior", "MiranaElf", "idle", MiranaElf.gender,30, None, None, None, mirana_enemy_tactics, [], True)
    $mirana_enemy_desc.img = {"hide":"/NPC/MiranaElf/MiranaElf_say_img.png","idle":"/NPC/MiranaElf/MiranaElf_say_img.png", "naked":"/NPC/MiranaElf/MiranaElf_say_img.png","lust":"/NPC/MiranaElf/MiranaElf_for_dialog_naked.png"}
    $mirana_enemy_desc.icon = "/images/NPC/MiranaElf/MiranaElf_icon.png"
    $mirana_enemy = Enemy(mirana_enemy_desc, 30, 10, 1, False)
    $mirana_enemy.icon = "/images/NPC/MiranaElf/MiranaElf_icon.png"
   
    $Battle_with_Mirana = Battle([mirana_enemy], "/images/TownSquare_empty_blur.jpg", "mirana_after_battle_label", True)
    
    #+0.1.0
    $santa_helper_enemy_tactics1 = EnemyTactics()
    $santa_helper_enemy_tactics1.AddTactics({"phase":0, "type":"lust", "from_to":(0,100), "type_choice_attack":"row", "cards": ({"attack":card_attack_santa_helper, "from_to":(0,0)}, {"attack":card_skill_gotstrength_all, "from_to":(1,1)})})
    $santa_helper_enemy_desc1 = EnemyDesc("Santa's helper", "santahelper", "Santa's helper", "SantaHelper", "idle", "male",15, None, None, None, santa_helper_enemy_tactics1, [mod_servant], False)
    $santa_helper_enemy_desc1.img = {"hide":"/NPC/Santa/npc_santahelper.png","idle":"/NPC/Santa/npc_santahelper.png", "naked":"/NPC/Santa/npc_santahelper.png","lust":"/NPC/Santa/npc_santahelper.png"}
    $santa_helper_enemy_tactics2 = EnemyTactics()
    $santa_helper_enemy_tactics2.AddTactics({"phase":0, "type":"lust", "from_to":(0,100), "type_choice_attack":"row", "cards": ({"attack":card_attack_santa_helper, "from_to":(0,0)}, {"attack":card_skill_getarmor10_all, "from_to":(1,1)})})
    $santa_helper_enemy_desc2 = EnemyDesc("Santa's helper", "santahelper", "Santa's helper", "SantaHelper", "idle", "male",15, None, None, None, santa_helper_enemy_tactics2, [mod_servant], False)
    $santa_helper_enemy_desc2.img = {"hide":"/NPC/Santa/npc_santahelper2.png","idle":"/NPC/Santa/npc_santahelper2.png", "naked":"/NPC/Santa/npc_santahelper2.png","lust":"/NPC/Santa/npc_santahelper2.png"}
    $santa_helper_enemy_desc1.icon = "/images/NPC/Santa/santahelper_icon.png"
    $santa_helper_enemy_desc2.icon = "/images/NPC/Santa/santahelper_icon.png"
    
    
    $santa_enemy_tactics = EnemyTactics()
    $santa_enemy_tactics.boss = True
    $santa_enemy_tactics.servants = [santa_helper_enemy_desc1, santa_helper_enemy_desc2]
    $santa_enemy_tactics.AddTactics({"phase":0, "type":"lust", "from_to":(0,100), "type_choice_attack":"row", "cards": ({"attack":card_attack_santa1, "from_to":(0,0)},{"attack":card_attack_santa2, "from_to":(1,1)},{"attack":card_attack_santa3, "from_to":(2,2)},{"attack":card_attack_santa4, "from_to":(3,3)})})
    $santa_enemy_desc = EnemyDesc(npc_Santa.name,"santa", "Legendary figure who is the traditional patron of Christmas in the United States and other countries, bringing gifts to children.", "Santa", "idle", npc_Santa.gender,80, None, None, None, santa_enemy_tactics, [], True, 0.6)
    $santa_enemy_desc.img = {"hide":"/NPC/Santa/npc_santa_idle.png","idle":"/NPC/Santa/npc_santa_fight.png", "naked":"/NPC/Santa/npc_santa_fight_naked.png",  "naked1":"/NPC/Santa/npc_santa_fight_naked1.png", "naked2":"/NPC/Santa/npc_santa_fight_naked2.png", "lust":"/NPC/Santa/npc_santa_fight_lust.png"}
    $santa_enemy_desc.icon = "/images/NPC/Santa/Santa_icon.png"
    $santa_enemy_desc.difficulty_hp = 20
    $santa_enemy = Enemy(santa_enemy_desc, 161, 10, 1, False)
    $santa_enemy.icon = "/images/NPC/Santa/Santa_icon.png"
    $Battle_with_Santa = Battle([santa_enemy], "/images/TownSquareEvents/ChristmasTree/snow_tree_bg.jpg", "santa_after_battle_label", False)
    #-0.1.0
    #----------------------enemy-----------------------

    #++++++++++QUESTs++++++++++++++++
    #name, number, type, reward, contractfee, reward_points, reward_item,quest_lvl, hr_need,goal_condition,client, desc, supply_items, target, replayable = True, need_sex_types = None, urgent = False, nqctu = [], reward_cards = []):
    #"Gathering", "Slaying", "Corrupting", "Hunting", "Cum extractor"
    $quest_list = []
    # $quest_list.append(QuestDesc("Clean up the library (Training)", 1, "Gathering", 30, 0, 0, [{"from":0,"to":100,"item":item_book,"condition":None}], standart_library_map, [],1,1,"Collect 10 Scattered Books", GafferChoo, "This is your first task. Someone scattered books around the library. Collect them in a red chest.",[],{"Gathering":[{"item":item_book, "count":10}]}, "images/Locations/Library/ui_place.png",True, None, False, [], [card_skill_secretknowledge]))
    #name, number, type, reward, contractfee, reward_points, reward_item, monsterlist,quest_lvl, hr_need,goal_condition,client, desc, supply_items, target, ui_place, replayable = True, need_sex_types = None, urgent = False, nqctu = [], reward_cards = []
    $quest_list.append(QuestDesc("Lust herb for my wife", 2, "Gathering", 150, 0, 1, [{"from":0,"to":100,"item":item_herb,"condition":None}],1,1,"Deliver 5 Lust herb", WagonKront, "My wife doesn't want to have sex with me for a few month. I need a lust herb to excite her. Please bring me it.",(item_supply_potion,),{"Gathering":[{"item":item_lustherb, "count":5}]},True, None, False, [], [card_skill_getarmor]))
    $quest_list.append(QuestDesc("Mushrooms cave", 3, "Gathering", 300, 50, 1, [{"from":0,"to":100,"item":item_blue_mushroom,"condition":None}],1,1,"Deliver 7 Exciteshroom and 7 Powershroom", HerbalicaFlower, "I need these mushrooms to make potions. There is a huge cave in the forest, find it. Be careful!",(item_supply_potion,item_supply_potion,item_supply_potion),{"Gathering":[{"item":item_exciteshroom, "count":7}, {"item":item_powershroom, "count":7}]},True, None, False, [], [card_skill_harness]))
    $quest_list.append(QuestDesc("Satyr's cum", 4, "Cum extractor", 500, 70, 2, [{"from":0,"to":100,"item":item_satyr_cum,"condition":None}], 1,1,"Extract and deliver 4 flusk of Satyr's cum", MysteriousFarmer, "I saw some satyrs in the forest, bring me their cum",(item_supply_potion,item_supply_potion,item_supply_potion),{"Cum extractor":[{"item":item_satyr_cum, "count":4}]}, True, [sex_titsjob_sub, sex_handjob_sub, sex_vaginal_sex_sub], False, [], [card_attack_boobsstrike]))

    $quest_list.append(QuestDesc("Forest fairy", 6, "Cum extractor", 1200, 120, 3, [{"from":0,"to":100,"item":item_honey,"condition":None},{"from":0,"to":100,"item":item_hairs,"condition":None}],2,1,"Extract and deliver 2 pollen", HerbalicaFlower, "Amazing! A forest fairy appeared in our forest. I need her pollen to make special potions. Bring me some stuff.",(item_supply_potion,item_supply_potion,item_supply_potion),{"Cum extractor":[{"item":item_pollen, "count":2}]}, True, [sex_scissors, sex_blowjob_dom, sex_cunnilingus_sub], False, [], [card_attack_twinstrike])) #0.0.4
    $quest_list.append(QuestDesc("Damn Nymphs", 7, "Slaying", 1500, 300, 5, [{"from":0,"to":100,"item":item_cloth_piece,"condition":None},{"from":0,"to":100,"item":item_hairs,"condition":None}],2,1,"Slaying 3 Nymph", GloomyJack, "Shit! Shit! Shiiiit! Fucking Nymphs started up in the forest. They have fun all the time. I hate it. You must kill them all. If you want, you can fuck them.",(item_supply_potion,item_supply_potion,item_supply_potion),{"Slaying":[{"item":[enemy_nymph_desc_f,enemy_nymph_futa_desc], "count":3, "count_get":0}]},True, None, False, [], [card_attack_buttslap])) #0.0.5
    
    $quest_list.append(QuestDesc("Trouble in the forest", 8, "Slaying", 3000, 600, 5, [{"from":0,"to":100,"item":item_testosterone,"condition":None},{"from":0,"to":100,"item":item_testosterone,"condition":None}],2,1,"Slaying 1 Muscular female", GloomyJack, "A mixture of testosterone and boobs is terrorizing our forest. Do everything so that she is no longer here",(item_supply_potion,item_supply_potion,item_supply_potion),{"Slaying":[{"item":enemy_muscular_desc_f, "count":1, "count_get":0}]},True, None, False, [], [card_attack_boobsstrike])) #0.0.5
    $quest_list.append(QuestDesc("Follow the footsteps", 9, "Special", 100, 0, 1, [],2,1,"Follow the footsteps and find the Giant Orc", GafferChoo, "Hunters found traces of a huge orc. They were very scared, so you alone will have to look for him. Follow the trail. But if you find an orc, run! Don't fight him! Good look!",[],{"Special":[{"item":[enemy_orc_desc,enemy_orc_f_desc], "count":"GR01D3", "type":"check_door_exists"}]},False, None, False, [], [card_attack_bodyslam]))#0.1.1
    
    $quest_list.append(QuestDesc("Slay the orc", 10, "Slaying", 6000, 1500, 1, [{"from":0,"to":100,"item":item_orc_skin,"condition":None},{"from":0,"to":100,"item":item_orc_fang,"condition":None}],3,1,"Slay one Orc", GafferChoo, "A Giant Orc catches our girls and takes them to a cave. What a bastard! Find him and slay him. Good look!",[],{"Slaying":[{"item":[enemy_orc_desc,enemy_orc_f_desc], "count":1, "count_get":0}]},False, None, True, [2,3,9], [card_attack_boobsstrike, card_attack_buttslap]))#0.1.1
    
    $quest_list.append(QuestDesc("The locket", 500, "Gathering", 333, 0, 21, [{"from":0,"to":100,"item":item_locket,"condition":None}],1,1,"Bring me the locket, please", NunChurch, "Father Troy went to the cemetery a few days ago and lost the locket. Could you find it? Search the graves in the old cemetery in the forest. Good look!",[],{"Gathering":[{"item":item_locket, "count":1}]}, False))#0.1.6
    
    $quest_list.append(QuestDesc("Open the Mysterious cave entrance.", 11, "Special", 100, 0, 1, [],1,2,"Find a way to open the cave entrance.", GafferChoo, "The hunters heard strange sounds near the blocked cave entrance. We decided to check what was there. Find the key. I think the merchants will help you. Good look!",[],{"Special":[{"item":[item_cave_key], "count":"BL03D1", "type":"check_door_open"}]},False, None, False, [], [card_attack_bodyslam]))#0.1.8
    $quest_list.append(QuestDesc("Three glassful for Rascal.", 12, "Special", 100, 0, 1, [],1,2,"Find three glassful for Rascal.", npc_Rascal, "The cave bastard Rascal has lost his cups. Find them.",[],{"Special":[{"item":item_glassful, "need_item":3, "count":"num0", "type":"check_npc_dialog", "npc":npc_Rascal, "value":1}]},False, None, False, [], []))#0.1.8
    
    $quest_list.append(QuestDesc("Nymphs. Damn Nymphs!", 13, "Cum and squirted", 900, 300, 1, [],2,2,"Cum 1 times on Nymph's face, tits and abdomen or 3 times squrting on Nymphs!", GloomyJack, "These funny bitches squirted me from head to toe while I slept under a tree. DAMN! I want to take revenge on them. Cum 1 on times Nymph's face, tits and abdomen or 3 times squrting on Nymphs!",[],{"Cum and squirted":[{"item":[enemy_nymph_desc_f,enemy_nymph_futa_desc], "type":["cum_on_face_dom","cum_squirted_dom"], "count":1, "count_get":0},{"item":[enemy_nymph_desc_f,enemy_nymph_futa_desc], "type":["cum_on_abdomen_dom","cum_squirted_dom"], "count":1, "count_get":0},{"item":[enemy_nymph_desc_f,enemy_nymph_futa_desc], "type":["cum_on_tits_dom","cum_squirted_dom"], "count":1, "count_get":0}]},True, None, False, [], []))#0.1.8
    
    $quest_list.append(QuestDesc("Sweet cream on monster faces", 14, "Cum and squirted", 5400, 900, 3, [],3,2,"Cum or squrting on monters face!", MysteriousFarmer, "I continue my experiments with the cum seed. You could cum or squirting on the faces of some of the monsters. I want to see what happens to them. Don't let me down!",[],{"Cum and squirted":[{"item":[enemy_satyr_desc_f, enemy_satyr_desc_m], "type":["cum_on_face_dom","cum_squirted_dom"], "count":1, "count_get":0},{"item":[enemy_muscular_desc_f], "type":["cum_on_face_dom","cum_squirted_dom"], "count":1, "count_get":0},{"item":[enemy_forest_fairy_desc_f], "type":["cum_on_face_dom","cum_squirted_dom"], "count":1, "count_get":0}]},True, None, False, [], [card_skill_secretknowledge]))#0.2.0
    
    $quest_list.append(QuestDesc("I need sleep herb", 15, "Gathering", 750, 90, 2, [{"from":0,"to":100,"item":item_sleep_herb,"condition":None}],2,2,"Deliver 5 Sleep herb", HerbalicaFlower, "I want to make a potent sleeping pill. You have to help me.",(item_supply_potion,),{"Gathering":[{"item":item_sleep_herb, "count":5}]},True, None, False, [], [card_skill_secretknowledge]))#0.2.0
    
    $quest_list.append(QuestDesc("My hut's roof was destroyed by the flydicks!", 16, "Gathering", 3, 0, 10, [{"from":0,"to":100,"item":item_bear_trap,"condition":None}],1,2,"Deliver 25 Small stick", npc_CrookedPeasant, "I sat and jerked off in my hut. But suddenly 3 flydicks appeared, they started to pick the roof in my hut. I need sticks to fix it. I have few coins, but I can give you an old trap.",[],{"Gathering":[{"item":item_smallstick, "count":25}]},True, None, False, [], []))#0.2.0
    
    $quest_list.append(QuestDesc("Slay 15 flydick or flydickqueen", 17, "Slaying", 10000, 1500, 1, [{"from":0,"to":100,"item":item_flydick_cum,"condition":None},{"from":0,"to":100,"item":item_flydick_cum,"condition":None}],3,2,"Slay 15 flydick or flydickqueen", GafferChoo, "It becomes unsafe near the caves. Recently, fladicks have crawled out of them and attacked the peasants with toothed teeth. You must save us all. Good look!",[],{"Slaying":[{"item":[enemy_flydick_desc_f,enemy_flydick_desc_m, enemy_flydick_desc_futa], "count":15, "count_get":0}]},False, None, True, [11,12,13,14], [card_catched]))#0.2.0
    
    $quest_list.append(QuestDesc("Catch the Nymph.", 18, "Hunting and Catching", 2000, 0, 5, [],5,3,"You have to catch the nymph and put her in jail.", MiranaElf, "Filling monsters with lust is hard. But catching them is even harder, but also much more interesting. Catch the nymph and you can do whatever you want with her in prison!",[],{"Hunting and Catching":[{"item":[enemy_nymph_desc_f,enemy_nymph_futa_desc], "count":1, "count_get":0, "type":"catch_enemy"}]},True, None, False, [], [card_catched]))#0.2.0
    
    $quest_list.append(QuestDesc("Catch the Muscular female.", 19, "Hunting and Catching", 3000, 500, 5, [],5,3,"You have to catch the 2 muscular female and put them in jail.", MiranaElf, "Filling monsters with lust is hard. But catching them is even harder, but also much more interesting. Catch the nymph and you can do whatever you want with her in prison!",[],{"Hunting and Catching":[{"item":[enemy_muscular_desc_f], "count":2, "count_get":0, "type":"catch_enemy"}]},True, None, False, [], [card_catched]))#0.2.3
    
    $quest_list.append(QuestDesc("Slay 4 mushrooms queen", 20, "Slaying", 12000, 2500, 1, [{"from":0,"to":100,"item":item_poisonshroom,"condition":None},{"from":0,"to":100,"item":item_poisonshroom,"condition":None}],6,3,"Slay 4 Mushrooms queen", GafferChoo, "Mushroom queens have sprung up in the caves. You need to free the cave, otherwise it will be very difficult for us to advance further. Good look!",[],{"Slaying":[{"item":[enemy_mushroomqueen_desc_f,enemy_mushroomqueen_desc_futa], "count":4, "count_get":0}]},True, None, False, [], [card_catched,card_catched]))#0.2.3
    
    $quest_list.append(QuestDesc("Bring me a Mushrooms hat", 21, "Special", 20000, 0, 1, [{"from":0,"to":100,"item":item_poisonshroom,"condition":None},{"from":0,"to":100,"item":item_poisonshroom,"condition":None}],6,3,"Bring me a Mushrooms hat", GloomyJack, "I want to be the most fashionable in the village. Bring me a giant mushroom hat!",[],{"Special":[{"item":[mushrooms_hat, mushrooms_hat_male], "count":1, "type":"bring_cloth"}]},False, None, False, [], [card_catched]))#0.2.5
    
    
    $quest_list.append(QuestDesc("The secret of the Slut Statue", 22, "Special", 100, 0, 20, [],6,3,"Find 2 dildos and 1 buttplug.", GafferChoo, "We could not find a way out of the labyrinth in debt, maybe you can do it. I think the clue is in the Statue of the Slut.",[],{"Special":[{"item":item_red_dildo, "need_item":1, "count":"num0", "type":"check_npc_dialog", "npc":npc_SlutStatue, "value":1},{"item":item_yellow_dildo, "need_item":1, "count":"num1", "type":"check_npc_dialog", "npc":npc_SlutStatue, "value":1},{"item":item_blue_dildo, "need_item":1, "count":"num2", "type":"check_npc_dialog", "npc":npc_SlutStatue, "value":1}]},False, None, False, [], []))#0.2.6
    
    $quest_list.append(QuestDesc("The wall of the Whores", 23, "Special", 100, 0, 10, [],6,3,"Find 4 pieces of old scrolls and solve the mystery of the wall of whores.", GafferChoo, "They say in a cave with a labyrinth there is a wall from which whores stick out. Some of them have pussy and some have dick. You have to satisfy them to find out what the matter is.",[],{"Special":[{"item":item_piece_scroll, "need_item":4, "count":"num5", "type":"check_npc_dialog", "npc":npc_SlutsWall, "value":6}]},False, None, False, [], []))#0.2.6
    
    $quest_list.append(QuestDesc("Find your way out of the cave maze", 24, "Special", 30, 0, 25, [],6,3,"Find 2 part of key.", GafferChoo, "In the old archive, I found records of a secret door at the exit from the cave labyrinth. You need a key to open it.",[],{"Special":[{"item":[item_cavemaze_key], "count":"MM00D2", "type":"check_door_open"}]},False, None, False, [], []))#0.2.6
    
    $quest_list.append(QuestDesc("I need mushrooms... again", 25, "Gathering", 15000, 4000, 0, [{"from":0,"to":100,"item":item_hot_drink,"condition":None}],4,3,"Deliver 10 red mushrooms", HerbalicaFlower, "I need red mushrooms. I want to make a hot drink. Be careful, they are hot!",[],{"Gathering":[{"item":item_red_mushroom, "count":10}]},True, None, False, [], []))#0.2.6
    
    $quest_list.append(QuestDesc("A total of 50 amber ore. Impossible?", 50, "Gathering", 3000, 1000, 0, [],7,3,"Deliver 50 ambre ore", GloomyJack, "I need 50 ambre ore. These stones can be implanted into my penis. I will be able to give great pleasure to women.",[],{"Gathering":[{"item":item_amber_ore, "count":50}]},True, None, False, [], [card_attack_tripletrike,card_attack_tripletrike,card_attack_tripletrike]))#0.2.6
    
    $quest_list.append(QuestDesc("Sticky troubles", 26, "Slaying", 30000, 6000, 50, [{"from":0,"to":100,"item":item_slime_fluid,"condition":None},{"from":0,"to":100,"item":item_slime_fluid,"condition":None},{"from":0,"to":100,"item":item_slime_part,"condition":None},{"from":0,"to":100,"item":item_slime_stone,"condition":None}],6,3,"Slay 3 slime girl", GafferChoo, "These greenish sexual creatures have filled the mystical caves. It's hard to chase them away but you have to try. Good look!",[],{"Slaying":[{"item":[enemy_slime_desc_f], "count":3, "count_get":0}]},False, None, True, [20,21,24], [card_attack_tripletrike,card_attack_tripletrike,card_attack_tripletrike]))#0.2.9
    
    $quest_list.append(QuestDesc("Sticky troubles 2", 27, "Slaying", 90000, 18000, 50, [{"from":0,"to":100,"item":item_slime_fluid,"condition":None},{"from":0,"to":100,"item":item_slime_fluid,"condition":None},{"from":0,"to":100,"item":item_slime_part,"condition":None},{"from":0,"to":100,"item":item_slime_stone,"condition":None},{"from":0,"to":100,"item":item_slime_fluid,"condition":None},{"from":0,"to":100,"item":item_slime_fluid,"condition":None},{"from":0,"to":100,"item":item_slime_part,"condition":None},{"from":0,"to":100,"item":item_slime_stone,"condition":None}],7,4,"Slay 9 slime girl", GafferChoo, "These greenish sexual creatures have filled the mystical caves. It's hard to chase them away but you have to try. Good look!",[],{"Slaying":[{"item":[enemy_slime_desc_f], "count":9, "count_get":0}]},True, None, False, [], [card_attack_tripletrike]))#0.2.9
    
    $quest_list.append(QuestDesc("Mysterious cave exploration", 28, "Gathering", 3000, 1000, 0, [],4,4,"Deliver 20 cave herb", HerbalicaFlower, "Actually I only need 10 cave herbs. But they are very poorly preserved in the light, so I ask you to bring twice as much.",[],{"Gathering":[{"item":item_cave_herb, "count":20}]},True, None, False, [], []))#0.2.9
    
    $quest_list.append(QuestDesc("Slime's parts", 29, "Gathering", 12000, 2000, 0, [],7,4,"Deliver 5 slime's fluid, 5 stone and 5 parts", GloomyJack, "Hmm ... how can I tell you. I want to do one experiment. I'm wondering what substance is more pleasant to stick a member in. I'll tell you later.",[],{"Gathering":[{"item":item_slime_fluid, "count":5},{"item":item_slime_stone, "count":5},{"item":item_slime_part, "count":5}]},True, None, False, [], []))#0.2.9
    
    
    $quest_list.append(QuestDesc("First lumberjack's request", 30, "Special", 100, 0, 30, [],5,4,"Find Lumberjack's ax.", npc_LumberJack, "The Lumberjack lost his ax on the other side of the river.",[],{"Special":[{"item":item_ax, "need_item":1, "count":"num1", "type":"check_npc_dialog", "npc":npc_LumberJack, "value":1}]},False, None, False, [], []))#0.3.1
    $quest_list.append(QuestDesc("Second lumberjack's request", 31, "Special", 100, 0, 30, [],5,4,"Find 30 the small sticks to repair the bridge.", npc_LumberJack, "The Lumberjack can fix the bridge if you bring him some sticks.",[],{"Special":[{"item":item_smallstick, "need_item":30, "count":"num0", "type":"check_npc_dialog", "npc":npc_LumberJack, "value":1}]},False, None, False, [30], []))#0.3.1
    
    $quest_list.append(QuestDesc("Lonely dominant woman", 32, "Slaying", 42000, 5500, 1, [{"from":0,"to":100,"item":item_rare_cloth,"condition":None},{"from":0,"to":100,"item":item_rare_cloth,"condition":None}],6,4,"Slay the Dom Widow", GafferChoo, "Once upon a time, a husband and wife lived in the thicket of the forest. Everything was great with them, until one day the husband put his penis into a bee hive. And then he died. The widow was alone for a long time, she became cruel, became dominant. So that no one else puts a penis into the hive, she carries a chastity belt with her and dreams of putting it on anyone she meets.",[],{"Slaying":[{"item":[enemy_domwidow_desc_f], "count":1, "count_get":0}]},True, None, False, [], []))#0.3.2
    
    $quest_list.append(QuestDesc("Enemies all around", 33, "Slaying", 50000, 6000, 1, [{"from":0,"to":100,"item":item_rare_cloth,"condition":None},{"from":0,"to":100,"item":item_slime_fluid,"condition":None},{"from":0,"to":100,"item":item_poisonshroom,"condition":None}],6,4,"Slay the Dom Widow, Slay Slime, Slay Mushroomsqueen.", GafferChoo, "There are too many enemies. You need to find them and finish them. Good luck!",[],{"Slaying":[{"item":[enemy_domwidow_desc_f], "count":1, "count_get":0},{"item":[enemy_slime_desc_f], "count":1, "count_get":0},{"item":[enemy_mushroomqueen_desc_f,enemy_mushroomqueen_desc_futa], "count":1, "count_get":0}]},True, None, False, [], []))#0.3.4
    
    $quest_list.append(QuestDesc("Slay 3 Snowmans in Snow Forest", 34, "Slaying", 30000, 3000, 1, [{"from":0,"to":100,"item":item_ice_crystal,"condition":None},{"from":0,"to":100,"item":item_ice_crystal,"condition":None}],6,4,"Slay 3 Snowmans", GafferChoo, "Something is wrong in the Snowy Forest. Fucking snowmen are hiding something. You have to collect snow from snowdrifts, make 3 snowmen and fight with them. Be careful they have a dildo-shaped icicle instead of a nose. And a huge penis.",[],{"Slaying":[{"item":[enemy_snowman_desc_m,enemy_snowman_desc_f], "count":3, "count_get":0}]},True, None, False, [], []))#0.3.7
    
    $quest_list.append(QuestDesc("Build 20 Snowmans in Snow Forest", 35, "Special", 20000, 0, 5, [{"from":0,"to":100,"item":item_ice_crystal,"condition":None},{"from":0,"to":100,"item":item_snowflake,"condition":None}],6,4,"Build 20 Snowmans", GafferChoo, "Building snowman is fun, so try building them all over the map. We want to find out where they disappear after you leave the location.",[],{"Special":[{"item":[enemy_snowman_desc_m,enemy_snowman_desc_f], "count":20, "count_get":0, "desc":["snowman"], "type":"building"}]},True, None, False, [], []))#0.3.7
    
    $quest_list.append(QuestDesc("Build 20 bear traps", 36, "Special", 2000, 0, 1, [],5,3,"Build 20 bear traps", MiranaElf, "Can you set 20 beartraps? Our hunters want to catch a lot of monsters.",[],{"Special":[{"item":[item_bear_trap], "count":20, "count_get":0, "desc":["beartrap"], "type":"building"}]},True, None, False, [], [card_catched]))#0.3.7
    
    $quest_list.append(QuestDesc("I want a soup", 37, "Gathering", 1000, 0, 0, [{"from":0,"to":100,"item":item_soup,"condition":None}],3,4,"Deliver 6 snowballs, 1 pumpkin, 1 herb, 1 red mushroom and 1 oil", GafferChoo, "The water in our village has become dirty, and I really want soup. Bring me some snow, I'll melt it and cook my own food.",[],{"Gathering":[{"item":item_snowball, "count":6},{"item":item_pumpkin, "count":1},{"item":item_herb, "count":1},{"item":item_red_mushroom, "count":1},{"item":item_oil, "count":1}]},True, None, False, [], []))#0.4.0
    
    #----------QUESTs----------------
    
    
    #+++++++++++++OpenWorldMap++++++++++++++
    $world_matrix = []
    python:
        for col in ["R","P","O","N","M","L","K","J","I","H","G","F","E","D","C","B","A"]:
            _outstr = ""
            _out = []
            for row in range(5,0,-1):
                _out.append("%sL0%s"%(col, row))  #"JL01"
            _out.append("%s%s00"%(col,col))
            for row in range(1,6):
                _out.append("%sR0%s"%(col, row))
            world_matrix.append(_out)
    
    $worldmap = WorldLocationMap()
    $worldmap.addUnlockedLoc("Village wall")
    #AA
    
    $worldmap.addLocation(Location("AA00", "Village wall", (9,5)))#, GenerateMazeFromCsv("/images/Locations/Forest/loc0_path.csv"), "/images/Locations/Forest/loc0_img.png", "/images/Locations/Forest/bg/loc0_bg.jpg", "/images/Locations/Forest/bg/sex_bg2.jpg", "/images/Locations/Forest/mini_map0.png"))
    $worldmap.addObjectToLoc("AA00", SupplyChestsPoints(3,7, "supply_chest", worldmap.findLocByIndex("AA00").supply_items, "supply"))
    # $worldmap.findLocByIndex("AA00").cur_return_chest = SupplyChestsPoints(3,8, "return_chest", worldmap.findLocByIndex("AA00").return_chest, "return") #use for chest, don't remove
    $worldmap.addObjectToLoc("AA00", SupplyChestsPoints(3,8, "return_chest", worldmap.return_chest, "return"))
    $worldmap.addObjectToLoc("AA00", DoorPoints("AA00D0", (6,0), "door", "AL01D0"))
    $worldmap.addObjectToLoc("AA00", DoorPoints("AA00D3", (9,5), "door", "EXIT"))
    $worldmap.addObjectToLoc("AA00", DoorPoints("AA00D4", (0,4), "door", "BB00D0"))
    # $worldmap.addObjectToLoc("AA00", DoorPoints("D1", (0,4), "door", "BA00"))
    $worldmap.addObjectToLoc("AA00", DoorPoints("AA00D2", (6,9),"door", "AR01D0"))
    $worldmap.addLocation(Location("AR01", "Village wall"))
    $worldmap.addObjectToLoc("AR01", DoorPoints("AR01D0", (6,0), "door", "AA00D2"))
    $worldmap.addObjectToLoc("AR01", DoorPoints("AR01D1", (3,9), "door", "AR02D0"))
    $worldmap.addLocation(Location("AR02", "Village wall"))
    $worldmap.addObjectToLoc("AR02", DoorPoints("AR02D0", (3,0), "door", "AR01D1"))
    $worldmap.addObjectToLoc("AR02", GoldenChestPoints(6,6,"goldenchest",{"coins":500, "points":5, "card":[card_attack_twinstrike], "item":[item_megapotion]}))
    $worldmap.addLocation(Location("AL01", "Village wall"))
    $worldmap.addObjectToLoc("AL01", DoorPoints("AL01D0", (6,9), "door", "AA00D0"))
    $worldmap.addObjectToLoc("AL01", DoorPoints("AL01D1", (2,0), "door", "AL02D0"))
    $worldmap.addLocation(Location("AL02", "Village wall"))
    $worldmap.addObjectToLoc("AL02", DoorPoints("AL02D0", (2,9), "door", "AL01D1"))
    $worldmap.addObjectToLoc("AL02", DoorPoints("AL02D1", (0,2), "door", "BL02D0"))
    #BB
    $worldmap.addLocation(Location("BL02", "Village wall"))
    $worldmap.addObjectToLoc("BL02", DoorPoints("BL02D0", (9,2), "door", "AL02D1"))
    $worldmap.addObjectToLoc("BL02", DoorPoints("BL02D1", (1,0), "door", "BL03D0"))
    $worldmap.addObjectToLoc("BL02", DoorPoints("BL02D2", (0,5), "door", "CL02D0"))
    $worldmap.addLocation(Location("BL03", "Village wall"))
    $worldmap.addObjectToLoc("BL03", DoorPoints("BL03D0", (1,9), "door", "BL02D1"))
    $worldmap.addObjectToLoc("BL03", DoorPoints("BL03D1", (0,3), "door_blocked", "CL03D0", True, {"type":"need_key_for_cave_BL03D1", "cond":"This door can be opened later."}))#{"type":"need_key_for_cave", "cond":"This door can be opened later."}
    
    $worldmap.addObjectToLoc("BL03", SpecialPoints(2,2, "glassful", [{"type":"additem", "param":item_glassful, "takequest":GetQuestByIndex(12)}], True))#0.1.8
    
    
    $worldmap.addLocation(Location("BB00", "Village wall"))
    $worldmap.addObjectToLoc("BB00", DoorPoints("BB00D0", (9,4), "door", "AA00D4"))
    $worldmap.addObjectToLoc("BB00", DoorPoints("BB00D1", (0,6), "door", "CC00D1"))
    $worldmap.addObjectToLoc("BB00", DoorPoints("BB00D2", (2,9), "door_hole", "BR01D0"))
    $worldmap.addLocation(Location("BR01", "Village wall",None,True))#underground
    $worldmap.addObjectToLoc("BR01", DoorPoints("BR01D0", (1,0), "door", "BB00D2"))
    $worldmap.addObjectToLoc("BR01", DoorPoints("BR01D1", (6,0), "door", "BL01D1"))
    $worldmap.addObjectToLoc("BR01", DoorPoints("BR01D2", (5,9), "door", "BR02D0"))
    $worldmap.addLocation(Location("BL01", "Village wall",None,True))#underground
    $worldmap.addObjectToLoc("BL01", DoorPoints("BL01D1", (6,9), "door", "BR01D1"))
    $worldmap.addLocation(Location("BR02", "Village wall",None,True))#underground
    $worldmap.addObjectToLoc("BR02", DoorPoints("BR02D0", (5,0), "door", "BR01D2"))
    $worldmap.addObjectToLoc("BR02", DoorPoints("BR02D1", (9,9), "door_hide", "BRS0D0"))
    $worldmap.addLocation(Location("BRS0", "Village wall",None,True))#underground
    $worldmap.addObjectToLoc("BRS0", DoorPoints("BRS0D0", (0,1), "door", "BR02D1"))
    $worldmap.addObjectToLoc("BRS0", GoldenChestPoints(4,3,"goldenchest",{"coins":0, "points":5, "card":[], "item":[item_megapotion]}))
    #CC
    $worldmap.addLocation(Location("CL02", "Village wall"))
    $worldmap.addObjectToLoc("CL02", DoorPoints("CL02D0", (9,5), "door", "BL02D2"))
    $worldmap.addObjectToLoc("CL02", DoorPoints("CL02D1", (4,9), "door", "CL01D0"))
    $worldmap.addObjectToLoc("CL02", DoorPoints("CL02D2", (0,3), "door", "DL02D0"))
    $worldmap.addLocation(Location("CL01", "Village wall"))
    $worldmap.addObjectToLoc("CL01", DoorPoints("CL01D0", (4,0), "door", "CL02D1"))
    $worldmap.addObjectToLoc("CL01", DoorPoints("CL01D1", (2,9), "door", "CC00D0"))
    $worldmap.addLocation(Location("CC00", "Village wall"))
    $worldmap.addObjectToLoc("CC00", DoorPoints("CC00D0", (2,0), "door", "CL01D1"))
    $worldmap.addObjectToLoc("CC00", DoorPoints("CC00D1", (9,6), "door", "BB00D1"))
    $worldmap.addObjectToLoc("CC00", DoorPoints("CC00D2", (2,9), "door", "CR01D0")) #0.3.1
    
    $worldmap.addLocation(Location("CR01", "Village wall"))#0.3.1
    
    python:
        for loc in worldmap.locations:
            if loc.index == "CR01":
                if renpy.variant("small"):
                    loc.img = "/images/Locations/Village wall/CR01_anim0.jpg"
                else:
                    loc.img = "CR01_anim"
    $worldmap.addObjectToLoc("CR01", DoorPoints("CR01D0", (2,0), "door", "CC00D2"))#0.3.1
    $worldmap.addObjectToLoc("CR01", DoorPoints("CR01D1", (5,9), "door", "CR02D0"))#0.3.2
    $worldmap.addObjectToLoc("CR01", SpecialPoints(8,7, "item_ax", [{"type":"additem", "param":item_ax, "takequest":GetQuestByIndex(31)}], True))#0.3.1
    
    $worldmap.addLocation(Location("CR02", "Village wall"))#0.3.2
    $worldmap.addObjectToLoc("CR02", DoorPoints("CR02D0", (5,0), "door", "CR01D1"))#0.3.2
    $worldmap.addObjectToLoc("CR02", DoorPoints("CR02D1", (3,6), "door", "CRH2D0"))#0.3.2
    
    $worldmap.addLocation(Location("CRH2", "Village wall"))#0.3.2
    $worldmap.addObjectToLoc("CRH2", DoorPoints("CRH2D0", (8,6), "door", "CR02D1"))#0.3.2
    $worldmap.addObjectToLoc("CRH2", GoldenChestPoints(1,4,"goldenchest",{"coins":1408, "points":10, "card":[], "item":[item_sleep_herb,item_sleep_herb,item_bear_trap,item_rare_cloth,item_rare_cloth]}))
    
    $worldmap.addLocation(Location("CL03", "Mysterious cave",(9,3),True))#underground
    $worldmap.addObjectToLoc("CL03", DoorPoints("CL03D0",(9,3), "door", "BL03D1"))
    $worldmap.addObjectToLoc("CL03", DoorPoints("CL03D1",(0,0), "door", "CL04D0")) #0.2.3
    $worldmap.addObjectToLoc("CL03", SupplyChestsPoints(4,3, "supply_chest", worldmap.findLocByIndex("CL03").supply_items, "supply"))
    $worldmap.addObjectToLoc("CL03", SupplyChestsPoints(4,4, "return_chest", worldmap.return_chest, "return"))
    $worldmap.addObjectToLoc("CL03", NPCPoints(4,8, "rascal_icon_map", npc_Rascal, None, True))
    
    $worldmap.addObjectToLoc("CL03", SpecialPoints(2,7, "glassful", [{"type":"additem", "param":item_glassful, "takequest":GetQuestByIndex(12)}], True))#0.1.8
    $worldmap.addObjectToLoc("CL03", SpecialPoints(0,3, "glassful", [{"type":"additem", "param":item_glassful, "takequest":GetQuestByIndex(12)}], True))#0.1.8
    
    $worldmap.addLocation(Location("CL04", "Mysterious cave",None,True))#underground #0.2.3
    $worldmap.addObjectToLoc("CL04", DoorPoints("CL04D0",(0,9), "door", "CL03D1")) #0.2.3
    $worldmap.addObjectToLoc("CL04", DoorPoints("CL04D1",(0,3), "door", "DL04D0")) #0.2.9
    
    $worldmap.addLocation(Location("DL04", "Mysterious cave",None,True))#underground #0.2.9
    $worldmap.addObjectToLoc("DL04", DoorPoints("DL04D0",(9,3), "door", "CL04D1")) #0.2.9
    $worldmap.addObjectToLoc("DL04", DoorPoints("DL04D1",(4,0), "door", "DL05D0")) #0.2.9
    $worldmap.addObjectToLoc("DL04", DoorPoints("DL04D2",(0,7), "door", "EL04D0")) #0.2.9
    
    $worldmap.addLocation(Location("DL05", "Mysterious cave",None,True))#underground #0.2.9
    $worldmap.addObjectToLoc("DL05", DoorPoints("DL05D0",(4,9), "door", "DL04D1")) #0.2.9
    
    $worldmap.addLocation(Location("EL04", "Mysterious cave",None,True))#underground #0.2.9
    $worldmap.addObjectToLoc("EL04", DoorPoints("EL04D0",(9,7), "door", "DL04D2")) #0.2.9
    # npc_Rascal
    #DD
    $worldmap.addLocation(Location("DL02", "Village wall"))
    $worldmap.addObjectToLoc("DL02", DoorPoints("DL02D0", (9,3), "door", "CL02D2"))
    $worldmap.addObjectToLoc("DL02", DoorPoints("DL02D1", (0,7), "door", "EL02D0"))
    #EE
    $worldmap.addLocation(Location("EL01", "Village wall"))
    $worldmap.addObjectToLoc("EL01", DoorPoints("EL01D0", (4,0), "door", "EL02D1"))
    $worldmap.addObjectToLoc("EL01", DoorPoints("EL01D1", (0,5), "door_blocked", "FL01D0", True, {"type":"sex_unlocked", "cond":[{"enemy":[enemy_muscular_desc_f], "count":1},{"enemy":[enemy_satyr_desc_m,enemy_satyr_desc_f,enemy_satyr_desc_futa], "count":5},{"enemy":[enemy_nymph_desc_f,enemy_nymph_futa_desc], "count":3},{"enemy":[enemy_forest_fairy_desc_f], "count":3}]}))
    $worldmap.addLocation(Location("EL02", "Village wall"))
    $worldmap.addObjectToLoc("EL02", DoorPoints("EL02D0", (9,7), "door", "DL02D1"))
    $worldmap.addObjectToLoc("EL02", DoorPoints("EL02D1", (4,9), "door", "EL01D0"))
    #FF
    $worldmap.addLocation(Location("FF00", "Forest"))
    $worldmap.addObjectToLoc("FF00", DoorPoints("FF00D0", (2,0), "door", "FL01D2"))
    $worldmap.addObjectToLoc("FF00", DoorPoints("FF00D1", (4,9), "door", "FR01D0"))
    
    $worldmap.addLocation(Location("FR01", "Forest"))
    $worldmap.addObjectToLoc("FR01", DoorPoints("FR01D0", (4,0), "door", "FF00D1"))
    $worldmap.addObjectToLoc("FR01", DoorPoints("FR01D1", (0,5), "door", "GR01D0"))
    
    $worldmap.addLocation(Location("FL01", "Forest", (9,5)))
    $worldmap.addObjectToLoc("FL01", DoorPoints("FL01D0", (9,5), "door", "EL01D1"))
    $worldmap.addObjectToLoc("FL01", DoorPoints("FL01D1", (1,0), "door", "FL02D0"))
    $worldmap.addObjectToLoc("FL01", DoorPoints("FL01D2", (2,9), "door_blocked", "FF00D0", True, {"type":"stepfounder", "cond":"orc"})) #locked
    $worldmap.addObjectToLoc("FL01", SupplyChestsPoints(5,5, "supply_chest", worldmap.findLocByIndex("FL01").supply_items, "supply"))
    $worldmap.addObjectToLoc("FL01", SupplyChestsPoints(5,6, "return_chest", worldmap.return_chest, "return"))
    $worldmap.addObjectToLoc("FL01", GoldenChestPoints(6,1,"goldenchest",{"coins":1000, "points":10, "card":[], "item":[]}))
    
    #GG
    $worldmap.addLocation(Location("GG00", "Forest",None,True))#underground
    $worldmap.addObjectToLoc("GG00", DoorPoints("GG00D0", (4,1), "door", "GR01D3"))
    $worldmap.addObjectToLoc("GG00", GoldenChestPoints(2,1,"goldenchest",{"coins":6000, "points":25, "card":[], "item":[]}))
    $worldmap.addObjectToLoc("GG00", DoorPoints("GG00D1", (0,5), "door_blocked", "JJ00D0", True, {"type":"sex_unlocked", "cond":[{"enemy":[enemy_orc_desc,enemy_orc_f_desc], "count":1}]}))#0.1.4
    $worldmap.addObjectToLoc("GG00", DoorPoints("GG00D2", (0,1), "door", "JJ00D1"))#0.1.4
    
    $worldmap.addLocation(Location("GL02", "Forest"))
    $worldmap.addObjectToLoc("GL02", DoorPoints("GL02D0", (9,6), "door", "FL02D1"))
    $worldmap.addObjectToLoc("GL02", DoorPoints("GL02D1", (0,7), "door", "HL02D0"))
    $worldmap.addLocation(Location("GR01", "Forest"))
    $worldmap.addObjectToLoc("GR01", DoorPoints("GR01D0", (9,5), "door", "FR01D1"))
    $worldmap.addObjectToLoc("GR01", DoorPoints("GR01D1", (0,7), "door", "HR01D0"))
    $worldmap.addObjectToLoc("GR01", DoorPoints("GR01D2", (0,1), "door", "HR01D1"))
    
    # $worldmap.addObjectToLoc("GR01", DoorPoints("GR01D3", (4,1), "door_hole", "GG00D0")) #to underground
    
    # $worldmap.addObjectToLoc("FL01", SpecialPoints(1,2, "return_chest", worldmap.return_chest, "return"))
    #posX, posY, img, specialAction = None, unlocked = False
    #$worldmap.addObjectToLoc("FL01", DoorPoints("FL01D2", (2,9), "door", "FF00D0")) #locked
    
    
    
    $worldmap.addLocation(Location("FL02", "Forest"))
    $worldmap.addObjectToLoc("FL02", DoorPoints("FL02D0", (1,9), "door", "FL01D1"))
    $worldmap.addObjectToLoc("FL02", DoorPoints("FL02D1", (0,6), "door", "GL02D0"))
    
    
    
    #HH
    $worldmap.addLocation(Location("HR01", "Forest"))
    $worldmap.addObjectToLoc("HR01", DoorPoints("HR01D0", (9,7), "door", "GR01D1"))
    $worldmap.addObjectToLoc("HR01", DoorPoints("HR01D1", (9,1), "door", "GR01D2"))
    $worldmap.addObjectToLoc("HR01", DoorPoints("HR01D1", (0,4), "door", "IR01D1"))
    $worldmap.addObjectToLoc("HR01", DoorPoints("HR01D2", (0,8), "door", "IR01D2"))
    $worldmap.addLocation(Location("HL01", "Forest"))
    $worldmap.addObjectToLoc("HL01", DoorPoints("HL01D0", (4,0), "door", "HL02D1"))
    $worldmap.addObjectToLoc("HL01", DoorPoints("HL01D1", (0,6), "door", "IL01D0"))
    $worldmap.addLocation(Location("HL02", "Forest"))
    $worldmap.addObjectToLoc("HL02", DoorPoints("HL02D0", (9,7), "door", "GL02D1"))
    $worldmap.addObjectToLoc("HL02", DoorPoints("HL02D1", (4,9), "door", "HL01D0"))
    
    #II
    $worldmap.addLocation(Location("IL01", "Forest"))
    $worldmap.addObjectToLoc("IL01", DoorPoints("IL01D0", (9,6), "door", "HL01D1"))
    $worldmap.addObjectToLoc("IL01", DoorPoints("IL01D1", (3,9), "door", "II00D0"))
    $worldmap.addLocation(Location("II00", "Forest"))
    $worldmap.addObjectToLoc("II00", DoorPoints("II00D0", (3,0), "door", "IL01D1"))
    $worldmap.addObjectToLoc("II00", DoorPoints("II00D1", (6,9), "door", "IR01D0"))
    $worldmap.addLocation(Location("IR01", "Forest"))
    $worldmap.addObjectToLoc("IR01", DoorPoints("IR01D0", (6,0), "door", "II00D1"))
    $worldmap.addObjectToLoc("IR01", DoorPoints("IR01D1", (9,4), "door", "HR01D1"))
    $worldmap.addObjectToLoc("IR01", DoorPoints("IR01D2", (9,8), "door", "HR01D2"))
    $worldmap.addObjectToLoc("IR01", GoldenChestPoints(7,5,"goldenchest",{"coins":5000, "points":10, "card":[], "item":[item_megapotion]}))
    
    
    $footstep14 = SpecialPoints(5,1, "footstep", [{"type":"unlockdoor", "param":"FL01D2", "loc":"FL01"},{"type":"spawndoor", "param":DoorPoints("GR01D3", (4,1), "door_hole", "GG00D0"), "loc":"GR01"},{"type":"spawnenemy", "param":EnemyPoints(worldmap.GenerateEnemyPos("GG00"), "enemy_image", None, Battle([Enemy(enemy_orc_desc, renpy.random.randint(500, 700), 200, 1, False)], None, "", False)), "loc":"GG00"}], False)
    $worldmap.addObjectToLoc("GR01", footstep14)
    $footstep13 = SpecialPoints(7,4, "footstep", [{"type":"unlockfootstep", "param":footstep14, "loc":"GR01"}], False)
    $worldmap.addObjectToLoc("GR01", footstep13)
    $footstep12 = SpecialPoints(8,1, "footstep", [{"type":"unlockfootstep", "param":footstep13, "loc":"GR01"}], False)
    $worldmap.addObjectToLoc("HR01", footstep12)
    $footstep11 = SpecialPoints(4,3, "footstep", [{"type":"unlockfootstep", "param":footstep12, "loc":"HR01"}], False)
    $worldmap.addObjectToLoc("HR01", footstep11)
    $footstep10 = SpecialPoints(8,8, "footstep", [{"type":"unlockfootstep", "param":footstep11, "loc":"HR01"}], False)
    $worldmap.addObjectToLoc("IR01", footstep10)
    $footstep9 = SpecialPoints(4,2, "footstep", [{"type":"unlockfootstep", "param":footstep10, "loc":"IR01"}], False)
    $worldmap.addObjectToLoc("IR01", footstep9)
    $footstep8 = SpecialPoints(6,8, "footstep", [{"type":"unlockfootstep", "param":footstep9, "loc":"IR01"}], False)
    $worldmap.addObjectToLoc("II00", footstep8)
    $footstep7 = SpecialPoints(3,8, "footstep", [{"type":"unlockfootstep", "param":footstep8, "loc":"II00"}], False)
    $worldmap.addObjectToLoc("IL01", footstep7)
    $footstep77 = SpecialPoints(3,2, "footstep", [{"type":"unlockfootstep", "param":footstep7, "loc":"IL01"}], False)
    $worldmap.addObjectToLoc("IL01", footstep77)
    $footstep6 = SpecialPoints(1,6, "footstep", [{"type":"unlockfootstep", "param":footstep77, "loc":"IL01"}], False)
    $worldmap.addObjectToLoc("HL01", footstep6)
    $footstep5 = SpecialPoints(5,5, "footstep", [{"type":"unlockfootstep", "param":footstep6, "loc":"HL01"}], False)
    $worldmap.addObjectToLoc("HL01", footstep5)
    $footstep4 = SpecialPoints(4,8, "footstep", [{"type":"unlockfootstep", "param":footstep5, "loc":"HL01"}], False)
    $worldmap.addObjectToLoc("HL02", footstep4)
    $footstep3 = SpecialPoints(6,3, "footstep", [{"type":"unlockfootstep", "param":footstep4, "loc":"HL02"}], False)
    $worldmap.addObjectToLoc("HL02", footstep3)
    $footstep2 = SpecialPoints(1,7, "footstep", [{"type":"unlockfootstep", "param":footstep3, "loc":"HL02"}], False)
    $worldmap.addObjectToLoc("GL02", footstep2)
    $footstep1 = SpecialPoints(1,6, "footstep", [{"type":"unlockfootstep", "param":footstep2, "loc":"GL02"}], False)
    $worldmap.addObjectToLoc("FL02", footstep1)
    $worldmap.addObjectToLoc("FL01", SpecialPoints(1,2, "footstep", [{"type":"unlockfootstep", "param":footstep1, "loc":"FL02", "takequest":GetQuestByIndex(9)}], True))
    
    
    #JJ
    $worldmap.addLocation(Location("JJ00", "Cave maze", (9,5),True))#0.1.4
    $worldmap.addObjectToLoc("JJ00", DoorPoints("JJ00D0", (9,5), "door", "GG00D1"))#0.1.4
    $worldmap.addObjectToLoc("JJ00", DoorPoints("JJ00D1", (9,1), "door", "GG00D2"))#0.1.4
    $worldmap.addObjectToLoc("JJ00", SupplyChestsPoints(5,2, "supply_chest", worldmap.findLocByIndex("JJ00").supply_items, "supply"))
    $worldmap.addObjectToLoc("JJ00", SupplyChestsPoints(5,4, "return_chest", worldmap.return_chest, "return"))
    $worldmap.addObjectToLoc("JJ00", DoorPoints("JJ00D2", (3,0), "door_blocked", "JL01D3", True, {"type":"need_goto_location_LL00", "cond":"This door is unlocked a little later."}))#0.2.6 #
    $worldmap.addObjectToLoc("JJ00", DoorPoints("JJ00D3", (0,3), "door_blocked", "KK00D2", True, {"type":"need_goto_location_LL00", "cond":"This door is unlocked a little later."}))#0.2.6 #
    $worldmap.addObjectToLoc("JJ00", DoorPoints("JJ00D4", (0,6), "door", "KK00D1"))#0.2.6
    $worldmap.addObjectToLoc("JJ00", DoorPoints("JJ00D5", (0,8), "door_blocked", "KK00D0", True, {"type":"need_key_for_door_JJ00D5", "cond":"You need a {color=#3498c7}BLUE{/color} dildo key to unlock this door."}))#0.2.6 #
    $worldmap.addObjectToLoc("JJ00", DoorPoints("JJ00D6", (6,9), "door_blocked", "JR01D0", True, {"type":"need_goto_location_LL00", "cond":"This door is unlocked a little later."}))#0.2.6 #
    
    $worldmap.addLocation(Location("JL01", "Cave maze",None,True))#0.2.6
    $worldmap.addObjectToLoc("JL01", DoorPoints("JL01D0", (7,0), "door", "JL02D3"))#0.2.6
    $worldmap.addObjectToLoc("JL01", DoorPoints("JL01D1", (4,0), "door", "JL02D2"))#0.2.6
    $worldmap.addObjectToLoc("JL01", DoorPoints("JL01D2", (0,4), "door", "KL01D0"))#0.2.6
    $worldmap.addObjectToLoc("JL01", DoorPoints("JL01D3", (3,9), "door", "JJ00D2"))#0.2.6
    $worldmap.addObjectToLoc("JL01", SpecialPoints(1,5, "piece_old_scroll", [{"type":"additem", "param":item_piece_scroll, "takequest":GetQuestByIndex(23)}], True))#0.2.6
    
    $worldmap.addLocation(Location("JL02", "Cave maze",None,True))#0.2.6
    $worldmap.addObjectToLoc("JL02", DoorPoints("JL02D0", (0,2), "door", "KL02D1"))#0.2.6
    $worldmap.addObjectToLoc("JL02", DoorPoints("JL02D1", (0,5), "door", "KL02D0"))#0.2.6
    $worldmap.addObjectToLoc("JL02", DoorPoints("JL02D2", (4,9), "door", "JL01D1"))#0.2.6
    $worldmap.addObjectToLoc("JL02", DoorPoints("JL02D3", (7,9), "door", "JL01D0"))#0.2.6
    
    $worldmap.addLocation(Location("JR01", "Cave maze",None,True))#0.2.6
    $worldmap.addObjectToLoc("JR01", DoorPoints("JR01D0", (6,0), "door", "JJ00D6"))#0.2.6
    $worldmap.addObjectToLoc("JR01", DoorPoints("JR01D1", (4,2), "door", "JR02D2"))#0.2.6
    $worldmap.addObjectToLoc("JR01", DoorPoints("JR01D2", (0,2), "door", "KR01D0"))#0.2.6
    $worldmap.addObjectToLoc("JR01", DoorPoints("JR01D3", (0,6), "door", "KR01D7"))#0.2.6
    $worldmap.addObjectToLoc("JR01", DoorPoints("JR01D4", (5,9), "door", "JR02D1"))#0.2.6
    $worldmap.addObjectToLoc("JR01", DoorPoints("JR01D5", (7,9), "door", "JR02D0"))#0.2.6
    $worldmap.addObjectToLoc("JR01", DoorPoints("JR01D6", (2,9), "door", "JR02D6"))#0.2.6
    $worldmap.addObjectToLoc("JR01", SpecialPoints(3,4, "piece_old_scroll", [{"type":"additem", "param":item_piece_scroll, "takequest":GetQuestByIndex(23)}], True))#0.2.6
    
    $worldmap.addLocation(Location("JR02", "Cave maze",None,True))#0.2.6
    $worldmap.addObjectToLoc("JR02", DoorPoints("JR02D0", (7,0), "door", "JR01D5"))#0.2.6
    $worldmap.addObjectToLoc("JR02", DoorPoints("JR02D1", (6,0), "door", "JR01D4"))#0.2.6
    $worldmap.addObjectToLoc("JR02", DoorPoints("JR02D2", (5,5), "door", "JR01D1"))#0.2.6
    $worldmap.addObjectToLoc("JR02", DoorPoints("JR02D3", (0,2), "door", "KR02D0"))#0.2.6
    $worldmap.addObjectToLoc("JR02", DoorPoints("JR02D4", (0,5), "door", "KR02D7"))#0.2.6
    $worldmap.addObjectToLoc("JR02", DoorPoints("JR02D5", (0,7), "door", "KR02D6"))#0.2.6
    $worldmap.addObjectToLoc("JR02", DoorPoints("JR02D6", (9,1), "door", "JR01D6"))#0.2.6
    
    $worldmap.addLocation(Location("KK00", "Cave maze",None,True))#0.2.6
    $worldmap.addObjectToLoc("KK00", DoorPoints("KK00D0", (9,8), "door", "JJ00D5"))#0.2.6
    $worldmap.addObjectToLoc("KK00", DoorPoints("KK00D1", (9,6), "door", "JJ00D4"))#0.2.6
    $worldmap.addObjectToLoc("KK00", DoorPoints("KK00D2", (9,3), "door", "JJ00D3"))#0.2.6
    $worldmap.addObjectToLoc("KK00", DoorPoints("KK00D3", (7,0), "door", "KL01D4"))#0.2.6
    $worldmap.addObjectToLoc("KK00", DoorPoints("KK00D4", (3,0), "door", "KL01D3"))#0.2.6
    $worldmap.addObjectToLoc("KK00", DoorPoints("KK00D5", (0,5), "door", "LL00D0"))#0.2.6
    $worldmap.addObjectToLoc("KK00", DoorPoints("KK00D6", (1,9), "door_blocked", "KR01D2", True, {"type":"need_goto_location_LL00", "cond":"This door is unlocked a little later."}))#0.2.6 #
    $worldmap.addObjectToLoc("KK00", DoorPoints("KK00D7", (4,9), "door", "KR01D1"))#0.2.6
    $worldmap.addLocation(Location("KL01", "Cave maze",None,True))#0.2.6
    $worldmap.addObjectToLoc("KL01", DoorPoints("KL01D0", (9,4), "door", "JL01D2"))#0.2.6
    $worldmap.addObjectToLoc("KL01", DoorPoints("KL01D1", (5,0), "door", "KL02D4"))#0.2.6
    $worldmap.addObjectToLoc("KL01", DoorPoints("KL01D2", (0,0), "door", "LL01D7"))#0.2.6
    $worldmap.addObjectToLoc("KL01", DoorPoints("KL01D3", (3,9), "door", "KK00D4"))#0.2.6
    $worldmap.addObjectToLoc("KL01", DoorPoints("KL01D4", (7,9), "door", "KK00D3"))#0.2.6
    $worldmap.addObjectToLoc("KL01", DoorPoints("KL01D5", (0,2), "door", "LL01D8"))#0.2.6
    $worldmap.addLocation(Location("KL02", "Cave maze",None,True))#0.2.6
    $worldmap.addObjectToLoc("KL02", DoorPoints("KL02D0", (9,5), "door", "JL02D1"))#0.2.6
    $worldmap.addObjectToLoc("KL02", DoorPoints("KL02D1", (9,2), "door", "JL02D0"))#0.2.6
    $worldmap.addObjectToLoc("KL02", DoorPoints("KL02D2", (0,2), "door", "LL02D0"))#0.2.6
    $worldmap.addObjectToLoc("KL02", DoorPoints("KL02D3", (0,7), "door", "LL02D5"))#0.2.6
    $worldmap.addObjectToLoc("KL02", DoorPoints("KL02D4", (5,9), "door", "KL01D1"))#0.2.6
    $worldmap.addObjectToLoc("KL02", SpecialPoints(5,5, "blue_dildo", [{"type":"additem", "param":item_blue_dildo, "takequest":GetQuestByIndex(22)}], True))#0.2.6
    $worldmap.addObjectToLoc("KL02", GoldenChestPoints(6,1,"goldenchest",{"coins":0, "points":0, "card":[], "item":[], "cloth":[mushrooms_hat, mushrooms_hat_male]}))
    
    $worldmap.addLocation(Location("KR01", "Cave maze",None,True))#0.2.6
    $worldmap.addObjectToLoc("KR01", DoorPoints("KR01D0", (9,2), "door", "JR01D2"))#0.2.6
    $worldmap.addObjectToLoc("KR01", DoorPoints("KR01D1", (4,0), "door", "KK00D7"))#0.2.6
    $worldmap.addObjectToLoc("KR01", DoorPoints("KR01D2", (1,0), "door", "KK00D6"))#0.2.6
    $worldmap.addObjectToLoc("KR01", DoorPoints("KR01D3", (0,1), "door", "LR01D0"))#0.2.6
    $worldmap.addObjectToLoc("KR01", DoorPoints("KR01D4", (0,7), "door", "LR01D7"))#0.2.6 
    $worldmap.addObjectToLoc("KR01", DoorPoints("KR01D5", (3,9), "door", "KR02D2"))#0.2.6
    $worldmap.addObjectToLoc("KR01", DoorPoints("KR01D6", (7,9), "door", "KR02D1"))#0.2.6
    $worldmap.addObjectToLoc("KR01", DoorPoints("KR01D7", (9,5), "door", "JR01D3"))#0.2.6
    $worldmap.addLocation(Location("KR02", "Cave maze",None,True))#0.2.6
    $worldmap.addObjectToLoc("KR02", DoorPoints("KR02D0", (9,2), "door", "JR02D3"))#0.2.6
    $worldmap.addObjectToLoc("KR02", DoorPoints("KR02D1", (7,0), "door", "KR01D6"))#0.2.6
    $worldmap.addObjectToLoc("KR02", DoorPoints("KR02D2", (3,0), "door", "KR01D5"))#0.2.6
    $worldmap.addObjectToLoc("KR02", DoorPoints("KR02D3", (0,5), "door", "LR02D0"))#0.2.6
    $worldmap.addObjectToLoc("KR02", DoorPoints("KR02D4", (0,7), "door", "LR02D5"))#0.2.6 
    $worldmap.addObjectToLoc("KR02", DoorPoints("KR02D5", (0,9), "door", "LR02D4"))#0.2.6
    $worldmap.addObjectToLoc("KR02", DoorPoints("KR02D6", (9,7), "door", "JR02D5"))#0.2.6
    $worldmap.addObjectToLoc("KR02", DoorPoints("KR02D7", (9,5), "door", "JR02D4"))#0.2.6
    
    $worldmap.addLocation(Location("LL00", "Cave maze",None,True))#0.2.6
    $worldmap.addObjectToLoc("LL00", DoorPoints("LL00D0", (9,5), "door", "KK00D5"))#0.2.6
    $worldmap.addObjectToLoc("LL00", DoorPoints("LL00D1", (7,0), "door", "LL01D6"))#0.2.6
    $worldmap.addObjectToLoc("LL00", DoorPoints("LL00D2", (3,0), "door", "LL01D4"))#0.2.6
    $worldmap.addObjectToLoc("LL00", DoorPoints("LL00D3", (0,5), "door", "MM00D0"))#0.2.6
    $worldmap.addObjectToLoc("LL00", DoorPoints("LL00D4", (7,9), "door", "LR01D1"))#0.2.6 
    $worldmap.addObjectToLoc("LL00", DoorPoints("LL00D5", (1,0), "door", "LL01D9"))#0.2.6
    $worldmap.addObjectToLoc("LL00", DoorPoints("LL00D6", (0,2), "door", "MM00D5"))#0.2.6
    $worldmap.addObjectToLoc("LL00", DoorPoints("LL00D7", (2,9), "door_hide", "LR01D3"))#0.2.6 
    $worldmap.addObjectToLoc("LL00", GoldenChestPoints(4,8,"goldenchest",{"coins":5000, "points":15, "card":[card_catched], "item":[]}))
    $worldmap.addObjectToLoc("LL00", SpecialPoints(4,5, "cavemaze_slutstate", [{"type":"openlabel", "param":"cavemaze_slutstate_label", "takequest":GetQuestByIndex(22)}], True))#
    
    $worldmap.addLocation(Location("LL01", "Cave maze",None,True))#0.2.6
    $worldmap.addObjectToLoc("LL01", DoorPoints("LL01D0", (7,0), "door", "LL02D4"))#0.2.6
    $worldmap.addObjectToLoc("LL01", DoorPoints("LL01D1", (4,0), "door", "LL02D3"))#0.2.6
    $worldmap.addObjectToLoc("LL01", DoorPoints("LL01D2", (0,3), "door", "ML01D0"))#0.2.6
    $worldmap.addObjectToLoc("LL01", DoorPoints("LL01D3", (0,6), "door", "ML01D4"))#0.2.6
    $worldmap.addObjectToLoc("LL01", DoorPoints("LL01D4", (3,9), "door", "LL00D2"))#0.2.6 
    $worldmap.addObjectToLoc("LL01", DoorPoints("LL01D5", (5,7), "door", "LR01D2"))#0.2.6
    $worldmap.addObjectToLoc("LL01", DoorPoints("LL01D6", (7,9), "door", "LL00D1"))#0.2.6
    $worldmap.addObjectToLoc("LL01", DoorPoints("LL01D7", (9,0), "door", "KL01D2"))#0.2.6
    $worldmap.addObjectToLoc("LL01", DoorPoints("LL01D8", (9,2), "door", "KL01D5"))#0.2.6
    $worldmap.addObjectToLoc("LL01", DoorPoints("LL01D9", (1,9), "door", "LL00D5"))#0.2.6
    
    $worldmap.addLocation(Location("LL02", "Cave maze",None,True))#0.2.6
    $worldmap.addObjectToLoc("LL02", DoorPoints("LL02D0", (9,2), "door", "KL02D2"))#0.2.6
    $worldmap.addObjectToLoc("LL02", DoorPoints("LL02D1", (0,5), "door", "ML02D0"))#0.2.6
    $worldmap.addObjectToLoc("LL02", DoorPoints("LL02D2", (0,7), "door", "ML02D2"))#0.2.6
    $worldmap.addObjectToLoc("LL02", DoorPoints("LL02D3", (4,9), "door", "LL01D1"))#0.2.6
    $worldmap.addObjectToLoc("LL02", DoorPoints("LL02D4", (7,9), "door", "LL01D0"))#0.2.6 
    $worldmap.addObjectToLoc("LL02", DoorPoints("LL02D5", (9,7), "door", "KL02D3"))#0.2.6
    $worldmap.addObjectToLoc("LL02", DoorPoints("LL02D6", (0,0), "door", "ML02D3"))#0.2.6
    
    
    $worldmap.addLocation(Location("LR01", "Cave maze",None,True))#0.2.6
    $worldmap.addObjectToLoc("LR01", DoorPoints("LR01D0", (9,1), "door", "KR01D3"))#0.2.6
    $worldmap.addObjectToLoc("LR01", DoorPoints("LR01D1", (7,0), "door", "LL00D4"))#0.2.6
    $worldmap.addObjectToLoc("LR01", DoorPoints("LR01D2", (5,0), "door_blocked", "LL01D5", True, {"type":"need_key_for_door_LR01D2", "cond":"You need a yellow dildo key to unlock this door."}))#0.2.6
    $worldmap.addObjectToLoc("LR01", DoorPoints("LR01D3", (2,0), "door", "LL00D7"))#0.2.6
    $worldmap.addObjectToLoc("LR01", DoorPoints("LR01D4", (0,5), "door", "MR01D0"))#0.2.6 
    $worldmap.addObjectToLoc("LR01", DoorPoints("LR01D5", (4,9), "door", "LR02D2"))#0.2.6
    $worldmap.addObjectToLoc("LR01", DoorPoints("LR01D6", (7,9), "door", "LR02D1"))#0.2.6
    $worldmap.addObjectToLoc("LR01", DoorPoints("LR01D7", (9,7), "door", "KR01D4"))#0.2.6
    $worldmap.addObjectToLoc("LR01", SpecialPoints(6,6, "cavemaze_slutswall", [{"type":"openlabel", "param":"cavemaze_slutswall_label", "takequest":GetQuestByIndex(23)}], True))#
    $worldmap.addObjectToLoc("LR01", SpecialPoints(4,3, "piece_old_scroll", [{"type":"additem", "param":item_piece_scroll, "takequest":GetQuestByIndex(23)}], True))#0.2.6
    
    $worldmap.addLocation(Location("LR02", "Cave maze",None,True))#0.2.6
    $worldmap.addObjectToLoc("LR02", DoorPoints("LR02D0", (9,5), "door", "KR02D3"))#0.2.6
    $worldmap.addObjectToLoc("LR02", DoorPoints("LR02D1", (7,0), "door", "LR01D6"))#0.2.6
    $worldmap.addObjectToLoc("LR02", DoorPoints("LR02D2", (4,0), "door", "LR01D5"))#0.2.6
    $worldmap.addObjectToLoc("LR02", DoorPoints("LR02D3", (0,5), "door", "MR02D0"))#0.2.6
    $worldmap.addObjectToLoc("LR02", DoorPoints("LR02D4", (9,9), "door", "KR02D5"))#0.2.6 
    $worldmap.addObjectToLoc("LR02", DoorPoints("LR02D5", (9,7), "door", "KR02D4"))#0.2.6
    $worldmap.addObjectToLoc("LR02", DoorPoints("LR02D6", (0,8), "door", "MR02D3"))#0.2.6
    $worldmap.addObjectToLoc("LR02", GoldenChestPoints(3,9,"goldenchest",{"coins":5000, "points":15, "card":[card_attack_tripletrike], "item":[]}))
    
    $worldmap.addLocation(Location("MM00", "Cave maze",None,True))#0.2.6
    $worldmap.addObjectToLoc("MM00", DoorPoints("MM00D0", (9,5), "door", "LL00D3"))#0.2.6
    $worldmap.addObjectToLoc("MM00", DoorPoints("MM00D1", (5,0), "door", "ML01D3"))#0.2.6
    $worldmap.addObjectToLoc("MM00", DoorPoints("MM00D2", (0,6), "door_blocked", "NN00D0", True, {"type":"need_key_for_cave_MM00D2", "cond":"Find the key to open the door."}))#0.2.6
    $worldmap.addObjectToLoc("MM00", DoorPoints("MM00D3", (7,9), "door", "MR01D1"))#0.2.6
    $worldmap.addObjectToLoc("MM00", DoorPoints("MM00D4", (1,0), "door", "ML01D5"))#0.2.6 
    $worldmap.addObjectToLoc("MM00", DoorPoints("MM00D5", (9,2), "door", "LL00D6"))#0.2.6
    $worldmap.addObjectToLoc("MM00", DoorPoints("MM00D6", (7,0), "door", "ML01D6"))#0.2.6
    $worldmap.addObjectToLoc("MM00", SpecialPoints(2,8, "piece_old_scroll", [{"type":"additem", "param":item_piece_scroll, "takequest":GetQuestByIndex(23)}], True))#0.2.6
    
    $worldmap.addLocation(Location("ML01", "Cave maze",None,True))#0.2.6
    $worldmap.addObjectToLoc("ML01", DoorPoints("ML01D0", (9,3), "door", "LL01D2"))#0.2.6
    $worldmap.addObjectToLoc("ML01", DoorPoints("ML01D1", (2,0), "door", "ML02D1"))#0.2.6
    # $worldmap.addObjectToLoc("ML01", DoorPoints("ML01D2", (2,6), "door", "MR01D2"))#0.2.6
    $worldmap.addObjectToLoc("ML01", DoorPoints("ML01D3", (5,9), "door", "MM00D1"))#0.2.6
    $worldmap.addObjectToLoc("ML01", DoorPoints("ML01D4", (9,6), "door", "LL01D3"))#0.2.6 
    $worldmap.addObjectToLoc("ML01", DoorPoints("ML01D5", (1,9), "door", "MM00D4"))#0.2.6
    $worldmap.addObjectToLoc("ML01", DoorPoints("ML01D6", (7,9), "door", "MM00D6"))#0.2.6
    $worldmap.addObjectToLoc("ML01", SpecialPoints(7,7, "red_dildo", [{"type":"additem", "param":item_red_dildo, "takequest":GetQuestByIndex(22)}], True))#0.2.6
    $worldmap.addObjectToLoc("ML01", GoldenChestPoints(2,6,"goldenchest",{"coins":20000, "points":5, "card":[], "item":[]}))
    
    $worldmap.addLocation(Location("ML02", "Cave maze",None,True))#0.2.6
    $worldmap.addObjectToLoc("ML02", DoorPoints("ML02D0", (9,5), "door", "LL02D1"))#0.2.6
    $worldmap.addObjectToLoc("ML02", DoorPoints("ML02D1", (2,9), "door", "ML01D1"))#0.2.6
    $worldmap.addObjectToLoc("ML02", DoorPoints("ML02D2", (9,7), "door", "LL02D2"))#0.2.6
    $worldmap.addObjectToLoc("ML02", DoorPoints("ML02D3", (9,0), "door", "LL02D6"))#0.2.6
    $worldmap.addObjectToLoc("ML02", SpecialPoints(9,2, "cavemaze_key_part2_worldmap", [{"type":"additem", "param":item_cavemaze_key_part2, "takequest":GetQuestByIndex(24)}], True))#0.2.6
    
    $worldmap.addLocation(Location("MR01", "Cave maze",None,True))#0.2.6
    $worldmap.addObjectToLoc("MR01", DoorPoints("MR01D0", (9,5), "door", "LR01D4"))#0.2.6
    $worldmap.addObjectToLoc("MR01", DoorPoints("MR01D1", (7,0), "door", "MM00D3"))#0.2.6
    # $worldmap.addObjectToLoc("MR01", DoorPoints("MR01D2", (2,0), "door", "ML01D2"))#0.2.6
    $worldmap.addObjectToLoc("MR01", DoorPoints("MR01D3", (3,9), "door", "MR02D2"))#0.2.6
    $worldmap.addObjectToLoc("MR01", DoorPoints("MR01D4", (7,9), "door", "MR02D1"))#0.2.6 
    
    $worldmap.addLocation(Location("MR02", "Cave maze",None,True))#0.2.6
    $worldmap.addObjectToLoc("MR02", DoorPoints("MR02D0", (9,5), "door", "LR02D3"))#0.2.6
    $worldmap.addObjectToLoc("MR02", DoorPoints("MR02D1", (7,0), "door", "MR01D4"))#0.2.6
    $worldmap.addObjectToLoc("MR02", DoorPoints("MR02D2", (3,0), "door", "MR01D3"))#0.2.6
    $worldmap.addObjectToLoc("MR02", DoorPoints("MR02D3", (9,8), "door", "LR02D6"))#0.2.6
    
    $worldmap.addLocation(Location("NN00", "Snow forest", (9,6), False))#0.1.4
    $worldmap.addObjectToLoc("NN00", DoorPoints("NN00D0", (9,6), "door", "MM00D2"))#0.1.4
    $worldmap.addObjectToLoc("NN00", SupplyChestsPoints(4,4, "supply_chest", worldmap.findLocByIndex("NN00").supply_items, "supply"))
    $worldmap.addObjectToLoc("NN00", SupplyChestsPoints(5,6, "return_chest", worldmap.return_chest, "return"))
    $worldmap.addObjectToLoc("NN00", DoorPoints("NN00D1", (4,0), "door", "NL01D0"))#0.3.7
    $worldmap.addObjectToLoc("NN00", DoorPoints("NN00D2", (0,4), "door", "OO00D0"))#0.3.7
    $worldmap.addObjectToLoc("NN00", DoorPoints("NN00D3", (4,9), "door", "NR01D0"))#0.3.7
    
    $worldmap.addLocation(Location("NL01", "Snow forest", None, False))#0.3.7
    $worldmap.addObjectToLoc("NL01", DoorPoints("NL01D0", (4,9), "door", "NN00D1"))#0.3.7
    $worldmap.addObjectToLoc("NL01", DoorPoints("NL01D1", (0,0), "door", "OL01D0"))#0.3.7
    $worldmap.addObjectToLoc("NL01", DoorPoints("NL01D2", (0,4), "door", "OL01D1"))#0.3.7
    $worldmap.addObjectToLoc("NL01", DoorPoints("NL01D3", (0,7), "door", "OL01D2"))#0.3.7
    
    $worldmap.addLocation(Location("NR01", "Snow forest", None, False))#0.3.7
    $worldmap.addObjectToLoc("NR01", DoorPoints("NR01D0", (4,0), "door", "NN00D3"))#0.3.7
    $worldmap.addObjectToLoc("NR01", DoorPoints("NR01D1", (0,3), "door", "OR01D1"))#0.3.7
    
    $worldmap.addLocation(Location("OO00", "Snow forest", None, False))#0.3.7
    $worldmap.addObjectToLoc("OO00", DoorPoints("OO00D0", (9,4), "door", "NN00D2"))#0.3.7
    $worldmap.addObjectToLoc("OO00", DoorPoints("OO00D1", (8,0), "door", "OL01D4"))#0.3.7
    $worldmap.addObjectToLoc("OO00", DoorPoints("OO00D2", (5,4), "door_blocked", "OOU0D0", True, {"type":"need_key_for_cave_OO00D2", "cond":"This door is unlocked a little later."}))#0.3.7
    $worldmap.addObjectToLoc("OO00", DoorPoints("OO00D3", (1,9), "door", "OR01D0"))#0.3.7
    $worldmap.addObjectToLoc("OO00", DoorPoints("OO00D4", (1,0), "door", "OL01D5"))#0.3.7
    $worldmap.addObjectToLoc("OO00", DoorPoints("OO00D5", (0,2), "door", "PP00D0"))#0.3.7
    
    
    $worldmap.addLocation(Location("OL01", "Snow forest", None, False))#0.3.7
    $worldmap.addObjectToLoc("OL01", DoorPoints("OL01D0", (9,0), "door", "NL01D1"))#0.3.7
    $worldmap.addObjectToLoc("OL01", DoorPoints("OL01D1", (9,4), "door", "NL01D2"))#0.3.7
    $worldmap.addObjectToLoc("OL01", DoorPoints("OL01D2", (9,7), "door", "NL01D3"))#0.3.7
    $worldmap.addObjectToLoc("OL01", DoorPoints("OL01D3", (3,1), "door_blocked", "OLU1D0", True, {"type":"need_key_for_cave_OL01D3", "cond":"This door is unlocked a little later."}))#0.3.7
    $worldmap.addObjectToLoc("OL01", DoorPoints("OL01D4", (8,9), "door", "OO00D1"))#0.3.7
    $worldmap.addObjectToLoc("OL01", DoorPoints("OL01D5", (1,9), "door", "OO00D4"))#0.3.7
    $worldmap.addObjectToLoc("OL01", DoorPoints("OL01D6", (0,3), "door", "PL01D0"))#0.3.7
    $worldmap.addObjectToLoc("OL01", DoorPoints("OL01D7", (0,5), "door", "PL01D1"))#0.3.7
    $worldmap.addObjectToLoc("OL01", GoldenChestPoints(5,4,"goldenchest",{"coins":10000, "points":10, "card":[], "item":[item_hot_drink, item_hot_drink, item_hot_drink, item_hot_drink, item_hot_drink],"cloth":[]}))
    
    $worldmap.addLocation(Location("OR01", "Snow forest", None, False))#0.3.7
    $worldmap.addObjectToLoc("OR01", DoorPoints("OR01D0", (1,0), "door", "OO00D3"))#0.3.7
    $worldmap.addObjectToLoc("OR01", DoorPoints("OR01D1", (9,3), "door", "NR01D1"))#0.3.7
    $worldmap.addObjectToLoc("OR01", DoorPoints("OR01D2", (0,5), "door", "PR01D0"))#0.3.7
    
    $worldmap.addLocation(Location("PP00", "Snow forest", None, False))#0.3.7
    $worldmap.addObjectToLoc("PP00", DoorPoints("PP00D0", (9,2), "door", "OO00D5"))#0.3.7
    $worldmap.addObjectToLoc("PP00", DoorPoints("PP00D1", (5,0), "door", "PL01D2"))#0.3.7
    $worldmap.addObjectToLoc("PP00", DoorPoints("PP00D2", (3,0), "door", "PL01D3"))#0.3.7
    $worldmap.addObjectToLoc("PP00", DoorPoints("PP00D3", (3,9), "door", "PR01D1"))#0.3.7
    $worldmap.addObjectToLoc("PP00", DoorPoints("PP00D4", (8,9), "door", "PR01D2"))#0.3.7
    $worldmap.addObjectToLoc("PP00", DoorPoints("PP00D5", (0,6), "door", "RR00D0"))#0.3.7
    $worldmap.addObjectToLoc("PP00", DoorPoints("PP00D6", (0,1), "door", "RR00D1"))#0.3.7
    
    $worldmap.addLocation(Location("PL01", "Snow forest", None, False))#0.3.7
    $worldmap.addObjectToLoc("PL01", DoorPoints("PL01D0", (9,3), "door", "OL01D6"))#0.3.7
    $worldmap.addObjectToLoc("PL01", DoorPoints("PL01D1", (9,5), "door", "OL01D7"))#0.3.7
    $worldmap.addObjectToLoc("PL01", DoorPoints("PL01D2", (5,9), "door", "PP00D1"))#0.3.7
    $worldmap.addObjectToLoc("PL01", DoorPoints("PL01D3", (3,9), "door", "PP00D2"))#0.3.7
    $worldmap.addObjectToLoc("PL01", DoorPoints("PL01D4", (0,2), "door", "RL01D0"))#0.3.7
    $worldmap.addObjectToLoc("PL01", DoorPoints("PL01D5", (1,5), "door", "RL01D1"))#0.3.7
    
    $worldmap.addLocation(Location("PR01", "Snow forest", None, False))#0.3.7
    $worldmap.addObjectToLoc("PR01", DoorPoints("PR01D0", (9,5), "door", "OR01D2"))#0.3.7
    $worldmap.addObjectToLoc("PR01", DoorPoints("PR01D1", (3,0), "door", "PP00D3"))#0.3.7
    $worldmap.addObjectToLoc("PR01", DoorPoints("PR01D2", (8,0), "door", "PP00D4"))#0.3.7
    
    $worldmap.addLocation(Location("RR00", "Snow forest", None, False))#0.3.7
    $worldmap.addObjectToLoc("RR00", DoorPoints("RR00D0", (9,6), "door", "PP00D5"))#0.3.7
    $worldmap.addObjectToLoc("RR00", DoorPoints("RR00D1", (9,1), "door", "PP00D6"))#0.3.7
    $worldmap.addObjectToLoc("RR00", DoorPoints("RR00D2", (3,5), "door_blocked", "RRU0D0", True, {"type":"need_key_for_cave_RR00D2", "cond":"This door is unlocked a little later."}))#0.3.7
    
    $worldmap.addLocation(Location("RL01", "Snow forest", None, False))#0.3.7
    $worldmap.addObjectToLoc("RL01", DoorPoints("RL01D0", (9,2), "door", "PL01D4"))#0.3.7
    $worldmap.addObjectToLoc("RL01", DoorPoints("RL01D1", (9,5), "door", "PL01D5"))#0.3.7
    
    $worldmap.addLocation(Location("RR01", "Snow forest", None, False))#0.3.7
    
    $worldmap.addLocation(Location("NL02", "Snow forest", None, False))#0.3.7
    $worldmap.addLocation(Location("OL02", "Snow forest", None, False))#0.3.7
    $worldmap.addLocation(Location("PL02", "Snow forest", None, False))#0.3.7
    $worldmap.addLocation(Location("RL02", "Snow forest", None, False))#0.3.7
    $worldmap.addLocation(Location("NR02", "Snow forest", None, False))#0.3.7
    $worldmap.addLocation(Location("OR02", "Snow forest", None, False))#0.3.7
    $worldmap.addLocation(Location("PR02", "Snow forest", None, False))#0.3.7
    $worldmap.addLocation(Location("RR02", "Snow forest", None, False))#0.3.7
    #-------------OpenWorldMap--------------
    
    #++++++++++Combo_list++++++++++++
    $comboBook = ComboBook("Combo lists")
    #num, item1, item2, item_result, success, quantity, hided_item1, hided_item2, hided_item_result
    $comboBook.addCombo(Combining(item_herb, item_blue_mushroom, item_potion, 100, 1, False, False, True))
    $comboBook.addCombo(Combining(item_potion, item_honey, item_megapotion, 100, 1, False, True, True))
    $comboBook.addCombo(Combining(item_ivy, item_hairs, item_net, 100, 1, False, True, True))
    $comboBook.addCombo(Combining(item_mucus, item_water, item_oil, 100, 1, False, True, True))#0.1.6
    $comboBook.addCombo(Combining(item_leather_piece, item_oil, item_latex_piece, 100, 1, False, True, True))
    $comboBook.addCombo(Combining(item_red_flower, item_oil, item_red_ink, 100, 1, False, True, True))#0.0.6
    $comboBook.addCombo(Combining(item_white_ink, item_red_ink, item_pink_ink, 100, 1, False, True, True))#0.0.6
    $comboBook.addCombo(Combining(item_megapotion, item_lustherb, item_lewdpotion, 100, 1, True, True, True))
    $comboBook.addCombo(Combining(item_cave_key_part1, item_cave_key_part2, item_cave_key, 100, 1, True, True, True))#0.1.8
    
    $comboBook.addCombo(Combining(item_trap_tool, item_satyr_horn, item_bear_trap, 100, 1, True, True, True))#0.1.9
    
    $comboBook.addCombo(Combining(item_honey, item_powershroom, item_catalist, 100, 1, True, False, True))#0.2.1
    $comboBook.addCombo(Combining(item_catalist, item_testosterone, item_potion_stamina, 100, 1, True, True, True))#0.2.1
    $comboBook.addCombo(Combining(item_catalist, item_blue_flower, item_potion_gain_armor, 100, 1, True, True, True))#0.2.1
    $comboBook.addCombo(Combining(item_catalist, item_satyr_cum, item_potion_draw_card, 100, 1, True, True, True))#0.2.1

    $comboBook.addCombo(Combining(item_cavemaze_key_part1, item_cavemaze_key_part2, item_cavemaze_key, 100, 1, True, True, True))#0.2.6
    
    $comboBook.addCombo(Combining(item_snowball_small, item_snowball_small, item_snowball, 100, 1, True, True, True))#0.3.7
    $comboBook.addCombo(Combining(item_snowball_small, item_snowball, item_snowman_item, 100, 1, True, True, False))#0.3.7
    
    #++++++++Items+++++++++++
    $items_list.append(item_lustherb)
    $items_list.append(item_herb)
    $items_list.append(item_ivy)
    $items_list.append(item_supply_potion)
    $items_list.append(item_potion)
    $items_list.append(item_megapotion)
    $items_list.append(item_smallstick)
    $items_list.append(item_cloth_piece)
    $items_list.append(item_leather_piece)
    $items_list.append(item_latex_piece)
    $items_list.append(item_book)

    $items_list.append(item_bone)
    $items_list.append(item_stone)
    $items_list.append(item_blue_mushroom)
    $items_list.append(item_powershroom)
    $items_list.append(item_exciteshroom)
    $items_list.append(item_honey)
    $items_list.append(item_hairs)
    $items_list.append(item_red_flower)
    $items_list.append(item_blue_flower)
    $items_list.append(item_yellow_flower)

    $items_list.append(item_mucus)
    $items_list.append(item_worm)
    $items_list.append(item_net)
    $items_list.append(item_pollen)
    $items_list.append(item_oil)
    
    $items_list.append(item_sap_plant)
    $items_list.append(item_testosterone)
    $items_list.append(item_orc_fang)
    $items_list.append(item_orc_skin)
    $items_list.append(item_sleep_herb)
    
    $items_list.append(item_return_pass)

    $items_list.append(item_satyr_horn)
    $items_list.append(item_satyr_fur)
    $items_list.append(item_satyr_cum)
    $items_list.append(item_flydick_cum)
    
    $items_list.append(item_pumpkin) #0.0.6
    $items_list.append(item_red_ink) #0.0.6
    $items_list.append(item_white_ink) #0.0.6
    $items_list.append(item_pink_ink) #0.0.6
    
    $items_list.append(item_lewdpotion) #0.1.6
    $items_list.append(item_water) #0.1.6
    
    $items_list.append(item_cave_key_part1) #0.1.8
    $items_list.append(item_cave_key_part2) #0.1.8
    $items_list.append(item_cave_key) #0.1.8
    $items_list.append(item_glassful) #0.1.8
    
    $items_list.append(item_trap_tool) #0.1.9
    $items_list.append(item_bear_trap) #0.1.9
    
    $items_list.append(item_potion_stamina)#0.2.1
    $items_list.append(item_catalist)#0.2.1
    $items_list.append(item_potion_gain_armor)#0.2.1
    $items_list.append(item_potion_draw_card)#0.2.1
    
    $items_list.append(item_poisonshroom)#0.2.3
    $items_list.append(item_amanita)#0.2.3
    $items_list.append(item_mushroom_slime)#0.2.3
    
    $items_list.append(item_red_dildo) #0.2.6
    $items_list.append(item_blue_dildo) #0.2.6
    $items_list.append(item_yellow_dildo) #0.2.6
    $items_list.append(item_piece_scroll) #0.2.6 
    $items_list.append(item_cavemaze_key) #0.2.6
    $items_list.append(item_cavemaze_key_part1) #0.2.6
    $items_list.append(item_cavemaze_key_part2) #0.2.6
    $items_list.append(item_red_mushroom) #0.2.6
    $items_list.append(item_hot_drink) #0.2.6
    $items_list.append(item_amber_ore) #0.2.6
    
    $items_list.append(item_slime_part) #0.2.9
    $items_list.append(item_slime_stone) #0.2.9
    $items_list.append(item_slime_fluid) #0.2.9
    $items_list.append(item_cave_herb) #0.2.9
    $items_list.append(item_snake_herb) #0.2.9
    
    $items_list.append(item_ax)#0.3.2
    $items_list.append(item_max_potion)#0.3.2
    $items_list.append(item_rare_cloth)#0.3.2
    
    $items_list.append(item_snowball_small)#0.3.7
    $items_list.append(item_snowball)#0.3.7
    $items_list.append(item_snowman_item)#0.3.7
    $items_list.append(item_snowflake)#0.3.7
    $items_list.append(item_ice_crystal)#0.3.7
    $items_list.append(item_ice)#0.3.7
    $items_list.append(item_pine_cone)#0.3.7
    
    #+0.3.8
    $items_list.append(item_recipes_scroll_001) # = Consumable("Recipies scroll (Lewdpotion)", im.Scale("/Items/recipes_scroll.png",64,64), [{"target":"unlock_combo", "item1":item_megapotion, "item2":item_lustherb, "item_result":item_lewdpotion}], "Unlock the recipe in combo list.",0)#0.3.8
    $items_list.append(item_recipes_scroll_002) # Consumable("Recipies scroll (Mega potion)", im.Scale("/Items/recipes_scroll.png",64,64), [{"target":"unlock_combo", "item1":item_potion, "item2":item_honey, "item_result":item_megapotion}], "Unlock the recipe in combo list.",0)#0.3.8
    $items_list.append(item_recipes_scroll_003) # Consumable("Recipies scroll (Net)", im.Scale("/Items/recipes_scroll.png",64,64), [{"target":"unlock_combo", "item1":item_ivy, "item2":item_hairs, "item_result":item_net}], "Unlock the recipe in combo list.",0)#0.3.8
    $items_list.append(item_recipes_scroll_004) # Consumable("Recipies scroll (Oil)", im.Scale("/Items/recipes_scroll.png",64,64), [{"target":"unlock_combo", "item1":item_mucus, "item2":item_water, "item_result":item_oil}], "Unlock the recipe in combo list.",0)#0.3.8
    $items_list.append(item_recipes_scroll_005) # Consumable("Recipies scroll (Piece of latex)", im.Scale("/Items/recipes_scroll.png",64,64), [{"target":"unlock_combo", "item1":item_leather_piece, "item2":item_oil, "item_result":item_latex_piece}], "Unlock the recipe in combo list.",0)#0.3.8
    $items_list.append(item_recipes_scroll_006) # Consumable("Recipies scroll (Red ink)", im.Scale("/Items/recipes_scroll.png",64,64), [{"target":"unlock_combo", "item1":item_red_flower, "item2":item_oil, "item_result":item_red_ink}], "Unlock the recipe in combo list.",0)#0.3.8
    $items_list.append(item_recipes_scroll_007) # Consumable("Recipies scroll (Pink ink)", im.Scale("/Items/recipes_scroll.png",64,64), [{"target":"unlock_combo", "item1":item_white_ink, "item2":item_red_ink, "item_result":item_pink_ink}], "Unlock the recipe in combo list.",0)#0.3.8
    $items_list.append(item_recipes_scroll_009) # Consumable("Recipies scroll (Key for hidden cave)", im.Scale("/Items/recipes_scroll.png",64,64), [{"target":"unlock_combo", "item1":item_cave_key_part1, "item2":item_cave_key_part2, "item_result":item_cave_key}], "Unlock the recipe in combo list.",0)#0.3.8
    $items_list.append(item_recipes_scroll_010) # Consumable("Recipies scroll (Bear trap)", im.Scale("/Items/recipes_scroll.png",64,64), [{"target":"unlock_combo", "item1":item_trap_tool, "item2":item_satyr_horn, "item_result":item_bear_trap}], "Unlock the recipe in combo list.",0)#0.3.8
    $items_list.append(item_recipes_scroll_011) # Consumable("Recipies scroll (Catalist)", im.Scale("/Items/recipes_scroll.png",64,64), [{"target":"unlock_combo", "item1":item_honey, "item2":item_powershroom, "item_result":item_catalist}], "Unlock the recipe in combo list.",0)#0.3.8
    $items_list.append(item_recipes_scroll_012) # Consumable("Recipies scroll (Stamina juice)", im.Scale("/Items/recipes_scroll.png",64,64), [{"target":"unlock_combo", "item1":item_catalist, "item2":item_testosterone, "item_result":item_potion_stamina}], "Unlock the recipe in combo list.",0)#0.3.8
    $items_list.append(item_recipes_scroll_013) # Consumable("Recipies scroll (Armor juice)", im.Scale("/Items/recipes_scroll.png",64,64), [{"target":"unlock_combo", "item1":item_catalist, "item2":item_blue_flower, "item_result":item_potion_gain_armor}], "Unlock the recipe in combo list.",0)#0.3.8
    $items_list.append(item_recipes_scroll_014) # Consumable("Recipies scroll (Cavemaze Key)", im.Scale("/Items/recipes_scroll.png",64,64), [{"target":"unlock_combo", "item1":item_cavemaze_key_part1, "item2":item_cavemaze_key_part2, "item_result":item_cavemaze_key}], "Unlock the recipe in combo list.",0)#0.3.8
    $items_list.append(item_recipes_scroll_015) # Consumable("Recipies scroll (Snowball (small))", im.Scale("/Items/recipes_scroll.png",64,64), [{"target":"unlock_combo", "item1":item_snowball_small, "item2":item_snowball_small, "item_result":item_snowball}], "Unlock the recipe in combo list.",0)#0.3.8
    $items_list.append(item_recipes_scroll_016) 
    #-0.3.8
    $items_list.append(item_soup) 
    #--------Items-----------
    
    
    #++++++++CardsList+++++++
    $cards_list.append(card_attack_slap) 
    $cards_list.append(card_attack_nipples)
    $cards_list.append(card_skill_getarmor)
    $cards_list.append(card_attack_twinstrike)
    $cards_list.append(card_attack_boobsstrike)
    $cards_list.append(card_attack_bodyslam)
    $cards_list.append(card_attack_buttslap)
    $cards_list.append(card_skill_harness)
    $cards_list.append(card_skill_secretknowledge)
    $cards_list.append(card_catched)
    $cards_list.append(card_attack_tripletrike)
    
    $cards_list.append(card_attack_excitation)
    $cards_list.append(card_skill_impervios)
    $cards_list.append(card_power_inflame)
    $cards_list.append(card_power_nimble)
    $cards_list.append(card_attack_massblow)
    $cards_list.append(card_skill_shutup)
    $cards_list.append(card_skill_painjoy)
    $cards_list.append(card_attack_massspray)
    $cards_list.append(card_skill_firstejaculation)
    $cards_list.append(card_attack_firstpenetration)
    #--------CardList--------
    
    #++++++++Mods+++++++++
    $mods_list.append(mod_weak)
    $mods_list.append(mod_frail)
    $mods_list.append(mod_disgusting)
    $mods_list.append(mod_strength)
    $mods_list.append(mod_strength2)
    $mods_list.append(mod_strength5)
    $mods_list.append(mod_strength3)
    $mods_list.append(mod_excitation)
    $mods_list.append(mod_excitation_plus)
    $mods_list.append(mod_barricade)
    $mods_list.append(mod_nimble2)
    $mods_list.append(mod_nimble3)
    $mods_list.append(mod_defencepoison)
    $mods_list.append(mod_unplayablecard)
    $mods_list.append(mod_slimed1)
    $mods_list.append(mod_slimed3)
    $mods_list.append(mod_servant)
    $mods_list.append(mod_puppeteer)
    $mods_list.append(mod_drawcard1)
    $mods_list.append(mod_drawcard2)
    $mods_list.append(mod_defend_boss)
    $mods_list.append(mod_invicible)
    $mods_list.append(mod_widow_dom)
    $mods_list.append(mod_naked3_inv)
    $mods_list.append(mod_chastity_belt)#0.3.2
    $mods_list.append(mod_remove_chastity_belt)#0.3.2
    $mods_list.append(mod_naked)#0.3.2
    #--------Mods---------
    
    #++++++++Relicts+++++++++
    $relicts_list.append(relict_escape15)
    $relicts_list.append(relict_escape25)
    $relicts_list.append(relict_escape50)
    $relicts_list.append(relict_escape75)
    $relicts_list.append(relict_maxhp5)
    $relicts_list.append(relict_maxhp7)
    $relicts_list.append(relict_maxhp10)
    $relicts_list.append(relict_maxhp15)
    $relicts_list.append(relict_maxhp20)
    $relicts_list.append(relict_maxhp40)
    $relicts_list.append(relict_ftblock10)
    $relicts_list.append(relict_stblock12)
    $relicts_list.append(relict_thdblock17)
    $relicts_list.append(relict_thdblock15)
    $relicts_list.append(relict_thdblock75)
    $relicts_list.append(relict_4rblock75)
    $relicts_list.append(relict_addCard2)
    $relicts_list.append(relict_strenght1)
    $relicts_list.append(relict_stamina1)
    $relicts_list.append(relict_stamina2)
    $relicts_list.append(relict_stamina3)
    $relicts_list.append(relict_handjob_sub_strenght5)
    $relicts_list.append(relict_blowjob_sub_strenght5)
    $relicts_list.append(relict_enemy_male_strenght3)
    $relicts_list.append(relict_enemy_female_strenght3)
    $relicts_list.append(relict_adrenalin5)
    $relicts_list.append(relict_getblock5If3attack)
    $relicts_list.append(relict_getstamina1If10cardplayed)
    $relicts_list.append(relict_sub_strenght1)
    $relicts_list.append(relict_sub_strenght3)
    $relicts_list.append(relict_dom_strenght3)
    $relicts_list.append(relict_addgathering1)
    $relicts_list.append(relict_addrestorehp10)
    $relicts_list.append(relict_addrestorehp15)
    $relicts_list.append(relict_addrestorehp20)
    $relicts_list.append(relict_addrestorehp25)
    $relicts_list.append(relict_addrestorehp50)
    $relicts_list.append(relict_getblock1everycard)
    $relicts_list.append(relict_dealattack5If3Skill)
    $relicts_list.append(relict_goldenchest20)
    $relicts_list.append(relict_goldenchest50)
    $relicts_list.append(relict_deal10damageIf10cardplayed)
    $relicts_list.append(relict_deal1damageIf1cardplayed)
    $relicts_list.append(relict_discountitemshop3)
    $relicts_list.append(relict_discountitemshop5)
    $relicts_list.append(relict_discountclothindshop3)
    $relicts_list.append(relict_protectfromdefencepoison)
    $relicts_list.append(relict_deal42AttackOn7Turn)#0.3.9
    #--------Relicts---------
    
    
    #++++++++Attacks+++++++++
    #--------Attacks---------
    
           
    $ _notify = ""
    $ _notify2 = []

    #remove+++++
    # $Player.AddWardrobeInventory(torso_rope)
    # $Player.AddWardrobeInventory(panty_schl)
    # $Player.AddWardrobeInventory(bra_schl)
    # $Player.AddWardrobeInventory(neck_schl)
    # $Player.AddWardrobeInventory(stocking_schl)
    # $Player.AddWardrobeInventory(shoe_schl)
    # $Player.AddWardrobeInventory(skirt_schl)
    # $Player.AddWardrobeInventory(shirt_schl)
    # # $Player.AddWardrobeInventory(skirt_defender)
    # # $Player.AddWardrobeInventory(arm_defender)
    # # $Player.AddWardrobeInventory(boot_defender)
    # # $Player.AddWardrobeInventory(shirt_defender)
    # $Player.AddWardrobeInventory(farmer_hat_male_muscular)
    # $Player.AddWardrobeInventory(farmer_suit_male_muscular)
    # $Player.AddWardrobeInventory(farmer_boots_male_muscular)
    # $Player.AddWardrobeInventory(harness1_panty_male_muscular)
    # $Player.AddWardrobeInventory(harness1_male_muscular)
    # $Player.AddWardrobeInventory(harness2_male_muscular)
    # $Player.AddWardrobeInventory(straps_panty_male_muscular)
    # $Player.AddWardrobeInventory(straps_arms_male_muscular)
    # $Player.AddWardrobeInventory(thong_black_male_muscular)
    # $Player.AddWardrobeInventory(thong_transparent_male_muscular)
    # $Player.AddWardrobeInventory(glade_male_muscular)

    # $Player.AddWardrobeInventory(arm_pinkgloves)
    # $Player.AddWardrobeInventory(panty_din_futa)
    # $Player.AddWardrobeInventory(bra_din)
    # $Player.AddWardrobeInventory(arm_din)
    # $Player.AddWardrobeInventory(leg_din)
    # $Player.AddWardrobeInventory(latex_suit)

    # $Player.AddWardrobeInventory(demon_suit)
    # $Player.AddWardrobeInventory(demon_arm)
    # $Player.AddWardrobeInventory(demon_leg)
    # $Player.AddWardrobeInventory(demon_mask)

    # $Player.AddWardrobeInventory(fairy_bra)
    # $Player.AddWardrobeInventory(fairy_panty)

    # $Player.AddWardrobeInventory(leather_leg)
    # $Player.AddWardrobeInventory(swimsuit)
    # $Player.AddWardrobeInventory(swimsuit_red)
    # $Player.AddWardrobeInventory(swimsuit_pink)

    # $Player.AddWardrobeInventory(ivypanty)
    # $Player.AddWardrobeInventory(ivycorset)
    # $Player.AddWardrobeInventory(ivyfoot)
    # $Player.AddWardrobeInventory(ivycloak)

    # $Player.AddWardrobeInventory(sailordress)
    # $Player.AddWardrobeInventory(sailorboot)
    # $Player.AddWardrobeInventory(sailorneck)
    # $Player.AddWardrobeInventory(sailorpanty)

    # $Player.AddWardrobeInventory(bikinipanty)
    # $Player.AddWardrobeInventory(bikinibra)

    # $Player.AddWardrobeInventory(stocking)
    
    # $Player.AddWardrobeInventory(freya_shirt)# Clothing("Freya shirt", "freya_shirt", ("chest","bra" ),["female", "futa"],relict_stamina1, 20, 10, 3) #0.0.8
    # $Player.AddWardrobeInventory(freya_leg)# Clothing("Freya troopers", "freya_leg", ("legs", ),["female"],relict_getblock5If3attack, 10, 5, 3) #0.0.8
    # $Player.AddWardrobeInventory(freya_leg_futa)# Clothing("Freya troopers", "freya_leg_futa", ("legs", "penis"),["futa"],relict_getblock5If3attack, 10, 5, 3) #0.0.8
    # $Player.AddWardrobeInventory(freya_boots)# Clothing("Freya boots", "freya_boots", ("foot", ),["female", "futa"],relict_addrestorehp25, 11, 3, 3) #0.0.8
    # $Player.AddWardrobeInventory(freya_belt_panty)# Clothing("Freya belt", "freya_belt_panty", ("belt",),["female", "futa"],relict_maxhp5, 20, 10, 3) #0.0.8
    # $Player.AddWardrobeInventory(freya_arm)# Clothing("Freya gloves", "freya_arm", ("arm", ),["female", "futa"],relict_goldenchest20, 8, 4, 3) #0.0.8

    # $Player.AddWardrobeInventory(pantyhose)# Clothing("Pantyhose", "pantyhose", ("panties", "legs"),["female", "futa"],relict_stamina1, 15, 10, 3)  #0.0.9

    # $Player.AddWardrobeInventory(snow_hat)# Clothing("Snow hat", "snow_hat", ("head", ),["female", "futa"],relict_addrestorehp50, 15, 10, 3)  #0.1.0
    # $Player.AddWardrobeInventory(snow_boots)# Clothing("Snow boots", "snow_boots", ("foot", ),["female", "futa"],relict_goldenchest20, 15, 10, 3)  #0.1.0
    # $Player.AddWardrobeInventory(snow_dress)# Clothing("Snow dress", "snow_dress", ("chest", "bra", "hips"),["female", "futa"],relict_maxhp20, 15, 10, 3)  #0.1.0

    # $Player.AddWardrobeInventory(katarina_troupers)# Clothing("Katarina's troopers", "katarina_troupers", ("legs","hips","penis","belt"),["female", "futa"],relict_enemy_female_strenght3, 6, 6, 2, None, "", 1, "clothing", ["All Hunters"]) #0.0.6 
    # $Player.AddWardrobeInventory(katarina_arms)# Clothing("Katarina's arms", "katarina_arms", ("arm",),["female", "futa"],relict_maxhp7, 6, 4, 1, None, "", 1, "clothing", ["All Hunters"]) #0.0.6
    # $Player.AddWardrobeInventory(katarina_boots)# Clothing("Katarina's boots", "katarina_boots", ("foot", ),["female", "futa"],relict_maxhp5, 8, 10, 2, None, "", 1, "clothing", ["All Hunters"]) #0.0.6
    # $Player.AddWardrobeInventory(katarina_shirt)# Clothing("Katarina's jacket", "katarina_shirt", ("chest",),["female", "futa"],relict_getblock1everycard, 6, 3, 2, None, "", 1, "clothing", ["All Hunters"]) #0.0.6 

    # $Player.AddWardrobeInventory(maid_suit)# Clothing("Maid suit", "maid_suit", ("panties","bra","penis"),["female", "futa"],relict_maxhp20, 12, 8, 2, None, "", 1, "clothing", None) #0.1.9 
    # #male
    # $Player.AddWardrobeInventory(farmer_hat_male_muscular)# Clothing("Farmer hat", "farmer_hat", ("head",),["male"],relict_escape15, 1, 1, 1)
    # $Player.AddWardrobeInventory(farmer_suit_male_muscular)# Clothing("Farmer suit", "farmer_suit", ("chest","legs","hips","penis"),["male"],relict_ftblock10, 1, 1, 1)
    # $Player.AddWardrobeInventory(farmer_boots_male_muscular)# Clothing("Farmer boots", "farmer_boots", ("foot",),["male"],relict_addgathering1, 1, 1, 1)

    # $Player.AddWardrobeInventory(harness1_male_muscular)# Clothing("Harness top", "harness1", ("bra",),["male"],relict_addrestorehp10, 3, 3, 1)
    # $Player.AddWardrobeInventory(harness1_panty_male_muscular)# Clothing("Harness panty", "harness1_panty", ("panties","penis"),["male"],relict_addrestorehp20, 3, 3, 1)

    # $Player.AddWardrobeInventory(harness2_male_muscular)# Clothing("Harness top 2", "harness2", ("bra","panties","penis"),["male"],relict_maxhp15, 4, 3, 1)

    # $Player.AddWardrobeInventory(straps_panty_male_muscular)# Clothing("Straps panty", "straps_panty", ("bra","panties","penis"),["male"],relict_deal10damageIf10cardplayed, 5, 5, 1)
    # $Player.AddWardrobeInventory(straps_arms_male_muscular)# Clothing("Straps arms", "straps_arms", ("arm",),["male"],relict_escape50, 5, 5, 1)

    # $Player.AddWardrobeInventory(thong_black_male_muscular)# Clothing("Thong black", "thong_black", ("panties","penis"),["male"],relict_maxhp5, 8, 8, 1)
    # $Player.AddWardrobeInventory(thong_transparent_male_muscular)# Clothing("Thong net", "thong_transparent", ("panties","penis"),["male"],relict_sub_strenght1, 7, 6, 1)

    # $Player.AddWardrobeInventory(glade_male_muscular)# Clothing("Glade", "glade", ("hips","bra","panties"),["male"],relict_sub_strenght1, 4, 4, 1)

    # $Player.AddWardrobeInventory(robe_cloak)# Clothing("Robe cloak", "robe_cloak", ("chest",),["male"],relict_maxhp20, 20, 8, 2, None, "", 1, "clothing",  None) #0.1.9

    # $Player.AddWardrobeInventory(yoga_shirt)# Clothing("Yoga shirt", "yoga_bra", ("chest","bra"),["female", "futa"],relict_stamina1, 20, 10, 3, None, "", 1, "clothing", ["All Hunters"]) #0.2.1
    # $Player.AddWardrobeInventory(yoga_pants)# Clothing("Yoga pants", "yoga_pants", ("legs", ),["female"],relict_getblock5If3attack, 10, 5, 3, None, "", 1, "clothing", ["All Hunters"]) #0.2.1
    # $Player.AddWardrobeInventory(yoga_pants_futa)# Clothing("Yoga pants", "yoga_pants_futa", ("legs", "penis"),["futa"],relict_getblock5If3attack, 10, 5, 3, None, "", 1, "clothing", ["All Hunters"]) #0.2.1


    # $Player.AddWardrobeInventory(male_swimsuit)# Clothing("Swimsuit", "male_swimsuit", ("panties","bra","penis"),["male"],relict_maxhp15, 10, 10, 2) #0.2.1 

    # $Player.AddWardrobeInventory(cocktail_dress)# Clothing("Cocktail dress", "cocktail_dress", ("chest", "bra", "hips"),["female"],relict_dom_strenght3, 2, 2, 1)
    # $Player.AddWardrobeInventory(cocktail_dress_futa)# Clothing("Cocktail dress", "cocktail_dress_futa", ("chest", "bra", "hips","penis"),["futa"],relict_dom_strenght3, 2, 2, 1)

    # $Player.AddWardrobeInventory(confident_shirt)# Clothing("Confident shirt", "confident_shirt", ("chest",),["female", "futa"],relict_sub_strenght1, 5, 6, 1)
    # $Player.AddWardrobeInventory(confident_pants)# Clothing("Confident pants", "confident_pants", ("hips","panties"),["female"],relict_sub_strenght1, 4, 4, 1)
    # $Player.AddWardrobeInventory(confident_pants_futa)# Clothing("Confident pants", "confident_pants_futa", ("hips","panties"),["futa"],relict_sub_strenght1, 4, 4, 1)



    # $Player.AddWardrobeInventory(schl_skirt_male)# Clothing("Schl skirt", "schl_skirt_male", ("hips", "penis"),["male"],relict_maxhp5, 5, 8, 1, None, "", 1, "clothing", ["All Hunters"]) #0.2.2
    # $Player.AddWardrobeInventory(swimsuit_new_male)# Clothing("Swimsuit new", "swimsuit_new_male", ("panties","bra","penis"),["male"],relict_getblock5If3attack, 10, 10, 2) #0.2.2 

    # $Player.AddWardrobeInventory(bodysuit)# Clothing("Bodysuit", "bodysuit", ("chest","hips", "legs"),["female"],relict_dom_strenght3, 20, 8, 1)#0.2.2 
    # $Player.AddWardrobeInventory(bodysuit_futa)# Clothing("Bodysuit", "bodysuit_futa", ("chest","hips", "legs","penis"),["futa"],relict_dom_strenght3, 20, 8, 1)#0.2.2 


    # $Player.AddWardrobeInventory(fatima_pants_futa)# Clothing("Fatima's pants", "fatima_pants_futa", ("legs","hips","penis","belt"),["futa"],relict_dom_strenght3, 8, 8, 3, None, "", 1, "clothing", ["All Hunters"]) #0.2.3
    # $Player.AddWardrobeInventory(fatima_arms)# Clothing("Fatima's arms", "fatima_arms", ("arm",),["female", "futa"],relict_maxhp7, 8, 5, 3, None, "", 1, "clothing", ["All Hunters"]) #0.2.3
    # $Player.AddWardrobeInventory(fatima_shoes)# Clothing("Fatima's boots", "fatima_shoes", ("foot", ),["female", "futa"],relict_maxhp5, 9, 12, 3, None, "", 1, "clothing", ["All Hunters"]) #0.2.3
    # $Player.AddWardrobeInventory(fatima_bra)# Clothing("Fatima's jacket", "fatima_bra", ("chest",),["female", "futa"],relict_getblock1everycard, 5, 5, 3, None, "", 1, "clothing", ["All Hunters"]) #0.2.3
    # $Player.AddWardrobeInventory(fatima_neck)# Clothing("Fatima neck", "fatima_neck", ("neck", ),["female", "futa"],relict_goldenchest20, 4, 4, 3, None, "", 1, "clothing", ["All Hunters"]) #0.2.3


    # $Player.AddWardrobeInventory(stringbody)# Clothing("Stringbody", "stringbody", ("bra","panties"),["female"],relict_dom_strenght3, 20, 8, 1)#0.2.4
    # $Player.AddWardrobeInventory(stringbody_futa)# Clothing("Stringbody", "stringbody_futa", ("bra","panties","penis"),["futa"],relict_dom_strenght3, 20, 8, 1)#0.2.4 

    # $Player.AddWardrobeInventory(lucidity_arms_male)# Clothing("Lucidity's arms", "lucidity_arms", ("arm",),["male"],relict_maxhp7, 6, 4, 1) #0.2.4
    # $Player.AddWardrobeInventory(lucidity_pants_male)# Clothing("Lucidity's troopers", "lucidity_pants", ("legs","hips","penis","belt"),["male"],relict_enemy_female_strenght3, 6, 6, 2) #0.2.4 
    # $Player.AddWardrobeInventory(lucidity_socks_male)# Clothing("Lucidity's socks", "lucidity_socks", ("foot", ),["male"],relict_maxhp5, 8, 10, 2) #0.2.4
    # $Player.AddWardrobeInventory(lucidity_jacket_male)# Clothing("Lucidity's jacket", "lucidity_jacket", ("chest",),["male"],relict_getblock1everycard, 6, 3, 2) #0.2.4
    # $Player.AddWardrobeInventory(lucidity_shirt_male)# Clothing("Lucidity's shirt", "lucidity_shirt", ("bra",),["male"],relict_addrestorehp25, 6, 3, 2) #0.2.4

    # $Player.AddWardrobeInventory(mushrooms_hat)# Clothing("Mushroom hat", "mushrooms_hat", ("head",),["female", "futa"],relict_stamina2, 30, 15, 4) #0.2.1
    # $Player.AddWardrobeInventory(mushrooms_hat_male)# Clothing("Mushroom hat", "mushrooms_hat_male", ("head",),["male"],relict_stamina2, 30, 15, 4) #0.2.1

    # $Player.AddWardrobeInventory(night_suit)# Clothing("Night suit", "night_suit", ("bra","chest","panties"),["female"],relict_addrestorehp25, 8, 5, 4, None, "", 1, "clothing", ["All Hunters"]) #0.2.5
    # $Player.AddWardrobeInventory(night_suit_futa)# Clothing("Night suit", "night_suit_futa", ("bra","chest","panties","penis"),["futa"],relict_addrestorehp25, 8, 5, 4, None, "", 1, "clothing", ["All Hunters"]) #0.2.5
    # $Player.AddWardrobeInventory(night_suit2_futa)# Clothing("Night suit 2", "night_suit2_futa", ("bra","chest","panties","penis"),["futa"],relict_addrestorehp25, 8, 5, 4, None, "", 1, "clothing", ["All Hunters"]) #0.2.5

    # $Player.AddWardrobeInventory(tifa_arms)# Clothing("Tifa's arms", "tifa_arms", ("arm",),["female", "futa"],relict_getstamina1If10cardplayed, 20, 10, 4, None, "", 1, "clothing", ["All Hunters"]) #0.2.6
    # $Player.AddWardrobeInventory(tifa_boots)# Clothing("Tifa's boots", "tifa_boots", ("foot",),["female", "futa"],relict_deal10damageIf10cardplayed, 22, 10, 4, None, "", 1, "clothing", ["All Hunters"]) #0.2.6
    # $Player.AddWardrobeInventory(tifa_shirt)# Clothing("Tifa's shirt", "tifa_shirt", ("chest","bra"),["female", "futa"],relict_escape50, 25, 15, 4, None, "", 1, "clothing", ["All Hunters"]) #0.2.6
    # $Player.AddWardrobeInventory(tifa_skirt)# Clothing("Tifa's skirt", "tifa_skirt", ("hips",),["female"],relict_stamina1, 30, 15, 4, None, "", 1, "clothing", ["All Hunters"]) #0.2.6
    # $Player.AddWardrobeInventory(tifa_skirt_futa)# Clothing("Tifa's skirt", "tifa_skirt_futa", ("hips","penis"),["futa"],relict_stamina1, 30, 15, 4, None, "", 1, "clothing", ["All Hunters"]) #0.2.6


    # $Player.AddWardrobeInventory(yoka_pants)# Clothing("Yoka's pants", "yoka_pants", ("panties",),["female"],relict_protectfromdefencepoison, 31, 16, 5) #0.2.7
    # $Player.AddWardrobeInventory(yoka_pants_futa)# Clothing("Yoka's pants", "yoka_pants_futa", ("panties","penis"),["futa"],relict_protectfromdefencepoison, 31, 16, 5) #0.2.7
    # $Player.AddWardrobeInventory(yoka_arms)# Clothing("Yoka's arms", "yoka_arms", ("arm",),["female", "futa"],relict_protectfromdefencepoison, 12, 10, 3) #0.2.7 
    # $Player.AddWardrobeInventory(yoka_bra)# Clothing("Yoka's bra", "yoka_bra", ("bra",),["female", "futa"],relict_maxhp15, 10, 11, 4) #0.2.7
    # $Player.AddWardrobeInventory(yoka_legs)# Clothing("Yoka's stoking", "yoka_legs", ("legs","foot"),["female", "futa"],relict_maxhp15, 7, 14, 4) #0.2.7
    # $Player.AddWardrobeInventory(yoka_neck)# Clothing("Yoka's neck", "yoka_neck", ("neck",),["female", "futa"],relict_stamina3, 5, 5, 7) #0.2.7

    # $Player.AddWardrobeInventory(wizard_boots_male)# Clothing("Wizard boots", "wizard_boots_male", ("foot", ),["male"],relict_maxhp20, 8, 5, 5) #0.2.7
    # $Player.AddWardrobeInventory(wizard_cloak_male)# Clothing("Wizard cloak", "wizard_cloak_male", ("head","neck"),["male"],relict_stamina3, 20, 13, 5) #0.2.7
    # $Player.AddWardrobeInventory(wizard_pants_male)# Clothing("Wizard troopers", "wizard_pants_male", ("legs","hips","penis"),["male"],relict_protectfromdefencepoison, 26, 10, 5) #0.2.7
    # $Player.AddWardrobeInventory(wizard_tunic_male)# Clothing("Wizard tunic", "wizard_tunic_male", ("chest","bra","arm","belt"),["male"],relict_protectfromdefencepoison, 25, 25, 5) #0.2.7

    # $Player.AddWardrobeInventory(lara_top)# Clothing("Lara's top", "lara_top", ("chest",),["female", "futa"],relict_goldenchest20, 11, 8, 3, None, "", 1, "clothing", ["All Hunters"]) #0.2.7
    # $Player.AddWardrobeInventory(lara_belt)# Clothing("Lara's belt", "lara_belt", ("belt",),["female", "futa"],relict_addgathering1, 14, 7, 3, None, "", 1, "clothing", ["All Hunters"]) #0.2.7
    # $Player.AddWardrobeInventory(lara_harness_futa)# Clothing("Lara's harness", "lara_harness_futa", ("panties","bra","penis"),["futa"],relict_escape75, 13, 10, 3, None, "", 1, "clothing", ["All Hunters"]) #0.2.7
    # $Player.AddWardrobeInventory(lara_shorts_futa)# Clothing("Lara's shorts", "lara_shorts_futa", ("hips","penis"),["futa"],relict_escape50, 12, 10, 3, None, "", 1, "clothing", ["All Hunters"]) #0.2.7
    # $Player.AddWardrobeInventory(lara_harness)# Clothing("Lara's harness", "lara_harness", ("panties","bra"),["female"],relict_escape75, 13, 10, 3, None, "", 1, "clothing", ["All Hunters"]) #0.2.7
    # $Player.AddWardrobeInventory(lara_shorts)# Clothing("Lara's shorts", "lara_shorts", ("hips"),["female"],relict_escape50, 12, 10, 3, None, "", 1, "clothing", ["All Hunters"]) #0.2.7

    # $Player.AddWardrobeInventory(warrior_panty_legs)# Clothing("Warrior troopers", "warrior_panty_legs", ("legs","hips","panties","penis"),["male"],relict_thdblock15, 30, 13, 6) #0.2.7
    # $Player.AddWardrobeInventory(warrior_jacket_male)# Clothing("Warrior jacket", "warrior_jacket_male", ("chest","arm"),["male"],relict_thdblock15, 30, 11, 5) #0.2.7
    # $Player.AddWardrobeInventory(warrior_hat_male)# Clothing("Warrior hat", "warrior_hat_male", ("head",),["male"],relict_thdblock15, 30, 13, 5) #0.2.7
    # $Player.AddWardrobeInventory(warrior_chest_male)# Clothing("Warrior chest", "warrior_chest_male", ("bra","neck"),["male"],relict_thdblock15, 30, 12, 4) #0.2.7

    # $Player.AddWardrobeInventory(x_jumpsuit)# Clothing("Lattice suit", "x_jumpsuit", ("bra","hips","legs","neck","panties"),["female"],relict_thdblock75, 32, 13, 6)
    # $Player.AddWardrobeInventory(x_jumpsuit_futa)# Clothing("Lattice suit", "x_jumpsuit_futa", ("bra","hips","legs","neck","panties","penis"),["futa"],relict_4rblock75, 32, 13, 6)

    # $Player.AddWardrobeInventory(demonsuit2)# Clothing("Demonsuit 2", "demonsuit2", ("hips","legs","neck","arm"),["female"],relict_thdblock15, 40, 15, 6)
    # $Player.AddWardrobeInventory(demonsuit2_futa)# Clothing("Demonsuit 2", "demonsuit2_futa", ("chest","hips","legs","neck","arm","penis"),["futa"],relict_thdblock15, 40, 15, 6)
    # $Player.AddWardrobeInventory(demonsuit2_pants)# Clothing("Demonsuit 2 body", "demonsuit2_pants", ("chest","bra","panties","belt"),["female"],relict_thdblock15, 36, 14, 6)
    # $Player.AddWardrobeInventory(demonsuit2_pants_futa)# Clothing("Demonsuit 2 body", "demonsuit2_pants_futa", ("chest","bra","panties","belt","penis"),["futa"],relict_thdblock15, 36, 14, 6)
    # $Player.AddWardrobeInventory(demonsuit2_mask)# Clothing("Demonsuit 2 mask", "demonsuit2_mask", ("head",),["female","futa"],relict_thdblock15, 39, 16, 6)

    # $Player.AddWardrobeInventory(sport_suit_bra)# Clothing("Sport's top", "sport_suit_bra", ("chest","bra"),["female", "futa"],relict_deal1damageIf1cardplayed, 41, 18, 5, None, "", 1, "clothing", ["All Hunters"]) #0.3.0
    # $Player.AddWardrobeInventory(sport_suit_leggins)# Clothing("Sport's leggins", "sport_suit_leggins", ("legs",),["female", "futa"],relict_deal1damageIf1cardplayed, 45, 10, 5, None, "", 1, "clothing", ["All Hunters"]) #0.3.0
    # $Player.AddWardrobeInventory(sport_suit_pantys)# Clothing("Sport's pants", "sport_suit_pantys", ("panties",),["female"],relict_deal1damageIf1cardplayed, 41, 16, 5, None, "", 1, "clothing", ["All Hunters"]) #0.3.0
    # $Player.AddWardrobeInventory(sport_suit_pantys_futa)# = Clothing("Sport's pants", "sport_suit_pantys_futa", ("panties","penis"),["futa"],relict_deal1damageIf1cardplayed, 41, 16, 5, None, "", 1, "clothing", ["All Hunters"]) #0.3.0
    
    # $Player.AddHomeInventory(item_herb)
    # $Player.AddHomeInventory(item_herb)
    # $Player.AddHomeInventory(item_lustherb)
    # $Player.AddHomeInventory(item_herb)
    # $Player.AddHomeInventory(item_ivy)
    # $Player.AddHomeInventory(item_supply_potion)
    # $Player.AddHomeInventory(item_potion)
    # $Player.AddHomeInventory(item_megapotion)
    # $Player.AddHomeInventory(item_smallstick)
    # $Player.AddHomeInventory(item_cloth_piece)
    # $Player.AddHomeInventory(item_leather_piece)
    # $Player.AddHomeInventory(item_latex_piece)
    # $Player.AddHomeInventory(item_book)
    # $Player.AddHomeInventory(item_bone)
    
    # $Player.AddHomeInventory(item_bone)
    # $Player.AddHomeInventory(item_stone)
    # $Player.AddHomeInventory(item_blue_mushroom)
    # $Player.AddHomeInventory(item_powershroom)
    # $Player.AddHomeInventory(item_exciteshroom)
    # $Player.AddHomeInventory(item_hairs)
    # $Player.AddHomeInventory(item_red_flower)
    # $Player.AddHomeInventory(item_blue_flower)
    # $Player.AddHomeInventory(item_yellow_flower)
    # $Player.AddHomeInventory(item_honey)
    

    # $Player.AddHomeInventory(item_mucus)
    # $Player.AddHomeInventory(item_worm)
    # $Player.AddHomeInventory(item_net)
    # $Player.AddHomeInventory(item_pollen)
    # $Player.AddHomeInventory(item_oil)
    # $Player.AddHomeInventory(item_return_pass)
    # $Player.AddHomeInventory(item_satyr_horn)
    # $Player.AddHomeInventory(item_satyr_fur)
    # $Player.AddHomeInventory(item_satyr_cum)
    # $Player.AddHomeInventory(item_flydick_cum)
    
    #remove------
    
    
    #+++++++Town Square events+++++++
    #n, name, available_genders, hr_need, replayable, stage_max
    $Player.AddTownSquareEvent(SquareEvent(1, "Where is Geralt?", ("male","female","futa"), 1, False, 5))
    $Player.AddTownSquareEvent(SquareEvent(2, "Richman with huge cock", ("female","futa"), 1, True, 1))
    $Player.AddTownSquareEvent(SquareEvent(3, "Coin on the ground", ("female","futa"), 1, True, 1))
    $events_christmas = SquareEvent(4, "Christmas tree", ("female","futa"), 1, False, 1) #0.1.0
    #-------Town Square events-------
    
    
    
    #Shop clothing+++++++++++++++++
    $product_arm_din = Product(arm_din, 350, [{"item":item_cloth_piece, "count":3}])
    $product_leg_din = Product(leg_din, 400, [{"item":item_cloth_piece, "count":1},{"item":item_ivy, "count":4}])
    $product_bra_din = Product(bra_din, 100, [])
    $product_panty_din = Product(panty_din, 100, [])
    $product_panty_din_futa = Product(panty_din_futa, 100, [])
    $product_panty_din_male_muscular = Product(panty_din_male_muscular, 100, [])
    $product_shirt_din_male_muscular = Product(shirt_din_male_muscular, 100, [])
    
    $product_arm_pinkgloves = Product(arm_pinkgloves, 600, [{"item":item_leather_piece, "count":2},{"item":item_pink_ink, "count":2}])
    
    $product_panty_glade = Product(panty_glade, 200, [{"item":item_cloth_piece, "count":2}])
    $product_torso_rope = Product(torso_rope, 500, [{"item":item_cloth_piece, "count":1},{"item":item_ivy, "count":16}])
    
    $product_panty_schl = Product(panty_schl, 500, [{"item":item_cloth_piece, "count":4},{"item":item_book, "count":1}])
    $product_bra_schl = Product(bra_schl, 500, [{"item":item_cloth_piece, "count":1},{"item":item_book, "count":2},{"item":item_ivy, "count":4}])
    $product_neck_schl = Product(neck_schl, 750, [{"item":item_book, "count":1},{"item":item_ivy, "count":1},{"item":item_stone, "count":1}])
    $product_stocking_schl = Product(stocking_schl, 500, [{"item":item_cloth_piece, "count":6},{"item":item_book, "count":2}])
    $product_shoe_schl = Product(shoe_schl, 400, [{"item":item_cloth_piece, "count":2},{"item":item_book, "count":2},{"item":item_stone, "count":2}])
    $product_skirt_schl = Product(skirt_schl, 600, [{"item":item_cloth_piece, "count":5},{"item":item_book, "count":1},{"item":item_red_flower, "count":4}])
    $product_shirt_schl = Product(shirt_schl, 800, [{"item":item_cloth_piece, "count":10},{"item":item_book, "count":2}])
    
    $product_skirt_satyr = Product(skirt_satyr, 750, [{"item":item_cloth_piece, "count":3},{"item":item_satyr_fur, "count":8}])
    $product_bra_satyr = Product(bra_satyr, 420, [{"item":item_cloth_piece, "count":4}])
    $product_arm_satyr = Product(arm_satyr, 350, [{"item":item_cloth_piece, "count":2}])
    $product_head_satyr = Product(head_satyr, 350, [{"item":item_satyr_horn, "count":2}])
    
    $product_latex_suit = Product(latex_suit, 2000, [{"item":item_latex_piece, "count":10}])#0.0.5
    
    $ShopWardrobe.addNewProduct(product_arm_din)
    $ShopWardrobe.addNewProduct(product_leg_din)
    $ShopWardrobe.addNewProduct(product_bra_din)
    $ShopWardrobe.addNewProduct(product_panty_din)
    $ShopWardrobe.addNewProduct(product_panty_din_futa)
    $ShopWardrobe.addNewProduct(product_panty_din_male_muscular)
    $ShopWardrobe.addNewProduct(product_shirt_din_male_muscular)
    $ShopWardrobe.addNewProduct(product_panty_glade)
    $ShopWardrobe.addNewProduct(product_torso_rope)
    
    $ShopWardrobe.addNewProduct(product_panty_schl)
    $ShopWardrobe.addNewProduct(product_bra_schl)
    $ShopWardrobe.addNewProduct(product_neck_schl)
    $ShopWardrobe.addNewProduct(product_stocking_schl)
    $ShopWardrobe.addNewProduct(product_shoe_schl)
    $ShopWardrobe.addNewProduct(product_skirt_schl)
    $ShopWardrobe.addNewProduct(product_shirt_schl)
    
    $ShopWardrobe.addNewProduct(product_skirt_satyr)
    $ShopWardrobe.addNewProduct(product_bra_satyr)
    $ShopWardrobe.addNewProduct(product_arm_satyr)
    $ShopWardrobe.addNewProduct(product_head_satyr)
    
    $ShopWardrobe.addNewProduct(product_latex_suit) #0.0.5
    
    $ShopWardrobe.addNewProduct(product_arm_pinkgloves)
    
    #+0.0.6
    $product_demon_suit = Product(demon_suit, 3000, [{"item":item_stone, "count":10},{"item":item_cloth_piece, "count":2},{"item":item_oil, "count":1}]) #0.0.6
    $product_demon_arm = Product(demon_arm, 1500, [{"item":item_stone, "count":8},{"item":item_oil, "count":1}]) #0.0.6
    $product_demon_leg = Product(demon_leg, 1500, [{"item":item_stone, "count":8},{"item":item_oil, "count":1}]) #0.0.6
    $product_demon_mask = Product(demon_mask, 2500, [{"item":item_stone, "count":7},{"item":item_oil, "count":1}]) #0.0.6

    $product_fairy_bra = Product(fairy_bra, 700, [{"item":item_pollen, "count":1},{"item":item_ivy, "count":2},{"item":item_cloth_piece, "count":2}]) #0.0.6 
    $product_fairy_panty = Product(fairy_panty, 700, [{"item":item_pollen, "count":1},{"item":item_ivy, "count":2},{"item":item_cloth_piece, "count":2}]) #0.0.6 
    
    $product_leather_leg = Product(leather_leg, 1000, [{"item":item_leather_piece, "count":8}])#0.0.5
    $product_swimsuit = Product(swimsuit, 2500, [{"item":item_leather_piece, "count":3},{"item":item_net, "count":6}])#0.0.5
    $product_swimsuit_red = Product(swimsuit_red, 2600, [{"item":item_leather_piece, "count":3},{"item":item_net, "count":6},{"item":item_red_ink, "count":1}])#0.0.5
    $product_swimsuit_pink = Product(swimsuit_pink, 2700, [{"item":item_leather_piece, "count":3},{"item":item_net, "count":6},{"item":item_pink_ink, "count":1}])#0.0.5

    $product_ivypanty = Product(ivypanty, 1800, [{"item":item_ivy, "count":8}])#0.0.6
    $product_ivycorset = Product(ivycorset, 1900, [{"item":item_ivy, "count":2}, {"item":item_leather_piece, "count":3}])#0.0.6
    $product_ivyfoot = Product(ivyfoot, 3000, [{"item":item_ivy, "count":2}, {"item":item_leather_piece, "count":2}])#0.0.6
    $product_ivycloak = Product(ivycloak, 14000, [{"item":item_ivy, "count":2}, {"item":item_leather_piece, "count":2},{"item":item_cloth_piece, "count":20}])#0.0.6

    $product_sailordress = Product(sailordress, 2000, [{"item":item_cloth_piece, "count":10},{"item":item_white_ink, "count":1}])#0.0.6
    $product_sailorboot = Product(sailorboot, 1700, [{"item":item_ivy, "count":2},{"item":item_cloth_piece, "count":10},{"item":item_white_ink, "count":1}])#0.0.6
    $product_sailorneck = Product(sailorneck, 1500, [{"item":item_cloth_piece, "count":1},{"item":item_white_ink, "count":1}])#0.0.6
    $product_sailorpanty = Product(sailorpanty, 1900, [{"item":item_cloth_piece, "count":2},{"item":item_white_ink, "count":1}])#0.0.6

    $product_bikinipanty = Product(bikinipanty, 15200, [{"item":item_ivy, "count":2},{"item":item_cloth_piece, "count":2},{"item":item_white_ink, "count":1}])#0.0.6
    $product_bikinibra = Product(bikinibra, 15100, [{"item":item_ivy, "count":2},{"item":item_cloth_piece, "count":2},{"item":item_white_ink, "count":1}])#0.0.6
    
    $product_stocking = Product(stocking, 1600, [{"item":item_leather_piece, "count":2},{"item":item_net, "count":4}])#0.0.6
    
    $ShopWardrobe.addNewProduct(product_demon_suit) #0.0.6
    $ShopWardrobe.addNewProduct(product_demon_arm) #0.0.6
    $ShopWardrobe.addNewProduct(product_demon_leg) #0.0.6
    $ShopWardrobe.addNewProduct(product_demon_mask) #0.0.6
    $ShopWardrobe.addNewProduct(product_fairy_bra) #0.0.6
    $ShopWardrobe.addNewProduct(product_fairy_panty) #0.0.6
    
    $ShopWardrobe.addNewProduct(product_leather_leg) #0.0.6
    $ShopWardrobe.addNewProduct(product_swimsuit) #0.0.6
    $ShopWardrobe.addNewProduct(product_swimsuit_red) #0.0.6
    $ShopWardrobe.addNewProduct(product_swimsuit_pink) #0.0.6
    
    $ShopWardrobe.addNewProduct(product_ivypanty) #0.0.6
    $ShopWardrobe.addNewProduct(product_ivycorset) #0.0.6
    $ShopWardrobe.addNewProduct(product_ivyfoot) #0.0.6
    $ShopWardrobe.addNewProduct(product_ivycloak) #0.0.6
    
    $ShopWardrobe.addNewProduct(product_sailordress) #0.0.6
    $ShopWardrobe.addNewProduct(product_sailorboot) #0.0.6
    $ShopWardrobe.addNewProduct(product_sailorneck) #0.0.6
    $ShopWardrobe.addNewProduct(product_sailorpanty) #0.0.6
    
    $ShopWardrobe.addNewProduct(product_bikinipanty) #0.0.6
    $ShopWardrobe.addNewProduct(product_bikinibra) #0.0.6
    
    $ShopWardrobe.addNewProduct(product_stocking) #0.0.6
    #-0.0.6
    
    #+0.0.9
    $product_pantyhose = Product(pantyhose, 8500, [{"item":item_net, "count":10}]) #0.0.9
    $ShopWardrobe.addNewProduct(product_pantyhose) #0.0.9
    #-0.0.9
    
    #+0.1.9
    # $product_robe_cloak = Product(robe_cloak, 50, [])
    # $product_maid_suit = Product(maid_suit, 50, [])
    # $ShopWardrobe.addNewProduct(product_robe_cloak) 
    # $ShopWardrobe.addNewProduct(product_maid_suit) 
    $product_katarina_troupers = Product(katarina_troupers, 50, [])
    $product_katarina_arms = Product(katarina_arms, 50, [])
    $product_katarina_boots = Product(katarina_boots, 50, [])
    $product_katarina_shirt = Product(katarina_shirt, 50, [])
    $ShopWardrobe.addNewProduct(product_katarina_troupers) 
    $ShopWardrobe.addNewProduct(product_katarina_arms) 
    $ShopWardrobe.addNewProduct(product_katarina_boots) 
    $ShopWardrobe.addNewProduct(product_katarina_shirt) 
    #-0.1.9
    
    $product_yoga_shirt = Product(yoga_shirt, 1000, [])
    $product_yoga_pants = Product(yoga_pants, 1000, [])
    $product_yoga_pants_futa = Product(yoga_pants_futa, 1000, [])
    $ShopWardrobe.addNewProduct(product_yoga_shirt) 
    $ShopWardrobe.addNewProduct(product_yoga_pants) 
    $ShopWardrobe.addNewProduct(product_yoga_pants_futa) 
    
    $product_male_swimsuit = Product(male_swimsuit, 3000, [])
    $ShopWardrobe.addNewProduct(product_male_swimsuit) 
    
    $product_cocktail_dress = Product(cocktail_dress, 6500, [{"item":item_cloth_piece, "count":3},{"item":item_blue_flower, "count":3},{"item":item_red_flower, "count":3}])
    $ShopWardrobe.addNewProduct(product_cocktail_dress) 
    $product_cocktail_dress_futa = Product(cocktail_dress_futa, 6500, [{"item":item_cloth_piece, "count":3},{"item":item_blue_flower, "count":3},{"item":item_red_flower, "count":3}])
    $ShopWardrobe.addNewProduct(product_cocktail_dress_futa) 

    $product_confident_shirt = Product(confident_shirt, 5500, [{"item":item_cloth_piece, "count":3},{"item":item_leather_piece, "count":1}])
    $ShopWardrobe.addNewProduct(product_confident_shirt) 
    $product_confident_pants= Product(confident_pants, 5500, [{"item":item_cloth_piece, "count":3},{"item":item_leather_piece, "count":1}])
    $ShopWardrobe.addNewProduct(product_confident_pants) 
    $product_confident_pants_futa = Product(confident_pants_futa, 5500, [{"item":item_cloth_piece, "count":3},{"item":item_leather_piece, "count":1}])
    $ShopWardrobe.addNewProduct(product_confident_pants_futa) 
    
    
    $product_schl_skirt_male = Product(schl_skirt_male, 6000, [{"item":item_cloth_piece, "count":5},{"item":item_book, "count":1},{"item":item_red_flower, "count":4}])
    $ShopWardrobe.addNewProduct(product_schl_skirt_male) 
    
    
    $product_fatima_pants_futa = Product(fatima_pants_futa, 8000, []) #0.2.3
    $product_fatima_arms = Product(fatima_arms, 4000, []) #0.2.3
    $product_fatima_shoes = Product(fatima_shoes, 2000, []) #0.2.3
    $product_fatima_bra = Product(fatima_bra, 7000, []) #0.2.3
    $product_fatima_neck = Product(fatima_neck, 3000, []) #0.2.3
    $ShopWardrobe.addNewProduct(product_fatima_pants_futa)
    $ShopWardrobe.addNewProduct(product_fatima_arms)
    $ShopWardrobe.addNewProduct(product_fatima_shoes)
    $ShopWardrobe.addNewProduct(product_fatima_bra)
    $ShopWardrobe.addNewProduct(product_fatima_neck)
    
    #+0.2.5
    $product_mushrooms_hat = Product(mushrooms_hat, 10000, [{"item":item_amanita, "count":5},{"item":item_mushroom_slime, "count":1} ]) #0.2.3
    $ShopWardrobe.addNewProduct(product_mushrooms_hat)
    $product_mushrooms_hat_male = Product(mushrooms_hat_male, 10000, [{"item":item_amanita, "count":5},{"item":item_mushroom_slime, "count":1} ]) #0.2.3
    $ShopWardrobe.addNewProduct(product_mushrooms_hat_male)
    
    $product_night_suit = Product(night_suit, 12000, [{"item":item_red_ink, "count":1},{"item":item_ivy, "count":3} ]) #0.2.5
    $product_night_suit_futa = Product(night_suit, 12000, [{"item":item_red_ink, "count":1},{"item":item_ivy, "count":3} ]) #0.2.5
    $product_night_suit2_futa = Product(night_suit, 13000, [{"item":item_red_ink, "count":2},{"item":item_ivy, "count":3} ]) #0.2.5
    $ShopWardrobe.addNewProduct(product_night_suit)
    $ShopWardrobe.addNewProduct(product_night_suit_futa)
    $ShopWardrobe.addNewProduct(product_night_suit2_futa)    
    #-0.2.5
    
    #+0.2.6
    $product_tifa_arms = Product(tifa_arms, 20000, [{"item":item_cloth_piece, "count":3},{"item":item_leather_piece, "count":3}])
    $ShopWardrobe.addNewProduct(product_tifa_arms) 
    $product_tifa_boots = Product(tifa_boots, 20000, [{"item":item_cloth_piece, "count":1},{"item":item_leather_piece, "count":3}])
    $ShopWardrobe.addNewProduct(product_tifa_boots) 
    $product_tifa_shirt = Product(tifa_shirt, 30000, [{"item":item_cloth_piece, "count":5},{"item":item_leather_piece, "count":1},{"item":item_ivy, "count":2}])
    $ShopWardrobe.addNewProduct(product_tifa_shirt) 
    $product_tifa_skirt = Product(tifa_skirt, 35000, [{"item":item_cloth_piece, "count":2},{"item":item_leather_piece, "count":5},{"item":item_ivy, "count":2}])
    $ShopWardrobe.addNewProduct(product_tifa_skirt)
    $product_tifa_skirt_futa = Product(tifa_skirt_futa, 35000, [{"item":item_cloth_piece, "count":2},{"item":item_leather_piece, "count":5},{"item":item_ivy, "count":2}])
    $ShopWardrobe.addNewProduct(product_tifa_skirt_futa)
    #-0.2.6
    
    #+0.1.7
    
    $product_farmer_hat_male_muscular = Product(farmer_hat_male_muscular, 350, [{"item":item_cloth_piece, "count":3}])
    $product_farmer_suit_male_muscular = Product(farmer_suit_male_muscular, 650, [{"item":item_cloth_piece, "count":6}])
    $product_farmer_boots_male_muscular = Product(farmer_boots_male_muscular, 250, [{"item":item_cloth_piece, "count":2}])

    $product_harness1_male_muscular = Product(harness1_male_muscular, 700, [{"item":item_cloth_piece, "count":1},{"item":item_ivy, "count":4}])
    $product_harness1_panty_male_muscular = Product(harness1_panty_male_muscular, 600, [{"item":item_cloth_piece, "count":2},{"item":item_ivy, "count":5}])

    $product_harness2_male_muscular = Product(harness2_male_muscular, 1200, [{"item":item_cloth_piece, "count":3},{"item":item_ivy, "count":6}])

    $product_straps_panty_male_muscular = Product(straps_panty_male_muscular, 900, [{"item":item_leather_piece, "count":4},{"item":item_ivy, "count":6}])
    $product_straps_arms_male_muscular = Product(straps_arms_male_muscular, 600, [{"item":item_leather_piece, "count":2}])

    $product_thong_transparent_male_muscular = Product(thong_transparent_male_muscular, 1700, [{"item":item_leather_piece, "count":2},{"item":item_net, "count":6}])
    $product_thong_black_male_muscular = Product(thong_black_male_muscular, 1500, [{"item":item_leather_piece, "count":5}])

    $product_glade_male_muscular = Product(glade_male_muscular, 1500, [{"item":item_cloth_piece, "count":4},{"item":item_satyr_fur, "count":4},{"item":item_ivy, "count":4}])
    
    $ShopWardrobe.addNewProduct(product_farmer_hat_male_muscular)
    $ShopWardrobe.addNewProduct(product_farmer_suit_male_muscular)
    $ShopWardrobe.addNewProduct(product_farmer_boots_male_muscular)
    $ShopWardrobe.addNewProduct(product_harness1_male_muscular)
    $ShopWardrobe.addNewProduct(product_harness1_panty_male_muscular)
    $ShopWardrobe.addNewProduct(product_harness2_male_muscular)
    $ShopWardrobe.addNewProduct(product_straps_panty_male_muscular)
    $ShopWardrobe.addNewProduct(product_straps_arms_male_muscular)
    $ShopWardrobe.addNewProduct(product_thong_transparent_male_muscular)
    $ShopWardrobe.addNewProduct(product_thong_black_male_muscular)
    $ShopWardrobe.addNewProduct(product_glade_male_muscular)
    
    
    
    
    $product_lara_top = Product(lara_top, 18500, [{"item":item_cloth_piece, "count":4}])
    $ShopWardrobe.addNewProduct(product_lara_top)
    $product_lara_belt = Product(lara_belt, 17900, [{"item":item_cloth_piece, "count":2},{"item":item_ivy, "count":4}])
    $ShopWardrobe.addNewProduct(product_lara_belt)
    $product_lara_harness_futa = Product(lara_harness_futa, 45500, [{"item":item_ivy, "count":6}])
    $ShopWardrobe.addNewProduct(product_lara_harness_futa)
    $product_lara_shorts_futa = Product(lara_shorts_futa, 19500, [{"item":item_cloth_piece, "count":8}])
    $ShopWardrobe.addNewProduct(product_lara_shorts_futa)
    $product_lara_harness = Product(lara_harness, 45500, [{"item":item_ivy, "count":6}])
    $ShopWardrobe.addNewProduct(product_lara_harness)
    $product_lara_shorts = Product(lara_shorts, 19500, [{"item":item_cloth_piece, "count":8}])
    $ShopWardrobe.addNewProduct(product_lara_shorts)
    
    
    #+0.3.0
    $product_sport_suit_bra = Product(sport_suit_bra, 22500, [{"item":item_leather_piece, "count":2},{"item":item_net, "count":2}])
    $ShopWardrobe.addNewProduct(product_sport_suit_bra)
    $product_sport_suit_leggins = Product(sport_suit_leggins, 24300, [{"item":item_leather_piece, "count":2},{"item":item_red_ink, "count":2},{"item":item_white_ink, "count":2}])
    $ShopWardrobe.addNewProduct(product_sport_suit_leggins)
    $product_sport_suit_pantys = Product(sport_suit_pantys, 30000, [{"item":item_leather_piece, "count":2}])
    $ShopWardrobe.addNewProduct(product_sport_suit_pantys)
    $product_sport_suit_pantys_futa = Product(sport_suit_pantys_futa, 30000, [{"item":item_leather_piece, "count":2}])
    $ShopWardrobe.addNewProduct(product_sport_suit_pantys_futa)
    #-0.3.0
    
    #+0.3.3
    # $product_re_sheva_alowar_arms = Product(re_sheva_alowar_arms, 15800, [])
    $ShopWardrobe.addNewProduct(Product(re_sheva_alowar_arms, 15800, []))
    $ShopWardrobe.addNewProduct(Product(re_sheva_alowar_belt, 11200, []))#  
    $ShopWardrobe.addNewProduct(Product(re_sheva_alowar_boots, 19200, []))# = Clothing("Sheva Alowar's boots", "re_sheva_alowar_boots", ("foot",),["female","futa"],relict_stamina1, 11, 11, 6)
    $ShopWardrobe.addNewProduct(Product(re_sheva_alowar_neck, 31600, []))# = Clothing("Sheva Alowar's neck", "re_sheva_alowar_neck", ("neck",),["female","futa"],relict_stamina1, 21, 21, 6)
    $ShopWardrobe.addNewProduct(Product(re_sheva_alowar_shirt_top, 31050, []))# = Clothing("Sheva Alowar's top", "re_sheva_alowar_shirt_top", ("chest","bra"),["female","futa"],relict_addrestorehp25, 12, 5, 6)
    $ShopWardrobe.addNewProduct(Product(re_sheva_alowar_pants, 85000, []))# = Clothing("Sheva Alowar's pants", "re_sheva_alowar_pants", ("hips", "panties"),["female"],relict_escape100, 35, 35, 6)
    $ShopWardrobe.addNewProduct(Product(re_sheva_alowar_pants_futa, 85000, []))# = Clothing("Sheva Alowar's pants", "re_sheva_alowar_pants_futa", ("hips", "panties","penis"),["futa"],relict_escape100, 35, 35, 6)

    $ShopWardrobe.addNewProduct(Product(sylvana_cloth_boots, 35000, []))# = Clothing("Sylvana's boots", "sylvana_cloth_boots", ("foot",),["female","futa"],relict_addgathering1, 14, 11, 6)
    $ShopWardrobe.addNewProduct(Product(sylvana_cloth_cloak, 44000, []))# = Clothing("Sylvana's cloak", "sylvana_cloth_cloak", ("head","neck"),["female","futa"],relict_thdblock75, 11, 19, 6)
    $ShopWardrobe.addNewProduct(Product(sylvana_cloth_cloak_futa, 44000, []))
    $ShopWardrobe.addNewProduct(Product(sylvana_cloth_legs, 40000, []))# = Clothing("Sylvana's legs", "sylvana_cloth_legs", ("legs"),["female"],relict_protectfromdefencepoison, 41, 21, 6)
    $ShopWardrobe.addNewProduct(Product(sylvana_cloth_legs_futa, 40000, []))# = Clothing("Sylvana's legs", "sylvana_cloth_legs_futa", ("legs","penis"),["futa"],relict_protectfromdefencepoison, 31, 16, 6)
    $ShopWardrobe.addNewProduct(Product(sylvana_cloth_shirt, 95000, []))# = Clothing("Sylvana's shirt", "sylvana_cloth_shirt", ("arms","chest","belt","bra"),["female","futa"],relict_maxhp75, 11, 19, 6)
    $ShopWardrobe.addNewProduct(Product(sylvana_cloth_panty, 37000, []))# = Clothing("Sylvana's panties", "sylvana_cloth_panty", ("panties"),["female"],relict_dom_strenght3, 38, 26, 6)
    $ShopWardrobe.addNewProduct(Product(sylvana_cloth_panty_futa, 37000, []))# = Clothing("Sylvana's panties", "sylvana_cloth_panty", ("panties","penis"),["futa"],relict_dom_strenght3, 38, 26, 6)
    
    
    $ShopWardrobe.addNewProduct(Product(light_weight_panties, 33000, [{"item":item_cloth_piece, "count":1}])) 
    $ShopWardrobe.addNewProduct(Product(light_weight_panties_futa, 33000, [{"item":item_cloth_piece, "count":1}])) 
    $ShopWardrobe.addNewProduct(Product(sexy_skinz_panties, 46000, [{"item":item_cloth_piece, "count":1}])) 
    $ShopWardrobe.addNewProduct(Product(sexy_skinz_panties_futa, 46000, [{"item":item_cloth_piece, "count":1}])) 
    #-0.3.3
    
    #+0.3.5
    $ShopWardrobe.addNewProduct(Product(widow_ribbon, 100000, [{"item":item_rare_cloth, "count":1},{"item":item_white_ink, "count":1}])) 
    $ShopWardrobe.addNewProduct(Product(widow_ribbon_futa, 100000, [{"item":item_rare_cloth, "count":1},{"item":item_white_ink, "count":1}])) 
    $ShopWardrobe.addNewProduct(Product(widow_ribbon_male, 100000, [{"item":item_rare_cloth, "count":1},{"item":item_white_ink, "count":1}])) 
    #-0.3.5
    
    #+0.3.6
    $ShopWardrobe.addNewProduct(Product(buttplug_horn_female, 10000, [{"item":item_satyr_horn, "count":1}])) 
    $ShopWardrobe.addNewProduct(Product(buttplug_horn_futa, 10000, [{"item":item_satyr_horn, "count":1}])) 
    $ShopWardrobe.addNewProduct(Product(buttplug_horn_male, 10000, [{"item":item_satyr_horn, "count":1}])) 
    #-0.3.6
    
    #+0.3.8
    $ShopWardrobe.addNewProduct(Product(presents_suit, 10000, [{"item":item_red_ink, "count":1}])) 
    $ShopWardrobe.addNewProduct(Product(presents_suit_futa, 10000, [{"item":item_red_ink, "count":1}])) 
    $ShopWardrobe.addNewProduct(Product(presents_suit_male, 10000, [{"item":item_red_ink, "count":1}])) 
    #-0.3.8
    
    #+0.4.0
    $ShopWardrobe.addNewProduct(Product(latex_skin, 200000, [{"item":item_latex_piece, "count":7}]))
    $ShopWardrobe.addNewProduct(Product(latex_skin_futa, 200000, [{"item":item_latex_piece, "count":7}]))
    #-0.4.0

    #Items
    #+0.0.4
    $product_item_herb = ProductItem(item_herb, 20)
    $product_item_potion = ProductItem(item_potion, 66)
    $product_item_oil = ProductItem(item_oil, 100)
    $product_item_book = ProductItem(item_book, 70)
    
    
    $ShopHerbalPotion.addNewProduct(product_item_herb)
    $ShopHerbalPotion.addNewProduct(product_item_potion)
    $ShopHerbalPotion.addNewProduct(product_item_oil)
    $ShopHerbalPotion.addNewProduct(product_item_book)
    
    $product_item_water = ProductItem(item_water, 5)
    $ShopHerbalPotion.addNewProduct(product_item_water)
    #-0.0.4
    
    #+0.0.5
    $product_item_lustherb = ProductItem(item_lustherb, 1, False)
    $product_item_ivy = ProductItem(item_ivy, 12, False)
    $product_item_supply_potion = ProductItem(item_supply_potion, 1, False)
    $product_item_megapotion = ProductItem(item_megapotion, 300, False)
    $product_item_smallstick = ProductItem(item_smallstick, 2, False)
    $product_item_cloth_piece = ProductItem(item_cloth_piece, 130, False)
    $product_item_leather_piece = ProductItem(item_leather_piece, 320, False)
    $product_item_latex_piece = ProductItem(item_latex_piece, 670, False)

    $product_item_bone = ProductItem(item_bone, 5, False)
    $product_item_stone = ProductItem(item_stone, 1, False)
    $product_item_blue_mushroom = ProductItem(item_blue_mushroom, 40)
    $product_item_powershroom = ProductItem(item_powershroom, 300, False)
    $product_item_exciteshroom = ProductItem(item_exciteshroom, 400, False)
    $product_item_honey = ProductItem(item_honey, 80, False)
    $product_item_hairs = ProductItem(item_hairs, 110, False)
    $product_item_red_flower = ProductItem(item_red_flower , 5, False)
    $product_item_blue_flower = ProductItem(item_blue_flower, 5, False)
    $product_item_yellow_flower = ProductItem(item_yellow_flower, 5, False)
    
    $product_item_mucus = ProductItem(item_mucus, 250, False)
    $product_item_worm = ProductItem(item_worm, 10, False)
    $product_item_net = ProductItem(item_net, 440, False)
    $product_item_pollen = ProductItem(item_pollen, 210, False)

    $product_item_return_pass = ProductItem(item_return_pass, 1, False)

    $product_item_satyr_horn = ProductItem(item_satyr_horn, 250, False)
    $product_item_satyr_fur = ProductItem(item_satyr_fur, 180, False)
    $product_item_satyr_cum = ProductItem(item_satyr_cum, 150, False)
    $product_item_flydick_cum = ProductItem(item_flydick_cum, 170, False)
    
    $product_item_testosterone = ProductItem(item_testosterone, 200, False)
    
    $ShopHerbalPotion.addNewProduct(product_item_lustherb)
    $ShopHerbalPotion.addNewProduct(product_item_ivy)
    $ShopHerbalPotion.addNewProduct(product_item_supply_potion)
    $ShopHerbalPotion.addNewProduct(product_item_megapotion)
    $ShopHerbalPotion.addNewProduct(product_item_smallstick)
    $ShopHerbalPotion.addNewProduct(product_item_cloth_piece)
    $ShopHerbalPotion.addNewProduct(product_item_leather_piece)
    $ShopHerbalPotion.addNewProduct(product_item_latex_piece)
    
    $ShopHerbalPotion.addNewProduct(product_item_bone)
    $ShopHerbalPotion.addNewProduct(product_item_stone)
    $ShopHerbalPotion.addNewProduct(product_item_blue_mushroom)
    $ShopHerbalPotion.addNewProduct(product_item_powershroom)
    $ShopHerbalPotion.addNewProduct(product_item_exciteshroom)
    $ShopHerbalPotion.addNewProduct(product_item_honey)
    $ShopHerbalPotion.addNewProduct(product_item_hairs)
    $ShopHerbalPotion.addNewProduct(product_item_red_flower)
    $ShopHerbalPotion.addNewProduct(product_item_blue_flower)
    $ShopHerbalPotion.addNewProduct(product_item_yellow_flower)
    
    $ShopHerbalPotion.addNewProduct(product_item_mucus)
    $ShopHerbalPotion.addNewProduct(product_item_worm)
    $ShopHerbalPotion.addNewProduct(product_item_net)
    $ShopHerbalPotion.addNewProduct(product_item_pollen)
    $ShopHerbalPotion.addNewProduct(product_item_return_pass)
    $ShopHerbalPotion.addNewProduct(product_item_satyr_horn)
    $ShopHerbalPotion.addNewProduct(product_item_satyr_fur)
    $ShopHerbalPotion.addNewProduct(product_item_satyr_cum)
    $ShopHerbalPotion.addNewProduct(product_item_flydick_cum)
    $ShopHerbalPotion.addNewProduct(product_item_testosterone)
    #-0.0.5
    
    #+0.0.6
    $product_item_pumpkin = ProductItem(item_pumpkin, 200)
    $ShopHerbalPotion.addNewProduct(product_item_pumpkin)
    
    $product_item_red_ink = ProductItem(item_red_ink, 120, False)
    $product_item_white_ink = ProductItem(item_white_ink, 120)
    $product_item_pink_ink = ProductItem(item_pink_ink, 120, False)
    
    $ShopHerbalPotion.addNewProduct(product_item_red_ink)
    $ShopHerbalPotion.addNewProduct(product_item_white_ink)
    $ShopHerbalPotion.addNewProduct(product_item_pink_ink)
    
    
    $product_item_trap_tool = ProductItem(item_trap_tool, 500, True)
    $ShopHerbalPotion.addNewProduct(product_item_trap_tool)
    #-0.0.6
    
    #+0.3.8
    $ShopHerbalPotion.addNewProduct(ProductItem(item_recipes_scroll_001, 50))
    $ShopHerbalPotion.addNewProduct(ProductItem(item_recipes_scroll_002, 100))
    $ShopHerbalPotion.addNewProduct(ProductItem(item_recipes_scroll_003, 200))
    $ShopHerbalPotion.addNewProduct(ProductItem(item_recipes_scroll_004, 500))
    $ShopHerbalPotion.addNewProduct(ProductItem(item_recipes_scroll_005, 1000))
    $ShopHerbalPotion.addNewProduct(ProductItem(item_recipes_scroll_006, 1000))
    $ShopHerbalPotion.addNewProduct(ProductItem(item_recipes_scroll_007, 1000))
    $ShopHerbalPotion.addNewProduct(ProductItem(item_recipes_scroll_009, 5000))
    $ShopHerbalPotion.addNewProduct(ProductItem(item_recipes_scroll_010, 10000))
    $ShopHerbalPotion.addNewProduct(ProductItem(item_recipes_scroll_011, 25000))
    $ShopHerbalPotion.addNewProduct(ProductItem(item_recipes_scroll_013, 100000))
    $ShopHerbalPotion.addNewProduct(ProductItem(item_recipes_scroll_014, 5000))
    $ShopHerbalPotion.addNewProduct(ProductItem(item_recipes_scroll_015, 10000))
    $ShopHerbalPotion.addNewProduct(ProductItem(item_recipes_scroll_016, 10000))
    #-0.3.8
    
    
    
    #+0.1.0
    $snow_hat = Clothing("Snow hat", "snow_hat", ("head", ),["female","futa"],relict_blowjob_sub_strenght5, 15, 10, 3)  #0.1.4
    $snow_boots = Clothing("Snow boots", "snow_boots", ("foot", ),["female","futa"],relict_ftblock10, 15, 10, 3)  #0.1.4
    $snow_dress = Clothing("Snow dress", "snow_dress", ("chest", "bra", "hips"),["female","futa"],relict_maxhp20, 15, 10, 3)  #0.1.4
    
    $santa_hat_male = Clothing("Santa's hat", "santa_hat_male", ("head", ),["male"],relict_blowjob_sub_strenght5, 15, 10, 3)  #0.3.8
    $santa_boots_male = Clothing("Santa's boots", "santa_boots_male", ("foot", ),["male"],relict_ftblock10, 15, 10, 3)  #0.3.8
    $santa_coat_male = Clothing("Santa's coat", "santa_coat_male", ("chest", "bra", "belt","neck","arm"),["male"],relict_maxhp20, 15, 10, 3)  #0.3.8
    $santa_pants_male = Clothing("Santa's pants", "santa_pants_male", ("legs", "hips","penis"),["male"],relict_stamina1, 15, 10, 3)  #0.3.8
    #-0.1.0
    
    
    #+0.3.9
     
    $ShopCustomizeBody.addNewProduct(ProductBody(hair_cady, 0)) 
    $ShopCustomizeBody.addNewProduct(ProductBody(hair_gili, 0))
    $ShopCustomizeBody.addNewProduct(ProductBody(hair_bald_head, 0))
    $ShopCustomizeBody.addNewProduct(ProductBody(hair_turbblonde, 10))
    $ShopCustomizeBody.addNewProduct(ProductBody(hair_turbopink, 0))
    $ShopCustomizeBody.addNewProduct(ProductBody(hair_calista, 0))
    $ShopCustomizeBody.addNewProduct(ProductBody(hair_carla, 0))
    $ShopCustomizeBody.addNewProduct(ProductBody(hair_pina, 0))
    $ShopCustomizeBody.addNewProduct(ProductBody(hair_katarina, 10))
    $ShopCustomizeBody.addNewProduct(ProductBody(hair_redhead, 100))
    $ShopCustomizeBody.addNewProduct(ProductBody(hair_tifa, 50))
    $ShopCustomizeBody.addNewProduct(ProductBody(hair_lara, 50))
    $ShopCustomizeBody.addNewProduct(ProductBody(hair_roxana, 20))#0.3.9
    
    $ShopCustomizeBody.addNewProduct(ProductBody(beard_bald_head, 0))
    $ShopCustomizeBody.addNewProduct(ProductBody(male_beard1, 0))
    $ShopCustomizeBody.addNewProduct(ProductBody(wizard_beard_male, 0))
    $ShopCustomizeBody.addNewProduct(ProductBody(armani_hair_male, 10))
    
    $ShopCustomizeBody.addNewProduct(ProductBody(herodius_hair_male, 10))
    $ShopCustomizeBody.addNewProduct(ProductBody(herodius_beard_male, 10))
    $ShopCustomizeBody.addNewProduct(ProductBody(spiki_hair_male, 10))
    #-0.3.9
    
    #+0.4.0
    $ShopCustomizeBody.addNewProduct(ProductBody(body_hair_shaved, 0))
    $ShopCustomizeBody.addNewProduct(ProductBody(body_hair0, 0))
    $ShopCustomizeBody.addNewProduct(ProductBody(body_hair1, 0)) 
    $ShopCustomizeBody.addNewProduct(ProductBody(body_hair2, 0)) 
    $ShopCustomizeBody.addNewProduct(ProductBody(body_hair_shaved_male, 0)) 
    $ShopCustomizeBody.addNewProduct(ProductBody(body_hair0_male, 0)) 
    $ShopCustomizeBody.addNewProduct(ProductBody(body_hair_shaved_futa, 0))
    $ShopCustomizeBody.addNewProduct(ProductBody(body_hair0_futa, 0)) 
    $ShopCustomizeBody.addNewProduct(ProductBody(body_hair1_futa, 0)) 
    $ShopCustomizeBody.addNewProduct(ProductBody(body_hair2_futa, 0)) 
    #-0.4.0
    
    #Shop clothing-----------------
    
    $map_visible = False
    
    $battle_visible = False
    
    $pathfound = None
    $endobject = None
    #hero
    # $hero_pos = (19,5)
    # $end_pos = (0,0)
    $movement = 0
    $movement_end = 0
    $movementIsOver = False
    # jump gen_loc
    
    $battle_timer = 30
    $who_turn = None
    
    $current_event = None
    
    jump story_in_home

screen plot_wait():
    zorder 999
    tag plot_wait_tag
    frame:
        xminimum 1920
        xmaximum 1920
        yminimum 1080
        ymaximum 1080
        background "#00000000"
        imagebutton idle "alpha_bg" action NullAction()#Function(renpy.notify, ["wait..."])
        # text "wait..." color "#fff" outlines [ (2, "#000000") ] size 16 xalign 0.0 yalign 1.0
        

image satyr_dickfallen_anim:
    "images/Story/satyr_dickfallen/fallen00.png"
    0.04
    "images/Story/satyr_dickfallen/fallen01.png"
    0.04
    "images/Story/satyr_dickfallen/fallen02.png"
    0.04
    "images/Story/satyr_dickfallen/fallen03.png"
    0.04
    "images/Story/satyr_dickfallen/fallen04.png"
    0.04
    "images/Story/satyr_dickfallen/fallen05.png"
    0.04
    "images/Story/satyr_dickfallen/fallen06.png"
    0.04
    "images/Story/satyr_dickfallen/fallen07.png"
    0.04
    "images/Story/satyr_dickfallen/fallen08.png"
    0.04
    "images/Story/satyr_dickfallen/fallen09.png"
    0.04
    "images/Story/satyr_dickfallen/fallen10.png"
    0.04
    "images/Story/satyr_dickfallen/fallen11.png"
    0.04
    "images/Story/satyr_dickfallen/fallen12.png"
    0.04
    "images/Story/satyr_dickfallen/fallen13.png"
    0.04
    "images/Story/satyr_dickfallen/fallen14.png"
    0.04
    "images/Story/satyr_dickfallen/fallen15.png"
    0.04
label init_plot:  
    $renpy.block_rollback()
    $ee = GafferChoo.name
    $gg = "???"  
    # show screen plot_wait
    scene blackscreen
    with Pause(1.5)
    # $renpy.hide_screen("plot_wait_tag")
    stop music
    if renpy.music.is_playing(channel="music_all") == False or renpy.music.get_playing(channel="music_all") != "/sound/story_intro.mp3":
        $renpy.music.play("/sound/story_intro.mp3", channel="music_all")
    # scene intro_forest_masturbated with fade_half_long
    scene lustforest0 with fade 
    with Pause(1.0)
    "The world was full of harmony."
    "Lust was everywhere..."
    scene lustforest0
    show screen plot_wait
    show lustforest:
        xalign 0.0
        ease 15.0 xalign 1.0
    with Pause(15)
    $renpy.hide_screen("plot_wait_tag")
    "But then they came and everything changed ..."
    
    scene lustforest1
    if renpy.music.is_playing(channel="music_all") == False or renpy.music.get_playing(channel="music_all") != "/sound/battle2.mp3":
        $renpy.music.play("/sound/battle2.mp3", channel="music_all")
    $renpy.sound.play("/sound/story_appear.mp3")
    show darkblue:
        alpha 0.0
        easeout 1 alpha 0.7
    with Pause(2)
    scene lustforest1
    $renpy.sound.play("/sound/story_appear.mp3")
    show darkblue:
        alpha 0.7
        easein 1 alpha 1.0    
    show whitebg:
        alpha 0.0
        easein 0.5 alpha 1.0 
        linear 0.5 alpha 1.0 
    scene lustforest1
    show witche1
    show darkblue:
        alpha 0.0
        easeout 1 alpha 0.7
    show whitebg:
        alpha 1.0
        easein 0.5 alpha 0.0
    with Pause(1)
    scene lustforest1
    show darkblue:
        alpha 0.7
        easein 1 alpha 1.0  
    show witche1
    show whitebg:
        alpha 0.0
        easein 0.5 alpha 1.0 
        linear 0.5 alpha 1.0 
    scene lustforest1
    show darkblue:
        alpha 0.0
        easeout 1 alpha 0.7
    show witche1
    show witche2
    show whitebg:
        alpha 1.0
        easein 0.5 alpha 0.0
    with Pause(1)
    "It is unknown where the two witches came from"
    "They took all the lust for themselves..."
    scene bg_anim_satyr with fade
    with Pause(1)
    show satyr_lust:
        xoffset 0.0
        yoffset 0.0
        alpha 0
        easein 0.5 alpha 0.5
        linear 2.0 alpha 0.5 xoffset 500
        linear 0.5 alpha 0.0 xoffset 625
    with Pause(4)    
    scene bg_anim    
    show satyr_dickfallen_anim
    with Pause(3)
    scene blackscreen with fade
    scene bg_anim_orc with fade
    with Pause(1)
    show orc_lust:
        xoffset 0.0
        yoffset 0.0
        linear 2.0 alpha 0.5 xoffset -500 
        linear 0.5 alpha 0.0 xoffset -625
    with Pause(3)    
    
    scene bg_anim_witches with fade
    show witche2_lust:
        xoffset 500
        yoffset -50
        alpha 0
        easein 0.5 alpha 0.5
        linear 2.0 alpha 0.5 xoffset 0 yoffset 0
        linear 0.5 alpha 0.0 
    show witche1_lust:
        xoffset -500
        yoffset -50
        alpha 0
        easein 0.5 alpha 0.5
        linear 2.0 alpha 0.5 xoffset 0 yoffset 0
        linear 0.5 alpha 0.0 
    with Pause(4)
    show whitebg:
        alpha 0.0
        easein 0.5 alpha 1.0 
        linear 0.5 alpha 1.0 
    scene lustforest1
    scene bg_anim
    show whitebg:
        alpha 1.0
        easein 0.5 alpha 0.0
    with Pause(3)
    "All lust has been stolen"    
    "Because lust is gone, sex is gone"
    "And only the chosen one can find and bring all the lust back" 
    "And it's you ..."
    scene blackscreen with fade
    scene logo with dissolve
    show lusthunter:
        alpha 0.0
        easein 0.5 alpha 1.0 
    with Pause(5)
    
    jump create_new_char
    
    
label story_in_home:
    $renpy.block_rollback()
    if Player.gender == "female":
        scene intro_home with fade_half_long
    elif Player.gender == "futa":
        scene intro_home_futa with fade_half_long
    elif Player.gender == "male":
        scene intro_home_male with fade_half_long
    $renpy.hide_screen("plot_wait_tag")
    $renpy.music.play("/sound/story_snoring.mp3", channel="music_all")
    g "*Zzzz*"
    e "Hmmm..."

    scene medieval_home with fade_half_long
    # $renpy.show_screen("player_for_dialoge", char_appear_left_to_right, 1, 0.85)
    $renpy.hide_screen("plot_wait_tag")
    show screen thegaffer_for_dialoge
    with Pause(0.5)
    $renpy.music.stop(channel="music_all")
    if Player.gender == "futa":
        if Player.clothing["penis"].icon_name == "futa_mid":
            show intro_cover_body_futa_mid:
                xzoom 0.85
                yzoom 0.85
                xoffset -250
                yoffset 230
            with shake
        if Player.clothing["penis"].icon_name == "futa_small":
            show intro_cover_body_futa_small:
                xzoom 0.85
                yzoom 0.85
                xoffset -250
                yoffset 230
            with shake
    if Player.gender == "female":
        show intro_cover_body:
            xzoom 0.85
            yzoom 0.85
            xoffset -250
            yoffset 230
        with shake
    if Player.gender == "male":
        show intro_cover_body_male:
            xzoom 0.95
            yzoom 0.95
            xoffset -250
            yoffset 100
        with shake
    
    $renpy.music.play("/sound/homeplace.mp3", channel="music_all")
    $renpy.sound.play("/sound/ooh.mp3")
    e "Ohhh!"
    e "Did you wake up?"
    if Player.gender == "futa":
        if Player.clothing["penis"].icon_name == "futa_mid":
            hide intro_cover_body_futa_mid
            show intro_cover_body2_futa_mid:
                xzoom 0.85
                yzoom 0.85
                xoffset -250
                yoffset 230
            with shake
        if Player.clothing["penis"].icon_name == "futa_small":
            hide intro_cover_body_futa_small
            show intro_cover_body2_futa_small:
                xzoom 0.85
                yzoom 0.85
                xoffset -250
                yoffset 230
            with shake
    elif Player.gender == "female":
        hide intro_cover_body
        show intro_cover_body2:
            xzoom 0.85
            yzoom 0.85
            xoffset -250
            yoffset 230
    if Player.gender == "male":
        hide intro_cover_body_male
        show intro_cover_body_male2:
            xzoom 0.95
            yzoom 0.95
            xoffset -250
            yoffset 100
    e "Fine...Fine..."
    e "What's your name?"
    
    $ gg = renpy.input("Enter your name", default=persistent.uname, allow=None, exclude='{}()!@#$%*:|~`;^&?-=+"\'.,\/\\<>', length=20)
    $ gg = gg.strip()
    if not gg:
        $ gg = "Lust Madness" 
    else:
        $Player.name = gg
    g "My name is [gg]"
    e "Hi [gg]"
    e "My name is [ee]"
    e "I found you by the river"
    e "You were completely naked so I was able to examine you well, he-he"
    e "Do you have a place to go?"
    g "..."
    e "Ok then i will help you"
    e "But you have to work for me"
    e "I canâ€™t let you go naked and defenseless on a quest, so keep these panties"
    if Player.gender == "female":
        call screen quest_reward_cloth_screen([panty_din], True)
        if _return == "addclothes":
            $Player.AddWardrobeInventory(panty_din)
    elif Player.gender == "futa":
        call screen quest_reward_cloth_screen([panty_din_futa], True)
        if _return == "addclothes":
            $Player.AddWardrobeInventory(panty_din_futa)
    elif Player.gender == "male":
        if Player.type == "male_muscular":
            call screen quest_reward_cloth_screen([panty_din_male_muscular], True)
            if _return == "addclothes":
                $Player.AddWardrobeInventory(panty_din_male_muscular)
    # $renpy.notify(["*Panties added to your wardrobe*"])
    # "*You got panties*"
    e "I put them in your wardrobe, be sure to put them on"
    menu:
        e "Are you a virgin?"
        "Yes":
            g "Yes"
            e "Okey. I will give you 300 coins."
            $Player.addCoins(300)
            $Player.virgin = True
            # $renpy.notify(["*You got +300 coins*"])
            # "*You got +300 coins*"
        "No":
            g "No"
            e "Okey. I will give you 100 coins"
            $Player.addCoins(100)
            $Player.virgin = False
            # $renpy.notify(["*You got +100 coins*"])
            # "*You got +100 coins*"
    $Player.addPoints(5)
    e "You can buy clothes or some items on this coin. You will find them in the Shop & Craft place."
    e "When you gather your strength, you can find me in the Tavern"
    e "Good luck"
    
        
    # hide screen player_for_dialoge
    hide screen thegaffer_for_dialoge
    with Pause(0.5)
    hide intro_cover_body2 with dissolve
    scene blackscreen with fade
    
    #################################################
    $enemy_test_desc = EnemyDesc("Test","test", "test", "test", "idle", "male", 30, [], {"first":"TEEEST!"}, None, None, [], True, 0.6)
    $item_test_cons = Consumable("Test cons", im.Scale("/Items/herb.png",64,64), None, "test",20)
    $item_test_uncons = Unconsumable("Test uncons", im.Scale("/Items/water.png",64,64),"test",99)
    $relict_test = Relict("Test","Test", "ui_relict_escape", "passive", "Test", Modifiers("Test", None, "test", "Test {color=#fff}{size=22}15%{/size}{/color}", 15, 0, 0))
    $test_clothing = Clothing("Test", "schl_boot", ("foot",),["female", "futa", "male"],relict_test, 2, 3, 1)
    
    $card_test = CardType("Test card", "lust_attack", "card_test_card", "Deal {color=#fff}{size=22}%s{/size}{/color} damage", 1, 5, 0, 1, 1, None, {"cost":1, "st":1, "repeat":1, "amount":8, "amount_block":0, "modifier":None, "desc":None, "features":[]})
    #################################################
    
    
    jump world_map_label_house


screen popup_info(_name, _timer = 180):
    zorder 520
    $_pos = renpy.get_mouse_pos()
    frame at show_popup_info(_pos):
        background Frame("gui/ui/ui_rockbutton.png")
        xmaximum 300
        xminimum 300
        text _name size 24 color "#fff" xalign 0.5
    timer _timer action Hide("popup_info")

screen sex_popup_info(_name, _text, _timer = 180):
    zorder 520
    $_pos = renpy.get_mouse_pos()
    frame at show_popup_info(_pos, -230):
        background Frame("gui/ui/ui_rockbutton.png")
        xmaximum 350
        # xminimum 300
        vbox:
            text _name size 30 color "#ffda10" xalign 0.5
            text _text size 24 color "#fff" xalign 0.5
    timer _timer action Hide("sex_popup_info")

screen name_popup_info(_name, _enemylist, _timer = 3):
    zorder 520
    $_pos = renpy.get_mouse_pos()

    frame at show_popup_info(_pos):
        background Frame("gui/ui/ui_rockbutton.png")
        xmaximum 300
        ymaximum 100
        vbox:
            hbox:
                for e in _enemylist:
                    text "%s"%(e.name) size 24 color "#fff" xalign 0.5
                    frame:
                        xminimum 24
                        xmaximum 24
                        yminimum 24
                        ymaximum 24
                        if e.gender == "male":
                            background Frame("ui_male")
                        elif e.gender == "female":
                            background Frame("ui_female")
                        elif e.gender == "futa":
                            background Frame("ui_futa")
            # text "%s"%(_name) size 24 color "#fff" xalign 0.5
            hbox:
                for e in _enemylist:
                    frame:
                        xminimum 64
                        xmaximum 64
                        yminimum 64
                        ymaximum 64
                        background Frame(e.icon)   
    timer _timer action Hide("name_popup_info")

screen npc_popup_info(_npc, _timer = 10):
    zorder 520
    $_pos = renpy.get_mouse_pos()

    frame at show_popup_info(_pos):
        background Frame("gui/ui/ui_npc_dialog_quest.png")
        xmaximum 400
        ymaximum 160
        hbox:
            frame:
                xminimum 128
                xmaximum 128
                yminimum 128
                ymaximum 128
                background Frame("/NPC/%s/%s_icon.png"%(_npc.name, _npc.name))   
            text "Hey! My name is %s"%(_npc.name) size 24 color "#fff" xalign 0.0 yalign 0.2
    timer _timer action Hide("npc_popup_info")

screen cond_door_popup_info(_cond, _timer = 5):
    zorder 520
    $_pos = renpy.get_mouse_pos()

    frame at show_popup_info(_pos):
        background Frame("gui/ui/ui_rockbutton.png")
        xmaximum 300
        ymaximum 600
        if _cond["type"] == "sex_unlocked":
            vbox:
                text "Need sex with enemy to unlock" size 24 color "#fff" xalign 0.5
                vbox:
                    for e in _cond["cond"]:
                        hbox:
                            for en in e["enemy"]:
                                frame:
                                    xminimum 64
                                    xmaximum 64
                                    yminimum 64
                                    ymaximum 64
                                    background Frame(en.icon)   
                            if getEnemyDescSexCount(e["enemy"]) >= e["count"]:
                                text "%s of %s"%(min(getEnemyDescSexCount(e["enemy"]),e["count"]), e["count"]) size 24 color "#1eb023" yalign 0.5 xalign 0.5 xoffset 30
                            else:
                                text "%s of %s"%(getEnemyDescSexCount(e["enemy"]), e["count"]) size 24 color "#fff" yalign 0.5 xalign 0.5 xoffset 30
        elif _cond["type"] == "stepfounder":
            if _cond["cond"] == "orc":
                text "Find an Orc to unlock" size 24 color "#fff" xalign 0.5
        elif _cond["type"] == "need_key_for_cave_BL03D1":
            if Player.hr == 1:
                text "%s"%_cond["cond"] size 24 color "#fff" xalign 0.5
            elif Player.hr >= 2:
                vbox:
                    text "You need a special key" size 24 color "#fff" xalign 0.5
                    frame:
                        xalign 0.5
                        xminimum 64
                        xmaximum 64
                        yminimum 64
                        ymaximum 64
                        background Frame(item_cave_key.icon)   
                    text "%s of %s"%(Player.getCountItems(item_cave_key), 1) size 24 color "#fff" yalign 0.5 xalign 0.5 #xoffset 30
        else:
            # if _cond["type"] == "need_key_for_door_JJ00D5":
            text "%s"%_cond["cond"] size 24 color "#fff" xalign 0.5
            #item_cave_key
            # text "%s"%_cond["cond"] size 24 color "#fff" xalign 0.5
# [{"enemy":[enemy_muscular_desc_f], "count":1},{"enemy":[enemy_satyr_desc_m], "count":5},{"enemy":[enemy_nymph_desc_f], "count":3},{"enemy":[enemy_forest_fairy_desc_f], "count":3}]                            
    timer _timer action Hide("popup_info")

       
screen thegaffer_for_dialoge:      
    frame at char_appear_right_to_left_show:
        background "#00000000"
        yoffset 200
        image "quest_giver_say_img" xzoom 1 yzoom 1
screen nunchurch_for_dialoge:      
    frame at char_appear_right_to_left_show:
        background "#00000000"
        yoffset 200
        image "nunchurch_say_img" xzoom 1 yzoom 1
    
init python:
    if renpy.variant("small" ):
        config.overlay_screens.append( "android_overlay" )
    config.has_autosave = False
    config.has_quicksave = False
    config.autosave_on_quit = False
    config.autosave_on_choice = False
    
    import urllib
    import urllib2
    import time
    import ast
    import json
    import ssl
    
    def GenRandomAuthCode():
        password = str(int(time.time()))
        for c in range(30):
            password += renpy.random.choice(chars)
        return password
    
    def IsDevVersion():
        _ret = False
        if cur_version.find("dev") > 0:
            _ret = True
        return _ret
        
    def RefreshPatronInfo():
        persistent.uname = "Hunter Name"
        persistent.pledgecent = 1000000
        persistent.tier = "Hunter 3"
        persistent.follower = True
        persistent.patron_status = "active_patron"
        persistent.pledge_cadence = 1000000
        _error = ""
    
    def ReAuthPatreonLogin():
        if persistent.auth_code == "":
            persistent.auth_code = GenRandomAuthCode()
        renpy.run(OpenURL("%s/loginrenpy?gencode=%s"%(persistent.server, persistent.auth_code)))
            # scene allow_patreon
            # menu:
            # "Click allow in your web browser and then select this option":
            
    def PatreonLogOut():
        try:
            userList = json.loads(urllib2.urlopen(urllib2.Request(url='%s/logoutpatreon?gencode=%s'%(persistent.server, persistent.auth_code)), context = ssl._create_unverified_context()).read())
            ret_status = userList["result"] 
        except:
            ret_status = "Failed"
        persistent.uname = ""
        persistent.pledgecent = 0 
        persistent.uimg = ""
        persistent.tier = ""
        persistent.follower = False
        persistent.patron_status = ""
        persistent.pledge_cadence = 0#all time
        persistent.auth_code = ""
        
    def IsLoggedInPatreon():
        _ret = True
        return _ret
        
    def IsTierHunter1():
        _ret = False
        if IsLoggedInPatreon() and persistent.tier == "Hunter 1":# or (persistent.pledge_cadence >= 500 and persistent.pledge_cadence < 1500):
            _ret = True
        return _ret
        
    def IsTierHunter2():
        _ret = False
        if IsLoggedInPatreon() and persistent.tier == "Hunter 2":
            _ret = True
        return _ret
        
    def IsTierHunter3():
        _ret = False
        if IsLoggedInPatreon() and persistent.tier == "Hunter 3":
            _ret = True
        return _ret
        
    def IsTierHunter4():
        _ret = False
        if IsLoggedInPatreon() and persistent.tier == "Hunter 4":
            _ret = True
        return _ret
    
    def IsTierHunter5():
        _ret = False
        if IsLoggedInPatreon() and persistent.tier == "Hunter 5":
            _ret = True
        return _ret
    
    def IsTierGoldenHunter():
        _ret = False
        if IsLoggedInPatreon() and persistent.tier == "Golden Hunter":
            _ret = True
        return _ret
    
    def IsTierKingOfHunters():
        _ret = False
        if IsLoggedInPatreon() and persistent.tier == "King of Hunters":
            _ret = True
        return _ret
    
    def IsHunter2OrHigher():
        _ret = False
        if IsTierHunter2() or IsTierHunter3() or IsTierHunter4() or IsTierHunter5() or IsTierGoldenHunter() or IsTierKingOfHunters():
            _ret = True
        return _ret
    
    def IsHunter3OrHigher():
        _ret = True
        return _ret
        
    def IsTiers():
        _ret = True
        return _ret
        
    def ReturnTier():
        _ret = "Hunter 3"
        if IsLoggedInPatreon():
            _ret = persistent.tier
        return persistent.tier
    
    def GetAllTiersByNameTier(_name):
        _ret = []
        _retAll = False
        for i in _name:
            if i == "All Hunters":
                _retAll = True
        if _retAll == True:
            _ret = ["Hunter 1","Hunter 2","Hunter 3","Hunter 4","Hunter 5","Golden Hunter","King of Hunters"]
        else:
            _ret = _name
        return _ret
    
    def GetStrokeTiersByList(_tiers):
        _ret = ""
        _counter = len(_tiers)
        if "All Hunters" in _tiers:
            _ret = "{color=#2ecc71}Hunter 1{/color} or higher"
        if "Hunter 1" in _tiers:
            _ret += "{color=#2ecc71}Hunter 1{/color}"
        if "Hunter 2" in _tiers:
            if _counter == 2:
                _ret += " or "
            elif _counter == 3:
                _ret += ", "
            _ret += "{color=#3498c7}Hunter 2{/color}"
        if "Hunter 3" in _tiers:
            if _counter == 2:
                _ret += " or "
            elif _counter == 3:
                _ret += " or "
            _ret += "{color=#e67a2a}Hunter 3{/color}"
        return _ret
    
    def GetColorTier(_tier, _name):
        _ret = _name
        if "Hunter 1" == _tier:
            _ret = "{color=#2ecc71}%s{/color}"%_name
        if "Hunter 2" == _tier:
            _ret = "{color=#3498c7}%s{/color}"%_name
        if "Hunter 3" == _tier:
            _ret = "{color=#e67a2a}%s{/color}"%_name
        if "Hunter Special" == _tier or "Hunter 4" == _tier or "Hunter 5" == _tier or "King of Hunters" == _tier or "Golden Hunter" == _tier:
            _ret = "{color=#ff26f1}%s{/color}"%_name 
        return _ret
    
    def GetQuestsIsNewExists(quest_from):
        _ret = False
        for q in getAllowQuests(quest_from, quest_list, 999):
            if q.is_new == True and q.hr_need <= Player.hr:
                _ret = True
        return _ret
        
    def SetTopPatronsList():
        # python:
        ret_status = ""
        try:
            userList = json.loads(urllib2.urlopen(urllib2.Request(url='%s/getlistdonationtmembers'%persistent.server), context = ssl._create_unverified_context()).read())
            ret_status = userList["result"]
        except:
            ret_status = "Failed"
        # campaigns.members
        
        if ret_status == "Sucsess":
            persistent.top_donators = userList["data"]  
            # ShowMenu("top_donators_list")
            #renpy.show_screen("top_donators_list")
    
    def SetKingPlaceNPCList():
        # python:
        ret_status = ""
        try:
            userList = json.loads(urllib2.urlopen(urllib2.Request(url='%s/getlistkingplace'%persistent.server), context = ssl._create_unverified_context()).read())
            ret_status = userList["result"]
        except:
            ret_status = "Failed"
        # campaigns.members
        
        if ret_status == "Sucsess":
            king_place = userList["data"] 
        else:
            king_place = None
        
        return king_place
    
    def GetTrophy():
        _p = persistent.pledge_cadence
        _ret = None
        if _p >= 90000:
            _ret = "trophy_diamond"
        elif _p >= 45000 and _p < 90000:
            _ret = "trophy_platinum"
        elif _p >= 15000 and _p < 45000:
            _ret = "trophy_golden"
        elif _p >= 7500 and _p < 15000:
            _ret = "trophy_silver"
        elif _p >= 4000 and _p < 7500:
            _ret = "trophy_bronze"
        return _ret 
        
    def CanYouCreateYourNPC():
        _p = persistent.pledge_cadence
        _ret = False
        if _p >= 15000 and IsLoggedInPatreon():
            _ret = True
        else:
            _ret = False
        return _ret 
    
screen auth_patreon_screen():
    add "allow_patreon"
    style_prefix "choice"

    zorder 505
    tag prepare_battle_tag
        
    vbox:   
        xalign 0.5
        yalign 0.5
        textbutton "Click allow in your web browser and then select this option" text_color "#fff" text_hover_color "#000" text_align 0.5  action [Function(RefreshPatronInfo), Hide("auth_patreon_screen"), Return()]#(Function(StartBattle, renpy.random.choice([True, False])))

image ui_become_a_patron_bg:
    "/gui/ui/ui_become_a_patron_bg.png"
image ui_become_a_patron_bg_change_gender:
    "/gui/ui/ui_become_a_patron_bg_change_gender.png"
image ui_become_a_patron_bg_alllocations:
    "/gui/ui/ui_become_a_patron_bg_alllocations.png"
image ui_become_a_patron_bg_unlockcombolist:
    "/gui/ui/ui_become_a_patron_bg_unlockcombolist.png"
image ui_become_a_patron_bg_allsextypes:
    "/gui/ui/ui_become_a_patron_bg_allsextypes.png"
  
screen become_a_patron_screen(typebecomepatrons, _text, _img = None):
    zorder 600
    if typebecomepatrons != "SaveGame":
        use player_ui_bars()
    frame:
        xminimum 1920
        xmaximum 1920
        yminimum 1080
        ymaximum 1080
        # background None
        background _img#Frame("#00000050")
        imagebutton idle "#00000050" action [Return(), With(fade)]
        
        #"ChangeGender" H2 if if IsHunter2OrHigher()
        # or typebecomepatrons == "AllLocations" H3: if IsHunter3OrHigher()
        #"UnlockComboList" H2 if IsHunter2OrHigher()
        #"UnlockAllTypesOfSex" H3 if IsHunter3OrHigher()
        frame:
            xminimum 1920
            xmaximum 1920
            yminimum 1080
            ymaximum 1080
            if typebecomepatrons == "SaveGame" or typebecomepatrons == "Church" or typebecomepatrons == "NavigationMap" or typebecomepatrons == "BuySpecialCloth" or typebecomepatrons == "SpecialChoice":
                background Frame("ui_become_a_patron_bg")
            elif typebecomepatrons == "ChangeGender" or typebecomepatrons == "SpecialMonthChurchClothing":
                background Frame("ui_become_a_patron_bg_change_gender")
            elif typebecomepatrons == "AllLocations":
                background Frame("ui_become_a_patron_bg_alllocations")
            elif typebecomepatrons == "UnlockComboList":
                background Frame("ui_become_a_patron_bg_unlockcombolist")
            elif typebecomepatrons == "UnlockAllTypesOfSex":
                background Frame("ui_become_a_patron_bg_allsextypes")
            hbox:
                xalign 0.5
                yalign 0.5
                yoffset 370
                frame:
                    xalign 0.0
                    yalign 1.0
                    xminimum 400
                    xmaximum 400
                    yminimum 60
                    ymaximum 60
                    # xoffset -150
                    background Frame("ui_become_a_patron3_idle")
                    # imagebutton auto "ui_become_a_patron2_%s" 
                    if typebecomepatrons == "ChangeGender"  or typebecomepatrons == "UnlockComboList":
                        text "UPGRADE TIER" size 34 color "#fff" xalign 0.5 yoffset 7 xoffset 37 #font "/fonts/WalsheimLight.ttf"
                        imagebutton auto "ui_android_becomeapatrons_button_%s" yoffset -6 xoffset 3 action OpenURL("https://www.patreon.com/join/LustMadness/checkout?rid=5741793&cadence=1")
                    elif typebecomepatrons == "AllLocations" or typebecomepatrons == "UnlockAllTypesOfSex" or typebecomepatrons == "SpecialMonthChurchClothing":
                        text "UPGRADE TIER" size 34 color "#fff" xalign 0.5 yoffset 7 xoffset 37 #font "/fonts/WalsheimLight.ttf"
                        imagebutton auto "ui_android_becomeapatrons_button_%s" yoffset -6 xoffset 3 action OpenURL("https://www.patreon.com/join/LustMadness/checkout?rid=6345675&cadence=1")
                    else:
                        text "UNLOCK WITH PATREON" size 34 color "#fff" xalign 0.5 yoffset 7 xoffset 37 #font "/fonts/WalsheimLight.ttf"
                        imagebutton auto "ui_android_becomeapatrons_button_%s" yoffset -6 xoffset 3 action OpenURL("https://www.patreon.com/join/LustMadness")
                if IsLoggedInPatreon() == False:
                    frame:
                        yoffset -5
                        xoffset 200
                        xalign 1.0
                        yalign 1.0
                        xminimum 162
                        xmaximum 162
                        yminimum 60
                        ymaximum 60
                        background Frame("ui_login_a_patron_idle")
                        # imagebutton auto "ui_login_a_patron_%s"
                        text "Log in" size 34 color "#f96753" xalign 0.5 yoffset 7 xoffset 7
                        imagebutton auto "ui_loginpatron_button_%s"  yoffset -6 xoffset -6 action [Hide("become_a_patron_screen"),Show("auth_patreon_screen"),Function(ReAuthPatreonLogin)]
                        text "If you are already a patron" size 20 color "#fff" outlines[ (2, "#212121") ] yoffset 60 xoffset 0 text_align 0.5
        # else:
            # frame:
                # xalign 0.5
                # yalign 0.4
                # xminimum 462
                # xmaximum 462
                # yminimum 150#210
                # ymaximum 150#210
                # background Frame("ui_become_a_patron_alert")
                # if IsTiers():
                    # text "{b}Upgrade tier!{/b}" color "#000" size 30 xalign 0.5 yalign 0.0 font "/fonts/WalsheimLight.ttf"
                # else:
                    # text "{b}Become a patron!{/b}" color "#000" size 30 xalign 0.5 yalign 0.0 font "/fonts/WalsheimLight.ttf"
                # frame:
                    # xalign 0.5
                    # yalign 0.5
                    # xoffset -10
                    # background None
                    # xminimum 430
                    # xmaximum 430
                    # text "%s"%_text color "#000" size 18 xalign 0.5 yalign 0.5 font "/fonts/sansserif.ttf" #Only {color=#f96854}patrons{/color} have access to Patrons Church. Become a {color=#f96854}patron{/color} and get more options!
                # hbox:
                    # yalign 1.0
                    # frame:
                        # yoffset -5
                        # xoffset 15
                        # xalign 0.0
                        # yalign 1.0
                        # xminimum 200
                        # xmaximum 200
                        # yminimum 30
                        # ymaximum 30
                        # background None
                        # imagebutton auto "ui_become_a_patron2_%s" action OpenURL("https://www.patreon.com/join/LustMadness")
                        # text "UNLOCK WITH PATREON" size 18 color "#fff" xalign 0.5 yoffset 7 xoffset 37 #font "/fonts/WalsheimLight.ttf"
                    # if IsLoggedInPatreon() == False:
                        # frame:
                            # yoffset -5
                            # xoffset 100
                            # xalign 1.0
                            # yalign 1.0
                            # xminimum 81
                            # xmaximum 81
                            # yminimum 30
                            # ymaximum 30
                            # background None
                            # imagebutton auto "ui_login_a_patron_%s" action [Hide("become_a_patron_screen"),Show("auth_patreon_screen"),Function(ReAuthPatreonLogin)]
                            # text "Log in" size 18 color "#212121" xalign 0.5 yoffset 5 xoffset 8
            
            # hbox:
                # yoffset 150
                # xalign 0.5
                # text "Are you already a patron?" color "#f96854" size 14
                # textbutton "{u}Refresh data{/u}" text_color "#f96854" text_hover_color "#fff" text_size 14 action [Hide("become_a_patron_screen"), Function(RefreshPatronInfo)] yoffset -6
            
            
screen devsettings_screen():
    modal True
    zorder 600
    frame:
        xminimum 1920
        xmaximum 1920
        yminimum 1080
        ymaximum 1080
        background "#00000090"
        vbox:
            xalign 0.5
            ypos 100
            text "Development settings:" color "#fff" size 60 xalign 0.5
            text "Character:" color "#fff" size 30 xalign 0.5
            textbutton "Get +1000 coins" action Function(Player.addCoins, 1000)
            textbutton "Get +50 points" action Function(Player.addPoints, 50)
            textbutton "Recover your hp" action Function(Player.addHP, Player.max_hp)
            
            textbutton "Unblock all types of sex" action Function(Player.unlockAllSexTypes)
            textbutton "Take all quests" action Function(Player.takeAllQuests)
            
            textbutton "Unlock all locations" action Function(worldmap.unlockAllLocations)
            
            
            text "Battle:" color "#fff" size 30 xalign 0.5
            if current_battle != None:
                textbutton "Set lust to max level of all enemy (You win in battle)" action [Function(current_battle.setLustToMax), Hide("devsettings_screen")]
                textbutton "Set you hp to 0 (You lose in battle)" action Function(Player.addHP, -Player.max_hp)
                
            text "Active quests:" color "#fff" size 30 xalign 0.5
            if worldmap.cur_loc != None:
                # textbutton "Unlock all locked doors in current location" action Function(worldmap.cur_loc.unlockAllLockedDoors)
                vbox:
                    for _current_quest in Player.quests:
                        hbox:
                            text _current_quest.name color "#fff" size 24 yoffset 10
                            textbutton "Completed"  action [Return({"type":"quest_completed","param":_current_quest}),Hide("devsettings_screen")]
            if dev_enable_grid == False:
                textbutton "Enable grid (dev func)" action SetVariable("dev_enable_grid", True)
            else:
                textbutton "Disable grid (dev func)" action SetVariable("dev_enable_grid", False)
            
            if dev_unlockall_door == False:
                textbutton "Unlock all locked doors (dev func)" action SetVariable("dev_unlockall_door", True)
            else:
                textbutton "Lock all locked doors (dev func)" action SetVariable("dev_unlockall_door", False)            
    textbutton "close" text_color "#f5f5f5" text_hover_color "#d9d9d9" action Hide("devsettings_screen") xalign 1.0 yalign 1.0  
 

screen choose_gender_screen(_gender):
    style_prefix "choice"

    zorder 506
    tag choose_gender_screen_tag

    text "Choose the gender of the monsters you want to fight (Only these genders will be available in battles)" xalign 0.5 size 30 yoffset 200 #color "#fff"
    vbox:   
        xalign 0.5
        yalign 0.5
        # yoffset 100
        if _gender == "male":
            textbutton "all (male and female and futa)" text_color "#fff" text_hover_color "#000" text_align 0.5  action [Return({"genders":["male", "female", "futa"]}), Hide("choose_gender_screen")] 
            textbutton "male and female (bisexual)" text_color "#fff" text_hover_color "#000" text_align 0.5  action [Return({"genders":["male", "female"]}), Hide("choose_gender_screen")] 
            textbutton "female only (straight)"  text_color "#fff" text_hover_color "#000" text_align 0.5  action [Return({"genders":["female"]}), Hide("choose_gender_screen")]
            text "male only (gay) {size=20}{i}(Will be available later){/i}{/size}" color "8f8f8f" xalign 0.5  #action [Return({"genders":["male"]}), Hide("choose_gender_screen")]
        elif _gender == "female":
            textbutton "all (male and female and futa)" text_color "#fff" text_hover_color "#000" text_align 0.5  action [Return({"genders":["male", "female", "futa"]}), Hide("choose_gender_screen")] 
            textbutton "male and female (bisexual)" text_color "#fff" text_hover_color "#000" text_align 0.5  action [Return({"genders":["male", "female"]}), Hide("choose_gender_screen")] 
            textbutton "female only (lesbian)"  text_color "#fff" text_hover_color "#000" text_align 0.5  action [Return({"genders":["female"]}), Hide("choose_gender_screen")]
            text "male only (straight) {size=20}{i}(Will be available later){/i}{/size}" color "8f8f8f" xalign 0.5  #action [Return({"genders":["male"]}), Hide("choose_gender_screen")]
        elif _gender == "futa":
            textbutton "all (male and female and futa)" text_color "#fff" text_hover_color "#000" text_align 0.5  action [Return({"genders":["male", "female", "futa"]}), Hide("choose_gender_screen")] 
            textbutton "female and futa" text_color "#fff" text_hover_color "#000" text_align 0.5  action [Return({"genders":["futa", "female"]}), Hide("choose_gender_screen")] 
            textbutton "male and female" text_color "#fff" text_hover_color "#000" text_align 0.5  action [Return({"genders":["male", "female"]}), Hide("choose_gender_screen")] 
            textbutton "female only"  text_color "#fff" text_hover_color "#000" text_align 0.5  action [Return({"genders":["female"]}), Hide("choose_gender_screen")]
            text "male only {size=20}{i}(Will be available later){/i}{/size}" color "8f8f8f" xalign 0.5  #action [Return({"genders":["male"]}), Hide("choose_gender_screen")]
        
        if _gender != "futa":
            text "all (male and female and futa) {size=20}{i}(Will be available later){/i}{/size}" color "#8f8f8f" xalign 0.5
            text "female and futa {size=20}{i}(Will be available later){/i}{/size}" color "#8f8f8f" xalign 0.5
        text "male and futa {size=20}{i}(Will be available later){/i}{/size}" color "#8f8f8f" xalign 0.5
        text "futa only {size=20}{i}(Will be available later){/i}{/size}" color "#8f8f8f" xalign 0.5
        
        # textbutton "Back" text_color "#fff" text_hover_color "#000" text_align 0.5  action Jump("create_new_char")
        

image trophy_diamond:
    "/gui/ui/trophy_diamond.png"
    xzoom 0.5 yzoom 0.5
image trophy_platinum:
    "/gui/ui/trophy_platinum.png"
    xzoom 0.5 yzoom 0.5
image trophy_golden:
    "/gui/ui/trophy_golden.png"
    xzoom 0.5 yzoom 0.5
image trophy_silver:
    "/gui/ui/trophy_silver.png"
    xzoom 0.5 yzoom 0.5
image trophy_bronze:
    "/gui/ui/trophy_bronze.png"
    xzoom 0.5 yzoom 0.5
    
screen top_donators_list():
    modal True
    frame at appear_dissolve:
        xminimum 1380
        xmaximum 1380
        # yminimum 1080
        ymaximum 11000
        # background Frame("#000000AA")
        background None
        # background Frame("#00000090")
        # imagebutton idle "#000000AA" action Hide("top_donators_list")
        $json_data = persistent.top_donators
        # hbox:
        # text "%s"%('Top hunter raiting: ') color "#fff" size 40 xoffset 500 yalign 0.0 yoffset 15
        vbox:
            xoffset 0 yoffset 700
            text "%s"%('% - completed path to the next trophy hunter') color "#fff" size 24 
            text "Color - %s tier"%(GetColorTier("Hunter 1","Hunter 1")) color "#fff" size 24 
            text "Color - %s tier"%(GetColorTier("Hunter 2","Hunter 2")) color "#fff" size 24 
            text "Color - %s tier"%(GetColorTier("Hunter 3","Hunter 3")) color "#fff" size 24 
            text "Color - %s tier"%(GetColorTier("Hunter Special","Hunter Special")) color "#fff" size 24 
            text "Color - %s tier"%(GetColorTier("Other","Other")) color "#fff" size 24
            
        # side "c r":
            # area (810,0,1110,1080)
            # viewport id "top_rating":
                # draggable True
                # mousewheel True
                # xinitial 0.5
                # yinitial 0.0
        vbox:
            xalign 0.5
            # text "Diamond Hunters: " color "#fff" size 30
            $not_patrons = False
            image "trophy_diamond"
            for m in json_data:
                if m["lifetime"] >= 90000:
                    $not_patrons = True
                    text "%s"%GetColorTier(m["tier"], m["name"]) color "#fff" size 20 xalign 0.5
            if not_patrons == False:
                text "Nothing :(" color "#fff" size 20 xalign 0.5
            # text "Platinum Hunters: " color "#fff" size 30
            image "trophy_platinum"
            $fr = 45000#15000
            $to = 90000#30000
            $not_patrons = False
            for m in json_data:
                if m["lifetime"] >= fr and m["lifetime"] < to: 
                    $not_patrons = True
                    frame:
                        xmaximum 300
                        xminimum 300
                        yminimum 30
                        ymaximum 30
                        background None
                        bar:
                            ysize 20
                            xmaximum 300
                            left_bar "#00000000"#"#ffff00" #ui_lust_bar_full3"
                            right_bar "#00000000"#"#ff0000" #"ui_lust_bar_empty3"
                            value m["lifetime"]-fr
                            range to-fr
                            yalign 0.5

                        text "%s"%(GetColorTier(m["tier"], m["name"])) color "#fff" size 20 xalign 0.5
                        text "%s%s"%(int((m["lifetime"]-fr)*100/(to-fr)),'%') color "#fff" size 20 xalign 1.0
            if not_patrons == False:
                text "Nothing :(" color "#fff" size 20 xalign 0.5
            # text "Gold Hunters: " color "#fff" size 30
            image "trophy_golden"
            $fr = 15000#25000#15000
            $to = 45000#30000
            $not_patrons = False
            for m in json_data:
                if m["lifetime"] >= fr and m["lifetime"] < to:
                    $not_patrons = True
                    frame:
                        xmaximum 300
                        xminimum 300
                        yminimum 30
                        ymaximum 30
                        background None
                        bar:
                            ysize 20
                            xmaximum 300
                            left_bar "#00000000"#"#ffff00" #ui_lust_bar_full3"
                            right_bar "#00000000"#"#ff0000" #"ui_lust_bar_empty3"
                            value m["lifetime"]-fr
                            range to-fr
                            yalign 0.5

                        text "%s"%(GetColorTier(m["tier"], m["name"])) color "#fff" size 20 xalign 0.5
                        text "%s%s"%(int((m["lifetime"]-fr)*100/(to-fr)),'%') color "#fff" size 20 xalign 1.0
            if not_patrons == False:
                text "Nothing :(" color "#fff" size 20 xalign 0.5
            # text "Silver Hunters: " color "#fff" size 30 
            image "trophy_silver"
            $fr = 7500#10000#9000
            $to = 15000#25000#15000
            $not_patrons = False
            for m in json_data:
                if m["lifetime"] >= fr and m["lifetime"] < to:
                    $not_patrons = True
                    frame:
                        xmaximum 300
                        xminimum 300
                        yminimum 30
                        ymaximum 30
                        background None
                        bar:
                            ysize 20
                            xmaximum 300
                            left_bar "#00000000"#"#ffff00" #ui_lust_bar_full3"
                            right_bar "#00000000"#"#ff0000" #"ui_lust_bar_empty3"
                            value m["lifetime"]-fr
                            range to-fr
                            yalign 0.5

                        text "%s"%(GetColorTier(m["tier"], m["name"])) color "#fff" size 20 xalign 0.5
                        text "%s%s"%(int((m["lifetime"]-fr)*100/(to-fr)),'%') color "#fff" size 20 xalign 1.0
            # text "Bronze Hunters: " color "#fff" size 30 
            image "trophy_bronze"
            $fr = 4000#5000#9000
            $to = 7500#10000#15000
            $not_patrons = False
            for m in json_data:
                if m["lifetime"] >= fr and m["lifetime"] < to:
                    $not_patrons = True
                    frame:
                        xmaximum 300
                        xminimum 300
                        yminimum 30
                        ymaximum 30
                        background None
                        bar:
                            ysize 20
                            xmaximum 300
                            left_bar "#00000000" #ui_lust_bar_full3"
                            right_bar "#00000000"#"#ff0000" #"ui_lust_bar_empty3"
                            value m["lifetime"]-fr
                            range to-fr
                            yalign 0.5

                        text "%s"%(GetColorTier(m["tier"], m["name"])) color "#fff" size 20 xalign 0.5
                        text "%s%s"%(int((m["lifetime"]-fr)*100/(to-fr)),'%') color "#fff" size 20 xalign 1.0
            if not_patrons == False:
                text "Nothing :(" color "#fff" size 20 xalign 0.5
            # vbar value YScrollValue("top_rating"):
                # xalign 1.0
                # unscrollable "hide"
    # textbutton "Close" text_color "#fff" xalign 1.0 yalign 1.0  action Return()#Hide("top_donators_list")#Return()   
                        
