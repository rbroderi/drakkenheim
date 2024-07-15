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

- [[Road to Drakkenheim|Road to Drakkenheim]]

%% DATAVIEW_PUBLISHER: end %%