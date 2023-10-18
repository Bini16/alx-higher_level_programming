-- That lists all shows in the database hbtn_0d_tvshows without a genre linked and Records are ordered by ascending tv_shows.title and tv_show_genres.genre_id.
SELECT tv_shows.'title', tv_show_genres.'genre_id'
  FROM 'tv_show_genres'
  RIGHT JOIN 'tv_shows'
  ON tv_shows.'id' = tv_show_genres.'show_id'
  WHERE tv_show_genres.'show_id' IS NULL
  ORDER BY tv_shows.'title', tv_show_genres.'genre_id';
