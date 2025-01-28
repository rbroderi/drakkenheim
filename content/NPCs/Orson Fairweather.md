---
type: npc
status: 
char-age: "%AGE%"
groups: 
job-title: "%JOB%"
race: "%RACE%"
publish: true
---

>[!INFO] Orson Fairweather
>- ![[Orson Fairweather.jpg|inlR|200]]
<br/> [[Orson Fairweather.jpg|show to players]]
>- **Age:** %AGE%
> - **Description:** The stout man has a heavily scarred and aged face, and a mouth of gold teeth.
> - **Personality:** N/A
 
 >[!NOTE] Background
 >
 >He speaks little of his own history or exploits, but entertains rumours about his past life as a pirate and adventurer.

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