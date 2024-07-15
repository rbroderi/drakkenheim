---
publish: true
---

# Listing
 
%% DATAVIEW_PUBLISHER: start
```dataview  
LIST  
WHERE contains(file.folder, this.file.folder) AND !contains(file.name, "TEMPLATE") AND file.name != this.file.name 
```
%%

- [[Maps/Westemär Region.md|Westemär Region]]

%% DATAVIEW_PUBLISHER: end %%
