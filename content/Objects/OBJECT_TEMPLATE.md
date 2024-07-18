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

## Appearances

%% DATAVIEW_PUBLISHER: start
```dataview
TABLE WITHOUT ID file.link AS "Session", session-title AS "Title", date
FROM [[#]]
WHERE type = "page-session"
SORT session-num asc
```
%%

| Session | Title | date |
| ------- | ----- | ---- |

%% DATAVIEW_PUBLISHER: end %%