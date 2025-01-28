---
type: npc
status: 
char-age: "%AGE%"
groups: 
job-title: "%JOB%"
race: Elvish
publish: true
---

>[!INFO] Holger Alsberg
>- ![[Holger Alsberg.jpg|inlR|200]]
<br/> [[Holger Alsberg.jpg|show to players]]
>- **Age:** %AGE%
> - **Description:** %DESCRIPTION%
> - **Personality:** Cordial
 
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