---
publish: true
---

# Listing

%% DATAVIEW_PUBLISHER: start
```dataview  
LIST  
WHERE contains(file.folder, this.file.folder) AND !contains(file.name, "TEMPLATE") AND !contains(file.name, "private") AND file.name != this.file.name 
```
%%

- [[NPCs/Adrien Ballard.md|Adrien Ballard]]
- [[NPCs/Tamond Stormwind.md|Tamond Stormwind]]

%% DATAVIEW_PUBLISHER: end %%

%%
```ccard
type: folder_brief_live
noteOnly: true
```
%%

