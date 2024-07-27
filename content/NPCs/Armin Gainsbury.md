---
type: npc
status: 
char-age: "%AGE%"
groups: 
job-title: "%JOB%"
race: "%RACE%"
---

>[!INFO] `=this.file.name`
>- ![[Armin Gainsbury.jpg|inlR|200]]
<br/> [[Armin Gainsbury.jpg|show to players]]
>- **Age:** `= this.char-age`
> - **Description:** A bespectacled and beanpole-shaped human
> - **Personality:** N/A
 
 >[!NOTE] Background
Owns [[Gainsbury Expeditionary Supply Company.jpg]]

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