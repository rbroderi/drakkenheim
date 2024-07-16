---
type: npc
status: 
char-age: 60
groups: The Silver Serpent
job-title: Captain
publish: true
---

>[!INFO] `=this.file.name`
>- ![[captain.jpg|inlR|200]]
<br/> [[captain.jpg|show to players]]
>- **Age:** `= this.char-age`
> - **Description:** Captain Tamond Stormwind is a seasoned sailor with a weathered face that bears the marks of a lifetime spent at sea. His silver hair, once a dark chestnut, now shines in the sunlight as a testament to his years of experience navigating the treacherous waters of the ocean. At 60 years old, he still carries himself with the confidence and strength of a man who has weathered many storms and emerged victorious.
> - Tamond's piercing blue eyes hold a deep wisdom that comes from years of leading his crew through perilous waters and facing down ruthless pirates. Despite his grizzled appearance, there is a kindness in his voice and a warmth in his smile that endears him to those under his command.
> - As captain of the renowned ship, *The Silver Serpent*, Tamond is respected by both his crew and fellow sailors for his tactical prowess and unwavering sense of honor. He is known for his quick thinking in times of crisis and his unwavering dedication to protecting those under his care
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

| Session                                                                      | Title               | date       |
| ---------------------------------------------------------------------------- | ------------------- | ---------- |
| [[Sessions/Road to Drakkenheim/Road to Drakkenheim.md\|Road to Drakkenheim]] | Road to Drakkenheim | 07/14/2024 |

%% DATAVIEW_PUBLISHER: end %%
