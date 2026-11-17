// Bouton de langue : ouvre la même page dans l'autre langue.
// Les pages françaises (racine du site) et arabes (dossier /ar/) ont les mêmes
// chemins, par exemple installation/java/ et ar/installation/java/.
document.addEventListener("click", function (ev) {
  if (ev.metaKey || ev.ctrlKey || ev.shiftKey || !ev.target.closest) return;
  var cible = ev.target.closest("a.md-select__link[hreflang]");
  if (!cible) return;
  var actuel = document.querySelector('a.md-select__link[hreflang="' + document.documentElement.lang + '"]');
  if (!actuel || cible === actuel) return;
  var racine = actuel.href;                 // racine de la langue affichée
  var page = location.href.split("#")[0];
  if (page.indexOf(racine) !== 0) return;
  ev.preventDefault();
  ev.stopPropagation();
  location.href = cible.href + page.slice(racine.length);
}, true);
