---
type: npc
status: 
char-age: "%AGE%"
groups: 
job-title: "%JOB%"
---

>[!INFO] `=this.file.name`
>- ![[placeholder.png|inlR|200]]
>- **Age:** `= this.char-age`
> - **Description:** %DESCRIPTION%
> - **Personality:** Cordial
 
 >[!NOTE] Background
 > {CONTENT}

 >[!EXAMPLE] Statistics
 > {CONTENT}

>[!TIP] Appearances
 >```dataview
TABLE WITHOUT ID file.link AS "Session", session-title AS "Title", date
FROM -"_resources/page_templates" AND [[#]]
WHERE type = "page-session"
SORT session-num asc