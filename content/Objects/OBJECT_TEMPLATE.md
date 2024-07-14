---
type: object
subtype: Ship
status: 
owner: "[[%OWNER%]]"
---

>[!INFO] `=this.file.name`
>- ![[placeholder.png|inlR|200]]
>- **Owner:** `= this.owner`
> - **Description:** %DESCRIPTION% 
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