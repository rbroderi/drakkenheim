---
type: npc
status: 
char-age: 60's
groups: 
job-title: Provisional Head of Drakkenheim Mages
race: Human
---

>[!INFO] `=this.file.name`
>- ![[Eldrick Runeweaver.jpg|inlR|200]]
<br/> [[Eldrick Runeweaver.jpg|show to players]]
>- **Age:** `= this.char-age`
> - **Description:** Eldrick Runeweaver is a towering and broad-shouldered man in his mid-sixties. His amber eyes glow softly behind his circular glasses, and he has a square-cut, greying black beard. He wears nine rings of silver, gold, and electrum: one on each finger except his left thumb. He wears flowing purple garb with golden embroidery, and carries an obsidian staff tipped with a delerium crystal.
> - **Personality:** I carefully calculate my every action, and I speak using a few well-chosen words. I'm a teacher at heart, so I often phrase my responses in the form of a pointed question.
 
 >[!NOTE] Background
 > One of the finest professors in the Amethyst Academy, Eldrick Runeweaver has personally instructed a generation of talented arcane spellcasters. He is the foremost living expert on abjuration magic, but is also highly regarded within the Academy as a dedicated administrator and calculating leader.

 >[!EXAMPLE] Statistics
 > {CONTENT}

## Appearances

%% DATAVIEW_PUBLISHER: start
```dataview
TABLE WITHOUT ID file.link AS "Session", session-title AS "Title", date
FROM -"_resources/page_templates" AND [[#]]
WHERE type = "page-session"
SORT session-num asc
```
%%

| Session | Title | date |
| ------- | ----- | ---- |

%% DATAVIEW_PUBLISHER: end %%