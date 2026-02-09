import os
import json
from country_codes import *

default = \
    {
        "name": "",
        "countries": [],
        "order": False,
        "difficulty": 0
    },

# countries cc "AR"
# if a group is order true, it will take the nths firsts items, otherwise, random
# difficulties 1 - 5  

groups = [
    
    # -> stats <-
    
    { # biggest
        "name": "Top Biggest Countries",
        "countries": [
            Russia, 
            Canada, 
            China, 
            UnitedStates, 
            Brazil, 
            Australia, 
            India, 
            Argentina, 
            Kazakhstan, 
            Algeria
        ],
        "order": True,
        "difficulty": 1
    },
    { # smallest
        "name": "Top Smallest Countries",
        "countries": [
            Vatican, 
            Monaco, 
            Nauru, 
            Tuvalu, 
            SanMarino,
            Liechtenstein, 
            MarshallIslands, 
            SaintKittsAndNevis,
            Maldives, 
            Malta
        ],
        "order": True,
        "difficulty": 1
    },
    { # most populated
        "name": "Top Most Populated Countries",
        "countries": [
            India,
            China,
            UnitedStates,
            Indonesia,
            Pakistan,
            Nigeria,
            Brazil,
            Bangladesh,
            Russia,
            Mexico
        ],
        "order": True,
        "difficulty": 1
    },
    { # least populated
        "name": "Top Least Populated Countries",
        "countries": [
            Vatican,
            Tuvalu,
            Nauru,
            Palau,
            SanMarino,
            Monaco,
            Liechtenstein,
            MarshallIslands,
            Greenland,
            SaintKittsAndNevis
        ],
        "order": True,
        "difficulty": 1
    },
    { # most gdp per capita
        "name": "Top Countries with the Highest GDP per capita",
        "countries": [
            Monaco,
            Liechtenstein,
            Luxembourg,
            Ireland,
            Switzerland,
            Norway,
            UnitedStates,
            Iceland,
            Qatar,
            Denmark
        ],
        "order": False,
        "difficulty": 1
    },
    { # least gdp per capita
        "name": "Top Countries with the Lowest GDP per capita",
        "countries": [
            Burundi,
            Afghanistan,
            Yemen,
            SouthSudan,
            CentralAfricanRepublic,
            Malawi,
            Somalia,
            Madagascar,
            Mozambique,
            NorthKorea
        ],
        "order": False,
        "difficulty": 1
    },
    { # most hdi 
        "name": "Top Countries with the Heighest HDI",
        "countries": [
            Iceland,
            Switzerland,
            Norway,
            Monaco,
            Denmark,
            Sweden,
            Germany,
            Australia,
            TheNetherlands,
            HongKong,
        ],
        "order": False,
        "difficulty": 1
    },
    { # least hdi 
        "name": "Top Countries with the Lowest HDI",
        "countries": [
            SouthSudan,
            Somalia,
            CentralAfricanRepublic,
            Chad,
            Mali,
            Niger,
            Burundi,
            BurkinaFaso,
            SierraLeone,
            Yemen
        ],
        "order": False,
        "difficulty": 1
    },

    # -> flags <-

    { # flags with text
        "name": "Countries which Flag has Text",
        "countries": [
            Afghanistan,
            Brazil,
            Iran,
            Iraq,
            SaudiArabia 
        ],
        "order": False,
        "difficulty": 2
    },
    { # flags with coat of arms
        "name": "Countries which Flag has a Coat of Arms",
        "countries": [
            Andorra,
            Belize,
            Brunei,
            Croatia,
            DominicanRepublic,
            Ecuador,
            Egypt,
            ElSalvador,
            EquatorialGuinea,
            Fiji,
            Guatemala,
            Haiti,
            Moldova,
            Montenegro,
            Nicaragua,
            Paraguay,
            Portugal,
            SanMarino,
            Serbia,
            Slovakia,
            Slovenia,
            Spain,
        ],
        "order": False,
        "difficulty": 1
    },
    { # flags with birds
        "name": "Countries which Flag has a Bird",
        "countries": [
            Albania,
            Egypt,
            Kazakhstan,
            Mexico,
            Moldova,
            Montenegro,
            Serbia,
            Kiribati,
            Uganda
        ],
        "order": False,
        "difficulty": 2
    },
    { # flags with borders
        "name": "Countries which Flag has Borders",
        "countries": [
            Grenada,
            Maldives,
            Montenegro,
            Nepal,
            SriLanka
        ],
        "order": False,
        "difficulty": 4
    },
    
    # -> goverment <-
    
    { # multiple capitals
        "name": "Countries which Multiple Capital Cities",
        "countries": [
            Benin,
            Bolivia,
            Chile,
            Estonia,
            Eswatini,
            Germany,
            Malaysia,
            SouthAfrica,
            SriLanka,
            Switzerland,
        ],
        "order": False,
        "difficulty": 5 
    },
    { # absolute monarchies
        "name": "Absolute Monarchies",
        "countries": [
            Vatican,
            Oman,
            SaudiArabia,
            Eswatini,
            Brunei,
        ],
        "order": False,
        "difficulty": 3
    },
    { # executive constitutional monarchies
        "name": "Executive Contitutional Monarchies",
        "countries": [
            Bahrain,
            Bhutan,
            Jordan,
            Kuwait,
            Liechtenstein,
            Monaco,
            Morocco,
            Qatar,
            Tonga,
            UnitedArabEmirates 
        ],
        "order": False,
        "difficulty": 4
    },
    { # ceremonial monarchies
        "name": "Ceremonial Monarchies",
        "countries": [
            Andorra,
            Belgium,
            Cambodia,
            Denmark,
            Japan,
            Lesotho,
            Luxembourg,
            Malaysia,
            TheNetherlands,
            Norway,
            Spain,
            Sweden,
            Thailand,
            UnitedKingdom
        ],
        "order": False,
        "difficulty": 4
    },
    { # elective monarchies
        "name": "Elective Monarchies",
        "countries": [
            Vatican,
            Andorra,
            Malaysia,
            Samoa
        ],
        "order": False,
        "difficulty": 5
    },
    { # dictatorships
        "name": "Current Dictatorships",
        "countries": [
            Afghanistan,
            Angola,
            Azerbaijan,
            Bahrain,
            Belarus,
            Chad,
            Cuba,
            DemocraticRepublicOfTheCongo,
            EquatorialGuinea,
            Eritrea,
            Iran,
            Laos,
            Myanmar,
            Nicaragua,
            NorthKorea,
            Russia,
            Turkmenistan,
            Uganda,
            Venezuela,
            Yemen
        ],
        "order": False,
        "difficulty": 3
    },
    { # dollarized
        "name": "Dollarized Countries",
        "countries": [
            MarshallIslands,
            Micronesia,
            Palau,
            Ecuador,
            ElSalvador,
            Liberia,
            Panama,
            TimorLeste,
            Venezuela
        ],
        "order": False,
        "difficulty": 4
    },
    { # commies
        "name": "Communist Party Ruling",
        "countries": [
            China,
            Cuba,
            Laos,
            NorthKorea,
            Vietnam    
        ],
        "order": False,
        "difficulty": 2    
    },
    
    # -> foreign policie <-
    
    { # nuclear weapons
        "name": "Countries with Nuclear Weapons",
        "countries": [
            Russia,
            UnitedStates,
            China,
            France,
            UnitedKingdom,
            India,
            Pakistan,
            Israel,
            NorthKorea
        ],
        "order": False,
        "difficulty": 4
    },
    { # antarctic claims
        "name": "Countries with Territorial Claims in Antarctica",
        "countries": [
            Argentina,
            Australia,
            Chile,
            France,
            NewZealand,
            Norway,
            UnitedKingdom
        ],
        "order": False,
        "difficulty": 0
    },
    { # onu security council
        "name": "Permanent Members of the ONU Security Council",
        "countries": [
            UnitedStates,
            France,
            China,
            Russia,
            UnitedKingdom    
        ],
        "order": False,
        "difficulty": 0    
    },
    
    # -> unions <-
    
    { # commonwealth
        "name": "Commonwealth Members",
        "countries": [
            UnitedKingdom,
            Canada,
            Australia,
            PapuaNewGuinea,
            NewZealand,
            Jamaica,
            SolomonIslands,
            Bahamas,
            Belize,
            SaintLucia,
            Grenada,
            SaintVincentAndTheGrenadines,
            SaintKittsAndNevis,
            AntiguaAndBarbuda,
            Tuvalu
        ],
        "order": False,
        "difficulty": 0
    },
    { # eu
        "name": "EU Members",
        "countries": [            
            Sweden,
            Denmark,
            Finland,
            Poland,
            Czechia,
            Hungary,
            Slovakia,
            Romania,
            Bulgaria,
            Greece,
            Estonia,
            Latvia,
            Lithuania,
            Belgium,
            TheNetherlands,
            Luxembourg,
            Italy,
            Austria,
            Croatia,
            France,
            Germany,
            Slovenia,
            Spain,
            Portugal,
            Malta,
            Cyprus,
            Ireland
        ],
        "order": False,
        "difficulty": 1
    },
    { # shengen area
        "name": "Shengen Area",
        "countries": [
            Switzerland,
            Iceland,
            Norway,
            Liechtenstein,         
            Sweden,
            Denmark,
            Finland,
            Poland,
            Czechia,
            Hungary,
            Slovakia,
            Romania,
            Bulgaria,
            Greece,
            Estonia,
            Latvia,
            Lithuania,
            Belgium,
            TheNetherlands,
            Luxembourg,
            Italy,
            Austria,
            Croatia,
            France,
            Germany,
            Slovenia,
            Spain,
            Portugal,
            Malta,
        ],
        "order": False,
        "difficulty": 2
    },
    { # euro zone
        "name": "Euro Zone",
        "countries": [
            Finland,
            Slovakia,
            Bulgaria,
            Greece,
            Estonia,
            Latvia,
            Lithuania,
            Belgium,
            TheNetherlands,
            Luxembourg,
            Italy,
            Austria,
            Croatia,
            France,
            Germany,
            Slovenia,
            Spain,
            Portugal,
            Malta,
            Cyprus,
            Ireland
        ],
        "order": False,
        "difficulty": 1
    },
    { # brics founders
        "name": "BRICS Founders",
        "countries": [
            Brazil,
            Russia,
            India,
            China,
            SouthAfrica
        ],
        "order": False,
        "difficulty": 2
    },
    { # brics 
        "name": "BRICS Members",
        "countries": [
            Brazil,
            Russia,
            India,
            China,
            SouthAfrica,
            Egypt,
            Ethiopia,
            Indonesia,
            Iran,
            UnitedArabEmirates
        ],
        "order": False,
        "difficulty": 3
    },
    { # nato founders
        "name": "Nato Founders",
        "countries": [
            Belgium,
            Canada,
            Denmark,
            UnitedStates,
            France,
            Iceland,
            Italy,
            Luxembourg,
            Norway,
            TheNetherlands,
            Portugal,
            UnitedKingdom
        ],
        "order": False,
        "difficulty": 2
    },
    { # g7
        "name": "G7 Members",
        "countries": [
            Canada,
            France,
            Germany,
            Italy,
            Japan,
            UnitedKingdom,
            UnitedStates    
        ],
        "order": False,
        "difficulty": 2
    },
    
    # -> languages <-
    
    { # Countries which use the cyrillic alphabet
        "name": "Countries Using the Cyrillic Writing System",
        "countries": [
            Russia,
            Belarus,
            Ukraine,
            Bulgaria,
            Serbia,
            Kosovo,
            Montenegro,
            NorthMacedonia,
            BosniaAndHerzegovina,
            Kazakhstan,
            Mongolia,
            Kyrgyzstan,
            Uzbekistan,
            Tajikistan
        ],
        "order": False,
        "difficulty": 3
    },
    
    # -> demographic <-
    
    { # buddhist
        "name": "Countries with Buddhism as Main Religion",
        "countries": [
            Mongolia,
            Cambodia,
            Thailand,
            Myanmar,
            Laos,
            Singapore,
            Bhutan,
            SriLanka
        ],
        "order": False,
        "difficulty": 2
    },
    
    # -> geography <-
    
    { # most oil reserves
        "name": "Top Countries with the Most Oil Reserves",
        "countries": [
            Venezuela,
            SaudiArabia,
            Iran,
            Iraq,
            Canada,
            UnitedArabEmirates,
            Kuwait,
            Russia,
            UnitedStates,
            Libya
        ],
        "order": True,
        "difficulty": 2
    },
    { # most coast line
        "name": "Top Countries with the Largest Coastline",
        "countries": [
            Canada,
            UnitedStates,
            Indonesia,
            Russia,
            Norway,
            Australia,
            Greenland,
            Chile,
            Philippines,
            Japan
        ],
        "order": True,
        "difficulty": 4
    },
    { # landlocked
        "name": "Landlocked Countries",
        "countries": [
            Afghanistan,
            Andorra,
            Armenia,
            Austria,
            Azerbaijan,
            Belarus,
            Bhutan,
            Bolivia,
            Botswana,
            BurkinaFaso,
            Burundi,
            CentralAfricanRepublic,
            Chad,
            Czechia,
            Eswatini,
            Ethiopia,
            Hungary,
            Kazakhstan,
            Kosovo,
            Kazakhstan,
            Kosovo,
            Kyrgyzstan,
            Laos,
            Lesotho,
            Liechtenstein,
            Luxembourg,
            Malawi,
            Mali,
            Moldova,
            Mongolia,
            Nepal,
            Niger,
            NorthMacedonia,
            Paraguay,
            Rwanda,
            SanMarino,
            Serbia,
            Slovakia,
            SouthSudan,
            Switzerland,
            Tajikistan,
            Turkmenistan,
            Uganda,
            Uzbekistan,
            Vatican,
            Zambia,
            Zimbabwe
        ],
        "order": False,
        "difficulty": 2
    },
    { # cut by the equator
        "name": "Countries Intersected by the Equator",
        "countries": [
            Ecuador,
            Colombia,
            Brazil,
            SaoTomeAndPrincipe,
            Gabon,
            RepublicOfTheCongo,
            DemocraticRepublicOfTheCongo,
            Uganda,
            Kenya,
            Somalia,
            Indonesia,
            Kiribati
        ],
        "order": False,
        "difficulty": 3
    },
    { # transcontinental
        "name": "Transcontinental Countries",
        "countries": [
            Egypt,
            Russia,
            Turkey,
            Chile,
            Spain,
            Denmark,
            UnitedStates,
            France,
            UnitedKingdom
        ],
        "order": False,
        "difficulty": 3 
    },
    
    # -> name <-
    
    { # STAN club
        "name": "The Stan Club",
        "countries": [
            Afghanistan,
            Kyrgyzstan,
            Kazakhstan,
            Pakistan,
            Tajikistan,
            Turkmenistan,
            Uzbekistan
        ],
        "order": False,
        "difficulty": 1
    },
    { # LAND club
        "name": "The LaLaLAND Club",
        "countries": [
            Switzerland,
            Finland,
            Greenland,
            Ireland,
            Iceland,
            TheNetherlands,
            NewZealand,
            Poland,
            Thailand
        ],
        "order": False,
        "difficulty": 2
    },
    { # GUINEA club
        "name": "The Guinea Club",
        "countries": [
            Guinea,
            EquatorialGuinea,
            GuineaBissau,
            PapuaNewGuinea
        ],
        "order": False,
        "difficulty": 1
    },
    
    # -> history <-
    
    { # ex ussr
        "name": "Former USSR",
        "countries": [
            Estonia,
            Latvia,
            Lithuania,
            Belarus,
            Ukraine,
            Moldova,
            Russia,
            Georgia,
            Azerbaijan,
            Armenia,
            Kazakhstan,
            Uzbekistan,
            Turkmenistan,
            Kyrgyzstan,
            Tajikistan    
        ],
        "order": False,
        "difficulty": 2
    },
    { # ex yugoslavia
        "name": "Former Yugoslavia",
        "countries": [
            BosniaAndHerzegovina,
            Croatia,
            Slovenia,
            NorthMacedonia,
            Montenegro,
            Serbia,
            Kosovo,
        ],
        "order": False,
        "difficulty": 0
    },
    
    # -> sports <-
    
    { # olympic medals
        "name": "Top Countries by Olympic Medals",
        "countries": [
            UnitedStates,
            Russia,
            Germany,
            China,
            UnitedKingdom,
            France,
            Italy,
            Sweden,
            Norway,
            Japan
        ],
        "order": True,
        "difficulty": 3
    },
    { # f1 gps
        "name": "Countries with a F1 GP",
        "countries": [
            Australia,
            Bahrain,
            Brazil,
            China,
            Japan,
            Singapore,
            SaudiArabia,
            Qatar,
            Azerbaijan,
            UnitedStates,
            Canada,
            Mexico,
            Spain,
            UnitedKingdom,
            TheNetherlands,
            Belgium,
            Austria,
            Italy,
            Hungary,
            Monaco,
            UnitedArabEmirates,
        ],
        "order": False,
        "difficulty": 3
    },
    { # fifa world cup champs
        "name": "FIFA World Cup Champions",
        "countries": [
            Uruguay,
            Italy,
            Germany,
            Brazil,
            UnitedKingdom,
            Argentina,
            France
        ],
        "order": False,
        "difficulty": 3
    }
    
    # -> Other <-

]

if __name__ == "__main__":
    print(f"\n<< {len(groups)} >>\n")
    
    with open("src-tauri/data/groups.json", "w", encoding="utf-8") as f:
        json.dump(groups, f, indent=4)