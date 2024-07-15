---
type: npc
status: 
char-age: 38
groups: 
job-title: helmsman
---

>[!INFO] `=this.file.name`
>- ![[helmsman.jpg|inlR|200]]
<br/> [[helmsman.jpg|Show Players]]
>- **Age:** `= this.char-age`
> - **Description:** %DESCRIPTION%
> - **Personality:** Reserved
 
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