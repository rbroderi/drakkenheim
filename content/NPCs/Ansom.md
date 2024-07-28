---
type: npc
status: 
char-age: "%AGE%"
groups: 
job-title: "%JOB%"
race: "%RACE%"
---

>[!INFO] `=this.file.name`
>- ![[Ansom Lang.jpg|inlR|200]]
<br/> [[Ansom Lang.jpg|show to players]]
>- **Age:** `= this.char-age`
> - **Description:** Lieutenant Ansom is a human urban ranger. He is an athletic young man with long black hair and a short neat beard, angular jaw, and rugged features. He is garbed in a hooded green cloak and light chain armor of the [Hooded Lanterns](https://mrbissell.com/Factions/Hooded+Lanterns) that prominently displays a captain’s insignia on his shoulder.
> - **Personality:** Fearless
 
 >[!NOTE] Background
 >
 >Lieutenant in Hooded Lanterns
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