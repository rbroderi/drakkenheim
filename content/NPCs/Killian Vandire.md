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
>- ![[Killian Vandire.jpg|inlR|200]]
<br/> [[Killian Vandire.jpg|show to players]]
>- **Age:** `= this.char-age`
> - **Description:** %DESCRIPTION%
> - **Personality:** N/A
 
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