---
type: npc
status: 
char-age: "%AGE%"
groups: 
job-title: "%JOB%"
race: "%RACE%"
---

>[!INFO] `=this.file.name`
>- ![[River.jpg|inlR|200]]
<br/> [[River.jpg|show to players]]
>- **Age:** `= this.char-age`
> - **Description:** Her attire is practical and professional, a hip-length purple-red jacket with a high collar, and belted at her waist are several pouches and pockets. She wears five rings on her right hand. Two oddly-shaped horns sprout backwards from her flowing purple hair. Has spotted skin and impish features: her teeth are too sharp, her tongue too long, and it’s slightly unsettling when she smiles.
> - **Personality:** N/A
 
 >[!NOTE] Background
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