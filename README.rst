TODO Notes:

* Currently the first tile on a movie DVD is assumed to be the main
  feature and the rest are assumed to be supporting content.  They
  are all dumped into a "Behind The Scenes" directory for later
  sorting.  That is a place Plex should put them and make them
  visible.  There are currently two problems:

  1. extra content is not showing up.  I think this is because the
     file name is just the, filename from makemkv, rather than the
     movie title.

  2. The first title is not always the main feature.  Maybe picking
     the biggest would be a better heuristic.

  Long term, it would be nice to have a database mapping makemkv titles
  to content names and categories (Behind the Scenes, Trailer, etc.)

* Need a license
