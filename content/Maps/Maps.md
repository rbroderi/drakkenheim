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

- [[Westemär Region Measure|Westemär Region Measure]]
- [[Westemär Region|Westemär Region]]

%% DATAVIEW_PUBLISHER: end %%
