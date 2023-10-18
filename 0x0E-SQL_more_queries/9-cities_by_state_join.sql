-- That lists all cities in the database hbtn_0d_usa and Records are sorted in order of ascending cities.id.
SELECT cities.'id' , cities.'name' , states.'name'
FROM 'cities'
INNER JOIN 'states'
ON cities.'state_id' = states.'id';
