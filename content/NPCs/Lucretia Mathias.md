---
type: npc
status: 
char-age: 92
groups: 
job-title: Prophet
race: Human
---

>[!INFO] `=this.file.name`
>- ![[Lucretia Mathias.jpg|inlR|200]]
<br/> [[Lucretia Mathias.jpg|show to players]]
>- **Age:** `= this.char-age`
> - **Description:** Lucretia Mathias is a willowy and wizened woman with piercing eyes and pursed lips. She is in her early nineties, and keeps her greying black hair in a coiled bun beneath a linen shawl. She wears simple grey robes, and clutches a heavy leather-bound tome. A glowing golden crystal dangles from a silver chain around her neck. Her garb lightly conceals the delerium shard embedded in her heart.
> - **Personality:** I speak in proverbs and quote scripture when I speak, inspiring others to interpret my cryptic words and come to their own revelations.
 
 >[!NOTE] Background
 > {CONTENT}

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