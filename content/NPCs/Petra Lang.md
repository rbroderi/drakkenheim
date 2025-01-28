---
type: npc
status: 
char-age: "%AGE%"
groups: 
job-title: "%JOB%"
race: "%RACE%"
publish: true
---

>[!INFO] `=this.file.name`
>- ![[Petra Lang.jpg|inlR|200]]
<br/> [[Petra Lang.jpg|show to players]]
>- **Age:** `= this.char-age`
> - **Description:** Lieutenant Petra is a human urban ranger. She is a fit and nimble teenager with long blonde hair, a narrow pointed chin, and bold features. She wears a hooded green cloak and light chain armor of the [Hooded Lanterns](https://mrbissell.com/Factions/Hooded+Lanterns) with a lieutenant’s insignia on her shoulder pauldron.
> - **Personality:** N/A
 
 >[!NOTE] Background
 >
 >Lieutenant in Hooded Lantern
 
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