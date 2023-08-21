SELECT IF(id%2<>0, IF(id=(SELECT MAX(id) FROM seat), id, id+1), id-1) AS id,
student FROM seat ORDER BY id;