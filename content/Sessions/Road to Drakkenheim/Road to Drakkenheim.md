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

## Scenes
- Small scene description.

## Locations

**Location**: Port Nyanzaru
**Location**: Open Ocean
**Location**: Ashbay

![[Leaving Port_PRIVATE]]