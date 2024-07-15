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

- [[Sessions/Road to Drakkenheim/Road to Drakkenheim.md|Road to Drakkenheim]]

%% DATAVIEW_PUBLISHER: end %%