---
type: object
subtype: Ship
status: 
owner: "[[Tamond Stormwind]]"
publish: true
---

>[!INFO] `=this.file.name`
>- ![[silver_serpent.jpg|inlR|200]]
>- **Owner:** `=this.owner`
> - **Description:** The medieval sailing vessel known as the Silver Serpent is a majestic sight on the open seas. With its sleek silver hull glistening in the sunlight, this ship is a formidable force to be reckoned with. Its large sails billowed in the wind, propelling it forward with impressive speed and grace.
> - The Silver Serpent is adorned with intricate carvings and embellishments, showcasing the craftsmanship and artistry of its creators.

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

| Session                                                  | Title               | date       |
| -------------------------------------------------------- | ------------------- | ---------- |
| [[Road to Drakkenheim\|Road to Drakkenheim]] | Road to Drakkenheim | 07/14/2024 |

%% DATAVIEW_PUBLISHER: end %%