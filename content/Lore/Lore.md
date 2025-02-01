---
publish: true
---
# Listing
%% DATAVIEW_PUBLISHER: start
```dataview  
LIST  
WHERE contains(file.folder, this.file.folder) AND !contains(file.name, "TEMPLATE") AND !contains(file.name, "private") AND file.name != this.file.name AND publish = true
```
%%

- [[Lore/Edicts of Lumen.md|Edicts of Lumen]]
- [[Lore/Sacred Flame.md|Sacred Flame]]

%% DATAVIEW_PUBLISHER: end %%