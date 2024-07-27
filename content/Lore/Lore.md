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

- [[Lore/Edicts of Lumen.md|Edicts of Lumen]]

%% DATAVIEW_PUBLISHER: end %%