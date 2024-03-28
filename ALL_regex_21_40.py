regex_dict_21_40 = {r"(?<!Louis\s)(?<!old\s)\b(Edmond\s+)?\b(?<!\w)(Dant[èe]s|Edmond|\b(The\s)?\b([Cc]ount\sof\s)?Monte\sCristo|Count\s+Monte\s+Cristo|Sinbad\b(\sthe\s[sS]ailor)?|\b([Ll]ord\s)?Wilmore|\b([Aa]bb[ée]\s)?Busoni|Zatarra|Maltese)(?!\w)|(?<!\w)Abb[ée](?!\sFaria)": "EdmondDantes", # all + add|(?<!\w)Abb[ée](?!\sFaria) for chapters 21-40 __1__2__3__4__5__6__7__8
 r"(?<!\w)\b(Louis\s|old\s)+Dantès(?!\w)": "LouisDantes", # 1-40, 100-117 __1__2__6
 r"\b(Merc[éeè]d[éeè]s|Madame\sde\sMorcerf)(?!\w)": "Mercedes", # all except 86-87 __1__2__3__4__5__7__8
 r"\b(Fernand)\b(\s+Mondego)?\b|(?<!\w)([Cc]omte\s+de\s+[Mm]orcerf)(?!\w)|M\.\sde\sMorcerf(?!\w)": "Fernand", #all |replace alternative Morcerf(?!\w) for chapters 86-88 __1__2__3__4__5__6__7__8
 r"(?<!Madame\s)(?<!Hermine\s)(?<!Eugénie\s)\b([Bb]aron\s)?\b(Danglars)(?!\w)": "Danglars", # all __1__2__3__4__5__6__7__8
 r"\b(?:Madame+|Hermine+)+\b(\sDanglars|\sde\s+Servieux)+(?!\w)|(?<!\w)[Bb]aroness(\sDanglars)?(?!\w)": "HermineDanglars", # all except 1-20, 86-87 __2__3__4__5__7__8
 r"(?<!\w)Eugénie\b(\sDanglars)?(?!\w)|(?<!\w)Mademoiselle\sDanglars(?!\w)": "EugenieDanglars", # all except 1-20, 86-87 __2__3__4__5__7__8
 r"(?<!Valentine\sde\s)(?<!Edward\sde\s)(?<!Noirtier\sde\s)(?<!Mad[ae]moiselle\sde\s)(?<!Madame\sde\s)\b(G[eé]rard\sde\s|M.\sde\s)?(Villefort)+(?!\w)|\b(G[eé]rard)+(?!\w)": "GerarddeVillefort", # all except 86-87 __1__2__3__4__5__7__8
 r"(?<!\w)Valentine\b(\sde\sVillefort)?(?!\w)|(?<!\w)Mademoiselle\sde\sVillefort(?!\w)": "ValentinedeVillefort", # all except 1__8-40, 86-87 __3__4__5__7__8
 r"\b(M.\s)?(?<!\w)Noirtier+(?!\w)\b(\sde\sVillefort)?(?!\w)": "NoirtierdeVillefort", # all except 86-87 __1__2__3__4__5__7__8
 r"\b(Edward)+\b(\sde\sVillefort)?(?!\w)": "EdwarddeVillefort", # all except 1-40, 86-87 __3__4__5__7__8
 r"(?<!\w)Hayd[ée]e(?!\w)": "Haydee", # 41-55, 70-117 __3__5__6__7__8
 r"(Ali(?!\sPasha)(?!Pasha)\b(\sTebelen)?|\sthe\sNubian)(?!\w)": "Ali", # all except 1-20 __2__3__4__5__6__7__8
 r"(?<!\w)Ali\sPasha(?!\w)": "AliPasha", # all except 1-20, 41-55, 100-117 __2__4__5__6__7__8
 r"(?<!\w)Vasiliki(?!\w)": "Vasiliki", # 70-99 __5__6__7 X
 r"Albert\b(\sde\sMorcerf)?|(?<!Comte\sde\s)(?<!Madame\sde\s)\b(Vicomte\sde\s)?Morcerf(?!\w)": "AlbertdeMorcerf", # all except 1-20,  change last part to: (?<!\w)Vicomte\sde\sMorcerf(?!\w) for 86-87 __2__3__4__5__6__7__8
 r"(?<!\w)\b(Abb[eé]\s)?Faria(?!\w)|(?<!\w)Abb[eé](?!\w)": "Faria", # prev. regex only chapters 1-20, otherwise only first alternative __1__2__3__4__5__6__7__8
 r"(?<!\w)Ch[aâ]teau-Renaud(?!\w)": "ChateauRenaud", # all except 1-20, 86-87 __2__3__4__5__7__8
 r"\b(Luigi\s)?(?<!\w)Vampa(?!\w)|(?<!\w)Luigi(?!\w)": "Vampa", # 21-55, 100-117 __2__3__8
 r"(?<!Madame\s)\b(Gaspard\s|M.\s)?(?<!\w)Caderousse(?!\w)|(?<!\w)Gaspard(?!\w)": "Caderousse", # all except 86-87 __1__2__3__4__5__7__8
 r"(?<!\w)La\sCarconte(?!\w)": "LaCarconte", # 21-55, 70-85 __2__3__5 X
 r"(?<!\w)Héloïse(?!\w)\b(\sde\sVillefort)?|(?<!\w)Madame\sde\sVillefort(?!\w)": "HeloisedeVillefort", # all except 1-40, 86-87 __3__5__7__8
 r"\b(Andrea\s|Prince\s)+Cavalcanti(?!\w)|\b(Benedetto|Andrea)+": "AndreaCavalcanti", # all from 41 onwards __3__4__5__6__7__8
 r"(?<!young\s)(?<!\w)\b(Monsieur\s|M.\s)Cavalcanti(?!\w)": "MonsieurCavalcanti", # all except 1-40, 86-87 __3__5__7__8
 r"(?<!\w)Beauchamp(?!\w)": "Beauchamp", # 21-55, 70-117 __2__3__5__6__7__8
 r"\b(Giovanni\s)?Bertuccio(?!\w)|(?<!\w)Giovanni(?!\w)": "Bertuccio", # all except 1-20, 86-87 __2__3__4__5__7__8
 r"(?<!\w)Assunta(?!\w)": "Assunta", # 41-55 __3 X
 r"\b(Marquise\sde\s||Madame\sde\s|Mme.\sde\s|Ren[ée]e\sde\s)+Saint-M[eé]ran(?!\w)|(?<!\w)Ren[ée]e(?!\w)": "MadamedeSaintMeran", # all except 86-87 __1__2__3__4__5__7__8
 r"\b(Marquis\sde\s||M.\sde\s)+Saint-M[eé]ran(?!\w)": "MonsieurdeSaintMeran", # all except 86-87 __1__2__3__4__5__7__8
 r"(?<!\w)Salvieux(?!\w)": "Salvieux", # 1-20 __1 X
 r"(?<!Maximilian\s)(?<!Julie\s)\b(M.\s)?Morrel(?!\w)": "MonsieurMorrel", # valid until chapter 41, then "(?<!Maximilian\s|Julie\s)\b(old\s)+Morrel(?!\w)" (only 1 match) __1__2__3__4__5__6__7__8
 r"(?<!\w)Madame\sMorrel(?!\w)": "MadameMorrel", # 21-40 X
 r"(?<!\w)Julie(?!\w)\b(\sMorrel)?|(?<!\w)Madame(\sEmmanuel)?\sHerbault(?!\w)": "JulieMorrel", # all except 1-20, 70-87 __2__3__4__7__8
 r"(?<!\w)Emmanuel(?!\w)\b(\sHerbault)?": "EmmanuelHerbault", # 21-69, 88-117 __2__3__4__7__8
 r"(?<!\w)Baptistin(?!\w)": "Baptistin", # all except 1-40, 86-87 __3__4__5__7__8
 r"\b(Signor\s)?Pastrini(?!\w)": "Pastrini", # 21-40, 100-117 __2__8
 r"\b(Lucien\s)?Debray(?!\w)|(?<!\w)Lucien(?!\w)": "LucienDebray", # all except 1-20, 86-87 __2__3__4__5__7__8
 r"\b(Louise\s|Mademoiselle\s|L[èe]on\s)?d'Armilly(?!\w)|(?<!\w)Louise(?!\w)": "LouisedArmilly", # all except 1-40, 86-87 __3__4__5__7__8
 r"(?<!\w)Boville(?!\w)": "Boville", # 21-40, 70-85, 88-117 __2__5__7__8
 r"(?<!\w)Franz(?!\w)\b(\sd'[ÉE]pinay|\sde\sQuesnel)?|\b(Baron\s|M.\s)?(?<!\w)d'[ÉE]pinay(?!\w)": "FranzdEpinay", # 21-85, 88-99 __2__3__4__5__7 X
 r"(?<!\w)General\s(Flavien\s)?de\sQuesnel(?!\w)": "GeneralQuesnel", # 56-85 __4 X
 r"(?<!\w)Jacopo(?!\w)": "Jacopo", # 21-40, 100-117 __2__8
 r"(?<!\w)Teresa(?!\w)": "Teresa", # 21-40 __2 X
 r"(?<!\w)Cocles(?!\w)": "Cocles", # 21-55 __2__3 X
 r"(?<!\w)Cucumetto(?!\w)": "Cucumetto", # 21-40 __2 X
 r"(?<!\w)Avrigny(?!\w)": "Avrigny", # 70-85, 88-117 __5__7__8
 r"(?<!\w)Barrois(?!\w)": "Barrois"} # 56-85, 88-117  __4__5__7__8
