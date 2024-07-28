---
type: page-session
dg_campaign: Drakkenheim
date: 07/14/2024
session-title: Road to Drakkenheim
publish: true
---

## Scene: Leaving Port
#### NPC Appearances

%% DATAVIEW_PUBLISHER: start
```dataview
TABLE WITHOUT ID file.link AS "Character Name", upper(status) AS "Current Status", job-title AS "Role", groups AS "Affiliations"
FROM outgoing([[]])
WHERE type = "npc"
```
%%

| Character Name                                 | Current Status | Role     | Affiliations       |
| ---------------------------------------------- | -------------- | -------- | ------------------ |
| [[NPCs/Tamond Stormwind.md\|Tamond Stormwind]] | \-             | Captain  | The Silver Serpent |
| [[NPCs/Adrien Ballard.md\|Adrien Ballard]]     | \-             | Helmsman | The Silver Serpent |
| [[NPCs/Zander Lawson.md\|Zander Lawson]]       | \-             | Bosun    | The Silver Serpent |

%% DATAVIEW_PUBLISHER: end %%
#### Objects / Items Appearances
%% DATAVIEW_PUBLISHER: start
```dataview
TABLE WITHOUT ID file.link AS "Name", owner AS "Owner"
FROM outgoing([[]])
WHERE type = "object"
```
%%

| Name                                          | Owner                                          |
| --------------------------------------------- | ---------------------------------------------- |
| [[Objects/Silver Serpent.md\|Silver Serpent]] | [[NPCs/Tamond Stormwind.md\|Tamond Stormwind]] |

%% DATAVIEW_PUBLISHER: end %%

## Audio
![[DAYTIME,-ETIOPIAN-FOOD-MARKED,-PEOPLE-BARGAINING,-CHATTING,-WALLA-MARKET_MOTHERLAND-ETHIOPIA_05.oga#loop]]
![[Port-ambience,-small-waves-hitting-boats.oga#loop]]

## Synopsis

Players leave Port Nyanzaru, meeting [[Tamond Stormwind]] Captain of the [[Silver Serpent]] and his crew including: Helmsman [[Adrien Ballard]] and Bosun [[Zander Lawson]]

## Locations

**Location**: Port Nyanzaru
**Location**: Open Ocean
**Location**: Ashbay

## Secrets and Clues

### Maelstrom

MAELSTROM Map  
Maelstrom appears

- Players hear commotion on deck and go and investigate
- Just as they reach deck they see a large wave wash most of crew overboard and knock out Helmsman.
    - 0:00
        
        0:00
        
        /
        
        0:01
        
        |Wood_Box_Break.oga
        
- Captain shouts out for them to take a position and help out.
- Players can take positions on Gunwales, at the mast or at the Wheel.
- Roll initiative
    - DC 12 Athletics or Acrobatics to stay standing
    - Try to turn ship into wave
        - DC 12 int if helmed
        - This lowers the wave DCs by 5
    - Wave hits ship
        - 0:00
            
            0:00
            
            /
            
            0:06
            
            |wave_crash.oga
            
        - DC 12 Athletics or Acrobatics to not get swept away
        - DC 15 Athletics or Acrobatics to catch on railing
        - If Gunwales manned someone can roll to catch - DC 10 Athletics or Acrobatics
    - Try to control rigging and sails
        - DC 10 to keep mast from breaking
        - 0:00
            
            0:00
            
            /
            
            0:07
            
            |mast_breaks.oga
            
- Ship is sucked into the Maelstrom and all are thrown overboard.

## Potential Monsters

- N/A

## Potential Treasure

If captain is saved he will give choice of one of the following items:

- [cloak of billowing](https://www.dndbeyond.com/magic-items/27040-cloak-of-billowing)
- [pipe of smoke monsters](https://www.dndbeyond.com/magic-items/27082-pipe-of-smoke-monsters)

---

## Scene: Turtle Island

TURTLE Map  
Our Heroes (and any crew if saved) Wake up on an island with a Tortle standing over them.

- Kyle introduces his character
- After introduction roll DC 17 perception to see if anyone notices the Dregs sneaking up in the water
- Kyle retrieves Map of Region
    - If anyone looks around then reveal they are on a huge turtle.
- DC 15 perception to see if anyone notices the Dregs
- If not reveled have Dregs pop up right at show with several clustered around the turtles head trying to put on a collar.
    - The Deep dregs are trying to claim the huge turtle in the name of the Duchess
- After defeating the Deep Dregs the huge turtle makes for shore.

## Potential Monsters

- [Deep Dreg Woman](https://www.dndbeyond.com/monsters/4668878-deep-dreg-woman)
- [Deep Dreg Man](https://www.dndbeyond.com/monsters/4668800-deep-dreg-man)

![[road to drakkenheim_PRIVATE]]