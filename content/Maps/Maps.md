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

- [[Maps/Westemär Region Measure.md|Westemär Region Measure]]
- [[Maps/Westemär Region.md|Westemär Region]]
- [[Maps/Drakkenheim.md|Drakkenheim]]

%% DATAVIEW_PUBLISHER: end %%
