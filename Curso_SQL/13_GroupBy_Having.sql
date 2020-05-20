SELECT carga FROM cursos
GROUP BY carga

SELECT carga, COUNT(nome) FROM cursos
GROUP BY carga

SELECT carga, COUNT(nome) FROM cursos
GROUP BY carga
HAVING COUNT(nome) > 3

SELECT carga, COUNT(*) FROM cursos
WHERE ano > 2015
GROUP BY carga
HAVING carga > (SELECT AVG(carga) FROM cursos)