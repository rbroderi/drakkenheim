---
type: npc
status: 
char-age: "%AGE%"
groups: 
job-title: "%JOB%"
race: "%RACE%"
publish: true
---

>[!INFO] Flamekeeper Hanna
>- ![[Flamekeeper Hanna.jpg|inlR|200]]
<br/> [[Flamekeeper Hanna.jpg|show to players]]
>- **Age:** %AGE%
> - **Description:** Hanna is a young woman who wears a simple white and yellow frock and keeps her black hair tied in a braid. 
> - **Personality:** Cordial
 
 >[!NOTE] Background
 >
 >Hanna was merely an acolyte when the last Flamekeeper died several years ago, but opted to take up the position herself rather than abandon the folk of Emberwood Village. She believes the Faith of the Sacred Flame is needed here now more than ever, and offers hospitality, kindness, and prayer to any who visit the chapel.

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