class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupes = defaultdict(list)
    
        for mot in strs:
            # 1. Trier les lettres du mot pour créer la clé unique (ex: "chien" -> "cehin")
            cle_triee = "".join(sorted(mot))
            
            # 2. Ajouter le mot d'origine dans le groupe correspondant
            groupes[cle_triee].append(mot)
            
        # 3. Retourner uniquement les listes de groupes
        return list(groupes.values())